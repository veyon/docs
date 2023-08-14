.. _ConfigurationReference:

Configuration reference
=======================

In this chapter all configuration pages within Veyon Configurator as well as all configuration options with their respective meanings are explained in detail. It mainly serves as a reference for looking up detailed configuration options. A manual and hints for the installation can be found in chapter :ref:`Configuration`.

.. note:: Some advanced settings are hidden in the standard view. You can switch to the advanced view using the menu.

.. _RefGeneral:

General
---------

.. _RefUserInterface:

User interface
++++++++++++++

.. index:: Language

Language
    The selected language can be configured for the graphical user interfaces as well as the command line tools. You can choose from all the languages which have been translated so far. Please note that changing the language will require a program restart in order to take effect. Per default Veyon uses the language of the operating system if a translation is available for that language. Otherwise English will be used as a fallback.

    **Default:** *Use system language setting*

Style
    This setting allows to change between certain styles of user interface controls. While the Fusion style offers a clean and pleasent look and feel, it's also possible to switch back to the native style of the operating system or desktop environment.

    **Default:** *Fusion*

.. _RefAuthentication:

Authentication
++++++++++++++

The :ref:`Configuration` chapter describes the :ref:`ConfAuthenticationMethods` available in Veyon.

.. index:: Authentication method

Method
    This option defines which authentication method to use. :ref:`Logon authentication <ConfLogonAuthentication>` does not require any further setup and can be used immediately. To use the :ref:`key file authentication <ConfKeyFileAuthentication>`, appropriate authentication keys must first be created and distributed.

    **Default:** *Logon authentication*

.. _RefNetworkObjectDirectory:

Network object directory
++++++++++++++++++++++++

.. index:: Network object directory, Network objects

In Veyon a network object directory provides information about network objects. Network objects can either be computers or their locations. The data supplied by the network object directory is used by Veyon Master to populate the :guilabel:`Locations & computers` view with entries. The data from the network object directory is also used for access control rules making use of computer location information. By default a backend is used which stores computers and locations in the local Veyon configuration and queries them from the configuration whenever required. See section :ref:`ConfLocationsAndComputers` for details.

.. index:: Network object directory backend

Backend
    You can use this setting to set the desired backend for the network object directory. Depending on the installation there may be several backends such as :ref:`LDAP` available beside the default backend.

    **Default:** *Builtin (computers and locations in local configuration)*

.. index:: Network object directory update interval

Update interval
    The network object directory automatically updates in background which especially is useful for dynamic backends such as LDAP. The time interval for these updates can be altered with this option.

    **Default:** *60 seconds*

.. _RefLogging:

Logging
+++++++

.. index:: Logging

Veyon can log various kinds of messages to component-specific log files or the logging system of the operating system. This information can be very helpful when troubleshooting issues with Veyon. The following logging settings allow to change the logging behaviour.

.. _RefLogFileDirectory:

.. index:: Log file directory

Log file directory
    You can use this setting to specify which directory the log files will be written in. It's strongly recommended to use path variables here. All information on supported variables can be found in section :ref:`RefPathVariables`.

    **Default:** *%TEMP%*

.. _RefLogLevel:

.. index:: Log level

Log level
    The log level defines the minimum severity for which log messages are written. When analyzing program failures it may be useful to set the log level to :guilabel:`Debug messages and everything else`. This will generate a huge amount of log data and is not recommended for production environments. The default log level *Warnings and errors* or higher should be used instead.

    **Default:** *Warnings and errors*

.. index:: Limit log file size

Limit log file size
    In order for log files not to become too large and occupy disk space unnecessarily their size can be limited through this setting. When enabled an upper limit for the size of a single log file can be configured.

    **Default:** *disabled / 100 MB*

.. index:: Rotate log files

Rotate log files
    In conjunction with limiting the size of log files it additionally may be useful to rotate the log files. When enabled each log file is renamed to ``Veyon...log.0`` after exceeding the configured limit. Previously rotated files are renamed so that the number of the file suffix is increased by 1. If the configured number of rotations is reached the oldest file (i.e. the one with the highest number as a suffix) is deleted.

    **Default:** *disabled / 10x*

.. index:: Standard error output

Log to standard error output
    When program components of Veyon are executed from a command line window (shell), you can use this option to specify, whether logging messages shall be printed to ``stderr`` or ``stdout``. This setting primarily is relevant for scripting operations only.

    **Default:** *enabled*

