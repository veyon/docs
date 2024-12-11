.. _InternetAccessControl:

Internet Access Control
=======================

General
-------

The Veyon Internet Access Control add-on allows blocking the access to the Internet for the whole class or individual computers in situations such as exams. The Internet access is blocked client-side by using mechanisms provided by the different backends.


Initial setup
-------------

First of all the Veyon Add-ons package needs to be installed. Make sure to download and install the version corresponding to your Veyon installation, i.e. Veyon 4.9.1 requires Veyon Add-ons 4.9.1 while for Veyon 4.8.3 you need to install version 4.8.3 of the add-ons. Please refer to :ref:`DeployingAddons` for further information.

After the installation has completed, you'll see some new configuration pages in the Veyon Configurator program. One of them is called :guilabel:`Internet access control` and allows to set up the add-on:

.. figure:: images/internet-access-control-configuration.png
   :class: image-drop-shadow
   :align: center

   Internet Access Control configuration page

In most cases you can leave the default settings and continue with deploying the add-on to the student computers.

.. important:: If you make changes to the configuration, remember to always deploy the updated configuration to the student computers! Only the client-side settings affect the way the Internet access is blocked on the clients.

Now you can start Veyon Master and can click the :guilabel:`Internet access` button to open the menu with the :guilabel:`Block Internet access` and :guilabel:`Unblock Internet access` items. After activating the :guilabel:`Block Internet access` item, the users on the selected computer(s) no longer should be able to open a website on the Internet. If they still are, please check the settings and possibly try another blocking mode or backend.

Backends
--------

There are currently two backends providing different mechanisms to block the Internet access. Both backends are described in the following subsections.

Block internet access via system firewall
+++++++++++++++++++++++++++++++++++++++++

This is the standard backend that should preferably be used, as it offers the most flexibility and works most reliably. When this backend is used, the Veyon Service makes changes to the system firewall to block Internet access. There are platform-specific differences here:


Windows
    Veyon controls the integrated Windows firewall and makes temporary changes to its configuration. This means that the Windows firewall must be activated. In addition, changes to the configuration of the Windows firewall must not be prevented by group policies.

Linux
    Veyon works on the basis of *nftables* and calls the related command line tool ``nft``. This is used to temporarily add additional rules to block Internet access.

For both operating systems, the backend configuration is identical. In general different modes are available. The mode selection depends on the network environment and the desired blocking behavior.

Block all outbound traffic for TCP ports
    This is the default mode and should work in most environments. In this mode the Veyon Service adds special rules to the firewall which block any traffic to the configured ports. Use this mode if blocking the TCP ports 80/443 and one or multiple custom ports (separated by space) is sufficient. To block all traffic use the second mode.

Block all outbound traffic to non-local subnets
    In this mode, all network traffic directed to networks outside the local subnets is blocked. On Windows, the Veyon service temporarily changes the configuration of all firewall profiles (domain, private, public) to “ Outbound connections that do not match a rule are blocked”. If :guilabel:`Exceptions` are configured, appropriate rules are added to allow access to these networks, hosts or ports. This can be used, for example, to preserve access to the intranet and other internally hosted platforms. External websites can also be defined as exceptions here under certain circumstances, but the addresses of all servers/CDNs from which the website loads resources must then also be specified.

Block traffic to (e.g. proxy or DNS) servers
    If the student computers access the Internet via a proxy server, you can select this option. A firewall rule is then added that simply blocks all traffic to the proxy address. Alternatively, access to certain DNS servers can also be blocked, although in most cases this leads to problems when accessing internal resources such as network drives etc.

Enable preconfigured firewall rule
    If the three modes above are not suitable for your network you can also configure an own custom rule in the Windows Firewall. This rule should be disabled by default. The Veyon Service will enable this rule while the Internet access is to be blocked. On Linux the Veyon Service calls ``nft`` to load the nftables rules from the file ``/etc/veyon/iac/firewall/rules.d/<RULENAME>``. You can define any nftables rules in this file.

Block internet access by modifying routing table
++++++++++++++++++++++++++++++++++++++++++++++++

If the firewall backend cannot be used (e.g. if a 3rdparty firewall software is used instead of the Windows Firewall), you can use this backend as a fallback. It works in a very simple way by temporarily removing the default route from the routing table and/or adding a user-defined (possibly deliberately invalid) route to block Internet access. In any case, the settings should be made carefully so that access to the internal network continues to function properly. Especially in larger segmented networks, both options should be combined by removing the default route on the one hand and adding a route to the internal network on the other.
