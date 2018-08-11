.. _Configuration:

Configuration
=============

To start the setup, start the Veyon Configurator if that has not already been done automatically upon completing the installation. With this program it is possible to set up and customize a local Veyon installation. The graphical user interface is divided into different topic or component related configuration pages. Depending on the installed plugins there may be additional configuration pages.

.. image:: images/configurator.png
   :scale: 75 %
   :align: center

The :ref:`ConfigurationReference` describes all configuration pages and configuration options with their respective meanings.


Overview
--------

The basic settings in the configuration page :ref:`RefGeneral` affect all :ref:`components` of Veyon. These include settings for the :ref:`RefUserInterface`, :ref:`RefLogging`, :ref:`RefAuthentication` as well as the :ref:`RefNetworkObjectDirectory` which stores the rooms and computers displayed in the Veyon Master.

The settings in the configuration page :ref:`RefService` influence the functionality of the Veyon Service and are used for fine-tuning and adaptation to implement special application scenarious. For smooth operation the default settings should normally not be changed.

All setting on configuration page :ref:`RefMaster` only affect the behavior and functions of the Veyon Master and apply system-wide for all users.

.. hint:: For a :index:`quick start` to get to know the software you only need to add a room and individual computers in configuration page :ref:`ConfRoomsAndComputers`. After the configuration has been :ref:`exported to all computers <ConfImportExport>` the Veyon Master can already be started and used. It should be ensured that the user used at logon exists with the same password on all computers.

.. index:: Authentication, Authentication methods

.. _ConfAuthentication:

Authentication
--------------

In order to access a computer running the Veyon Service the accessing user has to authenticate himself at first, meaning that he has to prove his identity resp. usage authorization. Otherwise an unrestricted access from every user on every computer running the Veyon Service would be possible. Access without authentication is not possible. The configuration can be done in the configuration page :ref:`RefGeneral` in section :ref:`RefAuthentication` in Veyon Configurator.

.. _ConfAuthenticationMethods:

Authentication methods
++++++++++++++++++++++

Basically Veyon offers two different authentication methods, key file authentication and logon authentication.

**Key file authentication** is based on `Public-Key-Cryptography <https://en.wikipedia.org/wiki/Public-key_cryptography>`_, meaning that a public key and a corresponding private key are used. Thereby the private key is just accessible for specific users. In case of a :index:`connection request` the Veyon Service sends a random char sequence to the Veyon Master and the Master signs this random data with his private key. The :index:`signature` is sent back to the Veyon Service and checked with the corresponding public key. This check is only successful, if the signature has been generated with the matching private key. In this case the authenticity of the signing party is guaranteed. If the signature check fails, the connection is closed.

In case of the **logon authentication** the counterpart encrypts his :index:`user name` and :index:`password` for the Veyon Service. Using this :index:`logon data` the Veyon Service attempts to connect to the local system. If the attempt fails, the conection is closed. Otherwise user name and password are correct, such that the authenticity of the counterpart is guaranteed.

Both methods have advantages and disadvantages so the choice of the right method depends on the environment, security requirements and desire for user comfort.

.. index:: key file authentication, public-key-cryptography, public key, private key, key file

.. _ConfKeyFileAuthentication:

**Key file authentication**

+-------------------------------------------------+-------------------------------------------------+
| Advantages                                      | Disadvantages                                   |
+=================================================+=================================================+
| * no login with username and password required  | * more effort during configuration              |
|   when starting Veyon Master                    | * user identity can not be assured even after   |
| * access to computers can be centrally handled  |   successful signature check                    |
|   by access rights to the file containing       | * exchange of compromised key pairs must be     |
|   the private key                               |   done system-wide                              |
+-------------------------------------------------+-------------------------------------------------+


.. index:: logon-authentication, username, password

.. _ConfLogonAuthentication:

**Logon authentication**

+-------------------------------------------------+-------------------------------------------------+
| Advantages                                      | Disadvantages                                   |
+=================================================+=================================================+
| * easy and effortless setup                     | * login with username and password necessary    |
| * identity of counterpart can be assured,       |   whenever Veyon Master is used                 |
|   allowing for effective and secure access      |                                                 |
|   control                                       |                                                 |
+-------------------------------------------------+-------------------------------------------------+

The authentication method can be chosen and configured as described in section :ref:`RefAuthentication` of the configuration reference.


Key management
++++++++++++++

