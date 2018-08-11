.. index:: Command Line Interface, Command Line Tool, Command Line

.. _CommandLineInterface:

Command line interface
======================

For administrative tasks, the *Veyon Configurator* and the command line tool *Veyon Control* are available. The program can be started via the command ``veyon-ctl`` in the command line. If the Veyon installation directory is not in the ``$PATH`` (Linux) or ``%PATH%`` (Windows) environment variable, you must first change to the installation directory or prepend the directory to the program name.

If the program is called with the ``help`` parameter, a list of all available modules is displayed. The list can vary depending on the installed Veyon plugins:

.. code-block:: none

    $ veyon-ctl help
    Available modules:
        authkeys - Commands for managing authentication keys
        config - Commands for managing the configuration of Veyon
        ldap - Commands for configuring and testing LDAP/AD integration
        networkobjects - Commands for managing the builtin network object directory
        remoteaccess - Remote view or control a computer
        service - Commands for configuring and controlling Veyon Service
        shell - Commands for shell functionalities

Each :index:`module` supports the ``help`` command, so that a list of all available commands can be displayed for each module. Sample output for the ``config`` module:

.. code-block:: none

    $ veyon-ctl config help
    Available commands:
        clear - Clear system-wide Veyon configuration
        export - Export configuration to given file
        get - Read and output configuration value for given key
        import - Import configuration from given file
        list - List all configuration keys and values
        set - Write given value to given configuration key
        unset - Unset (remove) given configuration key
        upgrade - Upgrade and save configuration of program and plugins

For some modules the ``help`` command can be supplied with a :index:`command name` as an additional argument to get specific help for each command:

.. code-block:: none

    $ veyon-ctl remoteaccess help control

    remoteaccess control <host>

Authentication key management
-----------------------------

The ``authkeys`` module allows the management of authentication keys so that common operations such as importing an authentication key or assigning a user group can be easily automated.

``create <NAME>``
    This command creates a new pair of authentication keys and stores the private and public keys in the configured key directory. The parameter must be a name for the key, which may only contain letters.

``delete <KEY>``
    This command deletes the ``<KEY>`` authentication key from the configured key directory. Please note that a key cannot be recovered once it has been deleted.

``export <KEY> [<FILE>]``
    This command exports the ``<KEY>`` to ``<FILE>`` authentication key. If ``<FILE>`` is not specified, the file name is derived from the name and type of ``<KEY>``.

``extract <KEY>``
    This command extracts the public key part from the private key ``<KEY>`` and saves it as the associated public key. When setting up another master computer, it is therefore sufficient to transfer the private key. The public key can then be extracted.

``import <KEY> [<FILE>]``
    This command imports the authentication key ``<KEY>`` from ``<FILE>``. If ``<FILE>`` is not specified, the file name is derived from the name and type of ``<KEY>``.

``list [details]``
    This command lists all available authentication keys in the configured key directory. If the ``details`` option is specified, a table with key details is output instead. Some details may be missing if a key cannot be accessed, e.g. due to missing read permissions.

``setaccessgroup <KEY> <ACCESS GROUP>``
    This command adjusts the file access permissions on the ``<KEY>`` so that only the user group ``<ACCESS GROUP>`` has read access to it.


.. _ConfigurationManagement:

Configuration management
------------------------

The local Veyon configuration can be managed using the ``config`` module. Both the complete configuration and individual `:index:`configuration keys` can be read or written.

``clear``
    This command resets the entire local configuration by deleting all configuration keys. Use this command to recreate a defined state before importing another configuration:

    ``veyon-ctl config clear``

``export``
    This command exports the local configuration to a file. The name of the destination file must be specified as an additional parameter:

    ``veyon-ctl config export myconfig.json``

``import``
    This command imports a previously exported configuration file into the local configuration. The name of the configuration file to be imported must be specified as an additional argument:

    ``veyon-ctl config import myconfig.json``

``list``
    This command shows a list of all configuration keys and their corresponding values.

    ``veyon-ctl config list``

    Using this command you can find the names of configuration keys in order to ``get`` oder ``set`` them one by one.

``get``
    This command allows reading a single configuration key. The name of the key must be supplied as a parameter.

    ``veyon-ctl config get Network/PrimaryServicePort``

``set``
    With this command a single configuration key can be written. The name of the key and the desired value must be passed as additional arguments:

    ``veyon-ctl config set Network/PrimaryServicePort 12345``

    ``veyon-ctl config set Service/Autostart true``

    ``veyon-ctl config set UI/Language de_DE``

``unset``
    This command deletes a single configuration key resulting in Veyon using the internal `index:`default value` for this key. The name of the key must be passed as an additional argument:

    ``veyon-ctl config unset Directories/Screenshots``

