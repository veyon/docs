.. _Installation:

Installation
============

Hardware and software requirements
----------------------------------

Veyon is designed to run on standard computers running Windows or Linux. The :index:`minimum requirements` for the hardware depend on the usage scenario and size of the environment in which Veyon is deployed. While there are no special requirements for client computers all master computers should be equipped with enough RAM and processors to monitor the desired number of client computers.

* At least 2 GB RAM - Veyon Master requires 20-30 MB per client computer, depending on the client's screen resolution
* Multi-core system (2-4 CPUs) highly recommended

All computers must be connected through a TCP-/IP-compatible network. Both wired and wireless network connections work. For using Veyon with more than 10 computers a Gigabit network is recommended, otherwise the performance of the demo mode feature (see user manual) may not be satisfactory. The same applies to wireless networks (:index:`Wifi`) where at least the IEEE 802.11n standard should be used.

On the software side an up-to-date :index:`operating system` supported by the vendor or the community must be run. Those include:

* Windows 7, 8 or 10 (32/64 Bit)
* Linux with at least version 5.5 of Qt
    * Debian 9 or higher
    * Ubuntu 16.04 or higher
    * openSUSE 42.2 or higher
    * Fedora 24 or higher
    * CentOS 7.3 or higher

Mixing Windows and Linux computers is no problem.

Preparing the installation
--------------------------

First of all download the installation files for your platform from the `Veyon download page <https://download.veyon.io>`_. For Windows computers it's recommended to use the 64-bit variant (`win64`). For 32-bit-installations, the 32-bit variant (`win32`) has to be used.

Installation on a Windows computer
----------------------------------

Run the :index:`installer file` with administrative privileges and follow the displayed instructions. On all computers on which no master application is required (e.g. student computers) you uncheck the component *Veyon Master* in the *Choose components* dialogue.

After the installation is finished the *Veyon Configurator* is launched by default. This program allows to set up and customize your Veyon installation. In the next chapter :ref:`Configuration` the usage is described in detail.

Installation on a Linux computer
--------------------------------

The installation of Veyon on :index:`Linux` heavily depends on the distribution used. If Veyon is available in the package archive of your distribution you can install the program through the appropriate software management application. Alternatively up-to-date binary packages for different distributions are available at the `Veyon download page <https://download.veyon.io>`_. In all other cases it's always possible to compile and install a current version of Veyon from source. For further information please visit the `Github page of Veyon <https://github.com/veyon/veyon/>`_.


.. index:: automated installation, unattended installation, silent installation, deinstallation, uninstalling
.. _AutoInstall:

Automated installation (silent installation)
--------------------------------------------

Basics
++++++

The Veyon Windows installer provided by the community can be executed in *silent* mode, meaning that there is no user interaction and the installation is performed automatically. This is especially helpful for automated deployments in larger environments. Veyon can thus be easily integrated with all common software distribution/deployment mechanisms.

After the :index:`installer` has been run with command line parameter ``/S``, all further operations are executed without requests for feedback or output. The same applies to the uninstaller.

Examples
++++++++

Install Veyon in *silent* mode:

.. code-block:: none

	veyon-x.y.z-win64-setup.exe /S

Uninstall Veyon in *silent* mode:

.. code-block:: none

	C:\Program Files\Veyon\uninstall.exe /S

Specify an :index:`installation directory` for an automated installation:

.. code-block:: none

	veyon-x.y.z-win64-setup.exe /S /D=C:\Veyon

.. note:: Because of a shortcoming of the installer software (NSIS) the option ``/D=...`` always has to be the last argument.

.. _InstallationConfigurationImport:

Apply Veyon configuration automatically after the installation:

.. code-block:: none

	veyon-x.y.z-win64-setup.exe /S /ApplyConfig=%cd%\MyConfig.json

.. important:: You must provide an absolute path to the :index:`configuration file`, since the internally called command line tool (*Veyon Control*) is not listed as working directory in the installation directory. Please use either the suggested ``%cd``-variable or replace with an absolute path.

Automated installation without Veyon Master:

.. code-block:: none

	veyon-x.y.z-win64-setup.exe /S /NoMaster

Delete all Veyon-related settings during uninstalling:

.. code-block:: none

	C:\Program Files\Veyon\uninstall.exe /ClearConfig
