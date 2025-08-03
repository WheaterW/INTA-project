display pim ipv6 invalid-packet
===============================

display pim ipv6 invalid-packet

Function
--------



The **display pim ipv6 invalid-packet** command displays statistics about invalid IPv6 PIM messages received by a device and details of these messages.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display pim ipv6 invalid-packet** [ **interface** { *interface-name* | *interface-type* *interface-number* } | **message-type** { **hello** | **join-prune** | **assert** | **bsr** } ] \*

**display pim ipv6 vpn-instance** *vpn-instance-name* **invalid-packet** [ **interface** { *interface-name* | *interface-type* *interface-number* } | **message-type** { **hello** | **join-prune** | **assert** | **bsr** } ] \*

**display pim ipv6 all-instance invalid-packet** [ **interface** { *interface-name* | *interface-type* *interface-number* } | **message-type** { **hello** | **join-prune** | **assert** | **bsr** } ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays statistics about invalid IPv6 PIM messages received by a specified interface. | - |
| **message-type** | Displays statistics about invalid IPv6 PIM messages of a specific type. | - |
| **hello** | Displays statistics about invalid Hello messages. | - |
| **join-prune** | Displays statistics about invalid Join/Prune messages. | - |
| **assert** | Displays statistics about invalid Assert messages. | - |
| **bsr** | Displays statistics about invalid BootStrap router (BSR) messages. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Specifies all VPN instance. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the **display pim ipv6 invalid-packet** command to view statistics and details of invalid IPv6 PIM messages for fault location and rectification.If IPv6 PIM entries fail to be generated on a multicast network, you can run the **display pim ipv6 invalid-packet** command first to check whether devices have received invalid IPv6 PIM messages.You can run the **display pim ipv6 invalid-packet** command to view statistics about invalid IPv6 PIM messages received by a specified interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about invalid IPv6 PIM messages received by a device in the public network instance.
```
<HUAWEI> display pim ipv6 invalid-packet

             Statistics of invalid packets for public net:                      
--------------------------------------------------------------------            
PIM General invalid packet:
Invalid PIM Version     : 0           Invalid PIM Type        : 0
Fault Length            : 0           Bad Checksum            : 0

PIM Register invalid packet:
Invalid Multicast Source: 0           Invalid Multicast Group : 0
Invalid Dest Addr       : 0

PIM Register-Stop invalid packet:
Invalid Multicast Source: 0           Invalid Multicast Group : 0
Invalid Dest Addr       : 0           IP Source not RP        : 0

PIM CRP invalid packet:
Invalid Dest Addr       : 0           Invalid CRP Addr        : 0
Fault Length            : 0           CRP Adv Fault Length    : 0
Invalid Multicast Group : 0

PIM Assert invalid packet:
Invalid Dest Addr       : 0           Invalid IP Source Addr  : 0
Invalid Multicast Source: 0           Invalid Multicast Group : 0

PIM BSR invalid packet:
Bad Payload             : 0           Fault Length            : 0
Bad Scope Mask          : 0           Invalid Multicast Group : 0
Not CBSR But BSR        : 0           Invalid BSR Addr        : 0
Fault Hash Length       : 0           Invalid IP Source Addr  : 0

PIM Hello invalid packet:
Invalid Addr List       : 0           Fault Length            : 0
Bad Holdtime Length     : 0           Bad LanPruneDelay Length: 0
Bad DrPriority Length   : 0           Bad GenID Length        : 0
Invalid Dest Addr       : 0           Invalid IP Source Addr  : 0

PIM Join/Prune invalid packet:
Invalid Multicast Source: 0           Invalid Multicast Group : 0
Invalid Up Neighbor     : 0           Invalid IP Source Addr  : 0
Invalid Dest Addr       : 0           Fault Length            : 0  

PIM Offer invalid packet:
Invalid Dest Addr       : 0           Invalid RP Addr         : 0

PIM Backoff invalid packet:
Invalid Dest Addr       : 0           Invalid RP Addr         : 0
Invalid Offer Addr      : 0

PIM Pass invalid packet:
Invalid Dest Addr       : 0           Invalid RP Addr         : 0
Invalid New Winner Addr : 0

PIM Win invalid packet:
Invalid Dest Addr       : 0           Invalid RP Addr         : 0
--------------------------------------------------------------------

```

**Table 1** Description of the **display pim ipv6 invalid-packet** command output
| Item | Description |
| --- | --- |
| Statistics of invalid packets for public net | VPN instance in which statistics about invalid IPv6 PIM messages need to be displayed. |
| PIM General invalid packet | General invalid IPv6 PIM messages. |
| PIM Register invalid packet | Invalid IPv6 PIM Register message. |
| PIM Register-Stop invalid packet | Invalid IPv6 PIM Register-Stop messages. |
| PIM CRP invalid packet | Invalid IPv6 PIM C-RP messages. |
| PIM Assert invalid packet | Messages with invalid IPv6 PIM Assert messages. |
| PIM BSR invalid packet | Invalid IPv6 PIM BSR messages. |
| PIM Hello invalid packet | Invalid IPv6 PIM Hello messages. |
| PIM Join/Prune invalid packet | Invalid IPv6 PIM Join/Prune messages. |
| PIM Offer invalid packet | Statistics about invalid IPv6 PIM Offer messages. |
| PIM Backoff invalid packet | Statistics about invalid IPv6 PIM Backoff messages. |
| PIM Pass invalid packet | Statistics about invalid IPv6 PIM Pass messages. |
| PIM Win invalid packet | Number of invalid IPv6 PIM Win messages. |
| Invalid PIM Version | Messages with invalid IPv6 PIM version. |
| Invalid PIM Type | Messages with invalid IPv6 PIM message type. |
| Invalid Multicast Source | Messages with invalid multicast source addresses. |
| Invalid Multicast Group | Messages with invalid multicast group addresses. |
| Invalid Dest Addr | Messages with invalid destination addresses. |
| Invalid CRP Addr | Messages with invalid C-RP addresses. |
| Invalid IP Source Addr | Messages with invalid source addresses. |
| Invalid BSR Addr | Messages with invalid BSR addresses. |
| Invalid Addr List | Messages with invalid address lists. |
| Invalid Up Neighbor | Messages with invalid upstream neighbors. |
| Invalid RP Addr | Statistics about messages with invalid RP addresses. |
| Invalid New Winner Addr | Invalid new Win message address. |
| Invalid Offer Addr | Invalid address of the Offer message. |
| Fault Length | Messages with invalid lengths. |
| Fault Hash Length | Messages whose hash mask fields of invalid lengths. |
| Bad Checksum | Messages with invalid checksum. |
| Bad Payload | Messages with invalid payloads. |
| Bad Scope Mask | Messages with invalid scope masks. |
| Bad Holdtime Length | Messages whose Holdtime fields are of invalid lengths. |
| Bad LanPruneDelay Length | Messages whose LanPruneDelay fields are of invalid lengths. |
| Bad DrPriority Length | Messages whose DrPriority fields are of invalid lengths. |
| Bad GenID Length | Messages whose GenerationID fields are of invalid lengths. |
| IP Source not RP | Messages whose source addresses are not the RP address. |
| CRP Adv Fault Length | Messages whose CRP Adv fields are of invalid lengths. |
| Not CBSR But BSR | Messages received from non-C-BSRs. |