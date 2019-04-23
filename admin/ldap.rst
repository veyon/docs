.. index:: LDAP, Active Directory, OpenLDAP, Samba, Directory service

.. _LDAP:

LDAP/AD integration
===================

This chapter covers the setup of Veyon for connecting it to LDAP-compatible servers. In the following the generic term *LDAP* will be used and refers to all LDAP-compatible products and technologies such as *OpenLDAP*, *Samba* or *Active Directory*. LDAP integration enables you to use information about users, user groups, computers and locations that already exist in most environments, instead of manually replicating it in the Veyon configuration. Once configured Veyon Master can retrieve locations and computers to be displayed directly from the directory service. Additionally LDAP users and user groups can serve as a base for :ref:`ComputerAccessControl`.

The configuration of the LDAP integration is done on configuration page :guilabel:`LDAP` in Veyon Configurator. The page is divided into several subpages for :ref:`LDAPBasicSettings`, :ref:`LDAPEnvironmentSettings`, :ref:`LDAPAdvancedSettings` and :ref:`LDAPIntegrationTests`.


.. _LDAPBasicSettings:

Basic settings
--------------

The basic settings affect all basic parameters for accessing an LDAP server. They are mandatory for a properly working LDAP integration.

General
+++++++

.. index:: LDAP server

LDAP server and port
    Enter the address of the LDAP server (hostname or IP address) here. If a port other than the default LDAP port 389 is used, the port parameter has to be adjusted accordingly.

.. index:: Anonymous bind, Use bind credentials

Anonymous bind / Use bind credentials
    Depending on the environment and configuration of the LDAP server, LDAP queries can be performed either as an anonymous user or with valid usernames and passwords only. If the server access requires a username and password, the option :guilabel:`Use bind credentials` has to be selected and the credentials have to be entered in the input fields below. Otherwise the default option :guilabel:`Anonymous bind` can be used.

.. index:: Bind DN

Bind DN
    The bind DN is the username used to log in at the server in order to perform LDAP operations. However, the required format heavily depends on the LDAP server and its configuration. Possible formats include ``User``, ``DOMAIN\User`` or ``cn=User,…,dc=example,dc=org``.

.. index:: Bind password

Bind password
    In addition to the bind DN the corresponding password has to be entered.

You can use the :guilabel:`Test` button to verify, whether server access is working with the supplied parameters.

.. hint:: Veyon only requires read access to the LDAP directory. As an additional security measure on the LDAP server a dedicated user with read-only access to the LDAP directory can be created, e.g. "Veyon-LDAP-RO". Access to relevant attributes can be further restricted for this user.

Connection security
+++++++++++++++++++

Veyon can establish encrypted connections to the LDAP server. For this purpose, settings are available in the section :guilabel:`Connection security`.

Encryption protocol
    You can choose between the encryption protocols *None*, *TLS* and *SSL*. The use of the modern TLS protocol is recommended.

    **Default:** *None*

.. index:: TLS certificate verification

TLS certificate verification
    This setting determines how the security certificate of the LDAP server is to be checked when the encrypted connection is established. With the default setting *System defaults*, depending on the operating system, an attempt is made to verify the certificate using the root certificates installed system-wide. The Windows certificate store is not taken into account here, so that a separate CA certificate file may have to be stored. With the *Never* setting, the server certificate is not verified at all. This however allows for case man-in-the-middle attacks and should therefore only be used in exceptional cases. The *User-defined CA certificate file* setting ensures that the certificate check is performed on the basis of a specified CA certificate file.

    **Default:** *System defaults*

.. index:: Custom CA certificate file

Custom CA certificate file
    If you use your own certification authority (CA), it may be necessary to store their certificate in a PEM file format so that Veyon can check the certificate of the LDAP server.

.. index:: Base DN

Base DN
+++++++

The base DN defines the address of the root object in the directory. All objects are stored below the base DN. Usually the base DN comes from the DNS or AD domain (see also `RFC 2247 <https://www.ietf.org/rfc/rfc2247.txt>`_).

In most cases a fixed base DN is used so the default option :guilabel:`Fixed base DN` has to be chosen. The base DN then has to be entered in the corresponding input field or selected from the server by using the :guilabel:`Browse` button. You can use the :guilabel:`Test` button to verify, whether the settings are correct and entries can be found.

