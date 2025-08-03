snmp-agent remote-engineid
==========================

snmp-agent remote-engineid

Function
--------



The **snmp-agent remote-engineid** command is used to create a remote engine ID for a remote SNMPv3 user.

The **undo snmp-agent remote-engineid** command is used to delete a remote engine ID.



By default, no remote engine ID is configured.


Format
------

**snmp-agent remote-engineid** *engine-Id*

**undo snmp-agent remote-engineid** *engine-Id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *engine-Id* | Specifies the remote engine Id. | The value ranges from 10 to 64, in hexadecimal notation. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

This command can create a remote engine ID, which can be associated with a remote SNMPv3 user.


Example
-------

# Create a remote engine
```
<HUAWEI> system-view
Enter system view, return user view with return command.
[~HUAWEI] snmp-agent remote-engineid 123654789654

```