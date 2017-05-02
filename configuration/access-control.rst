Access control
==============

Introduction
------------

The configuration page "Access control" allows to configure which users are allowed to access computers in an iTALC network in detail. Access control is performed during the connection initialization after the authentication. While the authentication is validating the authenticity of an accessing user, the access control functionality restricts the computer access to authorized users such as teachers.

The desired access control mode can be selected at the top of the access control configuration page. If authentication is sufficient (e.g. when using key authentication with limited access to the authentication keys) you can select the first option which does not perform any further access control at all. Select the second option to restrict access to members of certain user groups. The third option allows to configure fine-grained access control using custom access control rules. It is the most flexible mode while the initial configuration can be more complex to set up.

The access control configuration is part of the whole (machine-)local iTALC configuration just like all settings in the other configuration pages. The configuration has to be transfered to and applied on all client computers in order to work properly. Use the iTALC Configurator to easily perform this task in an automated manner (see section "Configuration management").


Simple access control by user groups
------------------------------------

The configuration of this access control mechanism is quite simple. The left list contains all available user groups. By default all local user groups are listed here. If you set up LDAP/AD integration all LDAP user groups will be shown here instead. You can select one or more groups and move them to the right list using the appropriate button between the two lists. All members of each group moved to the right list will be allowed to access computers. As usual don't forget to update the configuration on all clients.


Access control rules
--------------------

If you require fine-grained control of which user is allowed to access which computer you can make use of this access control mode. If an user tries to connect to a computer all access control rules are processed consecutively until the conditions of one rule match. In the following the term "rule" will be used synonymous for "access control rule".

By default the rule list is empty which leads to every access attempt being denied because there's no rule which explicitely allows access. This means that you will have to add at least one rule which allows access under certain conditions.

Adding and editing rules
~~~~~~~~~~~~~~~~~~~~~~~~

Use the "Add" button to open a dialog which allows to set up a new rule. In the section "General" you should enter at least a rule name which will be used to identify the rule and represent it in the rule list. Optionally you can enter a description for documentation purposes. Next you have to configure one or more conditions by selecting the desired entity (accessing user, accessing computer, ...) and activating the appropriate condition(s). You then have to select an argument for each activated condition such as the group the selected entity should be member of. You can also invert all conditions by checking the appropriate checkbox. However be careful with this option for not making the configuration too complex. See subsection "Logical linking of rules" for possible use cases.

Finally the desired action has to be selected. This can be either "Allow access" or "Deny access". If you want to disable the rule you can select the action "None".


Ordering rules
~~~~~~~~~~~~~~

Rules are processed consecutively which means the action of the first matching rule will be taken even if subsequent rules would also match and possibly would lead to a different action. This is very important to know when defining the ruleset.

In consequence all rules leading to access denial should be placed in front of those rules allowing access. You can use the "Move up" and "Move down" buttons to change the order of rules.


Logical linking of rules
~~~~~~~~~~~~~~~~~~~~~~~~

If more than one condition of a rule is activated each condition has to meet in order to make the rule apply (logical AND). If only one of multiple conditions has to meet (logical OR) multiple rules have to be created.

With a little knowledge of boolean algebra the "Invert all conditions" option can be used to set up advanced scenarios. Imagine the case where it is desired that a teacher is only allowed to access computers in the same computer lab as he is currently logged on. You could create a simple rule which says "Accessing computer is located in the same computer lab as local computer" with action "allow". However this would allow the access regardless of the user while it might be necessary to further restrict the access to members of a teacher group. The solution is to invert the rule by checking the "Invert all conditions" option and changing the action to "Deny access". Now every access attempt is denied if an accessing computer is not member of the same computer lab. Further rules afterwards can now safely allow access to individual users, groups or computers.
