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

* Automatically appy iTALC configuration from file after installation (replace `%cd%` with a different absolute path if desired):

  ```shell
  italc-x.y.z-win64-setup.exe /S /ApplyConfig=%cd%\MyConfig.xml
  ```
  
