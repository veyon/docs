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

Veyon 4.9
---------

Overview
++++++++

Veyon 4.9 comes with the new commercial Entra ID Connector add-on, allowing to work with devices, users and groups from the Entra ID cloud platform. The Windows version of Veyon is now based on the latest Qt 6.7 framework and OpenSSL 3.3.

Structural changes
++++++++++++++++++

The user groups backend is no longer specific to the access control feature but used in other scopes as well. This allows e.g. changing the access group of authentication keys to Entra ID groups. While this has no effect on existing features, the relevant configuration keys have been renamed to matcht the new scope. See the next subsection for details.

Configuration changes
+++++++++++++++++++++

Two configuration keys have been renamed in Veyon 4.9. When upgrading to Veyon 4.9 or newer the new configuration keys will be populated with the values of the old keys automatically.

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Old name
    - New name

  * - ``AccessControl/UserGroupsBackend``
    - ``UserGroups/Backend``

  * - ``AccessControl/DomainGroupsEnabled``
    - ``UserGroups/UseDomainUserGroups``


Veyon 4.8
---------

Overview
++++++++

Veyon 4.8 introduces image quality control mechanisms to better meet bandwidth contraints, especially in Wi-Fi networks. A static image quality can now be configured for monitoring mode and remote access views. The demo server controls the image quality dynamically based on the used bandwidth between two key frames and the configured bandwidth limit.

The Windows version of Veyon is now based on the latest Qt 6.5 framework as well as OpenSSL 3 and UltraVNC 1.4.2.0. Also the build environment has been updated to Debian 11 (i.e. GCC 10 and MinGW runtime 8). This allowed us to enable Link Time Optimization (LTO) resulting in better overall performance.

Structural changes
++++++++++++++++++

The WebAPI has been changed such that the ``/api/v1/user`` endpoint does not return the session ID any longer. Instead the new ``/api/v1/session`` endpoint should be used which also provides additional information about the session.

Configuration changes
+++++++++++++++++++++

No configuration keys have been changed or renamed in Veyon 4.8.

Veyon 4.7
---------

Overview
++++++++

Veyon 4.7 is the last minor release series of Veyon 4. One of the most long-awaited features is certainly the new screen selection menu in the remote access window. Also the overall performance and responsiveness has been improved thanks to a revised mechanism for sending and receiving control messages. Besides that, several issues from previous versions have been resolved.

* Core
    - Fixed binary compatibility issues between different versions of LibVNCServer/LibVNCClient.
    - Messages in log files (especially debug messages) are now much more human readable.
* Plugins
    - Demo: Screens in the Demo menu are now displayed with their actual hardware name and connector type/index.
    - LDAP: Fixed querying members of a group when the nested groups option is enabled.
    - TextMessage: Students can now select and copy the text message or parts of it.
    - TextMessage: Rich text (i.e. formatted text including hyperlinks) can now be entered and sent to students.
    - RemoteAccess: For remote computers with multiple screens, a button with a screen selection menu has been added.
    - RemoteAccess: The login name of the remote user is shown in the window title, if the full name is not available.
    - WebAPI: The header field lookup (e.g. for the connection UID) is now case insensitive.
* Linux
    - The parameter order for the ``ping`` utility has been improved.
    - Issues regarding the session identification have been fixed, solving various issues when running ``veyon-server`` manually e.g. via autostart entries.
* Master
    - A regression in Veyon 4.6.0 has been fixed to make the computer and user search case insensitive again.
    - Control messages between computers are now sent asynchronously which improves performance and responsiveness while reducing the CPU load.
    - When closing the program, it now stops all features on the student computers and waits until all corresponding control messages have been sent.
    - A new filter button has been added to show computers with logged on users only.
    - The dialog for confirming actions such as powering off computers only emphasizes *ALL* computers if all computers are selected.
    - If available, the full name of the user is now preferred in the tooltip.
* Server
    - Server-side framebuffer update rate control has been added which improves performance and responsive.
* Windows
    - Added an explicit initialization of the WinSock layer to prevent networking issues.
    - The service control has been made more resilient.
    - The Windows ICMP API is now used to ping computers in favor of calling the external ``ping`` utility.
    - Several 3rdparty libraries have been updated (Qt 5.12.12 snapshot, TurboJPEG 2.1.2, OpenLDAP 2.5.10 snapshot)

Even though there have been changes to the core and networking layer, there's only a small to medium risk for regressions, since most of the features haven't been touched. To benefit from the performance improvements, both teacher and student computers should be upgraded to Veyon 4.7.

Since the underlying LDAP library has been updated, users of Veyon's LDAP backend should test if Veyon 4.7 is able to retrieve all relevant information from your LDAP/AD server as usual.

Structural changes
++++++++++++++++++

There are no structural changes in Veyon 4.7.

Configuration changes
+++++++++++++++++++++

No configuration keys have been changed or renamed in Veyon 4.7.