.. index:: Windows event log

Write to logging system of operating system
    In some environments it may be desired to write log messages directly to the Windows event log e.g. in order to collect them afterwards. This option does not influence the normal recording of log files. On Linux, this option enables forwarding log messages from Veyon Server processes to the systemd journal of the ``veyon.service`` unit.

    **Default:** *disabled*

You can use the :guilabel:`Clear all log files` button to delete all Veyon log files in the log file directory of the current user as well as the ones of the system service. This will stop the Veyon Service temporarily.


.. _RefService:

Service
-------

.. _RefServiceGeneral:

General
+++++++

.. index:: Hide tray icon, Program version

Hide tray icon
    By default the Veyon Service displays a tray icon (also called *system control panel*, *info area* or similar) to indicate proper operation and provide basic information such as the program version and network port which the service is listening at. The tray icon can be hidden by enabling this option.

    **Default:** *disabled*

.. index:: Blocked access notification, Unauthorized access

Show notification when an unauthorized access is blocked
    This option specifies whether a notification should be displayed if the access to the local computer was blocked, either due to an authentication failure or access control denying the access. Especially during the deployment and setup of Veyon these notifications often indicate problems with the authentication settings. Typical failure reasons are invalid authentication keys or (when using logon authentication) invalid user credentials (username/password).

    **Default:** *enabled*

.. index:: Remote connection notification

Show notification on remote connection
    In some environments it may be desired or even required to inform the user that his computer is being accessed remotely. This behaviour can be achieved by enabling this option. In case the user has to be asked for permission instead appropriate access control rules have to be configured. More information can be found in chapter :ref:`AccessControlRules`.

    **Default:** *disabled*

.. index:: Autostart, System service

Autostart
    Upon the installation of Veyon the Veyon Service is registered as a system service in order to launch the Veyon Server automatically for user sessions. The start of the Veyon Service can be prevented by disabling this option. You'll then have to start the Veyon Server in user sessions manually. The logon screen will not be accessible in this case.

    **Default:** *enabled*


.. _RefSessions:

.. index:: Sessions, Session settings, Terminal server, Remote desktop server, RDP, Single session mode, Multi session mode

Single session mode (create server instance for local/physical session only)
    Choose this option for single-user scenarios, i.e. each user is working locally on a dedicated computer. In this mode the Veyon Service will always start exactly one server instance for the primary session of the computer, e.g. the console session on Windows.

    **Default:** *enabled*

.. _RefMultiSessionMode:

Multi session mode (for terminal and remote desktop servers)
    Enabling this option makes the Veyon Service launch a Veyon Server process for every user session on a computer. This includes both local and remote (RDP) sessions. Typically this is required to support terminal/remote desktop server scenarios. The server instances listen on individual network port numbers based on the :ref:`Veyon server port number <RefVeyonServerPort>` and the session ID. To access a session other than the default session, the corresponding port number has to be appended to the hostname in the :ref:`ConfLocationsAndComputers` configuration page. You can use e.g. ``myhost.example.org:11101`` to access the first RDP session on a computer. Alternatively consider using the `NetworkDiscovery add-on <https://veyon.io/addons/#networkdiscovery>`_ which scans computers for sessions and makes them available in Veyon Master automatically.

    **Default:** *disabled*

Maximum session count
    In multi session mode the number of server instances can be limited through this setting. Per default up to 100 concurrent sessions are supported on a computer. When using numbers higher than 100, make sure to adjust the :ref:`server port numbers <RefNetworkPortNumbers>` to be more than 100 apart. Otherwise port numbers of different instances and server types would overlap and cause malfunctions.

    **Default:** *100*

.. _RefNetworkPortNumbers:

.. index:: Network port, Network port numbers, Port numbers

Network port numbers
++++++++++++++++++++

.. index:: Veyon Server port number

.. _RefVeyonServerPort:

Veyon server
    This setting allows you to specify the network port number on which the Veyon Server listens for incoming connections.

    **Default:** *11100*

.. index:: Internal VNC server port number

Internal VNC server
    This setting allows you to specify the network port number used by the internal VNC server. The internal VNC server only listens on ``localhost``, so it is never directly accessible from the network. Only the local Veyon server accesses the internal VNC server and forwards screen data and user input accordingly.

    **Default:** *11200*

