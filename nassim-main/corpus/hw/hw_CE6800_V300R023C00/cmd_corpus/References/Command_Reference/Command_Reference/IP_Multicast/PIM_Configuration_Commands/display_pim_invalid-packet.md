display pim invalid-packet
==========================

display pim invalid-packet

Function
--------



The **display pim invalid-packet** command displays statistics about received invalid PIM messages and details of these messages.




Format
------

**display pim invalid-packet** [ **interface** { *interface-name* | *interface-type* *interface-number* } | **message-type** { **graft** | **graft-ack** | **hello** | **join-prune** | **state-refresh** | **assert** | **bsr** | **offer** | **backoff** | **win** | **pass** | **announcement** | **discovery** } ] \*

**display pim all-instance invalid-packet** [ **interface** { *interface-name* | *interface-type* *interface-number* } | **message-type** { **graft** | **graft-ack** | **hello** | **join-prune** | **state-refresh** | **assert** | **bsr** | **offer** | **backoff** | **win** | **pass** | **announcement** | **discovery** } ] \*

**display pim all-instance invalid-packet message-type** { **register** | **register-stop** | **crp** }

**display pim vpn-instance** *vpn-instance-name* **invalid-packet** [ **interface** { *interface-name* | *interface-type* *interface-number* } | **message-type** { **hello** | **join-prune** | **assert** | **bsr** | **announcement** | **discovery** } ] \*

**display pim invalid-packet message-type** { **register** | **register-stop** | **crp** }