.. index:: LDAP naming contexts

If a generic Veyon configuration is to be used across multiple sites with different base DNs, Veyon can be configured so that the base DN is always queried dynamically using LDAP naming contexts. For this to work the :guilabel:`Discover base DN by naming context` has to be chosen and the naming context attribute must be adapted. You can use the :guilabel:`Test` button to verify, whether a Base DN could be determined.

After importing a generic Veyon configuration without a fixed base DN it is also possible to determine the base DN through the :ref:`LDAPCLI` and write it to the local configuration.


.. _LDAPEnvironmentSettings:

Environment settings
--------------------

After the basic settings have been configured and tested, the environment-specific settings can now be made. These settings determine which trees contain objects of certain types as well as the names of certain object attributes. With these parameters Veyon can retrieve all required information from the LDAP directory.

.. index:: LDAP object trees, LDAP Common Names, LDAP Organizational Units

Object trees
++++++++++++

Object trees are organizational or structural units in which certain types of objects (users, groups, computers) are stored. The respective CNs (Common Names) or OUs (Organizational Units) must be entered **without the base DN part** in the respective input field. Next to each input field there are buttons for opening browse dialogs and for testing the individual setting.

.. index:: User tree

User tree
    The LDAP tree (without base DN) in which the user objects are located must be entered here, e.g. ``OU=Users`` or ``CN=Users``.

.. index:: Group tree

Group tree
    The LDAP tree (without base DN) in which the group objects are located must be entered here, e.g. ``OU=Groups`` or ``CN=Groups``.

.. index:: Computer tree

Computer tree
    The LDAP tree (without base DN) in which the computer objects are located must be entered here, e.g. ``OU=Computers`` or ``CN=Computers``.

.. _LDAPComputerGroupTree:

.. index:: Computer group tree

Computer group tree
    If the computer groups are located in a different tree than the regular user groups or in a subtree, the corresponding LDAP tree can be specified here. Otherwise the group tree is used to query computer groups and to filter them with a specific :ref:`object filter <LDAPObjectFilters>` if necessary.

.. index:: Recursive search operations

Perform recursive search operations in object trees
    This option can be used to control whether objects should be queried recursively. The search then takes place not only in the specified tree but also in any existing subtrees.

    **Default:** *disabled*

.. hint:: If objects of one type are stored in different object trees (e.g. users in both ``CN=Teachers`` and in ``CN=Students``), the parameter for the corresponding object tree can be left empty and the option :guilabel:`Perform recursive search operations in object trees` can be activated. A recursive search is then performed in the entire LDAP directory starting from the base DN. In this case, however it is strongly recommended to set the :ref:`object filters <LDAPObjectFilters>` for the respective object type.


.. index:: LDAP object attributes

Object attributes
+++++++++++++++++

For Veyon to be able to retrieve the required information from the queried objects, the names of some object attributes have to be configured, as these differ substantially depending on the environment and LDAP server. Next to each input field buttons for browsing the attribute of an existing object and testing the respective attribute name are available.


.. index:: User login name attribute, LDAP user object

User login name attribute
    This attribute must hold the login name of a user. The attribute is used to determine the LDAP user object associated with a particular username. In an OpenLDAP environment often the attribute name ``uid`` is used while the name ``sAMAccountName`` is common in Active Directories.

.. index:: Group member attribute

Group member attribute
    Members of a group are listed in group objects through this attribute. The attribute is used to determine the groups a particular user is a member of. Depending on the configuration the attribute also used map computers to locations. In an OpenLDAP environment often the attribute name ``member`` is used while the name ``memberUid`` is common in Active Directories.

.. index:: Computer display name attribute

Computer display name attribute
    The content of this optional attribute is used to determine the name of a computer displayed in Veyon Master. If left blank the common name (``cn``) is used instead.

    **Default:** *cn*

.. index:: Computer host name attribute, LDAP computer object

Computer host name attribute
    This attribute must hold the DNS name of the computer. It is used to determine the LDAP computer object associated with a particular computer hostname. In an OpenLDAP environment often the attribute name ``name`` is used while the name ``dNSHostName`` is common in Active Directories.

