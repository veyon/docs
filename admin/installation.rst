.. _Installation:

Installation
============

System Requirements
-------------------

Veyon is designed for operating on standard computers running Windows or Linux. There are no special
:index:`minimum requirements` for the hardware. However, an up-to-date :index:`operating system` supported
by the manufacturer or the community must be run. Those include:

* Windows 7, 8 or 10 (32/64 Bit)
* Linux with Qt 5.6 or newer
    * Debian 9
    * Ubuntu 16.04
    * openSUSE 42.2
    * Fedora 24
  
:index:`Parallel usage` of Windows and Linux computers is easily possible.
All computers must be connected to each other through a TCP-/IP-compatible network, however, transmission
technology (wired vs. wireless) is only of importance concerning the maximum performance. A gigabit network is
strongly recommended for environments that run Veyon on more than 10 computers, since the demo mode (see 
user manual) may otherwise not be performant enough. The same holds true for wireless networks (:index:`WLAN`) where
at least standard IEEE 802.11n should be used.  


Preparing the Installation
--------------------------

At first download the installation files for your platform from the Veyon download page [#releases]_. 
For Windows computers we recommend using the 64-bit-option (`win64`). 
For 32-bit-installations, the 32-bit-option (`win32`) has to be used.

.. [#releases] https://github.com/veyon/veyon/releases/

Installation on a Windows-Computer
----------------------------------

Execute the :index:`installation file` with administrator privileges and follow the instructions. For computers
that do not need a master application (e.g. student computers) you may uncheck the component *Veyon Master* in the
*Choose Components* dialogue.

After successful completion of the installation by default the *Veyon Configurator*, a tool for configuring and customizing
your installation, is started. Its usage is explained in detail in the (upcoming) chapter :ref:`Configuration`. 

Installation on a Linux-Computer
--------------------------------

The installation procedure for Veyon under :index:`Linux` vastly depends on the distribution used. 
Usually you can download the program through your software management, if Veyon is available for the 
packet archive of your distribution. However, there is always the possibility of compiling a current version
of Veyon from the sources and install it thereafter. For further information please visit the project's page 
on github [#github]. 

.. [#github] https://github.com/veyon/veyon/


.. index:: automated installation, unattended installation, silent installation, deinstallation, uninstalling
.. _AutoInstall:

Automated Installation (silent installation)
--------------------------------------------

Basics
++++++

The Veyon Windows installer provided by the community can be executed in *silent* mode, meaning that there is
no user interaction and installation is done automatically. This is especially helpful for automated deployment
in larger environments. Veyon is therefore easily integrated with all common software deployment mechanisms. 

After the :index:`installer` has been run with command line parameter ``/S``, all further operations are 
executed without requests for feedback or output. The same holds true for the unstalling program.

Examples
++++++++

Installation of Veyon in *silent* mode:

.. code-block:: none

	veyon-x.y.z-win64-setup.exe /S

Uninstalling of Veyon in *silent* mode:

.. code-block:: none

	C:\Program Files\Veyon\uninstall.exe /S

Specify an :index:`installation directory` for an automated installation:

.. code-block:: none

	veyon-x.y.z-win64-setup.exe /S /D=C:\Veyon

.. note:: Because of a shortcoming of the installer software (NSIS) the option ``\D=...`` always has to be the last argument.

.. _InstallationConfigurationImport:

Apply Veyon configuration automatically after the installation: 

.. code-block:: none

	veyon-x.y.z-win64-setup.exe /S /ApplyConfig=%cd%\MyConfig.json
  
.. important:: You must provide an absolute path to the :index:`configuration file`, since the internally called command line tool (*Veyon Control*) is not listed as working directory in the installation directory. Please use either the suggested ``%cd``-variable or replace with an absolute path.

Automated installation without applying Master application:

.. code-block:: none

	veyon-x.y.z-win64-setup.exe /S /NoMaster

Delete all Veyon-related settings during uninstalling:

.. code-block:: none

	C:\Program Files\Veyon\uninstall.exe /ClearConfig
