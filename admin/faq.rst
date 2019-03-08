.. _FAQ:

FAQ - Frequently Asked Questions
================================

Does Veyon run under Chrome OS (ChromeBooks) or MacOS?
------------------------------------------------------

Currently Veyon is only available for Linux- and Windows-based environments. Support for other platforms is being worked on though. The Veyon project relies on the help of experienced software developers, especially for porting Veyon to macOS and Android.


How can I add computers in order to access them?
------------------------------------------------

If the default :ref:`RefNetworkObjectDirectory` is used, all you need to do is add the appropriate locations and computers on the :ref:`ConfLocationsAndComputers` configuration page. Afterwards the added resources are available in Veyon Master.

If :ref:`LDAP` is configured the network object directory has to be changed to the appropriate LDAP backend so that the computers from the directory are displayed in the Veyon Master.

.. index:: iTALC

How can I migrate an existing iTALC installation to Veyon?
----------------------------------------------------------

Although iTALC and Veyon are conceptually similar, a complete new installation and configuration is necessary to use Veyon, since configuration and file formats as well as their paths have changed and are not compatible. For a migration iTALC has to be uninstalled completely first. It is recommended to reboot the computer afterwards. Veyon can then be installed and configured in the same way as iTALC.

While the configuration of authentication methods is very similar, the configuration of locations and computers is done via the Veyon Configurator and no longer in the Master application. In this context you should check whether the new :ref:`LDAP` can be used to make locations and computers automatically available in Veyon.


Is it possible to use Veyon Master on more than one computer?
-------------------------------------------------------------

The usage of Veyon Master on multiple computers is possible without any restrictions. For this to work an identical configuration has to be used on all master computers like its required for client computers in general. If logon authentication is used no further steps are necessary. If key file authentication is used the same private key has to be distributed to all master computers.


How can an existing VNC server be used in conjunction with Veyon?
-----------------------------------------------------------------

In some environments a VNC server is already installed (e. g. UltraVNC) or is provided by the system (e. g. VNC-based access to virtual desktops in VDI environments). This may result in degraded performance or conflicts with the Veyon-internal VNC server. In such cases it is recommended to configure Veyon to use the existing (external) VNC server instead of starting the internal VNC server. The configuration is done through the Veyon Configurator in the configuration page :ref:`RefService` in section :ref:`RefVNCServer`.


Can I import/use an existing or generated file with location and computer information?
--------------------------------------------------------------------------------------

As of Veyon 4.1, there is a new :ref:`module for the command line interface <CLINetworkObjectDirectory>`. This module can be used to import locations and computers from any kind of text files (including CSV files) into the builtin network object directory.


How can I view or control all monitors of a remote computer?
------------------------------------------------------------

On Windows by default only the primary monitor of a computer is accessible with Veyon. You can however change this behaviour in the :ref:`RefVNCServer` configuration. Select the VNC server plugin :guilabel:`Builtin VNC server` and enable the option :guilabel:`Enable multi monitor support`.


How can I import or export the selection of displayed computers?
----------------------------------------------------------------

The selection of displayed computers is saved in the personal :ref:`user configuration <RefUserConfiguration>`. There are two ways to share this configuration with multiple users. Either the user configuration file can be copied into the profile of the user, e.g. via login scripts. Alternatively, the user configuration can be also be stored in a shared directory (e.g. a network drive) and the :ref:`user configuration setting <RefUserConfiguration>` has to be changed accordingly so that the user configuration is loaded from this directory. Please note that the access rights may have to be adjusted so that changes made by users are not written back into the global user configuration.

In this context please also refer the function :ref:`Automatic switch to current classroom <RefAutoSelectLocation>`, which can be used to directly realize the desired behavior.


How can I hide the master computer from computer locations?
-----------------------------------------------------------

All you need to do is enable the option :ref:`Hide local computer <RefAutoHideLocalComputer>` in the master configuration page.


What happens if there is no matching access control rule?
---------------------------------------------------------

If there is no rule where all activated conditions apply when processing the configured access control rules, access is denied and the connection is closed. This prevents an attacker from being accidentally granted access due to an incomplete ruleset.