Veyon 4.6
---------

Overview
++++++++

Most notably in Veyon 4.6 the remote access module has been redesigned to reuse the computer connection of the main window. This way users get instant access to computers when starting the remote control or view feature and no longer have to wait until the connection has been established (which could take up to several seconds). Also users can now press and hold the left mouse button on a computer. This shows the computer's screen in fullscreen and realtime until the mouse button is released again. Veyon CLI gained two new modules for managing plugins and features. This allows starting and stopping Veyon features remotely on the command line, e.g. for scripting and automation tasks. On Linux the Veyon Service component has been greatly improved to start and stop Veyon Server instances more reliably on session changes (user logon/logoff etc.). In addition to the existing *single and multi session modes*, there's now a new *active session mode* on Windows which starts a single Veyon Server instance for the currently active local or remote session. This is very useful for environments in which some students are logged in locally while others access unoccupied computers via RDP from home.

Since mostly only a few specific modules have been changed or enhanced, there's a rather low risk for regressions in general. Especially Linux users are advised to upgrade soon to solve problems with the Veyon Service.

* Core
    - Protocol errors during the initial authentication phase are handled more reliably. This fixes problems when connecting to incompatible servers accidentally.
* CLI
    - The ``plugin`` and ``feature`` modules have been added.
    - The ``config`` and ``shell`` plugins have been integrated as static modules.
* Plugins
    - Demo: The visual feedback when (re-)connecting has been redesigned.
    - DesktopServices: The *Run program* feature has been renamed to *Start application*.
    - RemoteAccess: The visual feedback when (re-)connecting has been redesigned.
    - RemoteAccess: The computer connection of the main window is reused if available resulting in immediate access to the remote computer.
    - RemoteAccess: The remote cursor is no longer used in view only mode to prevent occasionally observed render artifacts.
    - UserSessionControl: Non-user sessions (such as display manager/login screen sessions) are no longer terminated by the user logoff feature.
    - WebAPI: An error code has been added to report protocol errors occuring while connecting to the Veyon Server.
    - WebAPI: The connection limit is enforced at the HTTP server level already to properly report the connection limit reached error instead of timing out.
    - WebAPI: Skip ping for hosts which no connection could be established to. This allows using a higher connection limit on Linux when the number of open file descriptors is limited.
* Linux
    - SHM support is being detected more reliably.
    - Logging off users is now initiated properly through the environment-specific session manager while ``systemd-logind`` is used as fallback only. This fixes the display manager (especially GDM3) not being shown again after logoff.
    - Reboot and power down via ``systemd-logind`` has been improved while the environment-specific session manager is used as fallback only. The reboot and poweroff binaries are not used any longer.
* Master
    - In addition to the hostname, the computer display name is shown in the tooltip of a computer.
    - A computer's screen is shown in fullscreen and realtime while pressing and holding the left mouse button on a computer.
    - For Linux clients, *[no user]* is displayed as the user name instead of the name of the display manager user.
* Server
    - Hostnames of connected computers (shown in the tooltip of the tray icon) are now reverse resolved in background to keep connections responsive.
* Windows
    - The 3rdparty component UltraVNC has been updated to the latest version.
    - The new *Active session mode* has been implemented.
    - Querying local and domain user groups has been improved to share more code in common and log more details in case of errors.
    - The Veyon Service additionally depends on the LanmanWorkstation and LSM services to improve reliability on start.
    - Several 3rdparty libraries have been updated (Qt 5.12.11 snapshot, OpenSSL 1.1.1l, TurboJPEG 2.1.1)

Structural changes
++++++++++++++++++

In Veyon 4.6 the *Run program* feature has been renamed to *Start application* but works identically.

Configuration changes
+++++++++++++++++++++

One configuration key has been renamed in Veyon 4.6. When upgrading to Veyon 4.6 or newer this new configuration key will be populated with the value of the old key automatically.

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Old name
    - New name

  * - ``DesktopServices/PredefinedPrograms``
    - ``DesktopServices/PredefinedApplications``

Veyon 4.5
---------

Overview
++++++++

Veyon 4.5 is the release series with the most changes since Veyon 4.0. Most notably, Veyon 4.5 includes a new WebAPI plugin which allows accessing computers by 3rdparty products via HTTP. Veyon Master introduces the new monitoring panels *Slideshow* and *Spotlight*. The demo mode has been greatly extended and improved. It's now possible to share a student's screen instead of the own screen easily. In environments where multiple monitors are connected to the computer running Veyon Master, the user can now choose to share a specific monitor only. Moreover, the performance and responsiveness of the demo mode is much better thanks to the demo server now being multithreaded. At the same time Veyon 4.5 focuses on application and desktop virtualization environments by delivering extended and improved multi session support. Additionally various compatibility issues on Linux have been fixed and the file transfer plugin received a configuration page.

