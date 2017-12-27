.. _Configuration:

Configuration
=============

To commence the configuration, start Veyon Configurator if that has not been done automatically upon completing
the installation. This program allows you to configure and customize a local Veyon installation. Thereby the graphical
user interface is divided into several topic or component related configuration pages. Depending on the 
installed plugins there may be additional configuration pages.

.. image:: images/configurator.png
   :scale: 75 %
   :align: center

In the :ref:`Configuration Reference` you can find a detailed description of all configuration pages and configuration options with
their respective meanings. 


Overview
--------

The basic configurations on configuration page :ref:`General` refer to all :ref:`components` of Veyon. This 
includes settings of :ref:`user interface`, :ref:`logging` and the :ref:`network object directory` in which the
rooms and computers displayed in the Master are located.

The setting on configuration page :ref:`Service Configuration` influence the functionality of the Veyon Service
and serve for fine tuning and customization for implementation of special scenarios. For smooth operation the 
default settings should normally not be changed.  

All setting on configuration page :ref:`Master Configuration` concern only behavior and functionality of the 
Veyon Master and apply system-wide for all users. 

.. hint:: For a :index:`quick start` to get to know the software you just have to activate the :ref:`Logon authentication <LogonAuthentication>` on configuration page :ref:`Authentication Configuration` and add one room and some computers on configuration page :ref:`Local Data`. After the configuration has been :ref:`exported to all computers <ImportExportConfiguration>` the Veyon Master can already be started and used.


.. index:: Authentication, Authentication methods

.. _Authentication:

Authentication
--------------

In order to access a computer running the Veyon Service the accessing user has to authenticate himself at first,
meaning that he has to prove his identity resp. usage authorization. Otherwise an unrestricted access from every
user on every computer running the Veyon Service would be possible. Access without authentication is not possible.
The configuration can be done on configuration page :ref:`Authentication Configuration` in Veyon Configurator.

.. _Authentication methods:

Authentication Methods
++++++++++++++++++++++

In essence Veyon offers two different authentication methods, the keyfile authentication and logon authentication,
that may be used singly or in parallel. 

**Keyfile authentication** is based on `Public-Key-Cryptography <https://en.wikipedia.org/wiki/Public-key_cryptography>`_,
meaning that a public key and a respective private key are used. Thereby the private key is just accessible for
specific users. In case of a :index:`connection request` the Veyon Service sends a random char sequence to the
Veyon Master and the Master signs this random data with his private key. The :index:`signature` is sent back to
the Veyon Service and checked with the corresponding public key. This check is only successful, if the signature
has been generated with the matching private key. In this case the authenticity of the signing party is guaranteed.
If the signature check fails, the connection is closed.

In case of the **logon authentication** the counterpart encrypts his :index:`user name` and :index:`password`
for the Veyon Service. Using this :index:`logon data` the Veyon Service attempts to connect to the local system. 
If the attempt fails, the conection is closed. Otherwise user name and password are correct, such that the 
authenticity of the counterpart is guaranteed.

Both methods have their respective assets and drawbacks. Thus the better choice depends on the environment,
the security requirement and desire for user comfort. 

.. index:: keyfile-authentication, public-key-cryptography, public key, private key, keyfile 

.. _KeyAuthentication:

**Keyfile authentication**

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

.. _LogonAuthentication:

**Logon authentication**

+-------------------------------------------------+-------------------------------------------------+
| Advantages                                      | Disadvantages                                   |
+=================================================+=================================================+
| * configuration with low expenditure            | * login with username and password necessary    |
| * identity of counterpart can be assured,       |   whenever Veyon Master is used                 |
|   allowing for effective and secure access      |                                                 |
|   control                                       |                                                 |
+-------------------------------------------------+-------------------------------------------------+

The chosen authentication method can be activated and configured as described in section :ref:`authentication configuration`
of the configuration reference. 


Key Management
++++++++++++++

In order to use the keyfile-authentication, at first a :index:`key pair` consisting of a public and a private key
has to be generated. For this purpose you can use the according assistant. Start the assistant and follow the
proposed steps. 

As soon as the keyfile-authentication is set up and working with one client computer, the keys can be deposited
on a shared network drive and the :ref:`Base Directories <BaseDirectories>` can be changed accordingly. 
Now the client computers just have to import the Veyon configuration, however, the files containing the keys
don't have to be manually imported. 

