undo rule (Layer 2 ACL view)
============================

undo rule (Layer 2 ACL view)

Function
--------



The **undo rule** command deletes an ACL rule in the Layer ACL view.



By default, no Layer 2 ACL rule is created and no description is configured for an ACL rule.


Format
------

**undo rule** *rule-id* **description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rule-id* | Specifies the ID of an ACL rule. | The value is an integer ranging from 0 to 4294967294. |
| **description** | Specify rule description. | - |



Views
-----

Layer 2 ACL view


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

# Configure a description for a Layer 2 ACL rule numbered 23, and then delete the description of the ACL rule.
```
<HUAWEI> system-view
[~HUAWEI] acl number 4999
[*HUAWEI-acl-L2-4999] rule 23 permit destination-mac 0-0-1 source-mac 0-0-2 type 0x0800
[*HUAWEI-acl-L2-4999] rule 23 description This rule is used to filter packets according to the MAC address and protocol type.
[*HUAWEI-acl-L2-4999] undo rule 23 description

```