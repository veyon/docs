Veyon WebAPI
============

Veyon 4.5 and newer feature a new WebAPI plugin. This plugin offers a RESTful API for accessing Veyon Server instances via HTTP. There are two possible usage scenarios:

* Local: WebAPI server on each computer running along with the Veyon Server and thus connects to ``localhost``
* Proxy: WebAPI server on a server node, acting as a proxy by connecting to the requested hosts

While running the WebAPI server locally can be beneficial in terms of performance, it requires the deployment of individual SSL certificates on all computers.

The WebAPI plugins also offers a CLI module, so the WebAPI server can be run standalone easily via ``veyon-cli webapi runserver``.

The following sections describe all supported API calls.

General
-------

* When a call succeeds, the indicated responses can be expected with HTTP status code 200.
* Any errors will be indicated through a corresponding (non-unambiguous) HTTP status codes and an additional error object in the response body, e.g. ``{"error":{"code":6,"message":"Authentication failed"}}``

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Error
    - Error code
    - HTTP status code
  * - NoError
    - 0
    - 200 (OK)
  * - InvalidData
    - 1
    - 400 (BadRequest)
  * - InvalidConnection
    - 2
    - 401 (Unauthorized)
  * - InvalidFeature
    - 3
    - 400 (BadRequest)
  * - InvalidCredentials
    - 4
    - 400 (BadRequest)
  * - AuthenticationMethodNotAvailable
    - 5
    - 400 (BadRequest)
  * - AuthenticationFailed
    - 6
    - 401 (Unauthorized)
  * - ConnectionLimitReached
    - 7
    - 429 (TooManyRequests)
  * - ConnectionTimedOut
    - 8
    - 408 (RequestTimeout)
  * - UnsupportedImageFormat
    - 9
    - 503 (ServiceUnavailable)
  * - FramebufferNotAvailable
    - 10
    - 503 (ServiceUnavailable)
  * - FramebufferEncodingError
    - 11
    - 500 (InternalServerError)
  * - ProtocolMismatch
    - 12
    - 501 (NotImplemented)

Connection management & authentication
--------------------------------------

.. rubric:: General

* Idle (inactive) connections are closed automatically after 60 s per default (configurable through the WebAPI/ConnectionIdleTimeout setting)
* Unauthenticated connections are closed automatically after 15 s per default (configurable through the WebAPI/ConnectionAuthenticationTimeout setting)
* Authenticated connections have a limited lifetime and are closed automatically after 3 hours per default (configurable through the WebAPI/ConnectionLifetime setting)

.. rubric:: Get authentication methods supported by host

* URL: /api/v1/authentication/<HOST>
* Method: **GET**
* Response: ``{ "methods": [ "<UUID1>", "<UUID2", ... ] }``

.. rubric:: Create new connection and perform authentication

* URL: /api/v1/authentication/<HOST>
* Method: **POST**
* Data: ``{ "method": "<AUTH-METHOD-UUID>", "credentials": <METHOD-SPECIFIC-CREDENTIALS> }``
* Response: ``{ "connection-uid": "<CONNECTION-UID>", "validUntil": <UTC-TIMESTAMP> }``
* The returned connection UUID identifies a single connection to a host and needs to be passed in the ``Connection-Uid`` header field in all subsequent API calls
* The connection's lifetime ends at the time specified in the ``validUntil`` field
* ``<HOST>`` should be ``localhost`` when connecting to WebAPI servers running on target computers

.. rubric:: Close connection

* URL: /api/v1/authentication/<HOST>
* Method: **DELETE**
* Headers: ``{ Connection-Uid: <CONNECTION-UID> }``
* Response: ``{ }``

