.. index:: Command Line Interface, Command Line Tool, Command Line

.. _CommandLineInterface:

Command Line Interface
======================

For administrative tasks you can use *Veyon Configurator* as well as the command line tool *Veyon Control*. 
The program can be opened by the ``veyon-ctl`` command via the command line. If the installation directory of
Veyon is not listed in the environment variable ``$PATH`` (Linux) resp. ``%PATH%`` (Windows), you have to change
to the installation directory or prefix the program name with this directory.

If the program is called with the parameter ``help``, a list of all available modules is shown. 
The list can vary depending on the installed Veyon-plugins:

.. code-block:: none

    $ veyon-ctl help
    Available modules:
        config - Commands for administering the Veyon-configuration
        ldap - Commands for configuring and testing the LDAP/AD integration
        service - Commands for configuring and controlling the Veyon-service
        remoteaccess - Remote view or remote control of a computer

Every :index:`module` supports the ``help`` command, so that a list of all available commands for the module
can be displayed. Sample output for the ``config`` module: 

.. code-block:: none

	$ veyon-ctl config help
	Available commands:
		clear - delete system wide Veyon-configuration
		export - export configuration to the given file
		get - read and print configuration value for the given key
		import - import configuration from the given file
		list - list key-value-pairs for all configuration keys
		set - write given value to the given configuration key
		unset - reset given configuration key 

In some modules the ``help`` command can be supplied with a :index:`command name` as a second parameter 
to display specific help for the inferred command:

.. code-block:: none

    $ veyon-ctl remoteaccess help control

    remoteaccess control <host>

.. _ConfigurationAdministration:

Administration of your Configuration
------------------------------------

You can administrate your local Veyon-configuration by using the ``config`` command. 
Thereby you can read or write an entire configuration as well as single :index:`configuration key`. 

``clear``
	This command resets the entire local configuration by deleting all configuration keys. Use this command to
	recreate a defined state before importing another configuration:

    ``veyon-ctl config clear``

``export``
	This command allows exporting the local configuration to a file. The name of the target file must be supplied
	as a parameter:

    ``veyon-ctl config export myconfig.json``

``import``
	This command imports a previously exported configuration file into the local configuration. The name of the 
	file containing the configuration to be imported must be supplied as a parameter:

    ``veyon-ctl config import myconfig.json``

``list``
	This command shows a list of all configuration keys and their corresponding values.

    ``veyon-ctl config list``

    Using this command you can find the names of configuration keys in order to ``get`` oder ``set`` them one by one.

``get``
	This command allows reading a single configuration key. The name of the key must be supplied as a parameter.
    
    ``veyon-ctl config get Network/PrimaryServicePort``

``set``
	This command allows writing to a single configuration key. The name of the key and its desired value must be 
	supplied as parameters.

    ``veyon-ctl config set Network/PrimaryServicePort 12345``

    ``veyon-ctl config set Authentication/KeyAuthenticationEnabled true``

``unset``
	This command allows deleting a single configuration key resulting in Veyon using the internal :index:`default value` for this key.
	The name of the key must be supplied as a parameter.
    
    ``veyon-ctl config unset Directories/Screenshots``


Control of Services
-------------------

You can control the local Veyon-service by using the module ``service``.

``register``
	This command registers the Veyon-service as a service running on the operating system, such that the service
	is automatically started when booting. 

    ``veyon-ctl service register``

``unregister``
	This command removes the :index:`registration of the service` on the operating system, such that the 
	Veyon-service is no longer automatically started when booting.
    
    ``veyon-ctl service unregister``

``start``
	This command starts the Veyon-service.

    ``veyon-ctl service start``

``stop``
	This command stops the Veyon-service.

    ``veyon-ctl service stop``

``restart``
	This command restarts the Veyon-service.

    ``veyon-ctl service restart``

``status``
	This command queries and displays the status of the Veyon-service.

    ``veyon-ctl service status``


LDAP
----

The commands available in the ``ldap`` module are documented in section :ref:`LDAP-CLI` in chapter :ref:`LDAP`. 


Remote Access
-------------

The ``remoteaccess`` module provides functions for a graphical remote access to remote computers. 
These are the same function that can be used from within the Veyon master. For example, a function provided by the 
command line tool can be used to create a :index:`link` for directly access on a specific computer. 

``control``
	This command opens a :index:`remote control` that can be used to control a remote computer. A computer name
	or IP-address (and optionally a TCP-port) has to be supplied as a parameter:

    ``veyon-ctl remoteaccess control 192.168.1.2``

``view``
	This command opens a :index:`remote view` that can be used to monitor a remote computer.
	In this mode the content on the screen is displayed in real time, but interaction isn't possible
	until the corresponding button in the tool bar has been clicked. A computer name
	or IP-address (and optionally a TCP-port) has to be supplied as a parameter:

    ``veyon-ctl remoteaccess view pc5:5900``
