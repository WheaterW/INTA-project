undo rule description (User ACL group view)
===========================================

undo rule description (User ACL group view)

Function
--------



The **undo rule description** command deletes the description of an ACL rule.



By default, no description is configured for an ACL rule.


Format
------

**undo rule** *rule-id* **description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rule-id* | Specifies the ID of an ACL rule. | The value is an integer ranging from 0 to 4294967294. |



Views
-----

User ACL group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Run the **rule description** command to configure a description for an ACL in any of the following situations:

* A large number of ACLs are configured, and their functions are difficult to identify.
* An ACL is used at a long interval, and its function may be left forgotten.To delete the description of an ACL rule, run this command.

**Prerequisites**



An ACL rule has been created using the **rule** command.



**Precautions**



If the description of an ACL rule is not configured, the ACL rule may be misunderstood or misused.




Example
-------

# Clear the description for a user-defined ACL rule numbered 23.
```
<HUAWEI> system-view
[~HUAWEI] acl number 5001
[*HUAWEI-acl-user-5001] rule 23 permit l2-head 0x0180C200 0xFFFFFFFF 14
[*HUAWEI-acl-user-5001] rule 23 description permitting packets in which the four consecutive bytes starting from the fourteenth byte of the Layer 2 header is 0180C200.
[*HUAWEI-acl-user-5001] undo rule 23 description

```