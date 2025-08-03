display configuration candidate
===============================

display configuration candidate

Function
--------



The **display configuration candidate** command displays commands that have been configured but not submitted.




Format
------

**display configuration candidate**


Parameters
----------

None

Views
-----

All views except the user view


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

This command can be used to display commands that have been configured but not submitted.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display commands that have been configured but not submitted.
```
<HUAWEI> system-view
[~HUAWEI] user-interface vty 0 4
[~HUAWEI-ui-vty0-4] idle-timeout 1 30
[*HUAWEI-ui-vty0-4] display configuration candidate
user-interface vty 0 4
 idle-timeout 1 30

```