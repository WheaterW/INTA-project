display pim ipv6 control-message counters message-type
======================================================

display pim ipv6 control-message counters message-type

Function
--------



The **display pim ipv6 control-message counters message-type** command displays the number of sent and received IPv6 PIM control messages.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display pim ipv6 control-message counters message-type** { **assert** | **bsr** | **hello** | **join-prune** } [ **interface** { *port-type* *port-num* | *port-name* } ]

**display pim ipv6** { **vpn-instance** *vpn-instance-name* | **all-instance** } **control-message** **counters** **message-type** { **assert** | **bsr** | **hello** | **join-prune** } [ **interface** { *port-type* *port-num* | *port-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **assert** | Indicates the number of Assert messages. | - |
| **bsr** | Indicates the number of BootStrap router (BSR) messages. | - |
| **hello** | Indicates the number of Hello messages. | - |
| **join-prune** | Indicates the number of Join/Prune messages. | - |
| **interface** *port-type* *port-num* | Specifies the type and number of an interface. | - |
| **interface** *port-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **all-instance** | Indicates all VPN instances. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display pim ipv6 control-message counters message-type** command is used to display the number received, sent, invalid, or filtered out IPv6 PIM control messages. This command is usually used to locate faults in IPv6 PIM, for example:

* If a PIM neighbor relationship cannot be set up, run this command on two ends to check whether they can normally send or receive Hello messages.
* If (\*, G) or (S, G) entries cannot be generated, run this command on an upstream or downstream device to check whether the device can normally send or receive Join/Prune messages.On live networks, check the number of PIM messages of a specific type based on fault symptoms.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about Assert control messages sent and received by 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] display pim ipv6 control-message counters message-type assert interface 100GE 1/0/1
 VPN-Instance: public net
 Register* - Register Anycast-RP, Probe* - Probe Anycast-RP
 Announcement - Auto-RP Announcement, Discovery - Auto-RP Discovery
 ----------------------------------------------------------------------------
 PIM control-message counters for interface: 100GE1/0/1
 MessageType      Received         Sent             Invalid          Filtered   
 Assert           0                0                0                0

```

**Table 1** Description of the **display pim ipv6 control-message counters message-type** command output
| Item | Description |
| --- | --- |
| Register\* | Statistics about Register messages in the Anycast-RP scenario. |
| Probe\* | Statistics about Probe messages in the Anycast-RP scenario. |
| Announcement | Statistics about Announcement messages in the Auto-RP scenario. |
| Discovery | Statistics about Discovery messages in the Auto-RP scenario. |
| PIM control-message counters for interface | Interface that collects statistics of PIM control messages. |
| MessageType | Type of a PIM control message. |
| Received | Number of PIM control messages received by the current interface. |
| Sent | Number of PIM control messages sent by the current interface. |
| Invalid | Number of invalid PIM control messages. |
| Filtered | Number of PIM control messages filtered out by the current interface. |
| VPN-Instance | VPN instance to which PIM control message statistics belong. |