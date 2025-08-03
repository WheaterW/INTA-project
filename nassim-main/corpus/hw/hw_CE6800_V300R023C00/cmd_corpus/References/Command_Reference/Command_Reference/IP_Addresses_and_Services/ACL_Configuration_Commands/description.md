description
===========

description

Function
--------



The **description** command configures a description for an ACL.

The **undo description** command restores the default description of an ACL.



By default, no description is configured for an ACL.


Format
------

**description** *text*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *text* | Specifies the description of an ACL. | The value is a string of 1 to 127 case-sensitive characters, spaces supported. The value must not start with spaces and can be a combination of letters, numbers, and spaces. |



Views
-----

ARP ACL view,Layer 2 ACL view,Basic ACL view,User ACL group view,Advanced ACL view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **description** command configures a description for an ACL in any of the following situations:

* A large number of ACLs are configured, and their functions are difficult to identify.
* An ACL is used at a long interval, and its function may be left forgotten.
* Names of named ACLs cannot fully explain the ACLs' functions.

**Precautions**



If the description of an ACL rule is not configured, the ACL rule may be misunderstood or misused.




Example
-------

# Configure a description for an ACL numbered 3100.
```
<HUAWEI> system-view
[~HUAWEI] acl 3100
[*HUAWEI-acl4-advance-3100] description This acl is used in 100GE 1/0/1

```