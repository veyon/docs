.. _Configuration reference:

Configuration Reference
=======================

In this chapter all configuration pages within Veyon Configurator as well as all configuration options with their
respective meanings are explained in detail. It mainly serves as a reference for looking up detailed configuration
options. A manual and hints for the installation can be found in chapter :ref:`Configuration`. 

.. _General:

General
---------

.. _UserInterface:

User Interface
++++++++++++++

:index:`Language`
	The selected language can be adapted for the graphical user interfaces as well as the command line tools.
	You can choose from all the languages that are already provided in a partly or complete translation. Please 
	note, that changing the language will take effect after a program restart. In default configuration Veyon uses
	the language of the operating system, if this language is already supported. Otherwise, English will be used
	as a fallback.

    **Default:** *use system language settings*

:index:`High-DPI-Scaling`
	In case Veyon is used on high resolution screens with a high pixel density (DPI>150) this option should be
	activated. In this case the user interfaces are displayed larger such that readability especially of visual elements with
	text caption is improved. 
	
	**Default:** *disabled*


.. _Logging:

Logging
+++++++

You have several options at hand to influce the :index:`logging` within Veyon. These options are primarily of
interest if you are experiencing problems using Veyon. The :index:`log files` may indicate potential causes for errors.


.. _LogFileDirectory:

:index:`Logfile directory`
	You can use this option to specify in which directory the log files will reside. Normally you should use a
	placeholder variable in this place. A more detailed description about possible values can be found 
	in section :ref:`placeholder variables`. 
	
	**Default:** *$TEMP*
	

.. _Loglevel:

:index:`Loglevel`
	The loglevel defines how detailed logging messages are recorded. For analysis of program failures it may be
	useful to even set the loglevel to :guilabel:`Debugmessages and everything else`. Thus, however, huge amounts
	of log data can be produced fast. In normal operating mode only warnings and errors should be recorded.

    **Vorgabe:** *Information, warnings and errors*

:index:`Limit logfile size`
	In order for logfiles not to become too large and occupy :index:`memory` unnecessarily, their size can be
	limited with this option. If activated, an upper limit for the size of a single logfile can be configured. 

    **Default:** *disabled / 1 MB*

:index:`Rotate logfiles`
	In conjunction with limiting the size of a single logfile, it may be useful furthermore to rotate the logfiles.
	In this case one logfile is renamed to ``Veyon...log.0`` after exceeding the configured limit. Previously 
	rotated files are renamed such that the number of the file suffix is increased by 1. If the maximum number of
	rotations is reached, the oldest file (i.e. the one with the highest number as a suffix) is deleted. 

    **Vorgabe:** *disabled / 10x*

Log to :index:`stderr`
	If program components of Veyon are executed from a command line window (i.e. a terminal), you can use this
	option to specify, whether logging messages shall be printed to ``stderr`` or ``stdout``. This option is
	primarily relevant for scripting operations. 
	
	**Default:** *activated*

Log to :index:`Windows-Event Log`
	For in central management in may be useful in some cases to log logging messages directly to the 
	Windows-Event Log. This option does not influence the normal recording of logfiles. Under Linux this
	option has no effect. 
	
	**Default:** *disabled*

You can use the :guilabel:`Clear all Logfiles` button to delete all Veyon logfiles in the logfile directory of the
current user as well as the ones of the system service. 


.. _NetworkObjectDirectory:

Network Object Directory
++++++++++++++++++++++++

In Veyon a :index:`network object directory` provides information about :index:`network objects`. 
Network objects include computers and rooms that computer are based in. THe data from the network object directory
is used by Veyon Master to supply the :index:`computer room management` with entries. On top of that data from the
network object directory is used for access control. By default a backend is used, that stores the data in the 
local Veyon configuration and queries them from this location. See section :ref:`local data` for more information.

:index:`Backend`
	You can use this option to define the desired backend for the network object directory. Depending on the 
	installation there may be several backends such as :ref:`LDAP` available beside the default backend. 
	
	**Default:** *Standard (store objects in local configuration)*

