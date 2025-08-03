step (ACL6 view)
================

step (ACL6 view)

Function
--------



The **step** command sets a step for an ACL6 rule group.

The **undo step** command restores the default step and renumbers ACL6 rules.



By default, the step of an ACL6 rule group is 5.


Format
------

**step** *step-value*

**undo step**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *step-value* | Specifies the step of an ACL6 rule group. | The value is an integer ranging from 1 to 20. |



Views
-----

Basic ACL6 view,Advanced ACL6 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



An ACL6 step is the difference between two adjacent and automatically allocated ACL6 rule numbers. For example, if the step is set to 5, rule numbers start at 5 and increase by an increment of 5, yielding rule numbers of 5, 10, 15, 20, and so on.To specify an ACL6 step, run the step command.You can use an ACL6 step to maintain ACL6 rules and add new ACL6 rules conveniently.Assume that a user has created four rules numbered from 1 to 4 in an ACL6. The user can reconfigure the ACL6 step, for example, to 2 by running the **step 2** command in the ACL6 view. The original rule numbers 1, 2, 3, and 4 are renumbered as 2, 4, 6, and 8, respectively. After that, the user can run the **rule 3 xxxx** command to add a rule numbered 3 between the renumbered rules 2 and 4.



**Configuration Impact**



The numbers of rules in an ACL6 realign automatically when the ACL6 step changes.



**Precautions**



Changing the ACL6 step causes rule numbers to change but does not affect the rules' priorities.




Example
-------

# Set the step of ACL6 3101 to 2.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 3101
[*HUAWEI-acl6-advance-3101] step 2

```