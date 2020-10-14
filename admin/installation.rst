.. _Installation:

Installation
============

Hardware and software requirements
----------------------------------

.. index:: Minimum requirements, Operating system

Veyon is designed to run on standard computers running Windows or Linux. The minimum requirements for the hardware depend on the usage scenario and size of the environment in which Veyon is deployed. While there are no special requirements for client computers all master computers should be equipped with enough RAM and CPU cores to monitor the desired number of client computers.

* At least 2 GB RAM - Veyon Master requires 20-30 MB per client computer, depending on the client's screen resolution
* Multi-core system (2-4 CPU cores) highly recommended

.. index:: Wifi

All computers must be connected through a TCP-/IP-compatible network. Both wired and wireless network connections work. For using Veyon with more than 10 computers a Gigabit network is recommended, otherwise the performance of the demo mode feature (see user manual) may not be satisfactory. The same applies to wireless networks (*Wifi*) where at least the IEEE 802.11n standard should be used.

From a software point of view, an up-to-date operating system supported by the manufacturer or the community must be used. The following operating systems are supported:

* Windows 7, 8 or 10 (32/64 Bit)
* Linux with at least version 5.5 of Qt
    * Debian 9 or higher
    * Ubuntu 16.04 or higher
    * openSUSE 42.2 or higher
    * Fedora 24 or higher
    * CentOS 7.3 or higher

The mixed operation of Veyon on Windows and Linux computers works without any restrictions.

Preparing the installation
--------------------------

First of all download the installation files for your platform from the `Veyon download page <https://download.veyon.io>`_. For Windows computers it is recommended to use the 64-bit version (`win64`). For 32-bit installations the 32-bit version (`win32`) has to be used.

Installation on a Windows computer
----------------------------------

Run the installer file with administrative privileges and follow the displayed instructions. On computers that do not require the Veyon Master application (e.g. student computers) you can deselect the component *Veyon Master* in the *Choose Components* dialog.

After the installation is finished the *Veyon Configurator* is started by default. This program allows setting up and customize your Veyon installation. In the next chapter :ref:`Configuration` the usage is described in detail.

Installation on a Linux computer
--------------------------------

.. index:: Linux

The installation of Veyon on Linux differs depending on the distribution used. If Veyon is available in the package archive of your distribution you can install the program through the appropriate software management application. Alternatively up-to-date binary packages for most major distributions are available at the `Veyon download page <https://download.veyon.io>`_. In all other cases it's always possible to build and install a current version of Veyon from source. For further information please visit the `Github page of Veyon <https://github.com/veyon/veyon/>`_.


.. index:: Automated installation, Unattended installation, Silent installation, Uninstallation, Uninstalling
.. _AutoInstall:

Automated/silent installation
-----------------------------

Basics
++++++

.. index:. Windows installer

The Veyon Windows installer provided by the community can be executed in *silent* mode, meaning that there is no user interaction and the installation is performed automatically. This is especially useful for automated deployments in larger environments. This way Veyon can be easily integrated with all common software distribution solutions and mechanisms.

By running the installer with the command line parameter ``/S``, all operations are performed without further questions and dialogs. The same applies to the uninstaller.

Examples
++++++++

Install Veyon in *silent* mode:

.. code-block:: none

    veyon-x.y.z-win64-setup.exe /S

Uninstall Veyon in *silent* mode:

.. code-block:: none

    C:\Program Files\Veyon\uninstall.exe /S

.. index:: Installation directory

Specify an installation directory for an automated installation:

.. code-block:: none

    veyon-x.y.z-win64-setup.exe /S /D=C:\Veyon

.. note:: Because of a shortcoming of the installer software (NSIS) the option ``/D=...`` always has to be the last argument.

.. _InstallationConfigurationImport:

Import and apply a given Veyon configuration automatically after the installation:

.. code-block:: none

    veyon-x.y.z-win64-setup.exe /S /ApplyConfig=%cd%\MyConfig.json

.. important:: You must specify an absolute path for the configuration file, since the internally called command line tool (*Veyon CLI*) is executed with in a different working directory. Please use either the suggested ``%cd%``-variable or replace with an absolute path.

Automated installation without the Veyon Master component:

.. code-block:: none

    veyon-x.y.z-win64-setup.exe /S /NoMaster

Automated installation without the Interception driver:

.. code-block:: none

    veyon-x.y.z-win64-setup.exe /S /NoInterception

Delete all Veyon-related settings during uninstallation:

.. code-block:: none

    C:\Program Files\Veyon\uninstall.exe /ClearConfig