:index:`Update interval`
	The network object directory can be automatically updated in the background which may come in handy if 
	dynamic backends such as LDAP are used. The time interval for these updates can be altered with this option.
	
	**Default:** *60 seconds*


.. _ServiceConfiguration:

Service
-------

.. _ServiceGeneral:

General
+++++++

:index:`Hide info area icon`
	By default the Veyon service displays an info area icon (see also *system section of the control panel*) to
	indicate proper operation and information concering :index:`program version` and used network ports. Displaying
	the icon can be prohibited by activating this option. 
	
	**Default:** *disabled*

Activate :index:`SAS generation` in the software (Ctrl+Alt+Del)
	In standard configuration it is not possible for applications running under Windows to generate the
	Secure-Attention-Sequence (Ctrl+Alt+Del) and simulate pressing these keys. With this option a policy is written
	to the Windows-Registry that alters this behavior. It is recommended to leave this option activated in order 
	to be able to send :kbd:`Ctrl+Alt+Del` to a remotely controlled computer. Otherwise it may for example not 
	possible to unlock the remotely controlled computer. A user login can also be prohibited since the keys
	:kbd:`Ctrl+Alt+Del` usually have to be pressed to this end.
	
	**Default:** *activated*  

:index:`Autostart`
	With this option you can specify whether the Veyon service is registered as a :index:`system service` in 
	the operating system meaning that is automatically started on booting the computer.
	
	**Default:** *activated* 

Additional parameters
	If the Veyon service is registered as a system service, you can use this option to supply additional parameters
	which the operating system passes to the Veyon service upon starting. A more detailed explanation of possible
	options can be found in section :ref:`ServiceParameters`.
	
	**Default:** *<empty>*


.. _NetworkSettings:

Network
+++++++

:index:`Primary service port`
	You can use this option to define the primary :index:`network port` the Veyon service is working with,
	meaning that it listens to incoming connections and accepts them. 
	
	**Default:** *11100*

Port of the interval VNC server
	You can use this option to define the network port the interval :index:`VNC server` is working with. This port
	is not reachable from the outside and is used exclusively by the Veyon service to access screen data via an internal
	VNC server and forward them. 
	
	**Default:** *11200*

Port for function manager
	You can use this option to define the network port the :index:`function manager` is working with. This internal
	components of the Veyon service is an interface between the Veyon service and function processes. In contrast
	to the Veyon service these function processes are running in the context of the signed in user and therefore
	have to communicate with the Veyon service through this interface. This port is not reachable from the outside.
	
	**Default:** *11300* 

Port for demo server
	You can use this option to define the network port the :index:`demo server` is working with. The demo server
	provides screen data from a teacher computer to the network during a demonstration. 
	
	**Default:** *11400*

Activate :index:`firewall exception`
	Depending on the system configuration can may be impossible for a process running under Windows to listen to
	a specific port since the :index:`Windows-Firewall` may be blocking connection requests. In order to provide
	access to the service port and the demo server port, exceptions for the Windows-Firewall have to be configured.
	This is automatically done during the installation process. If this behavior is unwanted and a manual 
	configuration is preferred, this option can be disabled. 
	
	**Default:** *activated*

Only allow connections from the local computer
	If the Veyon service shall not be reachable for other computers in the network, you can use this option. 
	For normal computers which shall be access from the Veyon Master, this option must not be activated. However,
	the option could be useful for teacher computers in order to provide an additional security layer beside the
	access control settings. Access to the demo server is not influenced by this option. 
	
	**Default:** *disabled*
	

.. index:: VNC server, internal VNC server, external VNC server

.. _VNCServer:

VNC server
++++++++++

Plugin
	By default Veyon uses an internal platform specific VNC server implementation to provide the screen data of
	a computer. In some cases, however, it may be desirable to utilize a plugin with a different implementation. 
	For example if a separate VNC server is already installed on the computer, this server can be used instead
	of the internal VNC server by choosing the plugin :guilabel:`External VNC Server`. In this case the password
	and network port of the installed VNC server have to be entered.
	
	**Default:** *Built-in VNC server*


.. _MasterConfiguration:

Master
------

