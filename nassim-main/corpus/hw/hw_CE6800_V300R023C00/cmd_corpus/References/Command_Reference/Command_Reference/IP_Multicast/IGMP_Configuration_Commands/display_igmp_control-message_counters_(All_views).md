display igmp control-message counters (All views)
=================================================

display igmp control-message counters (All views)

Function
--------



The **display igmp control-message counters** command displays statistics about IGMP control messages on a specific or all interfaces.




Format
------

**display igmp control-message counters** [ **interface** { *port-type* *port-num* | *interface-name* } ] **message-type** { **query** | **report** }

**display igmp control-message counters** [ **interface** { *port-type* *port-num* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *port-type* *port-num* | Displays statistics about IGMP control messages on a specified interface. | - |
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

* If interface is specified, the command displays statistics about IGMP control messages on the specified interface.
* If message-type and interface are specified, the command displays statistics about the specified type of IGMP control messages on the specified interface.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about IGMP control messages on 100GE1/0/1 in the public network instance.
```
<HUAWEI> display igmp control-message counters interface 100GE 1/0/1
Interface control-message counters information of VPN Instance: public net
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
 Others                      -           -           0           0  ------------------------------------------------------------------

```

**Table 1** Description of the **display igmp control-message counters (All views)** command output
| Item | Description |
| --- | --- |
| Interface control-message counters information of VPN Instance | Instance in which statistics about IGMP control messages are displayed. |
| Message Type | Type of IGMP control messages. |
| Sent | Number of sent IGMP control messages. |
| Valid | Number of received valid IGMP control messages. |
| Invalid | Number of received wrong IGMP control messages. |
| Ignore | Number of received but ignored IGMP control messages. |
| General Query | Statistics about IGMP General Query messages. |
| Group Query | Statistics about IGMP Group-Specific Query messages. |
| Source Group Query | Statistics about IGMP Group-and-Source-Specific Query messages. |
| Source Records Total | Statistics about multicast sources carried in IGMPv3 messages. |
| Report ASM | Statistics about IGMPv1 and IGMPv2 Report messages with multicast group addresses not in the source-specific multicast (SSM) group address range. |
| Report SSM | Statistics about IGMPv1 and IGMPv2 Report messages with multicast group addresses in the SSM group address range. |
| LEAVE ASM | Statistics about IGMP Leave messages with multicast group addresses not in the SSM group address range. |
| LEAVE SSM | Statistics about IGMP Leave messages with multicast group addresses in the SSM group address range. |
| ISIN Report | Statistics about IGMPv3 ISIN Report messages. |
| ISEX Report | Statistics about IGMPv3 ISEX Report messages. |
| TOIN Report | Statistics about IGMPv3 TOIN Report messages. |
| TOEX Report | Statistics about IGMPv3 TOEX Report messages. |
| ALLOW Report | Statistics about IGMPv3 ALLOW Report messages. |
| BLOCK Report | Statistics about IGMPv3 BLOCK Report messages. |
| Others | Statistics about invalid and ignored IGMP control messages whose types cannot be identified. |
| 100GE1/0/1(192.168.2.1) | Type, number, and IP address of an interface. |