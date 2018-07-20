.. _Installation:

Installation
============

System Requirements
-------------------

Veyon is designed to run on standard computers running Windows or Linux. There are no special :index:`minimum requirements` for the hardware. However, an up-to-date :index:`operating system` supported by the manufacturer or the community must be run. Those include:

* Windows 7, 8 or 10 (32/64 Bit)
* Linux with at least version 5.5 of Qt
    * Debian 9 or higher
    * Ubuntu 16.04 or higher
    * openSUSE 42.2 or higher
    * Fedora 24 or higher
    * CentOS 7.3 or higher

:index:`Parallel usage` of Windows and Linux computers is easily possible. All computers must be connected through a TCP-/IP-compatible network, where the transmission technology (wired/wireless) is only of importance concerning the maximum performance. For the use of Veyon with more than 10 computers a Gigabit network is recommended, otherwise the demo mode (see user manual) may not work well enough. The same applies to wireless networks (:index:`Wifi`) where at least standard IEEE 802.11n should be used.


Preparing the Installation
--------------------------

First of all download the installation files for your platform from the Veyon download page [#releases]_.  For Windows computers it's recommended to use the 64-bit variant (`win64`). For 32-bit-installations, the 32-bit variant (`win32`) has to be used.

.. [#releases] https://github.com/veyon/veyon/releases/

Installation on a Windows computer
----------------------------------

Run the :index:`installation file` with administrator privileges and follow the instructions on the screen. On computers on which no master application is required (e.g. student computers) you uncheck the component *Veyon Master* in the *Choose components* dialogue.

After the installation is finished the *Veyon Configurator* is started by default. This is a tool for setting up and customizing your installation. In the next chapter :ref:`Configuration` the usage is described in detail.

Installation on a Linux computer
--------------------------------

The installation of Veyon on :index:`Linux` strongly depends on the distribution used. Usually you can install the program through your software management, if Veyon is available in the package archive of your distribution. Otherwise there is always the possibility to compile and install a current version of Veyon from the sources and install it afterwards. For further information please visit the project's page on github [#github].

.. [#github] https://github.com/veyon/veyon/


.. index:: automated installation, unattended installation, silent installation, deinstallation, uninstalling
.. _AutoInstall:

Automated installation (silent installation)
--------------------------------------------

Basics
++++++

The Veyon Windows installer provided by the community can be executed in *silent* mode, meaning that there is no user interaction and installation is done automatically. This is especially helpful for automated deployments in larger environments. Veyon can thus be easily integrated with all common software distribution/deployment mechanisms.

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