**display pim vpn-instance** *vpn-instance-name* **invalid-packet** **message-type** { **register** | **register-stop** | **crp** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays statistics about invalid PIM messages received by a specified interface.  interface-type interface-number specifies the type and number of an interface. | - |
| **message-type** | Displays statistics about a specified type of invalid PIM messages received. | - |
| **graft** | Displays statistics about invalid Graft messages. | - |
| **graft-ack** | Displays statistics about invalid Graft-Ack messages. | - |
| **hello** | Displays statistics about invalid Hello messages. | - |
| **join-prune** | Displays statistics about invalid Join/Prune messages. | - |
| **state-refresh** | Displays statistics about invalid State-Refresh messages. | - |
| **assert** | Displays statistics about invalid Assert messages. | - |
| **bsr** | Displays statistics about invalid bootstrap router (BSR) messages. | - |
| **offer** | Displays statistics about invalid Offer messages. | - |
| **backoff** | Displays statistics about invalid Backoff messages. | - |
| **win** | Displays statistics about invalid Win messages. | - |
| **pass** | Displays statistics about invalid Pass messages received. | - |
| **announcement** | Displays statistics about invalid Auto-RP advertisement messages. | - |
| **discovery** | Displays statistics about invalid Auto-RP discovery messages. | - |
| **all-instance** | Indicates all VPN instances. | - |
| **register** | Displays the number of Register messages. | - |
| **register-stop** | Displays the number of Register-Stop messages. | - |
| **crp** | Displays the number of C-RP messages. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 characters. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view statistics and details of invalid PIM messages, run the **display pim invalid-packet** command. The command output helps you locate and rectify faults.If PIM entries fail to be generated on a multicast network, you can run the **display pim invalid-packet** command first to check whether devices have received invalid PIM messages. If the command output contains statistics about invalid PIM messages, run the **display pim invalid-packet verbose** command to view details of invalid PIM messages to locate faults.If interface interface-type interface-number is specified, the command displays statistics about invalid PIM messages received by the specified interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about invalid PIM messages received in the public network instance.
```
<HUAWEI> display pim invalid-packet
             Statistics of invalid packets for public net:                      
- -------------------------------------------------------------------
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
Fault Length            : 0
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
PIM Graft invalid packet:
Invalid Multicast Source: 0           Invalid Multicast Group : 0           
Invalid Up Neighbor     : 0           Invalid IP Source Addr  : 0           
Fault Length            : 0           
PIM Graft-Ack invalid packet:
Invalid Multicast Source: 0           Invalid Multicast Group : 0           
Invalid Up Neighbor     : 0           Invalid IP Source Addr  : 0           
Fault Length            : 0           
PIM State Refresh invalid packet:
Invalid Multicast Source: 0           Invalid Multicast Group : 0           
Invalid Originator Addr : 0           Fault Length            : 0
PIM Auto-RP Announcement invalid packet:
Invalid Dest Addr       : 0           Invalid Source Addr     : 0           
Invalid TTL             : 0           Invalid Source Port     : 0           
PIM Auto-RP Discovery invalid packet:
Invalid Source Addr     : 0           Invalid TTL             : 0           
Invalid Source Port     : 0           Fault Length            : 0           
Invalid RP Addr         : 0           Invalid Multicast Group : 0
PIM Offer invalid packet:
Invalid Dest Addr       : 0           Invalid RP Addr        : 0
PIM Backoff invalid packet:
Invalid Dest Addr       : 0           Invalid RP Addr        : 0
Invalid Offer Addr      : 0
PIM Pass invalid packet:
Invalid Dest Addr       : 0           Invalid RP Addr        : 0
Invalid New Winner Addr : 0
PIM Win invalid packet:
Invalid Dest Addr       : 0           Invalid RP Addr        : 0
- -------------------------------------------------------------------

```

**Table 1** Description of the **display pim invalid-packet** command output
| Item | Description |
| --- | --- |
| Statistics of invalid packets for public net | Instance in which statistics about invalid PIM messages are displayed. |
| PIM General invalid packet | Statistics about general invalid PIM messages. |
| PIM Register invalid packet | Statistics about PIM Register messages. |
| PIM Register-Stop invalid packet | Statistics about invalid PIM Register-Stop messages. |
| PIM CRP invalid packet | Statistics about invalid PIM C-RP messages. |
| PIM Assert invalid packet | Invalid PIM Assert messages. |
| PIM BSR invalid packet | Statistics about invalid PIM BSR messages. |
| PIM Hello invalid packet | Statistics about invalid PIM Hello messages. |
| PIM Join/Prune invalid packet | Statistics about invalid PIM Join/Prune messages. |
| PIM Graft invalid packet | Number of invalid PIM Graft messages. |
| PIM Graft-Ack invalid packet | Statistics about invalid PIM Graft-Ack messages. |
| PIM State Refresh invalid packet | Statistics about invalid PIM State-Refresh messages. |
| PIM Auto-RP Announcement invalid packet | Statistics about invalid PIM Auto-RP announcement messages. |
| PIM Auto-RP Discovery invalid packet | Statistics about invalid PIM Auto-RP discovery messages. |
| PIM Offer invalid packet | Statistics about invalid PIM Offer messages. |
| PIM Backoff invalid packet | Statistics about invalid PIM Backoff messages. |
| PIM Pass invalid packet | Statistics about invalid PIM Pass messages. |
| PIM Win invalid packet | Invalid PIM win messages. |
| Invalid PIM Version | Statistics about messages with invalid PIM versions. |
| Invalid PIM Type | Statistics about messages with invalid PIM message types. |
| Invalid Multicast Source | Messages with invalid multicast source addresses. |
| Invalid Multicast Group | Messages with invalid multicast group addresses. |
| Invalid Dest Addr | Messages with invalid destination addresses. |
| Invalid CRP Addr | Messages with invalid C-RP addresses. |
| Invalid BSR Addr | Messages with invalid BSR addresses. |
| Invalid Addr List | Messages with invalid address lists. |
| Invalid Up Neighbor | Messages with invalid upstream neighbors. |
| Invalid Originator Addr | Invalid Originator address. |
| Invalid Source Addr | Statistics about invalid source address. |
| Invalid TTL | Statistics about messages with invalid TTLs. |
| Invalid Source Port | Statistics about messages with invalid source port numbers. |
| Invalid RP Addr | Statistics about messages with invalid RP addresses. |
| Invalid Offer Addr | Invalid address of the Offer message. |
| Invalid New Winner Addr | Invalid new Win message address. |
| Invalid IP Source Addr | Invalid source IP address. |
| Fault Length | Statistics about messages with invalid lengths. |
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