.. index:: Fully qualified domain names

Hostnames stored as fully qualified domain names (FQDN, e.g. myhost.example.org)
    This option specifies whether to use the `fully qualified domain name (FQDN) <https://en.wikipedia.org/wiki/Fully_qualified_domain_name>`_ for mapping computer names to LDAP computer objects. If the computer names are stored without the domain part in the LDAP directory, this option has to be left disabled, otherwise it must be enabled.

    **Default:** *disabled*

.. index:: Computer MAC address attribute, MAC address

Computer MAC address attribute
    In addition to the computer name the MAC addresses of computers are stored in the LDAP directory in some environments, for example if the DHCP server also accesses the LDAP directory. If the Veyon feature is to be used to switch on computers via `Wake-on-LAN <https://en.wikipedia.org/wiki/Wake-on-LAN>`_, the corresponding attribute name must be entered here, since the MAC address is required for this functionality. Typical attribute names are ``hwAddress`` or ``dhcpAddress``.

.. hint:: In a standard Active Directory there is no attribute which stores MAC addresses. You must therefore populate MAC addresses manually in an existing unused attribute such as ``wwwHomepage`` or extend the AD schema. Additionally you can grant computers group write access to ``SELF`` and use a PowerShell script to make each computer automatically store the MAC address of its first physical LAN adapter when booting.

.. index:: Computer location attribute, Computer location

Computer location attribute
    If the LDAP schema for computer objects provides a special attribute for the mapping to a location, this attribute name can be entered here. The :guilabel:`Test` button can be used to verify whether the computers at a location can be queried correctly using the configured attribute. In the advanced settings, you can then specify in section :ref:`LDAPComputerLocations` that the computer location attribute is used.

.. index:: Location name attribute

Location name attribute
    When identifying computer locations via computer groups or computer containers, the value of a certain attribute can be displayed as the location name instead of the *Common Names* of these groups or objects. If, for example, computer groups have an attribute called ``name`` or ``description``, a meaningful location name can be stored in this attribute and the attribute name can be entered here.

.. _LDAPAdvancedSettings:

Advanced settings
-----------------

With the advanced settings the LDAP integration and the use of the information from the LDAP directory can be customized to individual needs.

.. index:: Object filters, LDAP object filter, LDAP filters

.. _LDAPObjectFilters:

Optional object filters
+++++++++++++++++++++++

With LDAP filters, the LDAP objects used by Veyon can be narrowed down if, for example, computer objects such as printers are not to be displayed in the Veyon Master. Next to each input field there is a button for checking the respective object filter.

As of Veyon 4.1 the optional filters follow the well-known scheme for LDAP filters (see for example `RFC 2254 <https://www.ietf.org/rfc/rfc2254.txt>`_ or `Active Directory: LDAP Syntax Filters <https://social.technet.microsoft.com/wiki/contents/articles/5392.active-directory-ldap-syntax-filters.aspx>`_) such as ``(objectClass=XYZ)``.

Filter for users
    You can define an LDAP filter for users here, e.g. ``(objectClass=person)`` or ``(&(objectClass=person)(objectClass=veyonUser))``.

Filter for user groups
    You can define an LDAP filter for user groups here, e.g. ``(objectClass=group)`` or ``(|(cn=teachers)(cn=students)(cn=admins))``.

Filter for computers
    You can define an LDAP filter for computers here, e.g. ``(objectClass=computer)`` or ``(&(!(cn=printer*))(!(cn=scanner*)))``.

.. _LDAPComputerGroupsFilter:

Filter for computer groups
    You can define an LDAP filter for computer groups here, e.g. ``(objectClass=room)`` or ``(cn=Room*)``. If computer groups are used as locations, you can filter the displayed locations this way.

.. _LDAPComputerContainersFilter:

Filter for computer containers
    You can define an LDAP filter for computer containers here, e.g. ``(objectClass=container)`` or ``(objectClass=organizationalUnit)``. If containers/OUs are used as locations, you can filter the displayed locations this way.


Group member identification
+++++++++++++++++++++++++++

