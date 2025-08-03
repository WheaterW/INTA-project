display mld snooping invalid-packet vlan
========================================

display mld snooping invalid-packet vlan

Function
--------



The **display mld snooping invalid-packet vlan** command displays statistics about invalid MLD messages received by the device of VLAN.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mld snooping invalid-packet vlan** [ *vlanid* ] [ **message-type** { **report** | **done** | **query** | **hello** } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlanid* | Displays statistics about invalid MLD snooping messages received by the specified VLAN:   * If vlan-id is not specified, statistics about invalid MLD snooping messages received by all VLANs are displayed. * If vlan-id is specified, statistics about invalid MLD snooping messages received by the specified VLAN are displayed. | The value is an integer that ranges from 1 to 4094. |
| **message-type** | Displays statistics about the specified type of invalid message. | - |
| **report** | Displays statistics about invalid Report message. | - |
| **done** | Displays statistics about invalid Done messages. | - |
| **query** | Displays statistics about invalid Query message. | - |
| **hello** | Displays statistics about invalid Hello messages. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If MLD snooping entries cannot be created on a multicast network, run the **display mld snooping invalid-packet vlan** command to check whether this fault is caused by invalid MLD snooping messages received of VLAN.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about invalid MLD snooping messages received by a device.
```
<HUAWEI> display mld snooping invalid-packet vlan
           Statistics of invalid packets for VLAN 100
--------------------------------------------------------------------
MLD Snooping General invalid packet:
Fault Length             : 0           Invalid MLD Type         : 0
Bad Checksum             : 0           Fault RouterAlert        : 0

MLD Snooping Query invalid packet:
Invalid Multicast Source : 0           Invalid Multicast Group  : 0

MLD Snooping Done invalid packet:
Invalid MLD Version      : 0           Invalid Multicast Group  : 0

MLD Snooping Report invalid packet:
Invalid MLD Version      : 0           Invalid Multicast Group  : 0
Invalid Multicast Source : 0

PIM Hello invalid packet:
Invalid PIM Version      : 0           Bad Checksum             : 0
Fault Length             : 0           Bad GenID Length         : 0
Bad Holdtime Length      : 0           Bad LanPruneDelay Length : 0
Bad DrPriority Length    : 0
--------------------------------------------------------------------

```

**Table 1** Description of the **display mld snooping invalid-packet vlan** command output
| Item | Description |
| --- | --- |
| Statistics of invalid packets for VLAN | Statistics about invalid MLD snooping messages received by a VLAN. |
| MLD Snooping General invalid packet | Statistics about general invalid MLD snooping messages. |
| MLD Snooping Query invalid packet | Statistics about invalid MLD snooping Query messages. |
| MLD Snooping Done invalid packet | Statistics about invalid MLD snooping Done messages. |
| MLD Snooping Report invalid packet | Statistics about invalid MLD snooping Report messages. |
| Fault Length | Number of messages with invalid message length. |
| Fault RouterAlert | Number of messages with error Router-Alert fields. |
| Invalid MLD Type | Number of messages with invalid message types. |
| Invalid Multicast Group | Number of messages with invalid multicast group addresses. |
| Invalid Multicast Source | Number of messages with invalid multicast source addresses. |
| Invalid MLD Version | Number of messages with invalid MLD version information. |
| Invalid PIM Version | Number of messages with invalid PIM version information. |
| Bad Checksum | Number of messages with invalid checksum. |
| Bad GenID Length | Number of messages with invalid GenerationID length. |
| Bad Holdtime Length | Number of messages with invalid Holdtime length. |
| Bad LanPruneDelay Length | Number of messages with invalid LanPruneDelay length. |
| Bad DrPriority Length | Number of messages with invalid DrPriority length. |
| PIM Hello invalid packet | Statistics about invalid PIM Hello messages. |