.. index:: Feature manager port number

Feature manager
    This setting allows you to specify the network port number used by the feature manager. This internal component is part of the Veyon Server and listens at ``localhost`` only. It starts/stops processes to provide specific features. In contrast to the Veyon Service these processes in most cases have to run in the context of the logged on user and therefore have to communicate with the Veyon Server through this network port.

    **Default:** *11300*

.. index:: Demo server port number

Demo server
    This setting allows you to specify the network port number used by the demo server. The demo server is a special high-efficiency VNC server that makes the screen data of the demo computer available to all participating computers.

    **Default:** *11400*

.. _RefNetworkMisc:

Miscellaneous settings
++++++++++++++++++++++

.. index:: Firewall exception, Firewall, Windows firewall

Enable firewall exception
    Depending on the system configuration it may be impossible to access listening ports such as the Veyon Server port from the network. On Windows the Windows firewall usually blocks any incoming connections. In order to allow access to the Veyon server port and the demo server port, exceptions for the Windows firewall must be configured. This is done automatically during the installation process. If this behavior is not desired and manual configuration is preferred, this option can be disabled.

    **Default:** *enabled*

.. index:: localhost

Allow connections from localhost only
    If you do not want the Veyon Server to be available to other computers in the network, you can use this option. This option must not be activated for normal computers that should be accessible from the Veyon Master application. However, this option can be useful for teacher computers to provide additional security beyond the access control functionality. Access to the demo server is not affected by this option.

    **Default:** *disabled*

Disable clipboard synchronization
    If you do not want the clipboard contents to be synchronized when remote controlling a computer, enable this option. This may also help to fix unspecific clipboard-related issues occurring while the Veyon Server is running.

.. index:: VNC server, Internal VNC server, External VNC server

.. _RefVNCServer:

VNC server
++++++++++

Plugin
    By default Veyon uses an internal platform-specific VNC server implementation to provide the screen data of a computer. In some cases, however, it may be desirable to use a plugin with a different implementation. If a separate VNC server is already running on the computer, this server instance can be used instead of the internal VNC server by choosing the plugin :guilabel:`External VNC server`. In this case the password and network port of the installed VNC server have to be supplied.

    **Default:** *Builtin VNC server*

.. hint:: Platform-specific information on how to configure the individual internal VNC server can be found in chapter :ref:`PlatformNotes`.

.. _RefMaster:

Master
------

All settings on this page influence the appearance, behaviour and features of the Veyon Master application.

Basic settings
++++++++++++++

**Directories**

In order to make a configuration generic and independent of the user, you should use path variables instead of absolute paths in the directory settings. All information on supported variables can be found in section :ref:`RefPathVariables`.

.. _RefUserConfiguration:

.. index:: User configuration

User configuration
    The user specific configuration of Veyon Master is stored in this directory. The configuration contains settings for the user interface as well as the computer selection of the last session.

    **Default:** *%APPDATA%/Config*

.. index:: Screenshots

Screenshots
    All image files that have been generated by using the screenshot feature are stored in this directory. In case you want to collect the files in a central folder, a different directory path can be supplied here.

    **Default:** *%APPDATA%/Screenshots*


.. index:: User interface

**User interface**

.. index:: Image quality

Image quality in monitoring mode
    Starting with Veyon 4.8 the quality of the image data transferred between client and master computers in monitoring mode can be configured such that it meets the possible network bandwidth constraints. While *Highest* uses lossless image encodings (default before Veyon 4.8), *Lowest* uses JPEG encoding which results in significantly reduced bandwidth usage but also clearly visible image artifacts.

    **Default:** *Medium*

Remote access image quality
   Like the image quality in monitoring mode, the image quality in remote access windows can be adjusted to limit bandwidth usage if necessary.

    **Default:** *Highest*

.. index:: Thumbnail update interval

Thumbnail update interval
    This setting determines the time interval in which the computer thumbnails in Veyon Master are updated. The shorter the interval, the higher the processor load on the master machine and the overall network load.

    **Default:** *1000 ms*

.. index:: Background color

Background color
    This setting allows customizing the background color of the monitor view.

    **Default:** *white*

.. index:: Text color

Text color
    This setting allows customizing the color which is used for displaying the computer thumbnail caption in the monitor view.

    **Default:** *black*

