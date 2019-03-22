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
    The selected language can be configured for the graphical user interfaces as well as the command line tools. You can choose from all languages which have been translated so far. Please note that changing the language will require a program restart in order to take effect. Per default Veyon uses the language of the operating system if a translation is available for that language. Otherwise English will be used as a fallback.

    **Default:** *Use system language setting*


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

Veyon can log various kinds of messages to component-specific log files or the logging system of the operating system. These information can be very helpful when troubleshooting issues with Veyon. The following logging settings allow to change the logging behaviour.

.. _RefLogFileDirectory:

.. index:: Log file directory

Log file directory
    You can use this setting to specify which directory the log files will written in. It's strongly recommended to use placeholder variables here. All information on supported variables can be found in section :ref:`RefPlaceholderVariables`.

    **Default:** *%TEMP%*

.. _RefLogLevel:

.. index:: Log level

Log level
    The log level defines the minimum severity for which log messages are written. When analyzing program failures it may be useful to set the log level to :guilabel:`Debug messages and everything else`. This will generate huge amount of log data and is not recommended for production environments. The default log level *Warnings and errors* or higher should be used instead.

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
    In some environments it may be desired to write log messages directly to the Windows event log e.g. in order to collect them afterwards. This option does not influence the normal recording of log files. On Linux this option currently has no effect.

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

.. index:: Failed authentication notification

Show notification on failed authentication attempts
    This option specifies whether a notification should be displayed if there was a failed logon attempt to the Veyon Service. These messages usually indicate that the authentication settings are not set up correctly. Typical failure reasons are invalid authentication keys or (when using logon authentication) invalid user credentials (username/password).

    **Default:** *enabled*

.. index:: Remote connection notification

Show notification on remote connection
    In some environments it may be desired or even required to inform the user that his computer is being accessed remotely. This behaviour can be achieved by enabling this option. In case the user has to be asked for permission instead appropriate access control rules have to be configured. More information can be found in chapter :ref:`AccessControlRules`.

    **Default:** *disabled*

.. index:: SAS generation, Secure Attention Sequence, Ctrl+Alt+Del

Enable SAS generation by software (Ctrl+Alt+Del)
    On Windows per default it's impossible for applications to generate the *Secure Attention Sequence* (Ctrl+Alt+Del) in order to simulate the press of these keys. When enabling this option a policy is written to the Windows registry which changes this behavior. It is recommended to leave this option enabled in order to be able to send :kbd:`Ctrl+Alt+Del` when remote controlling a computer. Otherwise it may be impossible to unlock a remotely controlled computer or logging on a user since in most cases the shortcut :kbd:`Ctrl+Alt+Del` has to be issued first.

    **Default:** *enabled*

.. index:: Autostart, System service

Autostart
    Upon the installation of Veyon the Veyon Service is registered as a system service in order to launch the Veyon Server automatically for user sessions. The start of the Veyon Service can be prevented by disabling this option. You'll then have to start the Veyon Server in user sessions manually. The logon screen will not be accessible in this case.

    **Default:** *enabled*


.. _RefNetwork:

.. index:: Network settings

Network
+++++++

.. index:: Primary service port, Network port

Primary service port
    You can use this setting to define the primary network port which the Veyon Server is listening at for incoming connections.

    **Default:** *11100*

.. index:: Internal VNC server port, Internal VNC server

Internal VNC server port
    You can use this setting to define the (localhost only) network port used by the internal VNC server. The VNC server will only listen to it at ``localhost`` so it never is reachable from the network directly. It's solely accessed by the Veyon Service which forwards screen data from and user inputs to the internal VNC server.

    **Default:** *11200*

.. index:: Feature manager port, Feature manager

Feature manager port
    You can use this setting to define the (localhost only) network port used by the feature manager. This internal component is part of the Veyon Service and starts and stops processes to provide specific features. In contrast to the Veyon Service these processes in most cases have to run in the context of the logged on user and therefore have to communicate with the Veyon Service through this network port.

    **Default:** *11300*

.. index:: Demo server port, Demo server

Demo server port
    You can use this setting to define the network port which the demo server is listening at. The demo server efficiently makes screen data from a selected computer available to all computers participating in a demonstration.

    **Default:** *11400*

.. index:: Firewall exception, Firewall, Windows firewall

Enable firewall exception
    Depending on the system configuration it may be impossible to access a listening ports such as the Veyon Service port from the network. On Windows the Windows firewall usually will block any incoming connections. In order to provide access to the service port and the demo server port, exceptions for the Windows-Firewall must be configured. This is done automatically during the installation process. If this behavior is not desired and manual configuration is preferred, this option can be disabled.

    **Default:** *enabled*

.. index:: localhost

Allow connections from localhost only
    If you do not want the Veyon Service to be available to other computers in the network, you can use this option. This option must not be activated for normal computers that should be accessible from the Veyon Master application. However, this option can be useful for teacher computers to provide additional security beyond the access control functionality. Access to the demo server is not affected by this option.

    **Default:** *disabled*


.. index:: VNC server, Internal VNC server, External VNC server

.. _RefVNCServer:

VNC server
++++++++++

Plugin
    By default Veyon uses an internal platform-specific VNC server implementation to provide the screen data of a computer. In some cases, however, it may be desirable to use a plugin with a different implementation. If a separate VNC server is already running on the computer, this server instance can be used instead of the internal VNC server by choosing the plugin :guilabel:`External VNC server`. In this case the password and network port of the installed VNC server have to be supplied.

    **Default:** *Builtin VNC server*


.. _RefMaster:

Master
------

All settings on this page influence the appearance, behaviour and features of the Veyon Master application.

Basic settings
++++++++++++++

**Directories**

