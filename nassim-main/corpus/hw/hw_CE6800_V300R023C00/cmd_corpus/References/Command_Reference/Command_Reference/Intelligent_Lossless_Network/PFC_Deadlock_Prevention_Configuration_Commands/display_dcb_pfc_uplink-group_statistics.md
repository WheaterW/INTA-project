display dcb pfc uplink-group statistics
=======================================

display dcb pfc uplink-group statistics

Function
--------



The **display dcb pfc uplink-group statistics** command displays statistics about PFC deadlock prevention.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dcb pfc uplink-group statistics** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view statistics about PFC deadlock prevention.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about PFC deadlock prevention. (CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ)
```
<HUAWEI> display dcb pfc uplink-group statistics slot 1
O/N: Original/New
Slot: 1  Chip: 0
-----------------------------------------------------------------------
Index   NewPriority   Dscp                 Count    LastAdjustmentTime
                       O/N
-----------------------------------------------------------------------
    0             3   30/5                219096    2023-04-21 01:31:41
    1             2   32/16               219097    2023-04-21 01:31:41
-----------------------------------------------------------------------

```

# Display statistics about PFC deadlock prevention. (CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM)
```
<HUAWEI> display dcb pfc uplink-group statistics slot 1
O/N: Original/New
Slot: 1  Chip: 0
----------------------------------------------------------------------------------------------
Index   PacketType   OutInterface   Priority Dscp                 Count    LastAdjustmentTime
                                    O/N       O/N                                 
----------------------------------------------------------------------------------------------
    0   Layer-2      100GE1/0/1     0/2       1/3               4532410    --
    1   Layer-2      Eth-Trunk1     0/2       1/3               4532410    --                
    2   Layer-3      --             0/2       1/3                     0    --                 
----------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display dcb pfc uplink-group statistics** command output
| Item | Description |
| --- | --- |
| Index | Index. |
| NewPriority | Changed queue of packets in the hook-shaped flow. |
| Dscp | Original and changed DSCP values of packets in the hook-shaped flow. |
| Count | Number of times ACL rules match packets in the hook-shaped flow. |
| LastAdjustmentTime | Last time when an ACL rule matches packets in the hook-shaped flow and the queue priority and DSCP value of packets in a hook-shaped flow matching a PFC uplink interface group are adjusted. |
| PacketType | Packet type. Layer-2 indicates Layer 2 traffic, and Layer-3 indicates Layer 3 traffic. For Layer 3 traffic, the outbound interface of the hook-shaped flow cannot be queried using this command. |
| OutInterface | Outbound interface of packets in the hook-shaped flow. If Layer 3 traffic does not have outbound interface information, this field is displayed as --. |
| Priority | Original and changed queues of packets in the hook-shaped flow. |
| Slot | Slot number. |
| Chip | Chip ID. |