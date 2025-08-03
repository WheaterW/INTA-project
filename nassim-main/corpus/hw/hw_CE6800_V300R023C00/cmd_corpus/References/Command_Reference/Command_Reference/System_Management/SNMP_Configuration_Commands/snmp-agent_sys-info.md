snmp-agent sys-info
===================

snmp-agent sys-info

Function
--------



The **snmp-agent sys-info** command configures SNMP system information.

The **undo snmp-agent sys-info** command restores the default SNMP system information.



By default, the system maintenance information is "R&D Beijing, Huawei Technologies Co.,Ltd.", the system location is "Beijing China".


Format
------

**snmp-agent sys-info** { **contact** *contact* | **location** *location* }

**undo snmp-agent sys-info contact**

**undo snmp-agent sys-info location**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **contact** *contact* | Specifies contact information of system maintenance. | The value is a string of 1 to 255 characters, with spaces supported. |
| **location** *location* | Specifies the location of a device. | The value is a string of 1 to 255 characters, with spaces supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To configure the contact information for a managed node, run the snmp-agent sys-info contact *contact*command.To configure the physical location of a node, run the snmp-agent sys-info location *location*command.


Example
-------

# Set the contact information on system maintenance to call Operator at 010-12345678.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent sys-info contact call Operator at 010-12345678

```

# Set the location of a device to shanghai China.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent sys-info location shanghai China

```