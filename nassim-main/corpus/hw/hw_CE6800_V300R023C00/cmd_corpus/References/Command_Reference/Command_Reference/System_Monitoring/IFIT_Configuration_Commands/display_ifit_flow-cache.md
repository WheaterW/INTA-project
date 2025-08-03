display ifit flow-cache
=======================

display ifit flow-cache

Function
--------



The **display ifit flow-cache** command displays IFIT flow table information.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ifit flow-cache** [ { **tcp** | **udp** } | **sip** *ipv4-sip-address* | **dip** *ipv4-dip-address* | **srcport** *srcport-number* | **dstport** *dstport-number* | **status** { **active** | **aged** } | **flow-id** *flow-id-number* ] \* **slot** *slot-id*

**display ifit flow-cache** [ { **tcp** | **udp** } | **sip** *ipv6-sip-address* | **dip** *ipv6-dip-address* | **srcport** *srcport-number* | **dstport** *dstport-number* | **status** { **active** | **aged** } | **flow-id** *flow-id-number* ] \* **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **tcp** | Indicates TCP packets. | - |
| **udp** | Indicates UDP packets. | - |
| **sip** *ipv4-sip-address* | Indicates source IPv4 address. | The value is in dotted decimal notation. |
| **sip** *ipv6-sip-address* | Indicates source IPv6 address. | The value is a 32-digit hexadecimal number in the format X:X:X:X:X:X:X:X. |
| **dip** *ipv4-dip-address* | Indicates destination IPv4 address. | The value is in dotted decimal notation. |
| **dip** *ipv6-dip-address* | Indicates destination IPv6 address. | The value is a 32-digit hexadecimal number in the format X:X:X:X:X:X:X:X. |
| **srcport** *srcport-number* | Specifies the source port. | The value is an integer in the range of 0 to 65535. |
| **dstport** *dstport-number* | Specifies the destination port number. | The value is an integer in the range of 0 to 65535. |
| **status** | Specifies the flow table status. | - |
| **active** | Sets the flow table status to active. | - |
| **aged** | Indicates that the flow table is aged. | - |
| **flow-id** *flow-id-number* | Specifies a flow ID. | The value is an integer that ranges from 0 to 1099511627775. |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After IFIT is enabled on a device and a flow table is created, you can run this command to view the cached IFIT flow table on a specified board.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the contents of the IFIT flow table on the board in slot 1.
```
<HUAWEI> display ifit flow-cache slot 1
FlowID             : 1056910
StreamStatus       : Active
PacketType         : IPv4
SrcAddress         : 1.1.1.1
DstAddress         : 2.2.2.2
Protocol           : TCP
AggretionType      : SourcePort
L4SrcPort          : -
L4DstPort          : 123
Direction          : Inbound
InterfaceName      : 10GE1/0/1
FlowStartTime      : 2023-08-23 09:56:48
FlowUpdateTime     : 2023-08-23 10:02:54
TTL                : 254
TunnelType         : Native
VNI                : 0
OuterTTL           : 253
VLAN               : 100
DQP                : -
-----------------------------------------------------------------------------------------------------------------------
Loss    PeriodID   PacketCounter   ByteCounter   TimeStamp(s)  TimeStamp(ns)  MeanDelay(ns)  MaxDelay(ns)  WarningInfo
-----------------------------------------------------------------------------------------------------------------------
   0    28213076           14109       1551880     1692895125      591623218           1024          1024  0x100000004
   1    28213077           14109       1551880     1692895145      591623218           1024          1024  0x100000004
-----------------------------------------------------------------------------------------------------------------------
FlowID             : 1056910
StreamStatus       : Aged
PacketType         : IPv4
SrcAddress         : 1.1.1.1
DstAddress         : 2.2.2.2
Protocol           : TCP
AggretionType      : SourcePort
L4SrcPort          : -
L4DstPort          : 123
Direction          : Inbound
InterfaceName      : 10GE1/0/1
FlowStartTime      : 2023-08-23 09:56:48
FlowUpdateTime     : 2023-08-23 10:02:54
TTL                : 254
TunnelType         : Native
VNI                : 0
OuterTTL           : 253
VLAN               : 100
DQP                : -
-----------------------------------------------------------------------------------------------------------------------
Loss    PeriodID   PacketCounter   ByteCounter   TimeStamp(s)  TimeStamp(ns)  MeanDelay(ns)  MaxDelay(ns)  WarningInfo
-----------------------------------------------------------------------------------------------------------------------
   0    28213076           14109       1551880     1692895125      591623218           1024          1024  0x100000004
   1    28213077           14109       1551880     1692895145      591623218           1024          1024  0x100000004
-----------------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display ifit flow-cache** command output
| Item | Description |
| --- | --- |
| FlowID | Flow ID, which uniquely identifies a flow. |
| StreamStatus | Flow status, which can be Active or Aged. |
| PacketType | Packet type, which can be IPv4 or IPv6. |
| SrcAddress | Source IP address. |
| DstAddress | Destination address. |
| Protocol | Protocol type, which can be TCP or UDP. |
| AggretionType | Aggregation type, which can be None, SourcePort, or DestinationPort. |
| L4SrcPort | TCP or UDP source port number. |
| L4DstPort | TCP or UDP destination port number. |
| Direction | Flow creation direction, which can be inbound or outbound. |
| InterfaceName | Interface name. The value is an inbound interface in the inbound direction and an outbound interface in the outbound direction. Only physical main interfaces are supported. |
| FlowStartTime | Flow creation time. |
| FlowUpdateTime | Time when flow statistics are last updated. |
| TTL | TTL. |
| TunnelType | Tunnel type, which can be Native, VXLAN, or GENEVE. |
| VNI | VNI. |
| OuterTTL | Outer TTL. |
| VLAN | VLAN. |
| DQP | Target queue pair. |
| Loss | Color flag for packet loss measurement. |
| PeriodID | Cycle ID. |
| PacketCounter | Packet statistics. |
| ByteCounter | Byte statistics. |
| TimeStamp(s) | Second-level timestamp. |
| TimeStamp(ns) | Nanosecond-level timestamp. |
| MeanDelay(ns) | Average delay. |
| MaxDelay(ns) | Maximum delay. |
| WarningInfo | Alarm information. |