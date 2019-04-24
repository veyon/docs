.. _PlatformNotes:

Platform specific notes
=======================

This chapter contains notes on platform-specific configuration options and pecularities.

.. _PlatformWindows:

Windows
-------

General
+++++++

.. index:: SAS generation, Secure Attention Sequence, Ctrl+Alt+Del

Enable SAS generation by software (Ctrl+Alt+Del)
    On Windows per default it's impossible for applications to generate the *Secure Attention Sequence* (Ctrl+Alt+Del) in order to simulate the press of these keys. When enabling this option a policy is written to the Windows registry which changes this behavior. It is recommended to leave this option enabled in order to be able to send :kbd:`Ctrl+Alt+Del` when remote controlling a computer. Otherwise it may be impossible to unlock a remotely controlled computer or logging on a user since in most cases the shortcut :kbd:`Ctrl+Alt+Del` has to be issued first.

    **Default:** *enabled*

.. index:: User authentication, Authentication mechanism

User authentication
+++++++++++++++++++

Veyon implements two different mechanisms to authenticate a user (i.e. verify its username and password) on Windows when using :ref:`logon authentication <ConfLogonAuthentication>`. The default mechanism has been used successfully for many years. It is based on the `Security Support Provider Interface <https://en.wikipedia.org/wiki/Security_Support_Provider_Interface>`_ and works in almost every environment. To verify that the mechanisms works properly in your environment you can change the :ref:`authentication method <RefAuthentication>` to :guilabel:`Logon authentication` and click the :guilabel:`Test` button.

Use alternative user authentication mechanism
    In case the default mechanism is not working in your environment you can try to use an alternative fallback mechanism. This mechanism utilizes a high level function in the operating system which performs a network user logon internally to verify the user credentials. This logon process can be slower than the simple authentication performed by the default mechanism. It should therefore only be used as a last resort.

    **Default:** *disabled*

Screen lock
+++++++++++

The screen lock feature per default disables all input devices and hides parts of the operating system user interface. This behaviour can be changed for cases where parts of the operating system user interface no longer function properly after a computer is unlocked.

Hide taskbar
    This option defines whether the taskbar and the start button should be disabled and hidden by the screen lock feature.

    **Default:** *enabled*

Hide start menu
    This option defines whether the start menu should be disabled and hidden by the screen lock feature.

    **Default:** *enabled*

Hide desktop
    This option defines whether the desktop should be disabled and hidden by the screen lock feature.

    **Default:** *enabled*

.. _UltraVNCServerSettings:

UltraVNC server settings
++++++++++++++++++++++++

Veyon uses a lightweight version of UltraVNC as a builtin VNC server on Windows. While the Veyon Server manages most UltraVNC settings on its own a few performance and system integration related settings can be changed manually. In general you should not need to change the default values unless you encounter problems while accessing or controlling remote computers.

Enable capturing of layered (semi-transparent) windows
    When using the traditional screen mirroring driver (i.e. Windows 7 is used or Desktop Duplication Engine is disabled) the VNC server can't capture semi-transparent windows. This can result in large parts of the screen not being captured if the Windows Aero theme is used. To circumvent this issue capturing of semi-transparent windows is enabled per default. Besides potentially lower performance this can also make the mouse cursor flicker on client computers.

    **Default:** *enabled*

Enable multi monitor support
    This option says whether to capture only the first of all monitors. On client computers it usually is desirable to see all monitors. On master computers this option can be disabled in order to broadcast only the contents of the first screen in demo mode. This way the teacher does not have to share its whole desktop. Broadcasting less screen data also improves performance.

    **Default:** *enabled*

Enable Desktop Duplication Engine on Windows 8 and newer
    When this option is enabled UltraVNC uses the new Desktop Duplication Engine on Windows 8 and newer. This engine is a new driver backend for capturing screen data and provides much better performance compared to the traditional screen mirroring driver. Additionally it also captures windows with DirectX-rendered content, e.g. allowing to view and control DirectX-based CAD applications remotely.

    **Default:** *enabled*

Poll full screen (leave this enabled per default)
    If no suitable driver for capturing screen data is found this determines whether to scan the whole screen for changed pixels. Otherwise only the foreground window is scanned which can reduce CPU load. It should only be disabled as a last resort if CPU load is an issue.

    **Default:** *enabled*

Low accuracy (turbo mode)
    Enabling this option will make the VNC server use a scan raster to detect changed screen areas which need to be sent to the viewer. As changes of individual pixels might only be detected every 4th scan pass, partial updates can be delayed by a few hundred milliseconds in some cases. At the same time this option greatly improves performance and reduces the CPU load caused by the VNC server.

    **Default:** *enabled*

.. _PlatformLinux:

Linux
-----

User authentication
+++++++++++++++++++

In order to authenticate a user (i.e. verify its username and password) on Linux the Veyon Server launches the Veyon Authentication helper (``veyon-auth-helper``). This small program actually performs the user authentication via `Linux PAM <https://en.wikipedia.org/wiki/Linux_PAM>`_. In almost every Linux installation several PAM services are configured and usually managed by Linux distribution specific tools. Veyon uses the PAM service ``login`` per default, i.e. authentication is performed through the modules configured in ``/etc/pam.d/login`` (Veyon 4.0/4.1 used ``/etc/pam.d/su``).

Custom PAM service for user authentication
    If you want to use a dedicated PAM service configuration to authenticate Veyon users you can enter a custom PAM service name here. A simple identifier such as ``veyon`` should be used. If for example set to ``veyon``, the Veyon Authentication helper will use the PAM service ``veyon``, i.e. configuration is taken from the file ``/etc/pam.d/veyon``. Please make sure to provide the PAM service configuration file before using this setting. Otherwise authentication will always fail.

    To verify that the custom PAM service is set up properly you can change the :ref:`authentication method <RefAuthentication>` to :guilabel:`Logon authentication` and click the :guilabel:`Test` button.
