.. _FAQ:

FAQ - Frequently Asked Questions
================================

Does Veyon run under Chrome OS (ChromeBooks) or MacOS?
------------------------------------------------------
Currently Veyon is only available for Linux or Windows based environments. However, one goal among others in the process
of further development is to port Veyon to other platforms and provide respective installation files.
In this context the Veyon-project is dependent on support from experienced software developers, especially for
porting Veyon to MacOS and Android.

How can I add computers in order to access them?
------------------------------------------------

If the preconfigured :ref:`network object register` is used, the only action required is adding the respective
rooms and computers on the configuration page :ref:`local data`. Afterwards the added resources are available 
to the Veyon master. 

If :ref:`LDAP-/AD-Integration <LDAP>` is configured the network object register has to be reconfigured to LDAP in
order to make the computers listed in the register available to the Veyon master.

.. index:: iTALC

How can I migrate an existing iTALC-Installation to Veyon?
----------------------------------------------------------

Although iTALC and Veyon are conceptually similar, a complete reinstall and reconfiguration is necessary to use Veyon,
because configuration and file formats as well as their paths have changed and are not compatible with each other.
For a migration iTALC has to be uninstalled completely at first. It is recommended to reboot the computer thereafter.
Afterwards Veyon can be installed and configured analogously to iTALC.

Whilst the configuration of authentication methods is very similar, the configuration of rooms and computers is 
done via the Veyon configurator and not via the master anymore. In this context you should check, whether the new
:ref:`LDAP-/AD-Integration <LDAP>` can be used to make rooms and computers automatically available in Veyon.

Is it possible to use the Veyon master on several computers?
------------------------------------------------------------

The used of Veyon master on several computers is possible without any problems. To that end it must be ensured
that an identical configuration is used on all master computers. This also holds true for the client computers. 
If the login-authentication is used, there are no further steps required.
If the key-authentication is uesd, the private key has to be distributed to all master computers. 

Can I import or use a self-generated file with room and computer information?
-----------------------------------------------------------------------------

This is not possible with Veyon 4.0, but Veyon 4.1 will provide a possibility for import and a command line 
interface to the room and computer administration.

How can I import or export the selection of displayed computers?
----------------------------------------------------------------

The selection of displayed computers is saved in the personal :ref:`User Configuration <User Configuration>`.
To extend this more multiple user, there a two options. First, the user configuration file can be copied into the
respective profile of the user, using login scripts for example. Second the user configuration can be moved to a
shared directory (e.g. a network drive) and the :ref:`Setting <User Configuration>` has to be changed accordingly,
such that the user configuration is loaded from this directory. However, you have to ensure that the access rights
may have to be changed, for that changes made by the user are not rewritten into the global user configuration.

In this context we point you to the function for :ref:`Automatic switch to current classroom <RoomAutoSwitch>`,
that may permit to realize the desired behavior directly. 

How can I hide the master computer in the room administration?
--------------------------------------------------------------

Just activate the option :ref:`Automatically hide local computer in room administration <AutoHideLocalComputer>`.

What happens if there is no matching access control rule?
---------------------------------------------------------

If there is no previously defined access control rule that matches all activated conditions, access is denied
and the connection is closed. In doing so we prohibit that an attacker may have access because of an unfinished
rule set.

