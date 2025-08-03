rule description (Advanced ACL6 view)
=====================================

rule description (Advanced ACL6 view)

Function
--------



The **rule description** command configures a description for an ACL6 rule.

The **undo rule description** command deletes the description of an ACL6 rule.



By default, no description is configured for an ACL6 rule.


Format
------

**rule** *rule-id* **description** *destext*

**undo rule** *rule-id* **description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rule-id* | Specifies the ID of an ACL6 rule. | The value is an integer ranging from 0 to 4294967294. |
| *destext* | Specifies the description of an ACL6 rule. | The value is a string of 1 to 127 case-sensitive characters, spaces supported. The value must not start with spaces and can be a combination of letters, numbers, and spaces. |



Views
-----

Advanced ACL6 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Run the **rule description** command to configure a description for an ACL6 in any of the following situations:

* A large number of ACL6s are configured, and their functions are difficult to identify.
* An ACL6 is used at a long interval, and its function may be left forgotten.

**Prerequisites**



An ACL6 rule has been created using the **rule** command.



**Precautions**



If the description of an ACL6 rule is not configured, the ACL6 rule may be misunderstood or misused.




Example
-------

# Configure a description for an advanced ACL6 rule numbered 23.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 3100
[*HUAWEI-acl6-advance-3100] rule 23 deny tcp source 2001:db8::1 64
[*HUAWEI-acl6-advance-3100] rule 23 description This rule is used to filter packets according to the source IPv6 address.

```