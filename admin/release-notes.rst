.. _ReleaseNotes:

Release notes
=============

This chapter contains information on changes in different Veyon release series. You should read them carefully before upgrading from an older version of Veyon. If not migrated properly, using newer versions of Veyon with old settings in the worst case can lead to security issues such as misbehaving access control rules.

Release notes for the individual releases can be found at the `Veyon releases page <https://github.com/veyon/veyon/releases>`_.

Upgrading configuration
-----------------------

Due to changes in Veyon and its plugins it may happen that both configuration keys and values change between the release series of Veyon. In general Veyon has builtin mechanisms to read old configuration keys and values and migrate them internally at runtime. This ensures that Veyon keeps running normally after upgrading the software only. It is still highly recommended to always upgrade the Veyon configuration stored in the system. This can be done in two ways:

1) Open Veyon Configurator and click the :guilabel:`Apply` button to save and apply the runtime-migrated configuration permanently.
2) Use the :ref:`CommandLineInterface` to upgrade the configuration through the :ref:`upgrade command of the config module <CLIConfigUpgrade>`.

If not using the second method in an automated manner on all computers, the upgraded configuration needs to be :ref:`exported to all other computers <ConfImportExport>` afterwards.

If configuration keys are renamed, the old keys are always kept for compatibility reasons allowing to switch back to a previous version more easily. There'll be a clean up mechanism in a future release which will remove all legacy configuration keys.

Veyon 4.4
---------

Overview
++++++++

Veyon 4.4 is mostly identical to Veyon 4.3. The most notable change is the updated VNC and networking stack which provides even better reliability. As a result Veyon 4.4 uses slightly different techniques and settings when establishing connections to client computers, so the new version should be tested thoroughly before deployment. Apart from this, the risk of regressions is very low.

Structural changes
++++++++++++++++++

There are no structural changes in Veyon 4.4.

Configuration changes
+++++++++++++++++++++

No configuration keys have been changed or renamed. Various internal settings of the VNC and networking stack (such as timeouts and intervals) are now configurable at the command line for debugging and tuning purposes.

Veyon 4.3
---------

Overview
++++++++

Veyon 4.3 is mostly identical to Veyon 4.2. A new plugin has been added which allows to log in a particular user remotely on all computers. The ``config`` CLI module has been improved to handle specific data types (such as JSON data and option indices) more intelligently. Upgrading to Veyon 4.3 does not require any configuration changes. Since only a new plugin has been added and some commands of the ``config`` CLI module have been extended the risk of regressions is very low.

Structural changes
++++++++++++++++++

There are no structural changes in Veyon 4.3.

Configuration changes
+++++++++++++++++++++

No configuration keys have been changed or renamed. The only new configuration keys are directly related to the new remote log in feature and usually do not have to be changed.

Veyon 4.2
---------

Overview
++++++++

Veyon 4.2 continues the Veyon 4 major release series with many internal modernizations, user interface optimizations and performance improvements in many areas. Veyon 4.2 lays the foundation for commercial addons offered starting in the second half of 2019. The following new features and improvements can be found in Veyon 4.2:

* Core
   - The network object management layer has been revised to allow using multi-level hierarchies in commercial addons.
   - The automatic detection of user interface language in some countries has been improved (e.g. use German in Austria or Switzerland).
   - Context information in log messages have been improved.
* Master
   - The computer sort order can now be configured.
   - The internal data models have been improved leading to more stability and reliability.
   - The connection and message handling has been improved to reduce latencies.
* Configurator
   - New view modes "Standard" and "Advanced" have been added.
   - An authentication test functionality has been added.
* Plugins
   - The new file transfer plugin allows to send files to all users and open them automatically if requested.
   - Wake-on-LAN can be used in the CLI via the power module.
   - The builtin network object directory gained support for importing CSV files with a type column.
   - The power down feature supports additional options to install updates, confirm shutdown or power down after timeout.
   - Users can now add custom programs and websites to the respective menu.
   - Thumbnail updates can be slowed down while the demo mode is active. This improves performance and reduces network traffic.
* LDAP
   - Browse buttons have been added to the configuration pages.
   - A new attribute for the computer display name has been added.
   - Computer attribute queries have been optimized to decrease load on the LDAP/AD server.
   - Computer location queries used by access control have been fixed if containers/OUs are used as locations.
   - The result messages of the integration tests have been improved.
* Linux
   - A configuration page with platform-specific settings has been added.
   - The PAM service ``login`` instead of ``su`` is now used to authenticate users.
   - Support for using a custom PAM service such as ``veyon`` has been added.
* Windows
   - A configuration page with platform-specific settings has been added.
   - Platform-specific network code has been improved for more reliable network connections.
   - An alternative authentication mechanism has been added for cases where the SSPI-based mechanism does not work.
   - The screen lock feature can now disable and hide the taskbar, start button and start menu.
   - The underlying Qt framework has been updated to the LTS version 5.12 leading to better Windows 10 support.
   - Performance and security of the builtin UltraVNC server have been improved.

Structural changes
++++++++++++++++++

Starting with Veyon 4.2 the more generic term *location* instead of *room* is used wherever appropriate. This affects both the user interface and configuration key names. The wording has been changed to better reflect where computers are located in multi-level hierarchies.

In Veyon 4.2 the command line utility has been renamed to ``veyon-cli``. All occurrences of the old name ``veyon-ctl`` in your scripts and installation routines have to be replaced accordingly. On Windows there's also a new non-console version ``veyon-wcli`` which allows to automate tasks without irritating command line window popups.

