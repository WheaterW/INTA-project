rule description (Basic ACL view)
=================================

rule description (Basic ACL view)

Function
--------



The **rule description** command configures the description of an ACL rule.



By default, no description is configured for an ACL rule.


Format
------

**rule** *rule-id* **description** *destext*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rule-id* | Specifies the ID of an ACL rule. | The value is an integer ranging from 0 to 4294967294. |
| *destext* | Specifies the description of an ACL rule. | The value is a string of 1 to 127 case-sensitive characters, spaces supported. The value must not start with spaces and can be a combination of letters, numbers, and spaces. |



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
* An ACL is used at a long interval, and its function may be left forgotten.

**Prerequisites**



An ACL rule has been created using the **rule** command.



**Precautions**



If the description of an ACL rule is not configured, the ACL rule may be misunderstood or misused.




Example
-------

# Configure a description for a basic ACL rule numbered 23.
```
<HUAWEI> system-view
[~HUAWEI] acl number 2999
[*HUAWEI-acl4-basic-2999] rule 23 deny source 10.1.1.1 0
[*HUAWEI-acl4-basic-2999] rule 23 description This rule is used to filter packets according to the source IP address.

```