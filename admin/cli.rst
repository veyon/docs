.. index:: Command line interface, Command line tool, Command line, CLI, Veyon CLI

.. _CommandLineInterface:

Command line interface
======================

For administrative tasks, the *Veyon Configurator* and the command line tool *Veyon CLI* are available. The program can be started via the command ``veyon-cli`` in the command line. On Windows there's an additional non-console version ``veyon-wcli`` which allows automating tasks without irritating command line window popups. If the :envvar:`$PATH` (Linux) or :envvar:`%PATH%` (Windows) environment variable does not contain the Veyon installation directory, you must first change to the installation directory or prepend the directory to the program name.

If the program is called with the ``help`` parameter, a list of all available modules is displayed. The list can vary depending on the installed Veyon plugins:

.. code-block:: none

    $ veyon-cli help
    Available modules:
        authkeys - Commands for managing authentication keys
        config - Commands for managing the configuration of Veyon
        ldap - Commands for configuring and testing LDAP/AD integration
        networkobjects - Commands for managing the builtin network object directory
        power - Commands for controlling power status of computers
        remoteaccess - Remote view or control a computer
        service - Commands for configuring and controlling Veyon Service
        shell - Commands for shell functionalities

Each CLI module supports the ``help`` command, so that a list of all available commands can be displayed for each module. Sample output for the ``config`` module:

.. code-block:: none

    $ veyon-cli config help
    Available commands:
        clear - Clear system-wide Veyon configuration
        export - Export configuration to given file
        get - Read and output configuration value for given key
        import - Import configuration from given file
        list - List all configuration keys and values
        set - Write given value to given configuration key
        unset - Unset (remove) given configuration key
        upgrade - Upgrade and save configuration of program and plugins

For some modules the ``help`` command can be supplied with a command name as an additional argument to get specific help for a command:

.. code-block:: none

    $ veyon-cli remoteaccess help control

    remoteaccess control <host>

Authentication key management
-----------------------------

The ``authkeys`` module allows the management of authentication keys so that common operations such as importing an authentication key or assigning a user group can be automated easily.

.. note:: The ``<KEY>`` parameter always refers to a key name consisting of a name identifier and a type, e.g. ``teacher/public``. A name identifier must consist of letters only. The type has to be either ``private`` or ``public``.

.. describe:: create <NAME>

    This command creates a authentication key pair with name <NAME> and saves private and public key to the configured key directories. The parameter must be a name for the key, which may only contain letters.

.. describe:: delete <KEY>

    This command deletes the authentication key <KEY> from the configured key directory. Please note that a key can't be recovered once it has been deleted.

.. describe:: export <KEY> [<FILE>]

    This command exports the <KEY> to <FILE> authentication key. If <FILE> is not specified a name will be constructed from name and type of <KEY>.

.. describe:: extract <KEY>

    This command extracts the public key part from the private key <KEY> and saves it as the associated public key. When setting up another master computer, it is therefore sufficient to transfer the private key only. The public key can then be extracted.

.. describe:: import <KEY> [<FILE>]

    This command imports the authentication key <KEY> from <FILE>. If <FILE> is not specified a name will be constructed from name and type of <KEY>.

.. describe:: list [details]

    This command lists all available authentication keys in the configured key directory. If the ``details`` option is specified a table with key details will be displayed instead. Some details might be missing if a key is not accessible e.g. due to the lack of read permissions.

.. describe:: setaccessgroup <KEY> <ACCESS GROUP>

    This command adjusts file access permissions to <KEY> so that only the user group <ACCESS GROUP> has read access to it.


.. _ConfigurationManagement:

Configuration management
------------------------

.. index:: Configuration key

The local Veyon configuration can be managed using the ``config`` module. Both the complete configuration as individual configuration keys can be read or written.

.. describe:: clear

    This command resets the entire local configuration by deleting all configuration keys. Use this command to recreate a defined state without old settings before importing a configuration.

.. describe:: export

    This command exports the local configuration to a file. The name of the destination file must be specified as an additional parameter:

    .. code-block:: none

        veyon-cli config export myconfig.json

.. describe:: import

    This command imports a previously exported configuration file into the local configuration. The name of the configuration file to be imported must be specified as an additional argument:

    .. code-block:: none

        veyon-cli config import myconfig.json

.. describe:: list [defaults | types]

    This command shows a list of all configuration keys and their corresponding values. This way you can get the names of the configuration keys in order to read or write them individually via the ``get`` or ``set`` commands. When additionally specifying ``defaults`` the default value for each configuration key is printed instead of the actual configured value. Alternatively the data types of the configuration keys can be inspected by specifying ``types``.

.. describe:: get

    This command allows reading a single configuration key. The name of the key must be supplied as a parameter.

    .. code-block:: none

        veyon-cli config get Network/VeyonServerPort

.. describe:: set

    This command can be used to write a single configuration key. The name of the key and the desired value must be passed as additional arguments:

    .. code-block:: none

        veyon-cli config set Network/VeyonServerPort 12345
        veyon-cli config set Service/Autostart true
        veyon-cli config set UI/Language de_DE

.. describe:: unset

    With this command a single configuration key can be deleted, i.e. Veyon then uses the internal default value. The name of the key must be passed as an additional argument:

    .. code-block:: none

        veyon-cli config unset Directories/Screenshots

