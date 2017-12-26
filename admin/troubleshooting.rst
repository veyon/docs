.. index:: troubleshooting, error analysis, debugging, error correction

.. _Troubleshooting:

Troubleshooting (Error Analysis and Correction)
===============================================

.. important:: If you should experience any problems in master-client-interaction, make sure that all computers are running an identical Veyon configuration. To avoid errors it is generally recommended not to import the configuration manually through Veyon Configurator, but to automate this process using the :ref:`Installation <AutoInstall>` or the :ref:`command line interface`. If you make any changes to the configuration in the debugging process, the updated configuration must always be mirrored to all affected computers. 

Access to a computer is not possible
------------------------------------

If a computer cannot be accessed through the Veyon Master, there can be several potential causes.

Problems with the network
+++++++++++++++++++++++++

As a first step, the reachability of the computer from the network should be checked. 
For this purpose take advantage of the program ``ping`` that usually comes with every operating system to
diagnose :index:`connection errors`. 

Problems with the Veyon Service
+++++++++++++++++++++++++++++++

If the computer is reachable via ``ping``, it has to be checked whether the Veyon Service is running correctly.
Open the Veyon Configurator and open configuration page :ref:`Service Configuration`. In section 
:ref:`ServiceGeneral` the status of the service should read *running*. Otherwise the service can be started
by pressing the :guilabel:`Start Service` button. If the service is not successfully started, a reinstallation
of Veyon could be the remedy. If a reinstallation doesn't change the situation, search the logfiles of the 
Veyon Service and the system logs of the operating system for reported errors and potential causes. Additionally,
the service management of the operating system might offer more hints or configuration possibilities.

.. index:: telnet, netstat

Service and Firewall Configuration
++++++++++++++++++++++++++++++++++

If the service is running, is must be assured, that it is listening on the right port for incoming connections.
This can be verified on the local computer using ``telnet``:

.. code-block:: none

    telnet localhost 11100

Among general program output the string ``RFB 003.008`` must be printed. If the output is not as expected, 
the :ref:`network settings <Networksettings>`, especially the primary service port, have to be checked and
probably reset to their default values.

In the next step the same access must be possible from another computer on the network. You can use ``telnet``
for diagnosis too, but the program argument ``localhost`` must be replaced with the name or IP-address of the
computer. If ``telnet`` access fails, it must be verified that the option :guilabel:`Only allow connections
from the local host` in the :ref:`network settings <Networksettings>` is disabled. :ref:`Computer access control`
should be disabled as well, since the service is automatically listening to ``localhost``, if external access is
prohibited by the current access control rule set. If both settings are okay, the output of

.. code-block:: none

    netstat -a

should reveal, that the service on port ``11100`` is not (only) listening to ``localhost`` resp. ``127.0.0.1``
(status ``LISTEN``).

If external :index:`port access` continues to fail, a firewall might prohibit the access and therefore must be
reconfigured. Under Linux this affects the settings of ``iptables``, ``ufw`` and the like. See the manuals of the
used software for further help. Under Windows the Windows-firewall which is integrated into the operating system
is automatically configured by Veyon if the option :guilabel:`Activate Firewall-exception` in the 
:ref:`network settings <Networksettings>` is set to its default value (*activated*). If a third-party firewall 
is used, it has to be configured in a way that TCP ports 11100 (primary service port) and 11400 (demo server) 
are reachable. 

Authentication Settings
+++++++++++++++++++++++

Another cause for errors could be false or unsufficient :ref:`authentication settings <Authentication>`. For first
tests during debugging both(!) computers should always have :ref:`Login-authentication <LoginAuthentication>` 
activated and *Keyfile-authentication* disabled. As soon as the login-authentication at the local computer has
been successfully tested, external access will also work.

If the :ref:`Keyfile-authentication <KeyfileAuthentication>` is used, it has to be activated and the key files
on master and client computer must be matching. The file containing the public key must be identical on client
and master computer. If access is not possible nevertheless, the :index:`access rights` may be wrong. The 
Veyon Service must have :index:`read access` to the *public key file*, whereas the user of Veyon Master must be
able to read the *private key file*. If the problem persists, the :ref:`Base Directories <BaseDirectories>` for
the key pairs must be deleted on all computers and the Master computer must generate a substitute key pair. 
Afterwards all client computers will have to import the public key again. 