Directories
+++++++++++

In order to make a configuration generic and independent of the user, you should use placeholder variables instead
of absolute paths in the directory settings. A more detailed explanation of possible values can be found in
section :ref:`placeholder variables`.


.. _UserConfiguration:

:index:`User configuration`
	The user specific configuration of the Master program resides in the directory defined here. This configuration
	includes the settings for the user interface and the computer choice from the last session.
	
	**Default:** *$APPDATA/Config*
	
:index:`Screenshots`
	All image files that have been generated by the screenshot function reside in the directory defined here. 
	For example if you want to store the files in a central collection folder, a different directory path can
	be entered here. 
	
	**Default:** *$APPDATA/Screenshots*


.. index:: computer room management, user interface

Behavior
++++++++

Perform access control on program start
	You can use this option to define whether the possibly configured :ref:`computer access control` should also
	be perform whenever the Veyon Master is started. Even though access control is enforced on client-side in 
	every case, this additional option assures, that users without proper access rights can not even start the Veyon
	Master, hence making security even more visible. 
	
	**Default:** *disabled*


.. _RoomAutoSwitch:

Automatically switch to current room
	By default all computers that have been selected the previous time are displayed after starting Veyon Master.
	If instead all computers in the Master computer's room shall be displayed, this option can be activated. The
	Veyon Master will then try to solve which room the local computer belongs to using the configured
	:ref:`network object directory`. All computers in the room are listed in this case. Precondition for this 
	function is a correctly working DNS setup in the network which translated computer names to IP addresses
	and vice versa. 
	
	**Default:** *disabled*

Adjust computers' thumbnail size automatically upon starting
	If the size of the computers' thumbnail is to be automatically adjusted upon starting Veyon Master (takes the same
	effect as clicking the :guilabel:`Auto` button), this option can be activated. The previously configured size
	will be ignored. This functionality primarily comes into play in conjunction with the
	:ref:`automatic room change <RoomAutoSwitch>`. 
	
	**Default:** *disabled*

Enforce chosen mode for client computer
	Some of Veyon's functions change the operating mode of a computer. Examples are the demo mode or the 
	screen lock. These mode function are activated only once per default and, for example, are not restored in case of a
	physical computer reboot. If this option is activated, the mode will even be enforced after a connection has been
	closed. 
	
	**Default:** *disabled*

Show confirm dialogue for potentially hazardous actions
	Actions such as rebooting a computer or logging off of a user are potentially hazardous such that an 
	unintentional activation is not desired. You can use this option to define that such actions have to be 
	confirmed in a confirm dialogue. 
	
	**Default:** *disabled*

Function on :index:`double-click`
	If a computer is double-clicked in Veyon Master, a predefined function can be triggered. The usage of the 
	functions *remote control* or *remote view* is conventional. 
	
	**Default:** *<no function>*
	

Computer Management
+++++++++++++++++++

Always open on start
	You can use this option to define that the computer management is opened upon program start by default. 
	**Default:** *disabled*

Only show current room
	As a default, the computer management lists all rooms in the configured :ref:`network object directory`.
	By activating this option you can assure that only the room the Master computer is based in is listed.
	This can increase lucidity especially in larger environments. 
	
	**Default:** *disabled*

Allow adding rooms manually
	In conjunction with the option *only show current room* is can be additionally specified, that further rooms
	can be added to the computer management manually. If this option is activated, an additional 
	:guilabel:`Add Room` button is shown that opens a dialogue with all available rooms. 

    **Default:** *disabled*

.. _AutoHideLocalComputer:

Hide local computer
	In normal operation mode it is often not desired to display one's own computer and activated room-wide 
	activated function on one's own computer as well (e.g. screen lock). Hiding a local computer can be activated
	through this option.
	
	**Default:** *disabled* 

Hide empty rooms
	Under certain circumstanced the :ref:`network object directory` contains rooms without computers, for example
	due to specific LDAP filters. These empty rooms can be hid away from the computer management through this option.
	
	**Default:** *disabled*

Hide filter field for computers
	The filter field for searching computers can be hid through this option, to keep the user interface as 
	simple as possible in small environments. 
	
	**Default:** *disabled*