.. _CLIConfigUpgrade:

.. describe:: upgrade

    With this command the configuration of Veyon and all plugins can be updated and saved. This may be necessary if settings or configuration formats have changed due to program or plugin updates.


LDAP
----

The commands available in the ``ldap`` module are documented in section :ref:`LDAPCLI` in chapter :ref:`LDAP`.

.. _CLINetworkObjectDirectory:

Network object directory
------------------------

As described in the section :ref:`ConfLocationsAndComputers`, Veyon provides a built-in network object directory that can be used when no LDAP server is available. This network object directory can be managed in the Veyon Configurator as well as on the command line. Certain operations such as CSV import are currently only available on the command line. For most commands, a detailed description with examples is available in the command-specific help. The following commands can be used in the ``networkobjects`` module:

.. describe:: add <TYPE> <NAME> [<HOST ADDRESS> <MAC ADDRESS> <PARENT>]

    This command adds an object, where ``<TYPE>`` can be ``location`` or ``computer``. ``<PARENT>`` can be specified as name or UUID.

.. describe:: clear

    This command resets the entire network object directory, i.e. all locations and computers are removed. This operation is particularly useful before any automated import.

.. describe:: dump

    This command outputs the complete network object directory as a flat table. Each property such as object UID, type or name is displayed as a separate column.

.. describe:: export <FILE> [location <LOCATION>] [format <FORMAT-STRING-WITH-VARIABLES>]

    This command can be used to export either the complete network object directory or only the specified location to a text file. The formatting can be controlled via a format string containing placeholder variables. This allows generating CSV file easily. Valid variables are ``%type%``, ``%name%``, ``%host%``, ``%mac%`` and ``%location%``. Various examples are given in the command help (``veyon-cli networkobjects help export``).

.. note:: When using this command in batch files or through scheduled tasks on Windows make sure to properly escape the percent sign, i.e. use ``%%type%%`` instead of ``%type%``. Otherwise the individual parts of the format strings will be treated as environment variables and substituted with empty strings in most cases. This will lead to unexpected parse errors.

.. describe:: import <FILE> [location <LOCATION>] [format <FORMAT-STRING-WITH-VARIABLES>] [regex <REGULAR-EXPRESSION-WITH-VARIABLES>]

    This command can be used to import a text file into the network object directory. The processing of the input data can be controlled via a format string or a regular expression containing placeholder variables. This way both CSV files and other types of structured data can be imported. Valid variables are ``%type%``, ``%name%``, ``%host%``, ``%mac%`` and ``%location%``. Various examples are given in the command help (``veyon-cli networkobjects help import``).

.. note:: When using this command in batch files or through scheduled tasks on Windows make sure to properly escape the percent sign, i.e. use ``%%type%%`` instead of ``%type%``. Otherwise the individual parts of the format strings will be treated as environment variables and substituted with empty strings in most cases. This will lead to unexpected parse errors.

.. describe:: list

    This command prints the complete network object directory as a formatted list. Unlike the ``dump`` command, the hierarchy of locations and computers is represented by appropriate formatting.

.. describe:: remove <OBJECT>

    This command removes the specified object from the directory. OBJECT can be specified by name or UUID. Removing a location will also remove all related computers.


Power
-----

The ``power`` module allows using power-related functions from the command line.

.. describe:: on <MAC ADDRESS>

    This command broadcasts a Wake-on-LAN (WOL) packet to the network in order to power on the computer with the given MAC address.


Remote access
-------------

The ``remoteaccess`` module provides functions for a graphical remote access to computers. These are the same functions that can be accessed from the Veyon Master. The function provided by the command line tool can be used for example to create an program shortcut for direct access to a specific computer.

.. describe:: control

    This command opens a window with the remote control function that can be used to control a remote computer. The computer name or IP address (and optionally the TCP port) must be passed as an argument:

    .. code-block:: none

        veyon-cli remoteaccess control 192.168.1.2

.. describe:: view

    This command opens a window with the remote view function to monitor a remote computer. In this mode the screen content is displayed in real time, but interaction with the computer is not possible until the corresponding button on the tool bar has been clicked. The computer or IP address (and optionally the TCP port) has to be passed as an argument:

    .. code-block:: none

        veyon-cli remoteaccess view pc5:5900


Service control
---------------

.. index:: Service control, Service registration

The ``service`` module can be used to control the local Veyon Service.

.. describe:: register

    This command registers the Veyon Service as a service in the operating system so that it is automatically started when the computer boots.

.. describe:: unregister

    This command removes the service registration in the operating system so that the Veyon Service is no longer automatically started at boot time.

.. describe:: start

    This command starts the Veyon Service.

.. describe:: stop

    This command stops the Veyon Service.

.. describe:: restart

    This command restarts the Veyon Service.

.. describe:: status

    This command queries and displays the status of the Veyon Service.


Shell
-----

Simple shell functionalities are provided by the ``shell`` module. If this module is called without further arguments, an interactive mode is started. In this mode, all CLI commands can be entered directly without having to specify and call the ``veyon-cli`` program for each command. The mode can be left by entering the keyword ``exit``.

Furthermore the module can be used for automated processing of commands in a text file in order to implement simple batch processing:

.. describe:: run <FILE>

    This command executes the commands specified in the text file line by line. Operations are executed independently of the result of previous operations, i.e. an error does not lead to termination.

