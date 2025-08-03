display drop-event flow-cache
=============================

display drop-event flow-cache

Function
--------



The **display drop-event flow-cache** command displays information about the packet loss visualization flow table.




Format
------

For CE6820H, CE6820H-K, CE6820S, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K:

**display drop-event flow-cache** [ **ipv4** | **ipv6** | **vxlan** | **ethernet** ] **slot** *slot-id*

For CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-LL (low latency mode), CE6885-SAN, CE8855, CE8851-32CQ4BQ:

**display drop-event flow-cache** [ **ipv4** | **ipv6** | **vxlan** ] **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv4** | Specifies IPv4 packets. | - |
| **ipv6** | Specifies IPv6 packets. | - |
| **vxlan** | Specifies VXLAN packets. | - |
| **ethernet** | Specifies Ethernet packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the display drop-event flow-cache command to view detailed information about the packet loss visualization flow table.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the packet loss visualization flow table.
```
<HUAWEI> display drop-event flow-cache slot 1
Total:1
------------------------------------------------------------
Number                  :1                                  
 Drop Reason            :DISCARD_CAUSE_XXX                  
 Drop packet Count      :25                                 
 Drop Byte Count        :1500                               
 Source MAC             :0000-c055-0102                     
 Destination MAC        :ffff-ffff-ffff                     
 PE-VLAN                :0                                  
 CE-VLAN                :0                                  
 Source IPv4            :-                                  
 Destination IPv4       :-                                  
 Source IPv6            :-                                  
 Destination IPv6       :-                                  
 ProtocolId             :0                                  
 L4 Source Port         :0                                  
 L4 Destination Port    :0                                  
 Outer TTL              :64                                 
 Inner TTL              :64                                 
 Tos                    :0                                  
 VNI ID                 :0                                  
 Queue                  :255                                
 Start Timestamp        :2022-10-10 19:49:12                
 Last Timestamp         :2022-10-10 19:49:13                             
 In Interface           :25GE1/0/1                         
 Out Interface          :-                                  
 causeID                :99                                 
 outerSrcIPv4           :-                                  
 outerDstIPv4           :-                                  
 outerSrcIPv6           :-                                  
 outerDstIPv6           :-
 RoCEv2 Qpair           :-
 NVME Namespace ID      :-
 SubCauseId             :0
 
<HUAWEI> display drop-event flow-cache ipv4 slot 1
------------------------------------------------------------
Number                  :1                                  
 Drop Reason            :DISCARD_CAUSE_XXX                  
 Drop packet Count      :25                                 
 Drop Byte Count        :1500                               
 Source MAC             :0000-c055-0102                     
 Destination MAC        :ffff-ffff-ffff                     
 PE-VLAN                :0                                  
 CE-VLAN                :0                                  
 Source IPv4            :10.1.1.1                           
 Destination IPv4       :10.1.1.2                           
 Source IPv6            :-                                  
 Destination IPv6       :-                                  
 ProtocolId             :0                                  
 L4 Source Port         :0                                  
 L4 Destination Port    :0                                  
 Outer TTL              :64                                 
 Inner TTL              :64                                 
 Tos                    :0                                  
 VNI ID                 :0                                  
 Queue                  :255                                
 Start Timestamp        :2022-10-10 19:49:12                
 Last Timestamp         :2022-10-10 19:49:13                
 In Interface           :25GE1/0/1                         
 Out Interface          :-                                  
 causeID                :99                                 
 outerSrcIPv4           :-                                  
 outerDstIPv4           :-                                  
 outerSrcIPv6           :-                                  
 outerDstIPv6           :-
 RoCEv2 Qpair           :-
 NVME Namespace ID      :-
 SubCauseID             :0

```

**Table 1** Description of the **display drop-event flow-cache** command output
| Item | Description |
| --- | --- |
| Drop Reason | Packet drop reason. |
| Drop packet Count | Number of dropped packets. |
| Drop Byte Count | Number of discarded bytes.  A hyphen (-) indicates that this parameter is not supported. |
| Source MAC | Source MAC address.  A hyphen (-) indicates that this parameter is not supported. |
| Source IPv4 | Source IPv4 address. |
| Source IPv6 | Source IPv6 address. |
| Destination MAC | Destination MAC address.  A hyphen (-) indicates that this parameter is not supported. |
| Destination IPv4 | Destination IPv4 address. |
| Destination IPv6 | Destination IPv6 address. |
| PE-VLAN | Outer VLAN.  A hyphen (-) indicates that this parameter is not supported. |
| CE-VLAN | Inner VLAN.  A hyphen (-) indicates that this parameter is not supported. |
| ProtocolId | Protocol of packets. |
| L4 Source Port | Layer 4 source port number. |
| L4 Destination Port | Layer 4 destination port number. |
| Outer TTL | Outer TTL. |
| Inner TTL | Inner TTL. |
| Tos | ToS. |
| VNI ID | VNI ID. |
| Queue | Queue. |
| Start Timestamp | Timestamp when the flow table is created. |
| Last Timestamp | Timestamp when the flow table is last updated. |
| In Interface | Inbound interface. |
| Out Interface | Outbound interface. |
| causeID | Drop cause ID. |
| outerSrcIPv4 | Outer source IPv4 address of a VXLAN packet.  A hyphen (-) indicates that this parameter is not supported. |
| outerDstIPv4 | Outer destination IPv4 address of a VXLAN packet.  A hyphen (-) indicates that this parameter is not supported. |
| outerSrcIPv6 | Outer source IPv6 address of a VXLAN packet.  A hyphen (-) indicates that this parameter is not supported. |
| outerDstIPv6 | Outer destination IPv6 address of a VXLAN packet.  A hyphen (-) indicates that this parameter is not supported. |
| RoCEv2 Qpair | Queue pair information in RoCEv2 packets. |
| NVME Namespace ID | Namespace ID information in an NVMe packet. |
| SubCauseID | Packet drop cause ID. |