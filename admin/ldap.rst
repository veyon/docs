.. index:: LDAP, Active Directory, OpenLDAP, Samba, directory service

.. _LDAP:

LDAP-/AD-Integration
====================

This chapter deals with connecting LDAP-compatible servers to Veyon. Below we will just use the generic term
*LDAP* and thereby mean all LDAP-compatible products and technologies such as *OpenLDAP*, *Samba* or
*Active Directory*. LDAP-integration enables you to use most of the information about
users, user groups, computers and rooms from existing environments, instead of manually reshaping them through
the Veyon configuration. On the one hand LDAP-users and -user groups may serve as data base for
:ref:`access control` and on the other hand the Veyon Master can load rooms and computers to be displayed 
directly from the directory service.  

The configuration of LDAP-integration can be done on configuration page :guilabel:`LDAP` in 
Veyon Configurator. The page is divided into several frames for :ref:`Basic Settings`, 
:ref:`Environment Settings`, :ref:`Advanced Settings` and :ref:`Integration Tests`. 


.. _BasicSettings:

Basic Settings
--------------

The basic settings affect all basic parameters for accessing an :index:`LDAP-server`. They are mandatory for a 
properly working LDAP-integration. 

General
+++++++

LDAP-Server and port
	Enter the address of the LDAP-server (name or IP-address) here. If a different port than the default 
	LDAP-port 389 is used, the port parameter has to be adjusted accordingly. 

Anonymous Bind / Bind-Credentials
	Depending on the environment and configuration of the LDAP-server, LDAP-queries can be performed either as
	an anonymous user or only with proper user name and password. If the server access requires a user name and
	password, the option :guilabel:`Bind-credentials` has to be activated and the credentials have to be entered
	into the following input fields. Otherwise the default option :guilabel:`Anonymous Bind` can be used.  

Bind-DN
	The :index:`Bind-DN` is the user name needed for a login at the server in order to process LDAP-operations. 
	However, the required format vastly depends on the LDAP-server and its configuration. Possible formats
	include ``User``, ``DOMAIN\User`` or ``cn=User,…,dc=example,dc=org``.
	
Bind-Password
	In connection with the Bind-DN the respective password has to be entered.

You can use the :guilabel:`Test` button to verify, whether server access is working with the supplied set 
of parameters.

.. hint:: Veyon exclusively perform reading LDAP-operations. For security reasons it may be a good option to create a read-only user, for example "Veyon-LDAP-RO". Access to relevant attributes can be further restricted for this user.
 

Base-DN
+++++++

An essential foundation which holds all objects that are to be used, is defined through the :index:`Base-DN`. 
This foundation usually is taken from the DNS- or AD-domain (see also `RFC 2247 <https://www.ietf.org/rfc/rfc2247.txt>`_).

In case a fixed Base-DN is used, the default option :guilabel:`Fixed Base-DN` has to be activated and the 
Base-DN has to be entered in the input field. You can use the :guilabel:`Test` button to verify, whether the
settings are correct and new entries can be found. 

If a generic Veyon configuration is to be used for example at several sites with different Base-DNs, Veyon can
be configured such that the Base-DN is always dynamically queried using the :index:`LDAP-Naming-Contexts`. 
Therefore the eponymic option has to be activated and the naming context attribute must be changed. 
You can use the :guilabel:`Test` button to verify, whether a Base-DN can be found.  

After importing a generic Veyon configuration without a fixed Base-DN it is also possible to find the Base-DN
through the :ref:`LDAP-CLI` and write it to the local configuration.


.. _EnvironmentSettings:

Environment Settings
--------------------

After the basic settings have been configured and tested, the environment settings can be processed. 
These settings define which trees hold objects and how particular object attributes are named. Using these
parameters, Veyon can query the information needed from the LDAP-directory. 

Object Trees
++++++++++++

:index:`Object Trees` are organizational and structural units, in which specific types of objects
(users, groups, computers) reside. The corresponding CNs (Common Names) or OUs (:index:`Organizational Units`)
must be entered in the respective input field, if *no Base-DN* is used. 
Next to each input field there is a button to check the corresponding object tree. 

:index:`User Tree`
	Enter the LDAP-tree (without Base-DN) the users (user objects) reside in.
	Typical examples are ``OU=Users`` or ``CN=Users``. 

:index:`Group Tree`
	Enter the LDAP-tree (without Base-DN) the groups (group objects) reside in.
	Typical examples are ``OU=Groups`` or ``CN=Groups``. 

:index:`Computer Tree`
	Enter the LDAP-tree (without Base-DN) the computers (computer objects) reside in.
	Typical examples are ``OU=Computers`` or ``CN=Computers``.


.. _ComputerGroupTree:

