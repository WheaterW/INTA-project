display igmp snooping invalid-packet
====================================

display igmp snooping invalid-packet

Function
--------



The **display igmp snooping invalid-packet** command displays statistics about received invalid IGMP snooping messages.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display igmp snooping invalid-packet vlan** [ *vlanid* ] [ **message-type** { **report** | **leave** | **query** | **hello** } ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display igmp snooping invalid-packet bridge-domain** [ *bdid* ] [ **message-type** { **report** | **leave** | **query** | **hello** } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **message-type** | Displays statistics about the specified type of invalid packet. | - |
| **report** | Displays statistics about invalid Leave packets. | - |
| **leave** | Displays statistics about invalid Query packets. | - |
| **query** | Displays statistics about invalid Report packets. | - |
| **hello** | Displays statistics about invalid Hello packets. | - |
| **bridge-domain** *bdid* | Displays the ID of a bridge domain.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 16777215. |
| **vlan** *vlanid* | Displays statistics about invalid IGMP Snooping packets received from the specified VLAN:   * If vlan-id is not specified, statistics about invalid IGMP Snooping packets received from all VLANs are displayed. * If vlan-id is specified, statistics about invalid IGMP Snooping packets received from the specified VLAN are displayed. | The value is an integer that ranges from 1 to 4094. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display igmp snooping invalid-packet** command displays statistics and information about invalid IGMP snooping packets, helping to locate and rectify faults.If IGMP Snooping entries cannot be created on a multicast network, you can run the **display igmp snooping invalid-packet** command to check whether this fault is caused by invalid IGMP Snooping packets received. If the command output shows that the number of invalid IGMP Snooping packets is not 0, run the **display igmp snooping invalid-packet verbose** command to check detailed information about the invalid IGMP Snooping packets for fault location.If the multicast layer-2 invalid-packet igmp snooping max-count has been configured and the max-number value differs from the packet-number value in the **display igmp snooping invalid-packet verbose** command, detailed information about invalid IGMP Snooping packets is displayed based on the smaller one of the two values.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about invalid IGMP Snooping packets received by a device.
```
<HUAWEI> display igmp snooping invalid-packet vlan
                                                                                
             Statistics of invalid packets for VLAN 1:                      
--------------------------------------------------------------------  
IGMP Snooping General invalid packet:
Fault Length             : 0           Invalid IGMP Type       : 0           
Bad Checksum             : 0           Fault RouterAlert       : 0  
         
IGMP Snooping Query invalid packet:
Invalid Multicast Source : 0          Invalid Multicast Group  : 0 

IGMP Snooping Leave invalid packet:
Invalid IGMP Version     : 0          Invalid Multicast Group  : 0 

IGMP Snooping Report invalid packet:
Invalid IGMP Version     : 0          Invalid Multicast Group  : 0
Invalid Multicast Source : 0           

PIM Hello invalid packet:
Invalid PIM Version      : 0          Bad Checksum             : 0 
Fault Length             : 0          Bad GenID Length         : 0
Bad Holdtime Length      : 0          Bad LanPruneDelay Length : 0
Bad DrPriority Length    : 0
--------------------------------------------------------------------

```

**Table 1** Description of the **display igmp snooping invalid-packet** command output
| Item | Description |
| --- | --- |
| Statistics of invalid packets for VLAN 1 | Number of invalid IGMP snooping messages of a specified VLAN. |
| IGMP Snooping General invalid packet | Number of general invalid IGMP snooping messages. |
| IGMP Snooping Query invalid packet | Number of invalid IGMP snooping Query messages. |
| IGMP Snooping Leave invalid packet | Number of invalid IGMP snooping Leave messages. |
| IGMP Snooping Report invalid packet | Number of invalid IGMP snooping Report messages. |
| Fault Length | Number of messages with invalid message length. |
| Fault RouterAlert | Number of messages with an incorrect Router-Alert field. |
| Invalid Multicast Group | Number of messages with invalid multicast group addresses. |
| Invalid Multicast Source | Number of messages with invalid multicast source addresses. |
| Invalid IGMP Version | Number of messages with an invalid IGMP version. |
| Invalid PIM Version | Number of messages with an invalid PIM version. |
| Invalid IGMP Type | Number of messages with an invalid IGMP type. |
| Bad Checksum | Number of messages with invalid checksum. |
| Bad GenID Length | Number of messages with invalid GenerationID length. |
| Bad Holdtime Length | Number of messages with invalid Holdtime length. |
| Bad LanPruneDelay Length | Number of messages with invalid LanPruneDelay length. |
| Bad DrPriority Length | Number of messages with invalid DrPriority length. |
| PIM Hello invalid packet | Number of invalid PIM Hello messages. |