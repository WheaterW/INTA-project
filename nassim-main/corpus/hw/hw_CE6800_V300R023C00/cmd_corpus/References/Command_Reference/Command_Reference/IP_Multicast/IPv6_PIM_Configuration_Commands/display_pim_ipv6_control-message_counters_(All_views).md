display pim ipv6 control-message counters (All views)
=====================================================

display pim ipv6 control-message counters (All views)

Function
--------



The **display pim ipv6 control-message counters** command displays the number of sent and received IPv6 PIM control messages.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display pim ipv6 control-message counters interface** { *interface-type* *interface-number* | *interface-name* } [ **message-type** { **assert** | **bsr** | **hello** | **join-prune** } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **message-type** | Indicates the type of a PIM message. | - |
| **assert** | Indicates the number of Assert messages. | - |
| **bsr** | Indicates the number of BootStrap router (BSR) messages. | - |
| **hello** | Indicates the number of Hello messages. | - |
| **join-prune** | Indicates the number of Join/Prune messages. | - |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display pim ipv6 control-message counters** command is used to display the number received, sent, invalid, or filtered out IPv6 PIM control messages. This command is usually used to locate faults in IPv6 PIM, for example:

* If a PIM neighbor relationship cannot be set up, run this command on two ends to check whether they can normally send or receive Hello messages.
* If (\*, G) or (S, G) entries cannot be generated, run this command on an upstream or downstream device to check whether the device can normally send or receive Join/Prune messages.On live networks, check the number of PIM messages of a specific type based on fault symptoms.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about various IPv6 PIM control messages sent and received by 100GE1/0/1.
```
<HUAWEI> display pim ipv6 control-message counters interface 100GE 1/0/1
VPN-Instance: public net
 Register* - Register Anycast-RP, Probe* - Probe Anycast-RP
- ---------------------------------------------------------------------------
 PIM control-message counters for interface: 100GE1/0/1
Message Type     Received         Sent             Invalid      Filtered
 Assert           0                0                0            0
 Hello            328              331              0            0
 Join-prune       2                0                0            0
 BSR              9778             0                0            0
 Offer            9                17               0            0
 Backoff          0                0                0            0
 Win              0                105              0            0
 Pass             0                0                0            0

```

**Table 1** Description of the **display pim ipv6 control-message counters (All views)** command output
| Item | Description |
| --- | --- |
| Register\* | Statistics about Register messages in the Anycast-RP scenario. |
| Register | Register messages. |
| Probe\* | Statistics about Probe messages in the Anycast-RP scenario. |
| Probe | Statistics about Null-Register messages. |
| PIM control-message counters for interface | Interface on which statistics about PIM control messages are collected. |
| Message Type | Type of a PIM control message. |
| Received | Number of PIM control messages received by the current interface. |
| Sent | Number of PIM control messages sent by the current interface. |
| Invalid | Number of invalid PIM control messages. |
| Filtered | Number of PIM control messages filtered out by the current interface. |
| Assert | Assert messages. |
| Hello | Hello messages. |
| Join-prune | Join/Prune messages. |
| BSR | Bootstrap messages. |
| Offer | Statistics about Offer messages in designated forwarder (DF) election. |
| Backoff | Statistics about Backoff messages in DF election. |
| Win | Statistics about Win messages in DF election. |
| Pass | Statistics about Pass messages in DF election. |
| VPN-Instance | VPN instance to which PIM control message statistics belong. |