In order to make a configuration generic and independent of the user, you should use placeholder variables instead of absolute paths in the directory settings. All information on supported variables can be found in section :ref:`RefPlaceholderVariables`.

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

.. index:: Thumbnail update interval

Thumbnail update interval
    This setting determines the time interval in which the computer thumbnails in Veyon Master are updated. The shorter the interval, the higher the processor load on the master machine and the overall network load.

    **Default:** *1000 ms*

.. index:: Background color

Background color
    This setting allows to customize the background color of the monitor view.

    **Default:** *white*

.. index:: Text color

Text color
    This setting allows to customize the color which is used for displaying the computer thumbnail caption in the monitor view.

    **Default:** *black*

.. index:: Computer thumbnail caption

Computer thumbnail caption
    This setting allows to define the caption for computer thumbnails in the monitor view. If the computer name is not important to users only the name of the logged on user can be displayed instead.

    **Default:** *User and computer name*

.. index:: Sort order

Sort order
    This setting allows to specify the sort order for computers in the monitor view. If the caption is configured to display only user names it may make sense to change the sort order to *Only user name* as well.

    **Default:** *Computer and user name*


Behaviour
+++++++++

In the tab :guilabel:`Behaviour` settings are available to change the behaviour of Veyon Master regarding to *program start*, *computer locations* as well as *modes and features*.

**Program start**

Perform access control
    You can use this option to define whether the possibly configured :ref:`ComputerAccessControl` should also be perform whenever the Veyon Master application is started. Even though access control is enforced client-side in every case, this additional option assures, that users without proper access rights can not even start Veyon Master, making security even more visible.

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

.. index:: Empty locations

Hide empty locations
    In some situations the :ref:`network object directory <RefNetworkObjectDirectory>` may contains locations without computers, for example due to specific LDAP filters. Such empty locations can be hidden automatically in the computer select panel by enabling this option.

    **Default:** *disabled*

.. index:: Computer filter

Hide computer filter field
    The filter field for searching computers can be hidden through this option. This allows to keep the user interface as simple as possible in small environments.

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
    This setting allows to define a feature to be triggered whenever a computer is double-clicked. In most cases it's desired to use the *remote control* or *remote view* feature here.

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

Placeholder variables should be used for both base directories. All information on supported variables can be found in section :ref:`RefPlaceholderVariables`. On Windows `UNC paths <https://en.wikipedia.org/wiki/Uniform_Naming_Convention>`_ can be used instead of absolute paths.

.. index:: Public key file base directory

Public key file base directory
    The specified base directory contains subdirectories for each key name (e.g. user role) with the actual public key file inside. This allows to set individual access permissions for the subdirectories. The public key files are placed in the corresponding subdirectory below the base directory on both creation and import. When loading the respective public key file for authentication the Veyon Service uses this base directory as well.

    **Default:** *%GLOBALAPPDATA%/keys/public*

.. index:: Private key file base directory

Private key file base directory
    The specified base directory contains subdirectories for each key name (e.g. user role) with the actual private key file inside. This makes it possible to define individual access rights for the subdirectories. During creation and import, the private key files are placed in the corresponding subdirectory below the base directory. Veyon Master searches for accessible private key files under this base directory and uses the private key files to authenticate against the Veyon Service on client computers.

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

    **Default:** 128 MB*


LDAP
----

All options for connecting Veyon to an LDAP-compatible server are described in detail in chapter :ref:`LDAP`.


.. _RefPlaceholderVariables:

Placeholder variables for file paths
------------------------------------

.. index:: Placeholder variables, Application data, User profile directory, Home directory, Temporary files

Placeholder variables have to be supplied in the format ``%VARIABLE%`` on all platforms.

.. describe:: %APPDATA%

    This variable is expanded to the user-specific directory for application data stored by Veyon, e.g. :file:`...\\User\\AppData\\Veyon` on Windows or :file:`~/.veyon` on Linux

.. describe:: %HOME%

    This variable is expanded to the home directory/user profile directory of the logged on user, e.g. :file:`C:\\Users\\Admin` on Windows or :file:`/home/admin` on Linux

.. describe:: %GLOBALAPPDATA%

    This variable is expanded to the system-wide directory for Veyon's application data,  e.g. :file:`C:\\ProgramData\\Veyon` on Windows or :file:`/etc/veyon` on Linux

.. describe:: %TEMP%

    This variable is expanded to the user-specific directory for temporary files, on Windows :file:`C:\\Windows\\Temp` is used for the Veyon Service and :file:`/tmp` on Linux


.. _RefEnvironmentVariables:

Environment variables
---------------------

Veyon evaluates various optional environment variables allowing to override default settings for runtime settings such as session ID, log level and authentication keys to use.

.. envvar:: VEYON_AUTH_KEY_NAME

    This variable allows to explicitely specify the name of the authentication key to use in case multiple authentication keys are available. This can be used to override the default behaviour of Veyon Master which uses the first readable private key even if multiple private key files are available.

.. envvar:: VEYON_LOG_LEVEL

    This variable allows to override the configured log level at runtime, e.g. for debugging purposes.

.. envvar:: VEYON_SESSION_ID

    This variable allows to specify the session ID and is evaluated by Veyon Server. When multi session support (multiple graphical sessions on the same host) is enabled each Veyon Server instance has to use distinct network ports for not conflicting with other instances. A server therefore adds the numerical value of this environment variable to the configured :ref:`network ports <RefNetwork>` to determine the port numbers to use. Usually this environment variable is set by Veyon Service for all Veyon Server instances automatically. In the :ref:`RefNetworkObjectDirectory` the absolute port (Primary service port + session ID) must be specified along with the computer/IP address, e.g. ``192.168.2.3:11104``.
