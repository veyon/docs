.. index:: Troubleshooting, Debugging, Error analysis, Error correction

.. _Troubleshooting:

Troubleshooting
===============

.. important:: If you encounter interaction or connection problems between master and client computers you should always ensure that an identical Veyon configuration is used on all computers. To avoid problems in general it's recommended to automate the configuration transfer during :ref:`installation <AutoInstall>` or via the :ref:`CommandLineInterface` instead of importing the configuration manually using the Veyon Configurator. The configuration must also be transferred to all affected computers each time a change is made during troubleshooting.

Computers can't be accessed
---------------------------

There are multiple causes which can prevent access to a computer using Veyon Master.

Networking problems
+++++++++++++++++++

.. index:: Connectivity problems

First of all the general network connectivity of the computer should be checked. Use the utility ``ping`` (which is usually included with every operating system) to diagnose connectivity problems.

Problems with the Veyon Service
+++++++++++++++++++++++++++++++

If the computer can be pinged you should verify that the Veyon Service is running correctly. Open the Veyon Configurator and open the configuration page :ref:`RefService`. In the section :ref:`RefServiceGeneral` the status of the service should be displayed with status *Running*. Otherwise the service can be started using the button :guilabel:`Start service`. If this is not successful you should try reinstalling Veyon. If a new installation does not help you can check the log files of the Veyon Service as well as the logging messages of the operating system for error messages and possible causes. Additionally you can find more hints or settings in the service management of your operating system.

.. index:: telnet, netstat

Service and firewall settings
+++++++++++++++++++++++++++++

If the service is running you have to ensure that it is listening for incoming connections on the correct network port. You can verify that on the local computer using ``telnet``:

.. code-block:: none

    telnet localhost 11100

Besides general program output the character string ``RFB 003.008`` must be displayed. If the output does not contain these characters you should check the :ref:`network port number settings <RefNetworkPortNumbers>` and :ref:`Miscellaneous network settings <RefNetworkMisc>`, especially the Veyon server port number. You should try to reset them to their default values.

Next the same access has to be possible from a different computer in the network. The utility ``telnet`` can be used again for the diagnosis. The program argument ``localhost`` has to be replaced with the name or IP address of the corresponding computer. If the access fails please ensure that the option :guilabel:`Allow connections from localhost only` in the :ref:`Miscellaneous network settings <RefNetworkMisc>` is disabled. Additionally :ref:`computer access control <ComputerAccessControl>` should be disabled initially as the service otherwise might listen on ``localhost`` only. This can happen if the external access would be denied because of currently matching rules. If both settings are correct the output of

.. code-block:: none

    netstat -a

has to indicate that the service is not (only) listening on ``localhost`` or ``127.0.0.1`` (status ``LISTEN`` or similar).

If the port access from remote computers still fails usually a firewall prevents the access and has to be reconfigured accordingly. On Linux this concerns settings of ``iptables``, ``ufw`` etc. Consult the corresponding manuals of the used software. On Windows Veyon automatically configures the integrated Windows firewall if the option :guilabel:`Enable firewall exception` in the :ref:`Miscellaneous network settings <RefNetworkMisc>` is set to its default value (*enabled*). If a 3rd party firewall solution is used it must be configured to allow external access to TCP ports 11100 (Veyon server port) and 11400 (demo server).

Authentication settings
+++++++++++++++++++++++

Another cause of the error can be wrong or insufficient :ref:`authentication settings <RefAuthentication>`. For first tests you should select :ref:`logon authentication <ConfLogonAuthentication>` instead of :ref:`key file authentication <ConfKeyFileAuthentication>` on both computers. As soon as the authentication test is successful on the local computer external access will also work.

If :ref:`key file authentication <ConfKeyFileAuthentication>` is used the key files on master and client computers must match exactly. On client computers the public key file must have exactly the same content as on the master computer. If the access still fails the access permissions to the key files may be wrong. The Veyon Service needs to have read permissions on the *public key file* while the user of Veyon Master has to be able to read the *private key file*. If the problem persists the :ref:`key file directories <RefKeyFileDirectories>` of the key files should be deleted on all computers and a new keypair generated on the master computer. The public key must then be imported again on all client computers.

Settings for computer access control
++++++++++++++++++++++++++++++++++++

An incorrect configuration of computer access control can also lead to computers being inaccessible. Initially it's recommended to disable :ref:`computer access control <ComputerAccessControl>` completely using the Veyon Configurator. This allows determining which method for computer access control is possibly incorrectly configured.

If :ref:`authorized user groups for computer access <RefAuthorizedUserGroups>` are used you should check whether the list of authorized user groups is complete and whether the accessing user is a member of one of these user groups.