Functions
+++++++++

With the help of the two lists in the :guilabel:`Functions` tab is can be defined which functions are available
in Veyon Master. Single functions can therefore be deactivated if necessary, such that respective buttons and
context menu entries are not displayed in Veyon Master. This may increase lucidity of the user interface if
certain functions are not to be used anyway. 

A function can be moved from one list to the other by marking and confirming the respective button with the arrow keys.
A double-click has the same effect on a function.  


.. _AuthenticationConfiguration:

Authentication
--------------

Authentication Methods
++++++++++++++++++++++

There are same-named options provided for the :ref:`authentication methods` described in chapter :ref:`configuration`.
After an option has been activated, the configuration of the respective authentication method is possible.

:index:`Keyfile authentication`
	You can use this option is activate :ref:`keyfile authentication <KeyfileAuthentication>`. The configuration
	can afterwards be done using the keyfile-assistant.
	
	**Default:** *disabled*

:index:`Login authentication`
	You can use this option to activate :ref:`login authentication <LoginAuthentication>`. No further configuration
	is required and you can test the functionality directly after activation using the :guilabel:`Test` button.
	
	**Default:** *disabled*


Key Management
++++++++++++++

.. _BaseDirectories:

Placeholder variables should be used for both base directories. A detailed description of possible values
can be found in the :ref:`configuration reference` in section :ref:`placeholder variables`. Under Windows
`UNC paths <https://de.wikipedia.org/wiki/Uniform_Naming_Convention>` _ can be used instead of absolute paths.

:index:`Base directory` of the public key file
	The keyfile-assistant places the role specific public key files in this directory after the keys have been 
	generated or imported. On top of that the Veyon Service loads the respective public key file for 
	authentication purposes from this directory.  
	
	**Default:** *$GLOBALAPPDATA/keys/public*

Base directory of the private key file
	The keyfile-assistant places the role specific private key files in this directory after the keys have been
	generated. On top of that the Veyon Master loads the respective private key file to authenticate itself to
	clients from this directory. 
	
	**Default:** *$GLOBALAPPDATA/keys/private*


.. _RefAccessControl:

Access Control
--------------

.. _ComputerAccessControl:

Computer Access Control
+++++++++++++++++++++++

:index:`Data backend`
	A data backend is required as a data base for access control. It provides users and groups as well as
	computers and rooms. Thereby you can choose between the standard backend and other plugin-specific backends
	such as LDAP. With a standard backend local users and groups as well as computers and rooms are loaded from
	the local configuration; see also section :ref:`local data`. If an LDAP connection is used, you should 
	select the backend *LDAP* here. 

Enable usage of domain groups
    When using computer access control in combination with the :ref:`local data:` backend only the local system groups are available per default. By enabling this option all groups of the domain can be queried and used. This option is not enabled per default for performance reasons. In environments with a huge number of domain groups computer access control can take a long time. In such scenarios you should consider setting up the :ref:`LDAP/AD integration <LDAP>` and use the *LDAP* backend.

    **Default:** *disabled*

Grant access to all authenticated users (default)
	If the predefined authentication is sufficient (e.g. when using a keyfile authentication with restricted
	access to the key files), this option can be selected. In this mode no further access control is performed.

Restrict access to members of specific user groups
	In this mode access to a computer is restricted to members of specific user groups. These authorized user
	groups can be configured in section :ref:`authorized user groups for computer access`. 

Process access control rules
	This mode allows for a detailed access control using user defined access control rules and offers maximum
	flexibility. However, its initial configuration is slightly more complicated such that one of the other two
	access control modes is recommended for initial testing. 

.. index:: Authorized User Groups

.. _AuthorizedUserGroupsForComputerAccess:

Authorized User Groups for Computer Access
++++++++++++++++++++++++++++++++++++++++++

Configuration of this access control mode is straightforward. The left list contains all user groups provided by
the data backend. By default these are all local user groups. If :ref:`LDAP/AD Integration <LDAP>` is configured,
all LDAP user groups are shown. You can now select one or more groups and move them to the right list using the
corresponding buttons between the two lists. All members of each group in the right list can access the computer.
Remember to mirror the configuration to all computers. 