Authentication methods
++++++++++++++++++++++

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Name
    - UUID
    - Credentials

  * - AuthKeys
    - ``0c69b301-81b4-42d6-8fae-128cdd113314``
    - ``{ "keyname": "<NAME>" (e.g. "teacher"), "keydata": "<PEM-ENCODED-PRIVATE-KEY>" }``

  * - AuthLDAP (Veyon >= 5)
    - ``6f0a491e-c1c6-4338-8244-f823b0bf8670``
    - ``{ "username": "<LDAP-USERNAME>", "password": "<LDAP-PASSWORD>" }``

  * - AuthLogon
    - ``63611f7c-b457-42c7-832e-67d0f9281085``
    - ``{ "username": "<USERNAME>", "password": "<PASSWORD>" }``

  * - AuthSimple (Veyon >= 5)
    - ``73430b14-ef69-4c75-a145-ba635d1cc676``
    - ``{ "password": "<MASTER-PASSWORD>" }``


Framebuffer
-----------

.. rubric:: Get current framebuffer image

* URL: /api/v1/framebuffer/get?format=[png|jpeg]&compression=[1-9]&quality=[1-100]&width=NNNN&height=NNNN
* Method: **GET**
* ``format``
    - Optional
    - Defaults to ``png``
* ``compression``
    - Optional
    - Used for the PNG format only
    - default=5
    - 1=no compression, 9=highest compression
* ``quality``
    - Optional
    - Used for the JPEG format only
    - default=75
    - 1=lowest quality, 100=highest quality
* ``width``/``height``
    - Optional
    - If none of both is not specified, the original framebuffer image will be returned
    - If either one is specified, the corresponding counterpart will be calculated automatically while keeping the aspect ratio
* Response: ``<IMAGE-DATA>``


Feature control
---------------

.. rubric:: Get available features

* URL: /api/v1/feature
* Method: **GET**
* Headers: ``{ Connection-Uid: <CONNECTION-UID> }``
* Response: ``[ <FEATURE OBJECTS> ]``

.. rubric:: Start or stop feature

* URL: /api/v1/feature/<FEATURE-UID>
* Method: **PUT**
* Data: ``{ "active": [true/false], "arguments": <ARGUMENTS> }``
* Arguments are feature specific and described in the feature table below
* Headers: ``{ Connection-Uid: <CONNECTION-UID> }``
* Response: ``{ }``

.. rubric:: Query feature status

* URL: /api/v1/feature/<FEATURE-UID>
* Method: **GET**
* Headers: ``{ Connection-Uid: <CONNECTION-UID> }``
* Response: ``{ "active": [true/false] }``
* Only applies to features implementing a certain mode such as ScreenLock. All features implementing simple actions will never be reported as active.

Available features
++++++++++++++++++

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Name
    - UUID
    - Arguments

  * - ScreenLock
    - ``ccb535a2-1d24-4cc1-a709-8b47d2b2ac79``
    - <none>
  * - InputDevicesLock (Veyon >= 4.5.0)
    - ``e4a77879-e544-4fec-bc18-e534f33b934c``
    - <none>
  * - UserLogoff
    - ``7311d43d-ab53-439e-a03a-8cb25f7ed526``
    - <none>
  * - Reboot
    - ``4f7d98f0-395a-4fff-b968-e49b8d0f748c``
    - <none>
  * - PowerDown
    - ``6f5a27a0-0e2f-496e-afcc-7aae62eede10``
    - <none>
  * - DemoServer
    - ``e4b6e743-1f5b-491d-9364-e091086200f4``
    - ``{ "demoAccessToken": <TOKEN> }``
  * - FullScreenDemoClient
    - ``7b6231bd-eb89-45d3-af32-f70663b2f878``
    - ``{ "demoAccessToken": <TOKEN>, "demoServerHost": <DEMO-SERVER-HOST-ADDRESS> }``
  * - WindowDemoClient
    - ``ae45c3db-dc2e-4204-ae8b-374cdab8c62c``
    - ``{ "demoAccessToken": <TOKEN>, "demoServerHost": <DEMO-SERVER-HOST-ADDRESS> }``

* A demo token is an arbitrary ASCII string (e.g. base64-encoded random data) with a recommended length of at least 16 bytes

User information
----------------

* URL: /api/v1/user
* Method: **GET**
* Response: ``{ "login": "<USER-LOGIN-NAME>", "fullName", "<FULL-NAME-OF-USER>", "session": <DESKTOP-SESSION-ID> }``
* If no user is logged on, the ``login`` and ``fullName`` fields are empty and ``session`` is set to ``-1``