In order to use the key file authentication, at first a :index:`key pair` consisting of a public and a private key has to be generated.  The configuration page :ref:`RefAuthenticationKeys` is available for this purpose. A new key pair is generated via the `guilabel:`Create key pair` button. A short, concise term such as ``teacher`` should be chosen as the name. An access group must then be set for both private and public keys. The private key access group may only include users who are to be allowed to access other computers via the Veyon Master. The public key should be assigned to a global access group so that the key is readable by all users and the operating system.

As soon as the keyfile-authentication is set up and working with one client computer, the keys can be deposited on a shared network drive and the :ref:`RefKeyFileDirectories` can be changed accordingly. Now the client computers just have to import the Veyon configuration, however, the files containing the keys don't have to be manually imported.

.. attention:: The private key file shall only be accessible for users that should have access to other computers. If the file is stored on a network drive, it must be thoroughly ensured that file access is restricted with an ACL or similar!


.. index:: computer access control

.. _ConfAccessControl:

Access control
--------------

With the help of the :index:`Access control` module it can be specified in detail which users may access a computer. Access control is performed during :index:`connection initialisation` after the authentication.  While authentication assures the authenticity of an accessing user, the access control functionality restricts :index:`computer access` to authorised users, e.g. teachers.

Setup is done from the :guilabel:`Access control` configuration page and is described in detail in chapter :ref:`AccessControlRules`.

.. important:: The configuration of the access control is like all settings part of the local Veyon configuration. The configuration must therefore be :ref:`transferred to all other computers <ConfImportExport>` to work properly.


.. index:: Rooms and computers

.. _ConfRoomsAndComputers:

Rooms & computers
-----------------

In the configuration page :guilabel:`Rooms & computers` you can create the :index:`rooms and computers` that are displayed in Veyon Master when the :ref:`RefNetworkObjectDirectory`-backend *Builtin* is used. Unlike backends such as :ref:`LDAP <LDAP>` this information is stored in the local configuration and must therefore be transferred to all computers.

The configuration page consists of two lists. The left list contains all configured rooms. Using the two buttons below the list, rooms may be added or deleted. Existing rooms can be edited and renamed by double-clicking.

The list on the right contains a computers that are stored for the currently selected rooms. Using the two buttons below the list, computers may be added or deleted. The individual cells in the table can be edited by double-clicking. A name and a computer/IP-address has to be specified for each computer. In case the Veyon function `Wake-on-LAN <https://en.wikipedia.org/wiki/Wake-on-LAN>`_ shall be used, the corresponding MAC address has also to be provided. Otherwise this column can be left blank.


LDAP
----

All information about connecting Veyon to an LDAP-compatible server such as *OpenLDAP* or *Active Directory* can be found in chapter :ref:`LDAP`.


.. index:: export configuration, import configuration, load settings, save settings

.. _ConfImportExport:

Importing/exporting a configuration
-----------------------------------

An imported prerequisite for the use of Veyon is an identical configuration on all computers. A transfer of the Veyon configuration to another computer can be done manually at first, but should be automated later. Different methods are available for both ways.

In the Veyon Configurator you can find the entry :guilabel:`Save settings to file` in menu :guilabel:`File`. This entry can be used to export the current configuration in JSON format to a file. This file can be imported to another computer using the entry :guilabel:`Load settings from file` in the same menu. Please note, that the settings are loaded into the user interface during the import, but are only applied and saved in the system only after pressing the :guilabel:`Apply` button.

The :ref:`ConfigurationManagement` module of the :ref:`CommandLineInterface` can be used to automate or script both configuration import and export.

Additionally, when performing an :ref:`automated installation <AutoInstall>` the configuration can be imported without any further interaction. In the example section you find an :ref:`Example <InstallationConfigurationImport>` for the install parameter ``/ApplyConfig``.


.. index:: reset configuration, reset settings, delete configuration

.. _ConfClear:

Reset configuration
-------------------

In some error situations it may be advisable to reset the Veyon configuration completely and then restart with the default values. For this purpose you can use the entry :guilabel:`Reset configuration` in the :guilabel:`File` menu within Veyon Configurator.

Alternatively the configuration can also be reset using the :ref:`ConfigurationManagement` within the :ref:`CommandLineInterface` module.

Furthermore the saved configuration can be reset on operating system level. Under Linux the file ``etc/xdg/Veyon Solutions/Veyon.conf`` has to be deleted, whereas under Windows the registry key ``HKLM\Software\Veyon Solutions`` and all of its subkeys have to be deleted.
