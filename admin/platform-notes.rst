.. _PlatformNotes:

Platform specific notes
=======================

This chapter contains notes on platform-specific configuration options and pecularities.

.. _PlatformWindows:

Windows
-------

.. _UserLogonMechanismsWindows:

User logon mechanisms
+++++++++++++++++++++

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

.. _UserLogonMechanismsLinux:

User logon mechanisms
+++++++++++++++++++++

Per default the Veyon Server launches the Veyon Authentication helper (``veyon-auth-helper``). This small program actually performs the user authentication via `Linux PAM <https://en.wikipedia.org/wiki/Linux_PAM>`_. In almost every Linux installation several PAM services are configured and usually managed by Linux distribution specific tools. The PAM service ``login`` is used per default, i.e. authentication is performed through the modules configured in ``/etc/pam.d/login`` (Veyon 4.0/4.1 used ``/etc/pam.d/su``).

If you want to use a dedicated PAM service configuration for Veyon you can enable the :ref:`alternative user authentication mechanism <RefUserAuthenticationMechanism>` option. Once enabled the Veyon Authentication helper will use the PAM service ``veyon``, i.e. configuration is taken from ``/etc/pam.d/veyon``. This allows to use dedicated PAM modules for authenticating Veyon users.
