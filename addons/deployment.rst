.. _DeployingAddons:

Deployment
==========

Initial steps
-------------

1. Install Veyon on the Master computer
2. Install Veyon addons on the Master computer
3. Import the license file(s)
4. Make changes to the configuration as desired
5. Export the configuration


Automated/silent installation
-----------------------------

Like Veyon itself the addons can also be installed in *silent mode* by passing the ``/S`` parameter and optionally ``/D=...``. Please refer to chapter :ref:`AutoInstall` in the administrator manual for details.

Deploying licenses
------------------

Since all licenses are part of a Veyon configuration they can be deployed easily using the well-known mechanisms for :ref:`importing the configuration during installation <InstallationConfigurationImport>`. A configuration containing the licenses can already be imported/applied when the addons are not yet installed. This will make the addons work instantly whenever they get installed later.