.. index:: Computer thumbnail caption

Computer thumbnail caption
    This setting allows defining the caption for computer thumbnails in the monitor view. If the computer name is not important to users only the name of the logged on user can be displayed instead.

    **Default:** *User and computer name*

.. index:: Sort order

Sort order
    This setting allows specifying the sort order for computers in the monitor view. If the caption is configured to display only user names it may make sense to change the sort order to *Only user name* as well.

    **Default:** *Computer and user name*


Behaviour
+++++++++

In the tab :guilabel:`Behaviour` settings are available to change the behaviour of Veyon Master regarding to *program start*, *computer locations* as well as *modes and features*.

**Program start**

Perform access control
    You can use this option to define whether the possibly configured :ref:`ComputerAccessControl` should also be performed whenever the Veyon Master application is started. Even though access control is enforced client-side in every case, this additional option assures, that users without proper access rights can not even start Veyon Master, making security even more visible.

    **Default:** *disabled*

.. _RefAutoSelectLocation:

.. index:: Current location

Automatically select current location
    By default all computers that have been selected the previous time are displayed after starting Veyon Master. If you want to display all computers at the master computer's location instead, this option can be enabled. Veyon Master will then try to determine the location of the local computer by using the configured :ref:`network object directory <RefNetworkObjectDirectory>`. All computers at the same location will then be selected and displayed. For this function to work properly, a correctly functioning DNS setup in the network is required so that both computer names can be resolved to IP addresses and reverse lookups for IP addresses return valid computer names.

    **Default:** *disabled*

.. index:: Computer thumbnail size, Thumbnail size

Automatically adjust computer thumbnail size
    If the size of the computer thumbnails should be adjusted automatically upon starting Veyon Master (same effect as clicking the :guilabel:`Auto` button manually), this option can be enabled. The previously configured size will be ignored. This functionality is especially useful in conjunction with the :ref:`automatic location change <RefAutoSelectLocation>`.

    **Default:** *disabled*

.. index:: Computer select panel

Automatically open computer select panel
    You can use this option to define that the computer select panel is opened upon program start by default.

    **Default:** *disabled*


**Computer locations**

.. _RefShowCurrentLocationOnly:

.. index:: Current location

Show current location only
    Per default, the computer select panel lists all locations provided by the configured :ref:`network object directory <RefNetworkObjectDirectory>`. If this option is enabled only the location of the master computer will be displayed instead. This can make the user interface more clear especially in larger environments with many locations.

    **Default:** *disabled*

Allow adding hidden locations manually
    When the option :ref:`Show current location only <RefShowCurrentLocationOnly>` is enabled the user can still be allowed to add otherwise hidden locations manually. If this option is enabled an additional button :guilabel:`Add location` is shown in the computer select panel. This button opens a dialog with all available locations.

    **Default:** *disabled*

.. _RefAutoHideLocalComputer:

Hide local computer
    In regular usage scenarios it often is not desired to display the own computer as this would start globally started features on the own computer as well (e.g. screen lock). Enabling this option will always hide the local computer to prevent such issues.

    **Default:** *disabled*

Hide own session
    Similar to the :ref:`Hide local computer <RefAutoHideLocalComputer>` option, enabling this option hides the own session from the computer list. This is only relevant when using the :ref:`Multi session mode <RefMultiSessionMode>`.

    **Default:** *disabled*

.. index:: Empty locations

Hide empty locations
    In some situations the :ref:`network object directory <RefNetworkObjectDirectory>` may contain locations without computers, for example due to specific LDAP filters. Such empty locations can be hidden automatically in the computer select panel by enabling this option.

    **Default:** *disabled*

.. index:: Computer filter

Hide computer filter field
    The filter field for searching computers can be hidden through this option. This allows keeping the user interface as simple as possible in small environments.

    **Default:** *disabled*


**Modes and features**

Enforce selected mode for client computers
    Some of Veyon's features change the operating mode of a computer e.g. the demo mode or the screen lock mode. These modes are enabled only once and are not restored in case of a physical computer reboot. If this option is enabled, the mode will even be enforced after a connection has been closed.

    **Default:** *disabled*

Show confirmation dialog for potentially unsafe actions
    Actions such as rebooting a computer or logging off users can have undesired side effects such as data loss due to unsaved documents. In order to prevent unintentional activation of such features a confirmation dialog can be enabled through this option.

    **Default:** *disabled*

