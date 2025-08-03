display iqcn statistics
=======================

display iqcn statistics

Function
--------



The **display iqcn statistics** command displays statistics about CNP packets proactively sent by an iQCN-enabled device.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display iqcn statistics slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After the iQCN function is enabled on a forwarding device, the forwarding device detects whether congestion occurs on the network. When detecting congestion, the forwarding device compares the interval at which CNP packets are received with the interval between rate increase events of the NIC. If the interval at which CNP packets are received is longer, the forwarding device proactively sends CNP packets to the NIC of the source host to ensure that the NIC can reduce the packet sending rate in a timely manner. You can run this command to view statistics about CNP packets proactively sent by the forwarding device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about CNP packets proactively sent by an iQCN-enabled device.
```
<HUAWEI> display iqcn statistics slot 1
iQCN: Enable
Queue: 3
RPG Time Reset: 300 us
TX CNP Packets: 0
TX CNP Rate(pps): 0
----------------------------------------------------------------------
Interface                 RX CNP Packets              RX CNP Rate(pps)
----------------------------------------------------------------------
100GE1/0/1                             0                             0
100GE1/0/2                             0                             0
----------------------------------------------------------------------

```

**Table 1** Description of the **display iqcn statistics** command output
| Item | Description |
| --- | --- |
| RPG Time Reset | Interval between rate increase events of the NIC. |
| TX CNP Packets | Number of sent CNP packets. |
| TX CNP Rate(pps) | Rate at which CNP packets are sent. |
| Interface | Interface enabled with the iQCN function. |
| RX CNP Packets | Number of received CNP packets. |
| RX CNP Rate(pps) | Rate at which CNP packets are received. |
| iQCN | Whether the iQCN function is enabled globally. |
| Queue | Lossless queue for which the iQCN function is enabled. |