:index:`Computer Group Tree`
	If the computer groups are located in different tree than the regular (user-)groups or in a subtree, the
	respective LDAP-tree can be entered here. Otherwise the group tree is also used to query 
	:index:`computer groups` and filter them with a specific :ref:`Object Filter <ObjectFilter>` if necessary. 

Perform :index:`recursive search operations` in object trees
	You can use this option to control whether objects shall be queried recursively. In this case the search
	is not only performed in the determined tree but also in all possible subtrees. 

	Default: *disabled*

.. hint:: If objects of a single type reside in various object trees (e.g. users in ``CN=Teachers`` and also in ``CN=Students``), the parameter for the respective object tree can be left empty and the option :guilabel:`Perform recursive search operations in object trees` can be activated. In this case a recursive search through the complete LDAP-directory starting from the Base-DN is performed. However, you should by all means set the :ref:`Object Filter <ObjectFilter>` for the respective object type. 


Object Attributes
+++++++++++++++++

In order for Veyon to retrieve the required information from the queried objects, the names of some 
:index:`object attributes` have to be configured, as they may vary broadly depending on the specific
environment and LDAP server. Next to each input field there is a button that can be used to check each
attribute name. 

:index:`User Login` attribute
	This attribute must contain the login name of a user. It is used to determine the 
	:index:`LDAP user object` belonging to a specific user. In an OpenLDAP environment often the attribute name
	``uid`` is used to this end, whereas Active Directory frequently uses ``sAMAccountName``. 

:index:`Group Member` attribute
	Members of a group are listed in group objects through this attribute. It is used to determine
	the groups a particular user is a member of. Depending on the configuration they attribute also also used
	for mapping computers and rooms. In an OpenLDAP environment often the attribute name
	``member`` is used to this end, whereas Active Directory frequently uses ``memberUid``.  

:index:`Computer Name` attribute
	This attribute takes the DNS-name of the computer. It is used to determine the LDAP computer object belonging
	to a specific computer name (host name). In an OpenLDAP environment often the attribute name
	``name`` is used to this end, whereas Active Directory frequently uses ``dNSHostName``.

Computer names are saves as :index:`fully qualified domain names`. 
	This option determines whether the `fully qualified domain name (FQDN) <https://de.wikipedia.org/wiki/Fully-Qualified_Host_Name>`_ 
	is used for the mapping of computer names to LDAP computer objects. If the computer names are saved without
	the domain part in the LDAP directory, this option has to be disabled. 
    
    Default: *disabled*

Computer-:index:`MAC address` attribute
	Additionally to the computer name the MAC addresses of computers are stored in the LDAP directory in some
	environments, for example, if the DHCP server is also accessing the LDAP directory. If the Veyon function
	`Wake-on-LAN <https://de.wikipedia.org/wiki/Wake_On_LAN>`_ shall be used, the respective attribute name has
	to be entered here, since the MAC address is required for this function. Typical examples are ``hwAddress``
	or ``dhcpAddress``. 

Computer room attribute
	If the LDAP scheme for computer objects needs a special attribute for the mapping to a room, this attribute
	name can be entered here. You can use the :guilabel:`Test` button to verify, whether the members of a 
	computer room can be correctly queried using the configured attribute. In the advanced settings, you can 
	configure in section :ref:`Computer Rooms` that the computer room attribute is used. 

Computer room name attribute
	If computer groups or computer contains are used as rooms, instead of the *Common Names* of these groups or
	objects, the value of a specific attribute for the displayed room name can be used. For example, if computer
	groups have an attribute ``name`` or ``description``, you can store a meaningful room declaration in this
	place. 

.. _AdvancedSettings:

Advanced Settings
-----------------

With the advanced settings the LDAP integration and usage of information from the LDAP directory can be tailored
to fit individual needs. 

.. index:: object filters, LDAP object filter

.. _ObjektFilters:

Optional Object Filters
+++++++++++++++++++++++

By using LDAP filters the LDAP objects used by Veyon can be limited, e.g., if computer objects such as printers
should not be displayed in Veyon Master. Next to each input field there is a button to check the respective
attribute name.

.. important:: These optional filters follow the well-known scheme for :index:`LDAP filters` (see for example `RFC 2254 <https://www.ietf.org/rfc/rfc2254.txt>`_ or `Active Directory: LDAP Syntax Filters <https://social.technet.microsoft.com/wiki/contents/articles/5392.active-directory-ldap-syntax-filters.aspx>`_). However, they have the feature that outer brackets must not be specified. For example, a simple objectClass filter must be defined as ``objectClass=XYZ`` rather than ``(objectClass=XYZ)``. 

Filter for users
	You can define an LDAP filter for users here, e.g. ``objectClass=person`` or ``&(objectClass=person)(objectClass=veyonUser)``.
	
Filter for user groups
	You can define an LDAP filter for user groups here, e.g. ``objectClass=group`` or ``|(cn=teachers)(cn=students)(cn=admins)``.

