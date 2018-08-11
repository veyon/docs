.. index:: access control, access control rules, rule set, computer access rules

.. _AccessControlRules:

Access control rules
====================

Introduction
------------

In case a detailed control over access to specific computers under specific circumstances for a user are needed, you can control the accesses with the help of access control rules. For convenience, throughout this text we will use the term *rule* synonymously with *access control rule*.

If a user tries to access a computer, all previously defined access control rules are flicked through until all conditions of a rule match. As soon as all activated conditions of a rule match, no further rules will be processed and the defined action will be triggered. (Exception: the rule is disabled.)

The rules can be configured through the Veyon Configurator at the configuration page :ref:`ConfAccessControl` in section :guilabel:`Access Control Rules`. By default the :index:`list of rules` is empty. In this case all attempts for access are denied, since there is no rule explicitly granting access. It follows, that there must be at least one rule defined which allows access under certain conditions.

Add and modify rules
----------------------

Upon clicking the button :guilabel:`+` a dialogue opens which allows creation of a new rule. Existing rules can be opened or edited by double-clicking them or clicking the button with the pen symbol.

In essence a rule consists of general settings, conditions and an action, that is triggered, if all conditions match. Hence the dialogue is splitted in three sections. Hereafter we will explain the meaning of the specific options in the different areas of the dialogue.

General
+++++++

At first a name for the rule should be defined in input field :guilabel:`rule name`. We use the name to identify the rule and display it in the list of rules. For documentation purposes an optional description can be entered in the :guilabel:`Rule Description` input field.

The option :guilabel:`Always process rule and ignore conditions` ensures that while :index:`processing the rules` the conditions specified below are not checked and the defined action is always triggered. This behavior is particularly helpful for the :index:`fallback rules` located at the botton of the list of rules to make sure that the signed in user is asked for permission if no other rule applies.

Through the option :guilabel:`Invert all conditions` you can determine that all activated conditions are inverted before evaluation, meaning that activated conditions must not be satisfied. For example, if the condition *No user logged in* is activated, the rule will only be applied if one or more users are logged in. If a condition is configured such that a user must be a member of a specific group, the rule only applies, if the said user is *not* a member of this group.


Conditions
++++++++++

For a rule to be processed, one or more :index:`conditions` must be satisfied.

User is member of group
    With this condition you can define that either the accessing or the locally signed in user must be a member of a specific group. The desired group can be choosen. If no or only wrong groups are selectable, you might adjust the *data backend* in the general settings for :ref:`ComputerAccessControl`.

Computer is based in room
    With this condition you can define that either the accessing or the local computer has to be based in a specific room. The desired room can be choosen. If no or only wrong rooms are selectable, you might adjust the *data backend* in the general settings for :ref:`ComputerAccessControl`.

Accessing computer is based in the same room as the local computer
    With this condition you can define that the accessing and the local computer have to be based in the same room. Thus is can be prohibited that a teacher accesses computers used in a different class in a different room.

Accessing computer is :index:`localhost`
    If this condition is activated, the rule applies only if the accessing computer is the local host. Thus is can be ensured that teachers can access the local Veyon Service. This access is necessary for the Veyon Master to execute specific functions via the Veyon Service (i. a. the server for demo mode).

Accessing user has one or more groups in common with local (signed in) user
    With this condition you can define that the accessing and the local user have to be common members of at least one group, for example a user group for a class or a seminar.

Accessing user is signed in user
    As an alternative to the condition *accessing computer is localhost* you can permit for a user to have
    access to his own sessions. Therefore this condition has to be activated.

Accessing user is already connected
    In conjunction with the condition *accessing computer is based in the same room as the local computer* an extended rule set can be created allowing access to other rooms under certain conditions. Included is the possibility to access a computer, if the accessing user is already connected. For example, if the teacher logs into a teacher computer in room A and B simultaneously and has the computers of room B displayed by Veyon Master, the Veyon Service running on the computers in room B receives a connection from the teacher. Thus the teacher can access resources in room B from within room A, if this condition is activated with a permissive action.

No user logged in
    With this condition you can define how a computer may be accessed, if no user is currently logged in. As a support in computer administration it may be helpful in some cases to be able to access a computer even though no user is logged in.


Action
++++++

If all activated conditions of a rule are satisfied, a predefined :index:`action` is triggered concerning the
access to the computer. You can define this action in section :guilabel:`Action`:

:index:`Allow Access`
    Access to a computer is allowed and further rules are not processed. If there existed a rule further down the list of rules denying access, however, access would still be granted. There must be at least one rule containing this action.

:index:`Deny Access`
    Access to a computer is denied and further rules are not processed. If there existed a rule further down the list of rules allowing access, however, access would still be denied.
    
:index:`Ask signed in user for permission`
    This action shows a dialogue on the screen by which the signed in user can choose whether he or she wants to allow or deny access. Independent of the outcome no further rules are processed.

:index:`Rule disabled`
    With this action the rule is ignored and processing is continued with the following rule. This option can be chosen to create an interactive dummy entry for visual subdivision of the list of rules.

By clicking the :guilabel:`OK` button the rule resp. the changes carried out are taken over and the dialogue is closed.


Sorting Rules
-------------

.. important:: The defined access control rules will be processed in the order they are defined in the list. However, the action for the first matching rule will be triggered even if there are subsequent rules that would also match and result in triggering another action.

All defined rules can be rearranged (meaning re-prioritized) using the arrow symbols. Rules containing criteria meant for general granting or denial of access should be listed topmost. Rules for coping with special cases may be listed further down the list. Rules defining some sort of fallback behavior should be and the bottom of the list.

Logical Concatenation of Rules
------------------------------

If more than one condition is activated, *all* conditions must be satisfied in order for the rule to be applied (logical AND). If only one out of several rules must be satisfied (logical OR), several access control rules have to be defined.

Using basic knowledge of Boolean algebra, the option *Reverse all Conditions* can be used as :index:`negation operator` in conjunction with inverted actions to model extended scenarios. For example, if a user has to be a member of two specific groups to grant access to a computer, two seperate rules may be generated that deny access, if the said user is *not* a member of one of these groups.

.. note:: If there is no matching access control rule such that all activated conditions are satisfied, access is denied and the connection is closed. Thus we prevent that an attacker can access resources because of an unfinished rule set.


Testing a Rule Set
------------------

In section :guilabel:`Computer Access Control` the configured rule set may be tested against various scenarios using the :guilabel:`Test` button. You can enter the parameter for reconstructing a specific scenario in the test dialogue. Press :guilabel:`OK` and the rules will be tested with the given parameters and a report with the test result is shown.
