display pim control-message counters
====================================

display pim control-message counters

Function
--------



The **display pim control-message counters** command displays statistics about PIM control messages.




Format
------

**display pim** { **vpn-instance** *vpn-instance-name* | **all-instance** } **control-message** **counters** **interface** { *interface-type* *interface-number* | *interface-name* } [ **message-type** { **assert** | **hello** | **join-prune** | **bsr** | **announcement** | **discovery** } ]

**display pim control-message counters interface** { *interface-type* *interface-number* | *interface-name* } **message-type** { **graft** | **graft-ack** | **state-refresh** }

**display pim all-instance control-message counters interface** { *interface-type* *interface-number* | *interface-name* } **message-type** { **graft** | **graft-ack** | **state-refresh** }

**display pim control-message counters message-type** { **graft** | **graft-ack** | **state-refresh** } [ **interface** { *interface-type* *interface-number* | *interface-name* } ]

**display pim** { **vpn-instance** *vpn-instance-name* | **all-instance** } **control-message** **counters** [ **message-type** { **crp** | **probe** | **register** | **register-stop** } ]

**display pim all-instance control-message counters message-type** { **graft** | **graft-ack** | **state-refresh** } [ **interface** { *interface-type* *interface-number* | *interface-name* } ]

**display pim control-message counters** [ **message-type** { **crp** | **probe** | **register** | **register-stop** } ]

**display pim** { **vpn-instance** *vpn-instance-name* | **all-instance** } **control-message** **counters** **message-type** { **assert** | **hello** | **join-prune** | **bsr** | **announcement** | **discovery** } [ **interface** { *interface-type* *interface-number* | *interface-name* } ]

**display pim control-message counters interface** { *interface-type* *interface-number* | *interface-name* } [ **message-type** { **assert** | **hello** | **join-prune** | **bsr** | **offer** | **backoff** | **win** | **pass** | **announcement** | **discovery** } ]

**display pim control-message counters message-type** { **assert** | **hello** | **join-prune** | **bsr** | **offer** | **backoff** | **win** | **pass** | **announcement** | **discovery** } [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Displays statistics about PIM control messages in a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of case-sensitive characters. |
| **all-instance** | Displays statistics about PIM control messages in all instances. | - |
| **interface** *interface-type* *interface-number* | Displays statistics about PIM control messages on a specified interface.  interface-type interface-number specifies the type and number of an interface. | - |
| **message-type** | Displays statistics about a specified type of PIM control messages. | - |
| **assert** | Displays statistics about Assert messages. | - |
| **hello** | Displays statistics about Hello messages. | - |
| **join-prune** | Displays statistics about Join/Prune messages. | - |
| **bsr** | Displays statistics about bootstrap router (BSR) messages. | - |
| **offer** | Displays statistics about Offer messages. | - |
| **backoff** | Displays the number of Backoff messages. | - |
| **win** | Displays statistics about Win messages. | - |
| **pass** | Displays the number of Pass messages. | - |
| **announcement** | Display statistics about Auto-RP advertisement messages. | - |
| **discovery** | Display statistics about Auto-RP discovery messages. | - |
| **graft** | Displays statistics about Graft messages. | - |
| **graft-ack** | Displays statistics about Graft-ack messages. | - |
| **state-refresh** | Displays statistics about State-Refresh messages. | - |
| **crp** | Displays statistics about candidate-rendezvous point (C-RP) messages. | - |
| **probe** | Displays statistics about Probe messages. | - |
| **register** | Displays the number of Register messages. | - |
| **register-stop** | Displays statistics about Register-Stop messages. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To display the number of received, sent, invalid, or filtered out PIM control messages, run the **display pim control-message counters** command.This command is usually used to locate faults in PIM, for example:

* If a PIM neighbor relationship cannot be set up, run this command on two ends to check whether they can normally send or receive Hello messages.
* If (\*, G) or (S, G) entries cannot be generated, run this command on an upstream or downstream device to check whether the device can normally send or receive Join/Prune messages.On live networks, check the number of PIM messages of a specific type based on fault symptoms.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the number of sent, received, invalid, filtered PIM control messages on GE 1/0/1 in the public network instance.
```
<HUAWEI> display pim control-message counters
VPN-Instance: public net
 Register* - Register Anycast-RP, Probe* - Probe Anycast-RP Announcement - Auto-RP Announcement, Discovery - Auto-RP Discovery
 ----------------------------------------------------------------------------
 PIM global control-message counters:
 MessageType      Received         Sent             Invalid          Filtered
 Register         0                0                0                0
 Register-Stop    0                0                0                0
 Probe            0                0                0                0
 C-RP             0                0                0                0
 Register*        0                0                0                0
 Probe*           0                0                0                0


 PIM control-message counters for interface: 100GE1/0/1
 MessageType      Received         Sent             Invalid          Filtered
 Assert           0                0                0                0
 Graft            0                1                0                0
 Graft-Ack        1                0                0                0 
 Hello            6295             3153             3147             0
 Join-Prune       3686             0                0                0
 State-Refresh    79               0                0                0
 BSR              0                0                0                0
 Announcement     0                0                0                0
 Discovery        0                0                0                0

```

**Table 1** Description of the **display pim control-message counters** command output
| Item | Description |
| --- | --- |
| Register\* | Statistics about Register messages in the Anycast-RP scenario. |
| Register | Statistics about Register messages. |
| Probe\* | Statistics about Probe messages in the Anycast-RP scenario. |
| Probe | Statistics about Null-Register messages. |
| Announcement | Auto-RP announcement messages. |
| Discovery | Auto-RP discovery messages. |
| PIM global control-message counters | Global statistics about PIM control messages. |
| PIM control-message counters for interface | Interface on which statistics about PIM control messages are collected. |
| MessageType | Type of a PIM control message. If Join-prune is displayed in the message type field and the value of the received field does not increase, check the sent field:   * If the value of the Sent field increases, the downstream device has sent out Join/Prune messages, and a communication failure has occurred between the PIM neighbors. * If the value of the Sent field does not increase, the downstream device is faulty. Locate and troubleshoot faults on the downstream device. |
| Received | Number of control messages received by an interface. |
| Sent | Number of control messages sent by the current interface. |
| Invalid | Number of invalid control packets. |
| Filtered | Number of control messages filtered out by an interface. |
| Register-Stop | Statistics about Register-Stop messages. |
| C-RP | Statistics about Advertisement messages of a C-RP. |
| Assert | Statistics about Assert messages. |
| Graft | Graft messages. |
| Graft-Ack | Graft-Ack messages. |
| Hello | Statistics about Hello messages. |
| Join-Prune | Statistics about Join/Prune messages. |
| State-Refresh | Statistics about State-Refresh messages. |
| BSR | Statistics about Bootstrap messages. |
| VPN-Instance | Instance in which statistics about PIM control messages are displayed. |