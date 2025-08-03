display vlan statistics
=======================

display vlan statistics

Function
--------



The **display vlan statistics** command displays statistics about both sent and received packets on all interfaces in a specified VLAN.




Format
------

**display vlan** *vlan-id* **statistics** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Displays packet statistics on all interfaces in a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **slot** *slot-id* | Displays packet statistics of a board in a specified slot. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

If a VLAN contains multiple interfaces, run the display vlan statistics command to view packet statistics of all interfaces in the VLAN. The command output helps you analyze interface faults.

**Prerequisites**

Collecting VLAN packet statistics has been enabled using the **statistic enable** command in the VLAN view.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display VLAN statistics on all interfaces.
```
<HUAWEI> display vlan 10 statistics
Slot: 1
--------------------------------------------------------------------------
Item                                   Packets                       Bytes
--------------------------------------------------------------------------
Inbound                                      0                           0
Outbound                                     0                           0
--------------------------------------------------------------------------

```

**Table 1** Description of the **display vlan statistics** command output
| Item | Description |
| --- | --- |
| Item | Inbound or outbound direction for packet statistics collection:   * Inbound: packets received by an interface. * Outbound: packets sent by an interface. |
| Packets | Number of packets sent and received. |
| Bytes | Number of bytes in packets sent and received. |
| Slot | Slot number of the board. |