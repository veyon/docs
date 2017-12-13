.. index:: troubleshooting, debugging, error analysis, problem correction

.. _Troubleshooting:

Troubleshooting
===============

.. important:: If you encounter interaction or connection problems betwen master and client computers you should always ensure that an identical Veyon configuration is used on all computers. To avoid problems in general it's recommended to automate the configuration transfer during :ref:`installation <AutoInstall>` or via the :ref:`command line interface <CLI>` instead of importing the configuration manually using the Veyon Configurator. During debugging the configuration needs to be transfered onto all computers on every change.

Computers can't be accessed
---------------------------

There are multiple causes which can prevent the access to a computer using Veyon Master.

Networking problems
+++++++++++++++++++

First of all the general network connectivity of the computer should be checked. Use the utility ``ping`` (which is usually included with every operating system) to diagnose :index:`connectivity problems`.

Problems with the Veyon Service
+++++++++++++++++++++++++++++++

If the computer can be pinged you should check whether the Veyon Service is running correctly. Open the Veyon Configurator and open the configuration page :ref:`Service configuration`. In the section :ref:`ServiceGeneral` the status of the service should be displayed with status *Running*. Otherwise the service can be started using the button :guilabel:`Start service`. If this is not successful you should try a reinstallation of Veyon. If a reinstallation does not help you can check the log files of the Veyon Service as well as the logging messages of the operation system for error messages and possible causes. Additionally you can find more hints or possibilities for adjustments in the service management of your operating system.

.. index:: telnet, netstat

Service and firewall settings
+++++++++++++++++++++++++++++

If the service is running you have to ensure that it is listening on the correct network port for incoming connections. You can verify that on the local computer using ``telnet``:

.. code-block:: none

    telnet localhost 11100

Besides general program output the string ``RFB 003.008`` has to be displayed. If the output does not match the expectations you should check the :ref:`Network settings`, especially the primary service port, and reset them to their default values.

Next the same access has to be possible from a different computer in the network. The utility ``telnet`` can be used again for the diagnosis. The program argument ``localhost`` has to be replaced with the name or IP address of the corresponding computer. If the access fails please ensure that the option :guilabel:`Allow connections from localhost only` in the :ref:`Network settings` is disabled. Additionally :ref:`Computer access control` should be disabled initially, as the service listens on ``localhost`` only if the external access would be denied because of currently matching rules. If both settings are correct the output of

.. code-block:: none

    netstat -a

has to indicate that the service is not (only) listening on ``localhost`` or ``127.0.0.1`` (status ``LISTEN`` or similar).

If the external :index:`port access` still fails usually a :index:`firewall` prevents the access and has to be reconfigured accordingly. On Linux this concerns settings of ``iptables``, ``ufw`` etc. Consult the corresponding manuals of the software used. On Windows the integrated Windows Firewall is configured by Veyon automatically as long as the option :guilabel:`Enable firewall exception` in the :ref:`Network settings` is set to its default value (*enabled*). If a 3rd party firewall solution is used it has to be configured such that the TCP ports 11100 (primary service port) as well as 11400 (demo server) can be accessed externally.

Authentication settings
+++++++++++++++++++++++

Another cause of error can be wrong or insufficient :ref:`Authentication settings`. For initial tests you should (on both computers!) enable :ref:`Logon authentication` and disable *Key file authentication*. As soon as the logon authentication is successful at the local computer external access should work too.

When using :ref:`Key file authentication` it has to be enabled and the key files on master and client computers have to correspond. On client computers the public key file needs to have the same content as on the master computer. If the access still fails in some circumstances the :index:`access permissions` are wrong. The Veyon Service needs to have :index:`read permissions` on the *public key file* while the user of Veyon Master has to be able to read the *private key file*. If the problem remains the :ref:`Base directories` of the key files should be deleted on all computers and a new keypair generated on the master computer. Then the public key needs to be imported again on all client computers.

Settings for computer access control
++++++++++++++++++++++++++++++++++++

An erroneous configuration of computer access control can lead to problems with accessing computers. Initially it's recommended to disable the :ref:`Computer access control` completely using the Veyon Configurator. Now you can determine which configured computer access control method is configured improperly.

When using :ref:`User groups authorized for computer access` you have to check whether the list of authorized user groups is complete and whether the accessing user is member of one of these groups.

Improperly configured :ref:`Access control rules` can also cause problems with accessing computers. There always has to be at least one rule which allows the access under certain conditions. Once ensured for further debugging a temporary test rule can be inserted at the end of the list which has the option :guilabel:`Always process rule and ignore conditions` enabled and the action :guilabel:`Allow access` selected. This rule stepwise can be moved upwards inside the rule list until the access works or the test gives the desired positive results. The access rule below the temporary test rule likely causes the access being denied and can be examined in detail and corrected appropriately.