.. index:: Double click

Feature on double click
    This setting allows defining a feature to be triggered whenever a computer is double-clicked. In most cases it's desired to use the *remote control* or *remote view* feature here.

    **Default:** *no function*


Features
++++++++

The two lists in the :guilabel:`Features` allow to define which features are made available in Veyon Master. Single features can be disabled if necessary so that respective buttons and context menu entries are not displayed. This can help to simplify the user interface if certain features are never used anyway.

A feature can be moved from one list to the other by selecting it and clicking the respective button with the arrow icon. Alternatively a feature can simply be double-clicked to move it to the other list.


.. _RefAccessControl:

Access control
--------------

.. _ComputerAccessControl:

Computer access control
+++++++++++++++++++++++

.. index:: User groups backend

User groups backend
    A user group backend provides user groups and their members (users) required for access control. While the default backend is suitable for system user groups the LDAP backends will make LDAP/AD user groups available for access control.

.. index:: Domain groups

Enable usage of domain groups
    When using access control in combination with the default backend only the local system groups are available per default. By enabling this option all groups of the domain which a computer belongs to can be queried and used. This option is not enabled per default for performance reasons. In environments with a huge number of domain groups performing access control can take a long time. In such scenarios you should consider setting up the :ref:`LDAP/AD integration <LDAP>` and use one of the *LDAP* backends.

    **Default:** *disabled*

Grant access to every authenticated user (default)
    If the selected authentication scheme is sufficient (e.g. when using a key file authentication with restricted access to the key files), this option can be enabled. In this mode no further access control is performed.

Restrict access to members of specific user groups
    In this mode access to a computer is restricted to members of specific user groups. These authorized user groups can be configured in section :ref:`RefAuthorizedUserGroups`.

Process access control rules
    This mode allows detailed access control based on user-defined access control rules and offers the greatest flexibility. However, its initial setup may be slightly more complicated and time-consuming, so you should choose one of the other two access control modes for initial testing.

.. _RefAuthorizedUserGroups:

User groups authorized for computer access
++++++++++++++++++++++++++++++++++++++++++

.. index:: Authorized user groups

Configuration of this access control mode is straightforward. The left list contains all user groups provided by the selected backend. By default these are all local user groups. If :ref:`LDAP/AD Integration <LDAP>` is configured, all LDAP user groups are displayed. You can now select one or more groups and move them to the right list using the corresponding buttons between the two lists. All members of each group in the right list can access the computer. Do not forget to transfer the configuration to all computers afterwards.

The :guilabel:`Test` button in the :guilabel:`Computer access control` section can be used to check whether a particular user is allowed to access a computer via the defined groups.


.. _RefAccessControlRules:

Access control rules
++++++++++++++++++++

The setup of a ruleset for access control including use cases is described in detail in chapter :ref:`AccessControlRules`.


.. _RefAuthenticationKeys:

Authentication keys
-------------------

.. _RefKeyFileDirectories:

Key file directories
++++++++++++++++++++

Path variables should be used for both base directories. All information on supported variables can be found in section :ref:`RefPathVariables`. On Windows `UNC paths <https://en.wikipedia.org/wiki/Uniform_Naming_Convention>`_ can be used instead of absolute paths.

.. index:: Public key file base directory

Public key file base directory
    The specified base directory contains subdirectories for each key name (e.g. user role) with the actual public key file inside. This allows setting individual access permissions for the subdirectories. The public key files are placed in the corresponding subdirectory below the base directory on both creation and import. When loading the respective public key file for authentication the Veyon Server uses this base directory as well.

    **Default:** *%GLOBALAPPDATA%/keys/public*

.. index:: Private key file base directory

Private key file base directory
    The specified base directory contains subdirectories for each key name (e.g. user role) with the actual private key file inside. This makes it possible to define individual access rights for the subdirectories. During creation and import, the private key files are placed in the corresponding subdirectory below the base directory. Veyon Master searches for accessible private key files under this base directory and uses the private key files to authenticate against the Veyon Server on client computers.

    **Default:** *%GLOBALAPPDATA%/keys/private*


Demo server
-----------

In the configuration page for the demo server, you can make some fine tunings to improve the performance of the demo mode. These settings should only be changed if the performance is not satisfactory or if only a small network bandwidth is available for data transfer.

