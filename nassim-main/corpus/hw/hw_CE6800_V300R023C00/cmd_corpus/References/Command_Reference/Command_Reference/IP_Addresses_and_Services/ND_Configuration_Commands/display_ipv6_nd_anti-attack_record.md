display ipv6 nd anti-attack record
==================================

display ipv6 nd anti-attack record

Function
--------



The **display ipv6 nd anti-attack record** command displays ND message attack records.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 nd anti-attack record** { **all** | { *interface-name* | *interface-type* *interface-num* } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays all ND message attack records. | - |
| *interface-name* | Displays all ND message attack records on a specified interface. | - |
| *interface-type* *interface-num* | Displays all ND message attack records on a specified interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the **display ipv6 nd anti-attack record** command to view ND message attack records, thereby obtaining information about the attack source. For example, you can configure a rate at which a device processes ND messages so that the device processes only the specified number of ND messages within a specified period and discards excess ND messages. To view records about discarded ND messages, run the **display ipv6 nd anti-attack record** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display ND message attack records on a specified interface.
```
<HUAWEI> display ipv6 nd miss anti-attack record 100ge 1/0/1
----------------------------------------------------------------------------------
Packet Type      : NA
Interface Name   : 100GE1/0/1
Source IP        : 2001:db8:1::1
Destination IP   : 2001:db8:1::2
Target IP        : 2001:db8:1::1
Source MAC       : 00-e0-fc-12-34-56
Destination MAC  : 00-e0-fc-12-34-78
PE Vlan          : -
CE Vlan          : -
Attack Count     : 12
Last Attack Time : 2021-02-18 03:42:57
Dropped Reason   : VR destination ip attack limit

----------------------------------------------------------------------------------
Total: 1

```

**Table 1** Description of the **display ipv6 nd anti-attack record** command output
| Item | Description |
| --- | --- |
| Packet Type | Type of a packet. |
| Interface Name | Interface name. |
| Source IP | The source IP address. |
| Source MAC | Source MAC address. |
| Destination IP | Indicates the destination IP address. |
| Destination MAC | Destination MAC addresses. |
| Target IP | Target IP address. |
| PE Vlan | Outer VLAN ID. |
| CE Vlan | Inner VLAN ID. |
| Attack Count | Number of attacks. |
| Last Attack Time | Latest attack time. |
| Dropped Reason | Reason for message discarding. |
| Total | Total number. |