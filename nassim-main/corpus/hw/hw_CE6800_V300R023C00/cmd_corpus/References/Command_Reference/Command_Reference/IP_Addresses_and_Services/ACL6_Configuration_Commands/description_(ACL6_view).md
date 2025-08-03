description (ACL6 view)
=======================

description (ACL6 view)

Function
--------



The **description** command configures a description for an ACL6.

The **undo description** command restores the default description of an ACL6.



By default, no description is configured for an ACL6.


Format
------

**description** *text*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *text* | Specifies the description of an ACL6. | The value is a string of 1 to 127 case-sensitive characters, spaces supported. The value must not start with spaces and can be a combination of letters, numbers, and spaces. |



Views
-----

Basic ACL6 view,Advanced ACL6 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **description** command configures a description for an ACL6 in any of the following situations:

* A large number of ACL6s are configured, and their functions are difficult to identify.
* An ACL6 is used at a long interval, and its function may be left forgotten.
* Names of named ACL6s cannot fully explain the ACL6s' functions.

**Precautions**



If the description of an ACL6 is not configured, the ACL6 may be misunderstood or misused.




Example
-------

# Configure a description for an ACL6 numbered 3100.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 3100
[*HUAWEI-acl6-advance-3100] description This acl is used in 100GE 1/0/1

```