On Linux the systemd unit has been renamed from ``veyon-service.service`` to ``veyon.service``.

The Veyon Configurator no longer shows all configuration options per default in order to present a cleaner user interface. If you miss certain advanced options you can switch the view to :guilabel:`Advanced` through the :guilabel:`View` menu.

Configuration changes
+++++++++++++++++++++

Several configuration keys have been renamed in Veyon 4.2. When upgrading to Veyon 4.2 or newer the new configuration keys will be populated with the value of the old keys automatically.

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Old name
    - New name

  * - ``Service/SoftwareSASEnabled``
    - ``Windows/SoftwareSASEnabled``

  * - ``Master/AutoSwitchToCurrentRoom``
    - ``Master/AutoSelectCurrentLocation``

  * - ``Master/OnlyCurrentRoomVisible``
    - ``Master/ShowCurrentLocationOnly``

  * - ``Master/ManualRoomAdditionAllowed``
    - ``Master/AllowAddingHiddenLocations``

  * - ``Master/EmptyRoomsHidden``
    - ``Master/HideEmptyLocations``

  * - ``Master/OpenComputerManagementAtStart``
    - ``Master/AutoOpenComputerSelectPanel``

  * - ``Master/ConfirmDangerousActions``
    - ``Master/ConfirmUnsafeActions``

  * - ``LDAP/UserLoginAttribute``
    - ``LDAP/UserLoginNameAttribute``

  * - ``LDAP/ComputerRoomMembersByAttribute``
    - ``LDAP/ComputerLocationsByAttribute``

  * - ``LDAP/ComputerRoomMembersByContainer``
    - ``LDAP/ComputerLocationsByContainer``

  * - ``LDAP/ComputerRoomAttribute``
    - ``LDAP/ComputerLocationAttribute``

  * - ``LDAP/ComputerRoomNameAttribute``
    - ``LDAP/LocationNameAttribute``

Veyon 4.1
---------

Overview
++++++++

Veyon 4.1 was the first feature release series of Veyon 4. Even though not visible to the end user the most notable change is the platform support modularization, i.e. all platform-specific functions have been moved to distinct plugins. This has significantly improved the support of the individual platforms and makes it easier to support further platforms in the future. In addition to that Veyon 4.1 offers many improvements and new features compared to 4.0:

* Core
    - All passwords in configuration are now encrypted.
    - Platform-specific code has been moved into platform plugins.
* Master
   - Computers can now be arranged via drag and drop.
   - A button for hiding powered off computers has been added.
   - Refresh interval, background color and thumbnail caption are now configurable.
* Plugins
   - Authentication key management for both Configurator and command line has been revised completely.
   - Computers and rooms can now be managed at the command line.
   - Computers and rooms can now be imported from CSV and text files.
   - Predefined programs and websites for "run program" and "open website" features can be configured.
* LDAP
    - Support for encrypted SSL/TLS connections has been added.
* Linux
   - Full systemd service support
   - The shutdown/reboot/session logout mechanisms have been rewritten to use DBus calls.
* Windows
    - All builds are based on an updated toolchain with GCC 7.3, Qt 5.9 LTS and OpenSSL 1.1.

Structural changes
++++++++++++++++++

As part of the changes for systemd support on Linux, in Veyon 4.1 the Veyon Service component has been split into two separate components. The Veyon Service no longer contains the actual functions to provide access to a computer. These functions have been moved into the new Veyon Server component which runs as a standalone process in user sessions. The Veyon Service now only monitors user sessions on a computer and starts Veyon Server instances within these sessions.

The ``LocalData`` plugin has been split into the ``BuiltinDirectory`` and ``SystemUserGroups`` plugins. This allows to use different data sources for access control, e.g. computers from an LDAP directory in combination with local user groups. After upgrading you should verify that the appropriate network object directory and access control user groups backend are selected as desired.

Configuration changes
+++++++++++++++++++++

The following configuration keys have changed in Veyon 4.1:

.. describe:: ExternalVncServer/Password

    In Veyon 4.0 this key contained the unencrypted password for an external VNC server. Starting with Veyon 4.1 this password is always stored encrypted. It will be encrypted automatically when upgrading the configuration to 4.1. There's no way to encrypt the password manually. When downgrading to 4.0 the password needs to be set explicitly again.

.. describe:: LDAP/BindPassword

    In Veyon 4.0 this key contained the unencrypted LDAP bind password. Starting with Veyon 4.1 this password is always stored encrypted. It will be encrypted automatically when upgrading the configuration to 4.1. There's no way to encrypt the password manually. When downgrading to 4.0 the password needs to be set explicitly again.

.. describe:: LDAP/UsersFilter, LDAP/UserGroupsFilter, LDAP/ComputersFilter, LDAP/ComputerGroupsFilter, LDAP/ComputerContainersFilter

    Veyon 4.0 used a non-standard syntax for LDAP filters. This has been fixed in Veyon 4.1 where all filter expressions must be placed in parentheses. The expressions will be adjusted automatically when upgrading the configuration to 4.1.

.. describe:: BuiltinDirectory/NetworkObjects

    In Veyon 4.0 the builtin network object directory was provided by a different plugin. Starting with Veyon 4.1 locations and computers are stored in ``BuiltinDirectory/NetworkObjects`` instead of ``LocalData/NetworkObjects``.

Veyon 4.0
---------

Veyon 4.0 was the first release series of Veyon 4, the successor of iTALC. It features a modular architecture, a rewritten Master application and LDAP/AD support. As of December 2018 the Veyon 4.0.x series is marked end-of-life and will not receive updates any longer.