Improperly configured :ref:`access control rules <AccessControlRules>` can also cause problems with accessing computers. It is necessary to always specify at least one rule to allow access under certain conditions. If this is ensured, a temporary test rule can be inserted at the end of the list for further debugging. This rule should be configured so that the option :guilabel:`Always process rule and ignore conditions` is enabled and the action :guilabel:`Allow access` is selected. This rule can then be moved up in the rule list step by step until the test returns the desired positive results and the access works. The access rule located directly below the test rule is then the cause for the access denial and can be examined more closely and corrected accordingly. Don't forget to remove the test rule afterwards to prevent unauthorized access.

Anti-virus software
+++++++++++++++++++

It has been reported by some users that an installed anti-virus software caused problems with Veyon, especially regarding the Veyon Service. As part of the troubleshooting process you should temporarily disable the anti-virus software in order to figure out whether the anti-virus software is the cause of error. If so, try to add an exception for the Veyon Service after enabling the anti-virus software again. Alternatively contact the vendor of your anti-virus software for further assistance.

Settings are not correctly saved/loaded
---------------------------------------

After updating to a new version of Veyon it may happen in rare cases that some configuration keys are inconsistent and need to be recreated. This can result in settings not being saved or reloaded correctly, such as the builtin location and computer information. In this case the :ref:`configuration should be reset <ConfigReset>` and rebuilt based on the default values.

Locations and computers from LDAP directory are not displayed in Veyon Master
-----------------------------------------------------------------------------

Please make sure that:

* the :ref:`network object directory <RefNetworkObjectDirectory>` on configuration page :guilabel:`General` is set to *LDAP Basic* or *LDAP Pro*
* LDAP integration tests :guilabel:`List all entries of a location` and :guilabel:`List all locations` are successful and return proper objects
* on the configuration page :guilabel:`Master` all options for fine-tuning the behavior are set to their default values


Selecting current location automatically doesn't work
-----------------------------------------------------

If the :ref:`option automatically selecting the current location <RefAutoSelectLocation>` is activated, but has no effect when starting Veyon Master, you should first make sure that the master computer is also listed as a computer for the respective room in the :ref:`network object directory <RefNetworkObjectDirectory>`.

If the problem persists although all entries in the network object directory are correct, there is usually a problem with the DNS configuration in the network. Make sure that computer names can be resolved to IP addresses and reverse lookups of IP addresses return the corresponding computer names. On most operating systems, the DNS diagnostic tool ``nslookup`` is available for this purpose. Calling the program with the local computer name as an argument must return a valid IP address. A second call with the determined IP address must again return the computer name.

If the function does not work as desired despite correct DNS setup, in the second step the :ref:`log level <RefLoglevel>` can be set to the highest value (*Debug messages and everything else*). After restarting Veyon Master, you can search the log file ``VeyonMaster.log`` in the :ref:`log file directory <RefLogFileDirectory>` for further error causes. The lines with the messages *"initializing locations"* and *"found locations"* indicate which host names and IP addresses were used to determine the location and which locations were eventually determined on the basis of these information.

.. index:: Ctrl+Alt+Del

Screen lock can be bypassed via Ctrl+Alt+Del
--------------------------------------------

To completely block all keystrokes and keyboard shortcuts in screen lock mode, you must restart your computer after installing Veyon on Windows. Without a restart, the Veyon-specific driver for input devices is not yet active and keystrokes cannot be intercepted.

In demo mode, only a black screen or window is displayed on client computers
----------------------------------------------------------------------------

Please make sure that:

* in the configuration page :guilabel:`Service` under :ref:`network port numbers <RefNetworkPortNumbers>` the demo server port is set to its default value ``11400``
* on the configuration page :guilabel:`Service` the firewall exception is enabled on the master computer or a third party firewall is configured to allow incoming connections to TCP port ``11400``
* the user of Veyon Master has access to its own computer (i.e. the local Veyon Service). In the :ref:`access control ruleset <AccessControlRules>` there may exist a rule prohibiting access to the computer if a teacher is logged on. In this case you should create a rule with the condition :ref:`Accessing computer is localhost <AccessingComputerIsLocalhost>` enabled as far up the list of rules as possible. Otherwise the demo server is unable to access the teacher computer's screen content and distribute it to the client computers.

Veyon Server crashes with XIO or XCB errors on Linux
----------------------------------------------------

There are known issues with specific KDE and Qt versions on Linux causing the Veyon Server to crash. This affects several other VNC server implementations as well. If you're affected by such crashes consider upgrading KDE/Qt. As a last resort you can disable the X Damage extension in the VNC server configuration. This will however decrease overall performance and increase the CPU load.
