# Silent installation on Windows

## Introduction

The NSIS installers provided by the iTALC project can be run in silent mode. This is useful for automated deployments in larger environments and should integrate easily with most software distribution mechanisms.

By passing the command line parameter "/S" to the installer all operations will be performed silently. The same applies to the uninstaller.


## Examples

* Install iTALC silently:

  ```shell
  italc-x.y.z-win64-setup.exe /S
  ```

* Uninstall iTALC silently:

  ```shell
  C:\Program Files\iTALC\uninstall.exe /S
  ```

* Specify installation directory with silent installation:

  ```shell
  italc-x.y.z-win64-setup.exe /S /D=C:\iTALC
  ```

  **Please note that due to a bug in NSIS the `/D=...` switch always has to be passed as last argument.**

* Automatically appy iTALC configuration from file after installation:

  ```shell
  italc-x.y.z-win64-setup.exe /S /ApplyConfig=%cd%\MyConfig.xml
  ```
  
  **IMPORTANT:** You have to specify an absolute path for the configuration file as the iTALC Configurator (which is used internally for applying the configuration) is not launched with the installer directory as current directory. Therefore either use the proposed `%cd%` variable or replace it with an absolute path. 

* Silent auto installation without Master component:

  ```shell
  italc-x.y.z-win64-setup.exe /S /NoMaster
  ```

* Clear configuration during uninstallation:

  ```shell
  C:\Program Files\iTALC\uninstall.exe /ClearConfig
  ```