Settings for Computer Access Control
++++++++++++++++++++++++++++++++++++

A corrupt configuration of the computer access control may result in users not being able to access computers.
As a first step we recommend to disable :ref:`computer access control` completely through the Veyon Configurator.
Afterwards it can be determined which of the specific methods for computer access control has been configured
in a wrong way.

If :ref:`authorizes user groups for computer access` are being used, it has to be checked, whether the list of
authorized user groups is complete and if the accessing user is a member of one of these user groups. 

Another potential cause in case of prohibited computer access may be the :ref:`access control rules`. There always
has to be at least one rule granting access under certain conditions. Using this method, you can add another
rule at the bottom of the list for debugging purposes. This rule should have the option
:guilabel:`Always process rule and ignore conditions` activated and the action :guilabel:`Allow Access` should
be selected. This rule can now be moved upwards step by step until access is granted or the test produces the
desired results. In this case the access rule directly below the test rule has to be the cause for the denial
of access and can be closely inspected and corrected accordingly. 

Settings are not correctly saved/loaded
---------------------------------------

Following the update of early beta-versions of Veyon 4 it may be the case that some configuration keys are
inconsistent and must be recreated. This may imply that settings cannot be correctly saved or reloaded, for 
example local information on room and computers. In this case the configuration should be reset completely
(:ref:`Completely Reset Configuration <ConfigClear>`) and recreated from scratch using the default values. 

Rooms and computers from the LDAP-directory are not displayed in Master
-----------------------------------------------------------------------

Please make sure that:

* the :ref:`network object directory` on configuration page :guilabel:`General` is set to *LDAP*
* LDAP-integration tests :guilabel:`List all members of a computer room` and :guilabel:`List all computer rooms` are successful and return objects
* all options for fine tuning the behavior on configuration page :guilabel:`Master` are set to their default values

Automated switching to the current room doesn't work
----------------------------------------------------

If the :ref:`option for automated switching to the current room <RoomAutoSwitch>` is activated, but doesn't show
any effect when starting Veyon Master, it should be ensured, that the master computer is set as computer for the
respective room in the :ref:`network object directory`. Independent from this option, the master computer can
be hid in the computer room management using the option :ref:`Hide local computer in computer room management <AutoHideLocalComputer>`. 

If all entries in the network object directory are correct, there arguably is a problem with the DNS-configuration
in the network. Make sure that computer names can be converted into IP-addresses and vice versa. Most common
operating systems offer the diagnosis tool ``nslookup`` for this purpose. Calling the program with the local 
computer name as a parameter should return a valid IP-address. A second call with the returned IP-address should
in turn return the computer name.

In case the function doesn't work as desired despite a correct DNS setup, it can be useful to set the 
:ref:`Loglevel <Loglevel>` to the highest value (*Debug*) and search the log file ``VeyonMaster.log`` in the
:ref:`Logfile Directory <LogfileDirectory>` for potential causes. Thereby the messages *"initializing rooms"* and
*"found local rooms"* might be particularly helpful to detect possible problems.

Screen lock can be bypassed with Ctrl+Alt+Del
---------------------------------------------

In order to completely block all keyboard input and shortcuts in screen lock mode, under Windows a reboot is 
required after completion of the Veyon installation. Without a reboot the Veyon-specific driver for input devices
is not yet active and keyboard input cannot be caught. 

When in demo mode, client computer screens just show a black screen or a black window
-------------------------------------------------------------------------------------

Please make sure that:

* the demo server's port under :ref:`Network Settings` on configuration page :guilabel:`Service` is set to a default value of ``11400``.
* all firewall exceptions for the master computer are activated on configuration page :guilabel:`Service` or a used third-party firewall is configured to allow incoming connections on port ``11400``.
* the user of Veyon Master has access to its own computer (i.e. the local Veyon Service). In a rule set there may exist a rule prohibiting access to a computer if a teacher is signed in. In this case you should create a rule with activated condition *accessing computer is localhost* as far up the list of rules as possible. Otherwise the demo server is unable to access the teacher PC's screen content and distribute it to the client computers.  