The content of the group membership attributes varies across different LDAP implementations. While in Active Directory the *distinguished name (DN)* of an object is stored in the member attribute, OpenLDAP usually stores the user login name (``uid`` or similar) or the computer name. In order for Veyon to use the correct value for querying groups of a user or computer, the appropriate setting must be chosen here.

Distinguished name (Samba/AD)
    This option has to be chosen, if the distinguished name (DN) of an object is stored in a member attribute of the group. Usually Samba and AD server use this scheme.

Configured attribute for user login name or computer hostname (OpenLDAP)
    This option has to be chosen, if the login name of a user (username) or the hostname of a computer is stored in the member attributes of a group. Usually OpenLDAP server use this scheme.

.. _LDAPComputerLocations:

Computer locations
++++++++++++++++++

Veyon offers several methods to represent computer locations in an LDAP directory. In the simple case there is one computer group for every location (e.g. room). All computers at a specific location are members of the corresponding group. If computers instead are organized in containers or organizational units (OUs), these parent objects can be used as locations. Both procedures do not require any adaptation of the LDAP schema. As a third possibility, the location name can also be stored as a special attribute in each computer object.

Computer groups
    This option specifies that computer locations are identified through computer groups. All computer groups are then displayed as locations in the Veyon Master. For each location all computers that are members of the corresponding group are displayed. If not all LDAP groups are to be displayed as locations, either a dedicated :ref:`computer group tree <LDAPComputerGroupTree>` must be configured or the computer groups must be restricted using a :ref:`computer group filter <LDAPComputerGroupsFilter>`.

    **Default:** *enabled*

Computer containers or OUs
    This option specifies that the containers/OUs containing computer objects are used as computer locations. Containers are objects that are parents to computer objects in the LDAP tree. If not all containers are to be displayed as locations, a corresponding :ref:`computer container filter <LDAPComputerContainersFilter>` can be set up.

    **Default:** *disabled*

Location attribute in computer objects
    If the LDAP schema for computer objects provides a special attribute for mapping computer objects to locations, this option can be enabled and the attribute name can be entered. The :guilabel:`Test` button can be used to check whether the members of a computer location can be queried correctly using the configured attribute.

    **Default:** *disabled*


.. _LDAPIntegrationTests:

Integration tests
-----------------

.. index:: LDAP integration tests

The integration tests can be used to check the LDAP integration as a whole. The buttons allow various tests to be performed. All tests should be successful and provide valid results before the LDAP connection is used in production.


Using LDAP backends
-------------------

.. index:: LDAP backend

With the successful configuration and testing of the LDAP integration, the LDAP backends can now be activated. For this, the :ref:`network object directory <RefNetworkObjectDirectory>` and the user groups backend for the :ref:`computer access control <ComputerAccessControl>` must be adapted. Only after switching the network object directory to *LDAP* the location and computer information from the LDAP directory are used in the Veyon Master.

.. attention:: After changing the backend for the computer access control, all previously configured access rules should under all circumstances be checked, since group and location information change and in most cases access rules will no longer be valid or not be processed correctly.

.. _LDAPCLI:

Command line interface
----------------------

The :ref:`CommandLineInterface` of Veyon allows some LDAP-specific operations. All operations are available using the ``ldap`` module. A list of all supported commands is displayed via ``veyon-cli ldap help``, while command-specific help texts can be displayed via ``veyon-cli ldap help <command>``.

.. describe:: autoconfigurebasedn

    This command can be used to automatically determine the used base DN and permanently write it to the configuration. An LDAP server URL and optionally a naming context attribute have to be supplied as parameters:

    .. code-block:: none

        veyon-cli ldap autoconfigurebasedn ldap://192.168.1.2/ namingContexts
        veyon-cli ldap autoconfigurebasedn ldap://Administrator:MYPASSWORD@192.168.1.2:389/

.. hint:: Special characters such as ``@`` or ``:`` – especially in the password - can be specified by using `URL percent-encoding <https://en.wikipedia.org/wiki/Percent-encoding>`_.

.. describe:: query

    This command allows to query LDAP objects (``locations``, ``computers``, ``groups``, ``users``) and is mainly used for testing. The function can also be used to develop scripts for system integration tasks.

    .. code-block:: none

        veyon-cli ldap query users
        veyon-cli ldap query computers
