display detector packet-trace profile
=====================================

display detector packet-trace profile

Function
--------



The **display detector packet-trace profile** command displays information about a specified packet template or all packet templates configured on the device.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display detector packet-trace profile** [ *profile-name* ]

**display detector packet-trace profile** *profile-name* **interface** { *interface-name* | *interface-type* *interface-number* } **result**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profile-name* | Specifies the name of a packet trace profile. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **interface** *interface-number* | Specifies the interface number. | The value is a string of 1 to 256 case-insensitive characters. It cannot contain spaces. |
| *interface-name* | Specifies the interface name. | The value is a string of 1 to 256 case-insensitive characters. It can contain spaces. |
| *interface-type* | Specifies the interface type. | The value is a string of 1 to 256 case-insensitive characters. It can contain spaces. |
| **result** | Packet trace result. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

A network typically carries a variety of services. However, packet loss may occur during packet forwarding on network devices, and the causes of such issues can be difficult to locate. The packet trace function can locate the cause of packet loss that occurs during forwarding on a device. Besides, this function can show you the packet forwarding entries on devices and the hash calculation results for path selection.

**Precautions**

Packet trace can locate the packet drop reason. However, if packet drop is caused by congestion, packet trace may not accurately locate the reason because congestion is unexpected and occurs randomly.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# View the configured profile information.
```
<HUAWEI> display detector packet-trace profile tcp_test
Packet trace profile: tcp_test
-------------------------------------------------------------------------------
Source MAC         : 00e0-fc12-3456
Destination MAC    : 00e0-fc56-7890
VLAN               : 100
8021P              : 2
Source IP          : 10.1.1.1
Destination IP     : 10.2.2.2
DSCP               : 23
TTL                : 10
IP protocol        : TCP
Source port        : 6580
Destination port   : 7850
Payload            : 1a6805d67407d387ebadefa850189f8817c300000980011ddb77019494
                     866f
-------------------------------------------------------------------------------

```

# Simulate the packet forwarding process inside a device with the specified inbound interface (the detection packet is constructed by the device based on the profile test) and display the packet drop reason and forwarding entries.
```
<HUAWEI> display detector packet-trace profile test interface 100GE 1/0/1 result
Packet trace result:
--------------------------------------------------------------------------------
Packet Profile                  : test
Packet Inbound Interface        : 100GE1/0/1
Packet Multicast Group          : - 
Packet Drop Reason              : DISCARD_QUEUE_DROP
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display detector packet-trace profile** command output
| Item | Description |
| --- | --- |
| Packet trace profile | Name of a packet trace profile. |
| Packet | Content of the detection packet. |
| Packet Profile | Name of a packet trace profile. |
| Packet Inbound Interface | Inbound interface of the detection packet. |
| Packet Drop Reason | Reason why a detection packet is discarded. |
| Packet trace result | Trace result of detection packets. |
| Packet Multicast Group | Information about the multicast group corresponding to the outbound interface of detection packets. |
| Source MAC | Source MAC address of the detection packet. |
| Source IP | Source IP address of the detection packet. |
| Source port | Source port number of a TCP or UDP detection packet. |
| Destination MAC | Destination MAC address of the detection packet. |
| Destination IP | Destination IP address of the detection packet. |
| Destination port | Destination port number of a TCP or UDP detection packet. |
| VLAN | VLAN ID of the detection packet. |
| 8021P | 802.1p priority of the detection packet. |
| IP protocol | Protocol type of the detection packet. The options are as follows:  TCP: indicates a TCP packet.  UDP: indicates a UDP packet.  ICMP: indicates an ICMP packet. |
| DSCP | DSCP field of the detection packet. |
| TTL | TTL of the detection packet. |
| Payload | Payload of the detection packet. |