Update interval
    This option can be used to set the interval between two screen updates. The smaller the interval, the higher the refresh rate and the smoother the screen transfer. However, a lower value leads to a higher CPU load and increased network traffic.

    **Default:** *100 ms*

Key frame interval
    During a screen broadcast, only changed screen areas are sent to the client computers (incremental updates) in order to minimize the network traffic. These updates are performed individually and asynchronously for each client, so that after a while the clients may no longer run synchronously depending on bandwidth and latency. Therefore, complete screen contents (*key frames*) are transmitted at regular intervals, so that a synchronous image is displayed on all clients at the latest when the key frame interval expires. The lower the value, the higher the processor and network traffic.

    **Default:** *10 s*

Memory limit
    All screen update data is stored by the demo server in an internal buffer and then distributed to clients. To prevent the internal buffer between two key frames from occupying too much memory due to too many incremental updates, the value specified here is used as a limit. This limit is a soft limit, so that if it is exceeded, a key frame update is attempted (even if the key frame interval has not yet expired), but the buffer still retains all data. The buffer is only reset when the double value is exceeded (hard limit). If there are repeated interruptions or delays while broadcasting a screen, this value should be increased.

    **Default:** *128 MB*

Bandwidth limit
    As of Veyon 4.8, the total bandwidth used for screen transmission can be limited. This involves determining the bandwidth used between two key frames and comparing it with the set limit. If it is above this limit, the demo server reduces the image quality so that less data is transmitted to the clients. Conversely, if the bandwidth used is below 80% of the limit, the image quality is increased again.

    If master and client computers are connected via Wi-Fi, the demo server bandwidth should be limited according to the available Wi-Fi bandwidth.

    **Default:** *100 MB/s*


LDAP
----

All options for connecting Veyon to an LDAP-compatible server are described in detail in chapter :ref:`LDAP`.

File transfer
-------------

Starting with Veyon 4.5, an additional configuration page with settings related to the file transfer feature is available in the advanced view.

Directories
+++++++++++

In order to make a configuration generic and independent of the user, you should use path variables instead of absolute paths in the directory settings. All information on supported variables can be found in section :ref:`RefPathVariables`.

Default source directory
    This directory will be opened by default when the user starts the file transfer feature and is asked for the files to transfer.

    **Default:** ``%HOME%``

Destination directory
    All received files will be saved in this directory on the client side. Change it if you do not want to store received files in root of the user's home directory.

    **Default:** ``%HOME%``

Options
+++++++

Remember last source directory
    When the user is asked for files to transfer, the directory which files have been transferred from previously, is opened if this option is enabled. Disable this option to always open the default source directory.

    **Default:** *enabled*

Create destination directory if it does not exist
    When using a destination directory other than the default one, it may happen that the destination directory does not exist. Keep this option enabled to create it automatically whenever receiving files on the client side.

    **Default:** *enabled*

WebAPI
------

Starting with Veyon 4.5, an additional configuration page with settings related to the WebAPI plugin is available in the advanced view.

General
+++++++

Enable WebAPI server
    This option defines whether to start the WebAPI server along with the Veyon Service.

    **Default:** *disabled*

Network port
    This setting specifies the network port at which the WebAPI server should listen for incoming requests.

    **Default:** *11080*

Connection settings
+++++++++++++++++++

A connection refers to an authentication resource identified by a connection UUID.

Lifetime
    Every connection is only valid for a certain period of time, regardless of its activity (in contrast to the idle timeout). This value can be changed to configure shorter or longer connection lifetimes.

    **Default:** *3 h*

Idle timeout
    If no request is received for a certain connection for longer than specified by this setting, the connection is closed automatically.

    **Default:** *60 s*

Authentication timeout
    This setting determines the time period within which a connection must be successfully authenticated. Unauthenticated connections will be closed automatically when timed out.

    **Default:** *15 s*

Maximum number of open connections
    This setting limits the number of simultaneous open connections, e.g. to mitigate possible denial of service attacks.

    **Default:** *10*

Connection encryption
+++++++++++++++++++++

Use HTTPS with TLS 1.3 instead of HTTP
    This option determines whether only HTTPS connections should be allowed instead of HTTP connections. When enabled, appropriate TLS certificate and private key files have to be configured as well.

    **Default:** *disabled*