Using the :guilabel:`Test` button in section :guilabel:`Computer Access Control` it can be checked, whether are
specific user could potentially access a computer through the current group configuration. 


.. _AccessControlRules:

Access Control Rules
++++++++++++++++++++

Configuration of a rule set for access control including use cases are described in detail in 
chapter :ref:`Rules Set for Computer Access`. 


Demo Server
-----------

Fine tuning can be done through the configuration page for the demo server to enhance performance in demo mode.
These configurations should only be altered if performance is not satisfying or if only a small bandwith is
available for transferring data. 

Update interval
	You can use this option to specify the interval between to screen updates. The smaller this interval is, the
	higher the update frequency and the smoother the screen transmission. However, a considerably low value might
	lead to higher CPU load and more network traffic. 

    **Default:** *100 ms*

Key frame interval
	During transmission of screen data only the parts of the screens that have actually changed are sent to the
	clients (incremental update) in order to minimize network load. These updates are carried out individually
	and asynchronously for each client. Thus, clients may not be running synchronously after a while depending on
	bandwidth and latency. To this end complete *key frames* are sent in equidistant intervals, such that after
	one key frame intervall all client will have a synchronized screen. The lower the value chosen, the higher
	the resulting CPU and network load will be. 
	
	**Default:** *10 sec*

Memory limit
	All screen update data is internally buffered by the demo server to be distributed to the clients later on. 
	In order not to use too much memory space for the internal buffer due to incremental updates between two key frames, the value defined
	here serves as a limit. This limit is a soft-limit meaning that on exceeding it a key frame updated is tried
	(even if the key frame interval has not passed entirely), but the buffer still holds all data. Only if the 
	specified limit is exceeded twofold (hard-limit) the buffer is reset. If there are frequent disruptions or
	lagging during a screen transmission, this value should be increased.
	
	**Default:** 128 MB*


LDAP
----

All options that describe how to connect Veyon to an LDAP compatible server are explained in detail in chapter
:ref:`LDAP`. 

.. _PlaceholderVariables:

Placeholder Variables for File Paths
------------------------------------

:index:`Placeholder variables` can be used with each operating system in both the Windows and Linux format
``$VARIABLE`` and ``%VARIABLE%``. 

============= =============
Variable      Expanded Path
============= =============
APPDATA   	  User specific directory for :index:`application data` from Veyon, e.g. ```...\User\AppData\Veyon`` under Windows or ``~/.veyon`` under Linux
HOME, PROFILE :index:`Home directory` of the signed in user, e.g. ``C:\Users\Admin`` under Windows or ``/home/admin`` under Linux
GLOBALAPPDATA System-wide directory for application data from Veyon, e.g. ``C:\ProgramData\Admin`` under Windows or ``/home/admin`` under Linux
TMP, TEMP	  User specific directory for :index:`temporary files`, under Windows ``C:\Windows\Temp`` is used for the Veyon Service and ``/tmp`` under Linux
============= =============


.. _ServiceParameters:

Program Parameters for Veyon Service
------------------------------------

Dependening on the operating system under which Veyon is run, the Veyon Service can take various
:index:`program parameters`. The desired parameters have to be entered in the :ref:`general service settings <ServiceGeneral>`. 

====================== ================= =======
Parameter              Operating System  Meaning
====================== ================= =======
``-session <ID>``       *<all>*          An integer between ``0`` and ``99`` can be used as optional :index:`session-ID`, to have multiple instances of the Veyon Service running in different user sessions on the same computer. The session-ID is added to the number of the port configured in the :ref:`network settings`, such that each instace of the Veyon Service is working with different ports. You have to enter the absolute port (primary service port plus session-ID) together with the computer/IP-address, e.g. ``192.168.2.3:11104``. 
``<x11vnc-parameter>``  Linux			 The Veyon Service can take all parameters supported by the program ``x11vnc``. For more information on this topic, please see the `x11vnc manual <http://...>` _.
====================== ================= =======
