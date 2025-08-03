display gtsm statistics
=======================

display gtsm statistics

Function
--------



The **display gtsm statistics** command displays GTSM statistics on a specified slot or all slots.




Format
------

**display gtsm statistics** { *slot-id* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *slot-id* | Specifies the slot ID. | - |
| **all** | Displays GTSM statistics on all slots. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



You can run the **display gtsm statistics** command to view GTSM statistics in all slots or a specified slot. The statistics include the total number of received BGP, BGPv6, RIP, OSPF, and OSPFv3 packets, the number of passed packets, and the number of discarded packets.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display GTSM statistics on all slots.
```
<HUAWEI> display gtsm statistics all
GTSM Statistics Table
---------------------------------------------------------------
SlotId  Protocol   Total Counters  Drop Counters  Pass Counters
---------------------------------------------------------------
1       BGP                    18              0             18
1       BGPv6                   0              0              0
1       OSPF                    0              0              0
1       OSPFv3                  0              0              0
1       RIP                     0              0              0
---------------------------------------------------------------

```

**Table 1** Description of the **display gtsm statistics** command output
| Item | Description |
| --- | --- |
| SlotId | Slot ID. |
| Protocol | Protocol type:  * Software-based forwarding: protocol differentiated. * Hardware-based forwarding: protocol undifferentiated, displayed as "-----". |
| Total Counters | Total number of packets. |
| Drop Counters | Total number of dropped packets. |
| Pass Counters | Total number of packets that have passed. |