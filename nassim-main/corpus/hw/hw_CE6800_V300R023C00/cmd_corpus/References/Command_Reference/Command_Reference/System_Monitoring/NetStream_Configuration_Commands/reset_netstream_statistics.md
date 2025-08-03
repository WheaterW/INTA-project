reset netstream statistics
==========================

reset netstream statistics

Function
--------



The **reset netstream statistics** command clears the IPv4, IPv6, or VXLAN flexible flow statistics on a device.




Format
------

**reset netstream statistics** { **ip** | **ipv6** | **vxlan** **inner-ip** } **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip** | Deletes IPv4 flow statistics. | - |
| **ipv6** | Deletes IPv6 flow statistics. | - |
| **vxlan** | Deletes VXLAN flexible flow statistics. | - |
| **inner-ip** | Specifies the inner packet of the IPv4 type for VXLAN packets. | - |
| **slot** *slot-id* | Specifies a slot ID. If no slot ID is specified, global statistics are cleared. | The value must be set according to the device configuration. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When diagnosing and locating network faults, collect flow statistics in a specified period. Before statistics collection starts, you can run this command to delete historical flow statistics.

**Precautions**

The **reset netstream statistics ethernet** command deletes all flow statistics. The statistics cannot be restored after being deleted. Before running this command, confirm the action.You can run this command multiple times at any interval.


Example
-------

# Delete IPv4 flow statistics on the device.
```
<HUAWEI> reset netstream statistics ip slot 1

```