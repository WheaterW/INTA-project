undo rule (Basic ACL view)
==========================

undo rule (Basic ACL view)

Function
--------



The **undo rule** command deletes an ACL rule in the basic ACL view.



By default, no basic ACL rule is created and no description is configured for an ACL rule.


Format
------

**undo rule** *rule-id* **description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **undo** | Cancel current setting. | - |
| **rule** *rule-id* | Specifies the ID of an ACL rule. | The value is an integer ranging from 0 to 4294967294. |
| **description** | Specify rule description. | - |



Views
-----

Basic ACL view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Run the **rule description** command to configure a description for an ACL in any of the following situations:

* A large number of ACLs are configured, and their functions are difficult to identify.
* An ACL is used at a long interval, and its function may be left forgotten.To delete the description of an ACL rule, run the undo **rule description** command.

**Prerequisites**



An ACL rule has been created using the **rule** command.



**Precautions**



If the description of an ACL rule is not configured, the ACL rule may be misunderstood or misused.




Example
-------

# Clear the description for a basic ACL rule numbered 23.
```
<HUAWEI> system-view
[~HUAWEI] acl number 2999
[*HUAWEI-acl4-basic-2999] rule 23 deny source 10.1.1.1 0
[*HUAWEI-acl4-basic-2999] rule 23 description This rule is used to filter packets according to the source IP address.
[*HUAWEI-acl4-basic-2999] undo rule 23 description

```