display igmp snooping statistics
================================

display igmp snooping statistics

Function
--------



The **display igmp snooping statistics** command displays statistics about IGMP snooping.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display igmp snooping statistics vlan** [ *vlanid* ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display igmp snooping statistics bridge-domain** [ *bdid* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **bridge-domain** *bdid* | Displays statistics about IGMP snooping running in a specified BD.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 16777215. |
| **vlan** *vlanid* | Displays statistics about IGMP snooping running in a specified VLAN. | The value is an integer that ranges from 1 to 4094. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



When vlan-id is specified, only the statistics about IGMP snooping in a specified VLAN only are displayed. The statistics about Layer 2 events in the VLAN are not displayed.When bd-id is specified, only the statistics about IGMP snooping in a specified BD are displayed. The statistics about Layer 2 events in the BD are not displayed.



When vlan-id is specified, only the statistics about IGMP snooping in a specified VLAN only are displayed. The statistics about Layer 2 events in the VLAN are not displayed.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about IGMP snooping in VLAN 10.
```
<HUAWEI> display igmp snooping statistics vlan 10
IGMP Snooping Packets Counter
     Statistics for Vlan 10
     Receive V1 Report:  16
     Receive V2 Report:  8768
     Receive V3 Report:  0
     Receive V1 Query :  0
     Receive V2 Query :  2243
     Receive V3 Query :  0
     Receive Leave:      215
     Receive Pim Hello:  0
     Send Query(S=0): 0
     Send Query(S!=0): 529
     Proxy Send General Query:  0
     Proxy Send Group-Specific Query:  0 
     Proxy Send Group-Source-Specific Query:  0
     Recv Invalid Packet:                    0
     Recv Ignore Packet:                     0
     Foward Report:           8784
     Foward Leave:            215     
     Foward Query:            2243

```

**Table 1** Description of the **display igmp snooping statistics** command output
| Item | Description |
| --- | --- |
| Receive V1 Report | Number of received IGMPv1 Report messages. |
| Receive V2 Report | Number of received IGMPv2 Report messages. |
| Receive V3 Report | Number of received IGMPv3 Report messages. |
| Receive V1 Query | Number of received IGMPv1 Query messages. |
| Receive V2 Query | Number of received IGMPv2 Query messages. |
| Receive V3 Query | Number of received IGMPv3 Query messages. |
| Receive Leave | Number of received IGMP Leave messages. |
| Receive Pim Hello | Number of received PIM Hello messages. |
| Send Query(S=0) | Number of sent IGMP Query messages with the source address 0.0.0.0. |
| Send Query(S!=0) | Number of sent IGMP Query messages with the source addresses not being 0. |
| Proxy Send General Query | Number of General Query messages sent by the proxy. |
| Proxy Send Group-Specific Query | Number of group-specific Query messages sent by the proxy. |
| Proxy Send Group-Source-Specific Query | Number of Group-Source-Specific Query messages sent by the proxy. |
| Recv Invalid Packet | Number of received invalid packets. |
| Recv Ignore Packet | Number of received ignored packets. |
| Foward Report | Number of forwarded IGMP Report messages. |
| Foward Leave | Number of forwarded IGMP Leave messages. |
| Foward Query | Number of forwarded IGMP Query messages. |