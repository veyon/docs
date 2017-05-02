Silent installation on Windows
==============================

Introduction
------------

The NSIS installers provided by the Veyon project can be run in silent mode. This is useful for automated deployments in larger environments and should integrate easily with most software distribution mechanisms.

By passing the command line parameter "/S" to the installer all operations will be performed silently. The same applies to the uninstaller.


Examples
--------

* Install Veyon silently:

.. code-block:: sh

	veyon-x.y.z-win64-setup.exe /S

* Uninstall Veyon silently:

.. code-block:: sh

	C:\Program Files\Veyon\uninstall.exe /S

* Specify installation directory with silent installation:

.. code-block:: sh

	veyon-x.y.z-win64-setup.exe /S /D=C:\Veyon

**Please note that due to a bug in NSIS the /D=... switch always has to be passed as last argument.**

* Automatically appy Veyon configuration from file after installation:

.. code-block:: sh

	veyon-x.y.z-win64-setup.exe /S /ApplyConfig=%cd%\MyConfig.json
  
**IMPORTANT:** You have to specify an absolute path for the configuration file as the Veyon Configurator (which is used internally for applying the configuration) is not launched with the installer directory as current directory. Therefore either use the proposed `%cd%` variable or replace it with an absolute path. 

* Silent auto installation without Master component:

.. code-block:: sh

	veyon-x.y.z-win64-setup.exe /S /NoMaster

* Clear configuration during uninstallation:

.. code-block:: sh

	C:\Program Files\Veyon\uninstall.exe /ClearConfig
