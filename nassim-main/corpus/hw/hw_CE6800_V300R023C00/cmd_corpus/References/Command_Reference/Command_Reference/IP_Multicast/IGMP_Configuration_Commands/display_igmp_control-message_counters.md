display igmp control-message counters
=====================================

display igmp control-message counters

Function
--------



The **display igmp control-message counters** command displays statistics about IGMP control messages on a specific or all interfaces.




Format
------

**display igmp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **control-message** **counters** [ **interface** { *port-type* *port-num* | *interface-name* } ] **message-type** { **query** | **report** }

**display igmp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **control-message** **counters** [ **interface** { *port-type* *port-num* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Displays statistics about IGMP control messages on interfaces in all instances. | - |
| **interface** *port-type* | Displays statistics about IGMP control messages on a specified interface type. | - |
| *port-num* | Displays statistics about IGMP control messages on a specified interface number. | - |
| **message-type** | Indicates an IGMP control message type. | - |
| **query** | Displays statistics about Query messages. | - |
| **report** | Displays statistics about Report messages. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Before using the **display igmp control-message counters** command, note the following:

* If neither vpn-instance nor all-instance is specified, the command displays statistics about IGMP control messages on interfaces in the public network instance.
* If interface is specified, the command displays statistics about IGMP control messages on the specified interface.
* If message-type and interface are specified, the command displays statistics about the specified type of IGMP control messages on the specified interface.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about IGMP control messages on 100GE1/0/1 in the public network instance.
```
<HUAWEI> display igmp control-message counters interface 100GE 1/0/1
Interface control-message counters information of VPN instance: public net
 100GE1/0/1(192.168.2.1):
 Message Type                Sent        Valid       Invalid     Ignore
 ------------------------------------------------------------------
 General Query               1           0           0           0
 Group Query                 0           0           0           0
 Source Group Query          0           0           0           0
 ------------------------------------------------------------------
IGMPV1V2
 Report ASM                  0           0           0           0
 Report SSM                  0           0           0           0
 ------------------------------------------------------------------
 LEAVE ASM                   0           0           0           0
 LEAVE SSM                   0           0           0           0
 ------------------------------------------------------------------
 IGMPV3
 ISIN Report                 0           0           0           0
 ISEX Report                 0           0           0           0
 TOIN Report                 0           0           0           0
 TOEX Report                 0           0           0           0
 ALLOW Report                0           0           0           0
 BLOCK Report                0           0           0           0
 Source Records Total        0           0           0           0
 ------------------------------------------------------------------
 Others                      -           -           0           0  
------------------------------------------------------------------

```

**Table 1** Description of the **display igmp control-message counters** command output
| Item | Description |
| --- | --- |
| Interface control-message counters information of VPN instance | Instance in which statistics about IGMP control messages are displayed. |
| General Query | Number of general query messages. |
| Group Query | Number of group query messages. |
| Source Group Query | Number of source/group query messages. |
| Source Records Total | Number of source-Records-total messages. |
| Report ASM | Number of igmp-v1v2 asm-report messages. |
| Report SSM | Number of IGMP SSM-v1v2-report messages. |
| LEAVE ASM | Number of igmp-v1v2 asm-leave messages. |
| LEAVE SSM | Number of igmp-v1v2 ssm-leave messages. |
| ISIN Report | Number of igmp-v3 isin-report messages. |
| ISEX Report | Number of igmp-v3 isex-report messages. |
| TOIN Report | Number of igmp-v3 toin-report messages. |
| TOEX Report | Number of igmp-v3 toex-report messages. |
| ALLOW Report | Number of igmp-v3 allow-report messages. |
| BLOCK Report | Number of igmp-v3 block-report messages. |
| Others | Number of messages of unknown types. |
| 100GE1/0/1(192.168.2.1) | Type, number, and IP address of an interface. |