Filter for computers
	You can define an LDAP filter for computers here, e.g. ``objectClass=computer`` or ``&(!(cn=printer*))(!(cn=scanner*))``.


.. _ComputerGroupFilter:

Filter for computer groups
	You can define an LDAP filter for computer groups here, e.g. ``objectClass=room`` or ``cn=Room*``. If 
	computer groups are used as rooms, you can limit the rooms to be displayed with this method. 


.. _ComputerContainerFilter:

Filter for computer container
	You can define an LDAP filter for computer groups here, e.g. ``objectClass=container`` or
	``objectClass=organizationalUnit``. If container/OUs are used as rooms, you can limit the rooms to be displayed with this method. 


Identification of group members
+++++++++++++++++++++++++++++++

The content of the group membership attributes varies across different LDAP implementations. Whilst in
Active Directory the :index:`distinguished name (DN)` of an object is stored in a member attribute,
OpenLDAP usually stores the login name of a user (``uid`` or similar) or the computer name. In order for Veyon
to use the correct value for querying a user's groups or computers, the correct setting has to be chosen.

Distinguished name (Samba/AD)
	This option has to be chosen, if the distinguished name (DN) of an object is stored in a member 
	attribute of the group. Usually Samba and AD server use this scheme. 
	
Configured attribute for user login or computer name (OpenLDAP)
	This option has to be chosen , if the user login name or computer name is stored in a member attribute 
	of a group. Usually OpenLDAP server use this scheme. 

.. _ComputerRooms:

Computer Rooms
++++++++++++++

Veyon provides several methods to map computer rooms to an LDAP directory. In the most simple case there is
one :index:`computer group` for every :index:`computer room` which all computers of a room are a member of.
If computers reside in containers or Organizational Units (OUs), these superior objects can be used as rooms.
In both cases do not entail an update of the LDAP scheme. As a third possibility the room name can be stored as
special attribute in each computer object.   

Computer groups
	You can use this option to define, that computer rooms are mapping using computer groups. All computer groups
	will be displayed as rooms in Veyon Master. In each room all computers that are members of the specific group
	are displayed. In case not all LDAP groups shall be displayed as rooms, you must either configure a dedicated
	computer group tree or restrict the computer groups by using a computer group filter. 
	
	Default: *activated*

Computer container or OUs
	This settings defines that the containers/OUs in which the computer objects reside are used as computer rooms.
	Containers are objects that are superior to computer objects in the LDAP tree. In case not all containers
	shall be displayed as rooms, a respective computer container filter can be defined. 
	
	Default: *disabled*
	
Common attribute
	If the LDAP scheme expects a special attribute for the mapping of computer objects to a room, this option can
	be activated and the attribute name can be entered. You can use the :guilabel:`Test` button to check, whether
	the members of a computer room can be queried correctly with the configured attribute. 
	
	Default: *disabled*


.. _IntegrationTests:

Integration Tests
-----------------

By using :index:`integration tests` the LDAP integration as a whole can be tested. The buttons allow for
various tests to be performed. All tests should be run successfully and return valid results before the LDAP
connection is used in production. 


.. index:: LDAP backend

Utilizing LDAP Backends
-----------------------

After successful configuration of the LDAP integration, the LDAP backend can be activated. To this end the
:ref:`network object directory` as well as the database backend for the :ref:`computer access control` have to
be customized. Only after the network object directory has been changed to *LDAP* the room and computer information
from the LDAP directory are used in Veyon Master. 

.. attention:: After the database backend has been reconfigured for the computer access control, the previously configured access rules should under all circumstances be checked, since group and room information change and in most cases access rules will no longer be valid or not be processed correctly.


.. _LDAPCLI:

Command Line Interface
----------------------

There are several LDAP specific opertions provided through the :ref:`command line interface` of Veyon. All 
operations are provided through the ``ldap`` module. All list of all supported commands is printed on entering
``veyon-ctl ldap help``, whilst command specific help texts can be shown via ``veyon-ctl ldap help <Command>``.

``autoconfigurebasedn``
	This command can be used to automatically determine the used Base-DN and permanently write it to the
	configuration. An LDAP server URL and optionally a naming-context attribute have to be supplied as parameters:

    ``veyon-ctl ldap autoconfigurebasedn ldap://192.168.1.2/ namingContexts``

    ``veyon-ctl ldap autoconfigurebasedn ldap://Administrator:MYPASSWORD@192.168.1.2:389/``

``query``
	This command allows querying LDAP objects (``rooms``, ``computers``, ``groups``, ``users``) and is designed
	mainly for debugging purposes. However, the function can also be used for developing scripts that may be 
	helpful for system integration. 

    ``veyon-ctl ldap query users``

    ``veyon-ctl ldap query computers``