``upgrade``
    With this command the configuration of Veyon and all plugins can be updated and saved. This may be necessary if settings or configuration formats have changed due to program or plugin updates.


LDAP
----

The commands available in the ``ldap`` module are documented in section :ref:`LDAPCLI` in chapter :ref:`LDAP`.

.. _CLINetworkObjectDirectory:

Network object directory
------------------------

As described in the section `ref:`Rooms and Computers`, Veyon provides a built-in network object directory that can be used when no LDAP server is available. This network object directory can be managed in the Veyon Configurator as well as on the command line. Certain operations such as CSV import are currently only available on the command line. For most commands, a detailed description with examples is available in the command-specific help. The following commands can be used in the ``networkobjects`` module:

``add <TYPE> <NAME> [<HOST ADDRESS> <MAC ADDRESS> <PARENT>]``
    This command adds an object, where ``<TYPE>`` can be ``room`` or ``computer``. ``<PARENT>`` can be specified as name or UUID.

``clear``
    This command resets the entire network object directory, i.e. all rooms and computers are removed. This operation is particularly useful before any automated import.

``dump``
    This command outputs the complete network object directory as a flat table. Each property such as object UID, type or name is displayed as a separate column.

``export <FILE> [room <ROOM>] [format <FORMAT-STRING-WITH-VARIABLES>]``
    This command can be used to export either the complete network object dictionary or only the specified room to a text file. The formatting can be controlled via a format string and the variables it contains, so that, for example, a CSV file can be generated. Valid variables are ``%type%``, ``%name%``, ``%host%``, ``%mac%`` and ``%room%``.

``import ``FILE> [room < SPACE>] [format `FORMATSTRING-MIT-VARIABLEN>] [regex `REGULAR EXPRESSION-MIT-VARIABLEN>]``
    This command can be used to import a text file into the network object directory. The processing of the input data can be controlled via a format string or a regular expression and contained variables. This way both CSV files and otherwise structured data can be imported. Valid variables are ``%name%``, ``%host%``, ``%mac%`` and ``%room%``. Various examples are given in the command help.

``list``
    This command prints the complete network object directory as a formatted list. Unlike the ``dump`` command, the hierarchy of rooms and computers is represented by appropriate formatting.

``remove <OBJECT>``
    This command removes the specified object from the directory. ``<OBJECT>`` can be specified as name or UUID. When a room is removed, all computers in it are also removed.


Remote access
-------------

The ``remoteaccess`` module provides functions for a graphical remote access to computers. These are the same function that can be accessed from the Veyon Master. For example, the function provided by the command line tool can be used to create a :index:`program shortcut` for direct access to a particular computer.

``control``
    This command opens a window with the :index:`remote control` function that can be used to control a remote computer. The computer name or IP address (and optionally the TCP port) must be passed as an argument:

    ``veyon-ctl remoteaccess control 192.168.1.2``

``view``
    This command opens a window with the :index:`remote view` function to monitor a remote computer. In this mode the screen content is displayed in real time, but interaction with the computer is not possible until the corresponding button on the tool bar has been clicked. The computer or IP address (and optionally the TCP port) has to be passed as an argument:

    ``veyon-ctl remoteaccess view pc5:5900``


Service control
---------------

The local Veyon service can be controlled using the ``service`` module.

``register``
    This command registers the Veyon service in the operating system as a service so that it starts automatically when the computer starts up.

    ``veyon-ctl service register``

``unregister``
    This command removes the :index:`service registration` in the operating system so that the Veyon service will not start automatically on startup.

    ``veyon-ctl service unregister``

``start``
    This command starts the Veyon service.

    ``veyon-ctl service start``

``stop``
    This command stops the Veyon service.

    ``veyon-ctl service stop``

``restart``
    This command restarts the Veyon service.

    ``veyon-ctl service restart``

``status``
    This command queries and displays the status of the Veyon service.

    ``veyon-ctl service status``


Shell
-----

Simple shell functionalities are provided by the ``shell`` module. If this module is called without further arguments, an interactive mode is started. In this mode, all CLI commands can be entered directly without having to specify and call the ``veyon-ctl`` program for each command. The mode can be exited by entering the keyword ``exit``.

Additionally the module can be used for automated processing of commands in a text file in order to implement simple batch processing:

``run <FILE>``
    This command executes the commands specified in the text file line by line. Operations are executed independently of the result of previous operations, i.e. an error does not lead to termination.

