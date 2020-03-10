.. _Licensing:

Licensing
=========

General
-------

All commercial addons for Veyon require a valid license. A license is valid for a specific addon and a certain installation ID. The unique installation ID is created upon the first installation of Veyon and is part of the program configuration. You should never change the installation ID e.g. by editing the configuration JSON file since this will make your licensed addons not work any longer.

Installing a license
--------------------

After having received one or multiple license files they can be installed through the :guilabel:`Licensing` configuration page in the Veyon Configurator. Click on the :guilabel:`+` button to select the license file and import it. After a successful import the licenses and additional information show up in the table. Click on the :guilabel:`Apply` button to save the imported licenses permanently.

In order to access the licensed addons you have to restart all Veyon-related program components. Usually restarting the Veyon Configurator is sufficient since you'll first have to configure the new addons anyway.

Transferring installed licenses to other computers
--------------------------------------------------

Some addons require a valid license on all involved computers. For example the Internet Access Control addon not only adds control elements to Veyon Master but also implements the actual internet access control functionality on client computers.

In order to transfer licenses to other computers you have to export the configuration on the computer on which you imported the licenses. The exported configuration then contains both the installation ID and the imported licenses. It can be imported on all client computers as desired. See chapter :ref:`ConfImportExport` in the administrator manual for details.

Command line interface
----------------------

There's a CLI module ``licensing`` which allows managing licenses at the command line:

.. describe:: add <LICENSE FILE>

    This command imports the license in the given file into the local configuration.

.. describe:: show

    This command shows details on all installed licenses.

.. describe:: remove <LICENSE ID>

    This command removes the license with the specified ID.