* Core
    - The feature plugin API has been revised.
    - The invocation of worker processes and communication with them has been improved, resulting in increased reliability of certain Veyon features such as the demo mode.
    - Session IDs are now managed internally. This allows reusing a session ID after a user session has been closed. RDP session IDs (which are increased continuously) are no longer used for calculating server port numbers.
* Configurator
    - Several parts of the user interface have been improved.
    - Settings for new Veyon Master features have been added.
* Plugins
    - Demo: The server has been refactored to be multithreaded which improves performance and responsiveness especially with many clients.
    - Demo: A feature has been added to share a user's screen instead of the own one.
    - Demo: The modes (window/fullscreen) have been made subfeatures displayed in a drop down menu.
    - Demo: A feature has been added to share only one of multiple own screens.
    - FileTransfer: A configuration page has been added allowing to configure source and destination folders.
    - RemoteAccess: The username is now displayed in the window title.
    - WebAPI: Added a new plugin offering a RESTful API for accessing Veyon Server instances.
* Linux
    - The reboot/poweroff functions now prefer using systemd-logind.
    - The reboot/poweroff functions now look for binaries in /sbin and /usr/sbin if they are not in the PATH environment variable.
    - The user session management code has been improved to start Veyon Server more reliably.
    - The screenlock feature is now working properly with most desktop environments.
* Master
    - The new Slideshow panel cycles through all computers and shows a magnified view of each computer for a short time.
    - The new Spotlight panel shows one or multiple computers in realtime. This allows keeping an eye on users requiring special attention.
    - The size of computer icons is now always adjusted automatically whenever the panel is resized or computers are added or removed.
    - States and sizes of panels are now saved when closing the program and restored upon the next start.
    - The aspect ratio of computer icons is now adjusted to the original screen sizes.
* Server
    - A notification is now shown for both incomplete and failed authentication attempts.
    - Support for external VNC servers without any authentication/password configured has been added.
* Windows
    - The Interception driver is now disabled in multi session mode to prevent issues with hanging RDP sessions.
    - The 3rdparty component UltraVNC has been updated to the latest version.
    - Several 3rdparty libraries have been updated (Qt 5.12.11 snapshot, OpenLDAP 2.4.56, OpenSSL 1.1.1h)

Due to the large number of changes, there's a medium risk for regressions. Therefore especially the initial release (v4.5.0) should be tested thoroughly before deploying.

Structural changes
++++++++++++++++++

There are no structural changes in Veyon 4.5.

Configuration changes
+++++++++++++++++++++

Several configuration keys have been renamed in Veyon 4.5. When upgrading to Veyon 4.5 or newer the new configuration keys will be populated with the values of the old keys automatically.

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Old name
    - New name

  * - ``Network/PrimaryServicePort``
    - ``Network/VeyonServerPort``

  * - ``Master/AutoAdjustGridSize``
    - ``Master/AutoAdjustIconSize``

  * - ``Master/LocalComputerHidden``
    - ``Master/HideLocalComputer``

  * - ``Master/ComputerFilterHidden``
    - ``Master/HideComputerFilter``

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

Veyon 4.3 is mostly identical to Veyon 4.2. A new plugin has been added which allows logging in a particular user remotely on all computers. The ``config`` CLI module has been improved to handle specific data types (such as JSON data and option indices) more intelligently. Upgrading to Veyon 4.3 does not require any configuration changes. Since only a new plugin has been added and some commands of the ``config`` CLI module have been extended the risk of regressions is very low.

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

Veyon 4.2 continues the Veyon 4 major release series with many internal modernizations, user interface optimizations and performance improvements in many areas. Veyon 4.2 lays the foundation for commercial add-ons offered starting in the second half of 2019. The following new features and improvements can be found in Veyon 4.2:

* Core
   - The network object management layer has been revised to allow using multi-level hierarchies in commercial add-ons.
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
   - The new file transfer plugin allows sending files to all users and open them automatically if requested.
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

In Veyon 4.2 the command line utility has been renamed to ``veyon-cli``. All occurrences of the old name ``veyon-ctl`` in your scripts and installation routines have to be replaced accordingly. On Windows there's also a new non-console version ``veyon-wcli`` which allows automating tasks without irritating command line window popups.

On Linux the systemd unit has been renamed from ``veyon-service.service`` to ``veyon.service``.

The Veyon Configurator no longer shows all configuration options per default in order to present a cleaner user interface. If you miss certain advanced options you can switch the view to :guilabel:`Advanced` through the :guilabel:`View` menu.

Configuration changes
+++++++++++++++++++++

Several configuration keys have been renamed in Veyon 4.2. When upgrading to Veyon 4.2 or newer the new configuration keys will be populated with the values of the old keys automatically.

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

The ``LocalData`` plugin has been split into the ``BuiltinDirectory`` and ``SystemUserGroups`` plugins. This allows using different data sources for access control, e.g. computers from an LDAP directory in combination with local user groups. After upgrading you should verify that the appropriate network object directory and access control user groups backend are selected as desired.

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
