display auto-source-trace record
================================

display auto-source-trace record

Function
--------



The **display auto-source-trace record** command displays statistics about proactive source tracing.




Format
------

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**display auto-source-trace record** [ **packet** { **arp-request** | **arp-request-uc** | **arp-reply** | **nd** } ] [ **slot** *slot-id* ]

For CE6885-LL (low latency mode):

**display auto-source-trace record** [ **packet** { **arp-request** | **arp-request-uc** | **arp-reply** } ] [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **packet** | Displays statistics about proactive source tracing based on the specified packet type. | - |
| **arp-request** | Displays statistics about proactive source tracing of arp-request packets. | - |
| **arp-request-uc** | Displays statistics about proactive source tracing of arp-request-uc packets. | - |
| **arp-reply** | Displays statistics about proactive source tracing of arp-reply packets. | - |
| **nd** | Displays statistics about proactive source tracing of nd packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **slot** *slot-id* | Specifies the slot ID. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After the proactive source tracing function is configured, you can run the **display auto-source-trace** command to view statistics about proactive source tracing.You can run this command to view packet statistics within a maximum of 32 sampling intervals for proactive source tracing. If you run this command for the first time, you can view the packet statistics within the first sampling interval. If you run this command again, you can view the packet statistics within the second sampling interval, and so on. Packet statistics within a sampling interval can be obtained only once by running this command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about proactive source tracing.
```
<HUAWEI> display auto-source-trace record slot 1
Slot               : 1
PacketType         : ARP-REQUEST
Start Time         : 2019-11-07 11:44:24
End Time           : 2019-11-07 11:44:33
--------------------------------------------------------------------------------
 NO 1 Packet Info:
  Interface Name   : 100GE1/0/1
  Source MAC       : 00e0-fc12-3456
  PE VLAN          : 1000
  CE VLAN          : --
  Source IP        : 192.168.1.1
  Protocol         : --
  Packet Count     : 25536
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display auto-source-trace record** command output
| Item | Description |
| --- | --- |
| Slot | Slot ID. |
| PacketType | Packet type. |
| Start Time | Time when traffic statistics collection starts. |
| End Time | Time when traffic statistics collection ends. |
| NO 1 Packet Info | Information about the first packet. |
| Packet Count | Number of packets. |
| Interface Name | Name of an interface. |
| Source MAC | Source MAC address. |
| Source IP | Source IP address. |
| PE VLAN | Outer VLAN ID. |
| CE VLAN | Inner VLAN ID. |
| Protocol | Packet type. |