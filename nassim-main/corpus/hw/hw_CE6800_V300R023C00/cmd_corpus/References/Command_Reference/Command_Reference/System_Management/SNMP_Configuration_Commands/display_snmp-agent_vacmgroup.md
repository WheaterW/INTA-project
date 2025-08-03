display snmp-agent vacmgroup
============================

display snmp-agent vacmgroup

Function
--------



The **display snmp-agent vacmgroup** command displays all the configured View-based Access Control Model (VACM) groups.




Format
------

**display snmp-agent vacmgroup**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view the information about the group to which a User-based Security Model (USM) user is added, run the **display snmp-agent vacmgroup** command.

**Prerequisites**

An SNMP agent group has been configured using the snmp-agent group command. An SNMP community has been configured using the snmp-agent community command. A USM user has been configured using the snmp-agent usm-user v3 command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configured VACM groups.
```
<HUAWEI> display snmp-agent vacmgroup
--------------------------------------------------
Security name  : john
Group name     : johngroup
Security model : USM
--------------------------------------------------

```

**Table 1** Description of the **display snmp-agent vacmgroup** command output
| Item | Description |
| --- | --- |
| Security name | Security name of a VACM group. |
| Security model | Security model of a VACM group. |
| Group name | Name of a VACM group. |