.. attention:: The private key file shall only be accessible for users that should have access to other computers. If the file is stored on a network drive, it must be thoroughly ensured that file access is restricted with an ACL or similar!


.. index:: computer access control

.. _AccessControl:

Access Control
--------------

With the help of the :index:`Access Control` module it can be specified in detail which users may access a 
computer. Access control is carried out during :index:`connection initialisation` after the authentication.
Whilst authentication assures the authenticity of an accessing user, the access control functionality restricts
:index:`computer access` to authorised users, e.g. teachers. 

Configuration can be done via configuration page :guilabel:`Access Control` and is described in detail in section
:ref:`Access Control` in the configuration reference. 

.. important:: As with all other settings, the configuration of access control is part of the local Veyon configuration. Hence the configuration must be :ref:`exported to all other computers <ImportExportConfiguration>` in order to work properly.  


.. index:: local data

.. _LocalData:

Local Data
----------

On configuration page :guilabel:`Local Data` the :index:`Rooms and Computers` can be created, such that they
can be displayed in Veyon Master if the :ref:`network object directory`-backend *Standard* is used. 
In contrast to backend such as :ref:`LDAP <LDAP>` this information is stored in the local configuration
and therefore must be transmitted to all computers. 

The configuration page consists of two lists. The left list contains all configured rooms. Using the two 
buttons below the list, rooms may be added or deleted. Existing rooms can be edited and renamed with a double-click.

The right list contains a computers that are based in the currently selected rooms. Using the two buttons below
the list, computers may be added or deleted. The single lies in the table can be edited with a double-click. For
each computer a name and a computer/IP-address has to be provided. In case the Veyon function
`Wake-on-LAN <https://en.wikipedia.org/wiki/Wake-on-LAN>` _ shall be used, the respective MAC-address has to
be provided as well. Otherwise this column can be left empty. 


LDAP
----

All information dealing with connecting Veyon to an LDAP-compatible server such as *OpenLDAP* or
*Active Directory* are collated in chapter :ref:`LDAP`.


.. index:: error report, program error, crash

Error Report
------------

Configuration page *Error Report* contains a step-by-step guide for creation of an error report. This information
can be used to provide feedback concerning errors or faulty behavior to the developers. However, before you 
create an error report, make sure you have extensively consulted the chapter :ref:`Troubleshooting`, since the
problem may potentially be a configuration error. 


.. index:: export configuration, import configuration, load settings, save settings

.. _ImportExportConfiguration:

Importing/Exporting a Configuration
-----------------------------------

One important premise for the use of Veyon is an identical configuration on all computers. 
A transmission of the Veyon configuration to another computer can be carried out manually for a start,
but should be automated later on. There are several methods available for both ways. 

In Veyon Configurator you can find the entry :guilabel:`Save Settings to File` in menu :guilabel:`File`. This
entry can be used to export the current configuration in JSON format to a file. This file can be imported by 
another computer using the entry :guilabel:`Load Settings from File` in the same menu. Please note, that any 
settings that are imported through the graphical user interface are immediately loaded, but are saved in the system only after
pressing the :guilabel:`Apply` button. 

Through the :ref:`Configuration Management` module within the :ref:`command line interface` configuration 
import and export can be carried out automated or script-controlled.

Additionally, when using an :ref:`automated Installation <AutoInstall>` the configuration can be imported
without any further interaction. In the example section you find an :ref:`Example <InstallationConfigurationImport>` for the install parameter ``/ApplyConfig``.


.. index:: reset configuration, reset settings, delete configuration

.. _ConfigClear:

Reset Configuration
-------------------

In some faulty situations it may be helpful to reset the entire Veyon configuration and rebuild it from scratch
with the default values. For this purpose you can use the entry :guilabel:`Reset Configuration` in the 
:guilabel:`File` menu within Veyon Configurator.

Alternatively the configuration can also be reset using the :ref:`configuration management` within the 
:ref:`command line interface` module.

Furthermore a saved configuration can be reset on operating system level. Under Linux the file 
``etc/xdg/Veyon Solutions/Veyon.conf`` has to be deleted, whereas under Windows the registry key
``HKLM\Software\Veyon Solutions`` and all of its subkeys have to be deleted.