TLS certificate file
    The path to the TLS certificate file for the HTTPS server.

TLS private key file
    The path to the TLS private key file for the HTTPS server.

.. _RefPathVariables:

Path variables
--------------

.. index:: Path variables, Application data, User profile directory, Home directory, Temporary files, Desktop directory, Documents directory, Downloads directory, Pictures directory, Videos directory

Path variables have to be supplied in the format ``%VARIABLE%`` on all platforms.

.. describe:: %APPDATA%

    This variable is expanded to the user-specific directory for application data stored by Veyon, e.g. :file:`...\\User\\AppData\\Veyon` on Windows or :file:`~/.veyon` on Linux.

.. describe:: %DESKTOP%

    This variable is expanded to the local or redirected Desktop directory of the logged on user, e.g. :file:`C:\\Users\\Admin\\Desktop` on Windows or :file:`/home/admin/Desktop` on Linux (requires Veyon 4.7.3 or newer).

.. describe:: %DOCUMENTS%

    This variable is expanded to the local or redirected documents directory of the logged on user, e.g. :file:`C:\\Users\\Admin\\Documents` on Windows or :file:`/home/admin/Documents` on Linux (requires Veyon 4.7.3 or newer).


.. describe:: %DOWNLOADS%

    This variable is expanded to the local or redirected download directory of the logged on user, e.g. :file:`C:\\Users\\Admin\\Downloads` on Windows or :file:`/home/admin/Downloads` on Linux (requires Veyon 4.7.3 or newer).


.. describe:: %GLOBALAPPDATA%

    This variable is expanded to the system-wide directory for Veyon's application data,  e.g. :file:`C:\\ProgramData\\Veyon` on Windows or :file:`/etc/veyon` on Linux.

.. describe:: %HOME%

    This variable is expanded to the home directory/user profile directory of the logged on user, e.g. :file:`C:\\Users\\Admin` on Windows or :file:`/home/admin` on Linux.

.. describe:: %HOSTNAME%

    This variable is expanded to the hostname of the local computer, allowing to access files in computer-specific directories (requires Veyon 4.7.3 or newer).


.. describe:: %PICTURES%

    This variable is expanded to the local or redirected pictures directory of the logged on user, e.g. :file:`C:\\Users\\Admin\\Pictures` on Windows or :file:`/home/admin/Pictures` on Linux (requires Veyon 4.7.3 or newer).


.. describe:: %TEMP%

    This variable is expanded to the user-specific directory for temporary files, e.g. :file:`...\\User\\AppData\\Local\\Temp` on Windows or :file:`/tmp` (or any path specified in the :envvar:`$TMPDIR` environment variable) on Linux. Processes running with system privileges (Veyon Service, Veyon Server and all sub processes) use :file:`C:\\Windows\\Temp` on Windows and :file:`/tmp` on Linux.

.. describe:: %VIDEOS%

    This variable is expanded to the local or redirected videos directory of the logged on user, e.g. :file:`C:\\Users\\Admin\\Videos` on Windows or :file:`/home/admin/Videos` on Linux (requires Veyon 4.7.3 or newer).



.. _RefEnvironmentVariables:

Environment variables
---------------------

Veyon evaluates various optional environment variables allowing to override default settings for runtime settings such as session ID, log level and authentication keys to use.

.. envvar:: VEYON_AUTH_KEY_NAME

    This variable allows explicitly specifying the name of the authentication key to use in case multiple authentication keys are available. This can be used to override the default behaviour of Veyon Master which uses the first readable private key even if multiple private key files are available.

.. envvar:: VEYON_LOG_LEVEL

    This variable allows overriding the configured log level at runtime, e.g. for debugging purposes.

.. envvar:: VEYON_SESSION_ID

    This variable allows overriding the session ID and is evaluated by Veyon Server. When multi session mode (multiple local and remote sessions on the same host) is enabled each Veyon Server instance has to use distinct network numbers for not conflicting with other instances. A server therefore adds the numerical value of this environment variable to the configured :ref:`network port numbers <RefNetworkPortNumbers>` to determine the port numbers to use. In the :ref:`RefNetworkObjectDirectory` the absolute port (Veyon server port + session ID) must be specified along with the computer/IP address, e.g. ``192.168.2.3:11104``.
