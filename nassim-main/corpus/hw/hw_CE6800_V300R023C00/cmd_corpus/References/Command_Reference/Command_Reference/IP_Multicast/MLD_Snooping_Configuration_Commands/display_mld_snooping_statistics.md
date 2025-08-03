display mld snooping statistics
===============================

display mld snooping statistics

Function
--------



The **display mld snooping statistics** command displays MLD snooping statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mld snooping statistics vlan** [ *vlan-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Displays MLD snooping statistics of a specified VLAN. | The value is an integer ranging from 1 to 4094. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If vlanid is specified, only MLD snooping statistics in the specified VLAN is displayed and the number of Layer 2 events occurring in the VLAN is not displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the MLD snooping statistics of VLAN 10.
```
<HUAWEI> display mld snooping statistics vlan 10
 MLD Snooping Packets Counter:
   Statistics for VLAN 10
     Receive V1 Report:          0
     Receive V2 Report:          0
     Receive V1 Query:           0
     Receive V2 Query:           0
     Receive Done:               0
     Receive Pim Hello:          0
     Send Query (S=0):           0
     Send Query (S!=0):          0
     Proxy Send General Query:               0
     Proxy Send Group-Specific Query:        0
     Proxy Send Group-Source-Specific Query: 0
     Recv Invalid Packet:                    0
     Recv Ignore Packet:                     0
     Foward Report:           0
     Foward Done:             0
     Foward Query:            0

```

**Table 1** Description of the **display mld snooping statistics** command output
| Item | Description |
| --- | --- |
| MLD Snooping Packets Counter | Statistics about MLD Snooping packets. |
| Receive V1 Report | Number of received MLDv1 Report messages. |
| Receive V2 Report | Number of received MLDv2 Report messages. |
| Receive V1 Query | Number of received MLDv1 Query messages. |
| Receive V2 Query | Number of received MLDv2 Query messages. |
| Receive Done | Number of received MLD Done messages. |
| Receive Pim Hello | Number of received PIM Hello messages. |
| Send Query (S=0) | Number of sent MLD Query messages with the source address 0.0.0.0. |
| Send Query (S!=0) | Number of sent MLD Query messages with the source address that is not 0.0.0.0. |
| Proxy Send General Query | Number of general Query messages sent by the proxy. |
| Proxy Send Group-Specific Query | Number of group-specific Query messages sent by the proxy. |
| Proxy Send Group-Source-Specific Query | Number of source-and group-specific Query messages sent by the proxy. |
| Recv Invalid Packet | Number of received invalid PIM messages. |
| Recv Ignore Packet | Number of MLD messages that were received but ignored. |
| Foward Report | Number of forwarded MLD Report messages. |
| Foward Done | Number of forwarded MLD Done messages. |
| Foward Query | Number of forwarded MLD Query messages. |