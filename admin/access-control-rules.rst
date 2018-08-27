.. index:: access control, computer access control, access control rules, rule set, computer access rules

.. _AccessControlRules:

Access control rules
====================

Introduction
------------

Access control rules can be used to provide detailed control over which users can access certain computers under certain circumstances. In the following, the term *rule* is used as a synonym for *access control rule*.

When a user attempts to access a computer, the defined access control rules are processed one after another until all conditions of a rule apply. As soon as all activated conditions of a rule apply, no further rules are processed and the stored action is executed (exception: rule is disabled).

The rules can be configured through the Veyon Configurator on the configuration page :ref:`ConfAccessControl` in section :guilabel:`Access control rules`. The :index:`rule list` is empty by default. In this case, all access attempts are denied since there is no rule that explicitly allows access. This means that at least one rule must be defined that allows access under certain conditions.

Add and modify rules
----------------------

Upon clicking the button :guilabel:`+` a dialog opens which allows the creation of a new rule. Existing rules can be opened or edited by double-clicking them or by clicking the button with the pen symbol.

A rule basically consists of general settings, conditions and an action that is executed when all conditions apply. The dialogue is divided into three sections. The meanings of the individual options in the various dialog sections are explained below.

General
+++++++

A name for the rule should be defined in input field :guilabel:`Rule name` first. The name is later used to identify the rule and is displayed in the rule list. For documentation purposes an optional description can be added to the :guilabel:`Rule description` input field.

The option :guilabel:`Always process rule and ignore conditions` causes the conditions set below not to be examined for :index:`rule processing` and the set action is always executed. This particularly useful for :index:`fallback rules` at the botton of the rule list, where you can specify that the logged on user is asked for permission if no other rules apply.

You can use the :guilabel:`Invert all conditions` option to determine that all activated conditions are inverted before evaluation, meaning that activated conditions must not apply. For example, if the condition *No user logged on* is activated, the rule only applies if one or more users are logged on. If a condition is configured such that a user must be a member of a specific group, the rule only applies, if the said user is *not* a member of the group.


Conditions
++++++++++

For a rule to be processed, one or more :index:`conditions` must apply.

User is member of group
    With this condition you can define that either the accessing or the locally logged on user must be a member of a specific group. The desired group can be chosen. If no or only wrong groups are selectable, the *User groups backend* under the general settings for :ref:`ComputerAccessControl` may have to be adjusted.

Computer is located in room
    With this condition you can define that either the accessing or the local computer has to be located in a specific room. The desired room can be chosen. If no or only wrong rooms are selectable, the :ref:`RefNetworkObjectDirectory` has to be adjusted.

Accessing computer is located in the same room as local computer
    With this condition you can determine that the accessing computer and the local computer have to be located in the same room. This can for example prevent a teacher from accessing computers in another classroom.

Accessing computer is :index:`localhost`
    If this condition is enabled, the rule applies only if the accessing computer is the local computer. This ensures for example that teachers can access the local Veyon Service. This access is necessary for the Veyon Master to execute specific functions via the Veyon Service (e.g. the server for demo mode).

Accessing user has one or more groups in common with local (logged on) user
    You can use this condition to specify that the accessing and the local user have to be members of at least one common group, for example a user group for a class or a seminar.

Accessing user is logged on user
    As an alternative to the condition *accessing computer is localhost* you can also allow a user to access his own sessions. This condition must be activated for this purpose.

Accessing user is already connected
    In conjunction with the condition *accessing computer is located in the same room as the local computer* an extended ruleset can be created allowing access to other rooms under certain conditions. This includes the possibility to access a computer if the accessing user is already connected. For example, if the teacher logs on to a teacher computer in room A and B simultaneously and displays the computers of room B displayed in Veyon Master, the computers in room B have a connection from the teacher. Then the teacher can also access room B from Veyon Master in room A if this condition is activated with an allow action.

No user logged on
    This condition determines how a computer can be accessed when no user is logged on. For example, to assist with computer administration, it can be helpful to always be able to access a computer when no user is logged in.


Action
++++++

If all the enabled conditions of a rule apply, a specific :index:`action` is performed concerning the access to the computer. You can define this action in section :guilabel:`Action`:

:index:`Allow access`
    Access to a computer is allowed and further rules are not processed. If there is a rule in the rule list below that would deny access, access is still allowed. There must be at least one rule with this action.

:index:`Deny access`
    Access to a computer is denied and further rules are not processed. If there is a rule in the rulelist below that would allow access, access is still denied.

:index:`Ask logged on user for permission`
    This action displays a dialog on the computer in question where the logged on user can choose whether to allow or deny access. No further rules are processed, regardless of the user decision.

:index:`None (rule disabled)`
    With this action the rule is ignored and processing is continued with the next rule. This option can be chosen to create an inactive dummy entry to visually subdivide the rule list.

By clicking the :guilabel:`OK` button the rule and the changes made are accepted and the dialog is closed.


Sorting rules
-------------

.. important:: In general access control rules are processed in the order they appear in the list. However, the action of the first matching rule will be taken even if subsequent matching rules exist and would lead to different actions.

All defined rules can be reordered using the buttons with the arrow symbols. Rules containing criteria meant for general granting or denial of access should be placed as high up as possble. Rules for coping with special cases may be listed further down the list. Rules defining some sort of fallback behavior should be at the bottom of the list.

Logical concatenation of rules
------------------------------

If multiple conditions are activated in a rule, *each* conditions must apply in order for the rule to be applied (logical AND). If only one of several rules must apply (logical OR), several access control rules have to be defined.

With a basic knowledge of Boolean algebra, the option *Invert all conditions* can be used as :index:`negation operator` in conjunction with inverted actions to model extended scenarios. For example, if a user has to be a member of two specific groups to grant access to a computer, two seperate rules may be generated that deny access, if the user is *not* a member of either group.

.. note:: If there is no matching access control rule such that all activated conditions apply, access is denied and the connection is closed. This prevents an attacker from being accidentally allowed access due to an incomplete ruleset.


Testing a ruleset
-----------------

In section :guilabel:`Computer access control` the configured rule set may be tested against various scenarios using the :guilabel:`Test` button. In the test dialog you can enter the parameters to simulate a scenario. With the button :guilabel:`OK` the rules are processed with the help of the parameters and a message with the test result is displayed.

