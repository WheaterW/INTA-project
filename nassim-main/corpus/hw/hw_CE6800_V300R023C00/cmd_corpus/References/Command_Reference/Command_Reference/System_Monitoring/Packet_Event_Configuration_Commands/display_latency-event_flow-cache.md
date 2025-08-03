display latency-event flow-cache
================================

display latency-event flow-cache

Function
--------



The **display latency-event flow-cache** command displays information in the latency visualization flow table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K:

**display latency-event flow-cache** [ **ipv4** | **ipv6** | **vxlan** | **ethernet** ] **slot** *slot-id*

For CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ:

**display latency-event flow-cache** [ **ipv4** | **ipv6** | **vxlan** ] **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv4** | Specifies IPv4 packets. | - |
| **ipv6** | IPv6 protocol. | - |
| **vxlan** | VXLAN protocol. | - |
| **ethernet** | Ethernet protocol.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM. | - |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can use the display latency-event flow-cache command to view detailed information in the latency visualization flow table.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information in the latency visualization flow table.
```
<HUAWEI> display latency-event flow-cache slot 1
Total:1
------------------------------------------------------------
Number                  :3                                  
 Latency packet Count   :1                                  
 Latency Byte Count     :124                                
 Latency Peak           :1376329803                         
 Latency Last           :1376329803                         
 Source MAC             :0000-c055-0107                     
 Destination MAC        :0000-0000-0077                     
 PE-VLAN                :0                                  
 CE-VLAN                :0                                  
 Source IPv4            :11.1.1.1                           
 Destination IPv4       :10.1.1.1                           
 Source IPv6            :-                                  
 Destination IPv6       :-                                  
 ProtocolId             :253                                
 L4 Source Port         :0                                  
 L4 Destination Port    :0                                  
 Outer TTL              :64                                 
 Inner TTL              :64                                 
 Tos                    :0                                  
 VNI ID                 :0                                  
 Queue                  :48                                 
 Start Timestamp        :2022-10-10 09:58:33                         
 Last Timestamp         :2022-10-10 09:58:33                
 In Interface           :25GE1/0/1                         
 Out Interface          :-                                  
 causeID                :8191                               
 outerSrcIPv4           :-                                  
 outerDstIPv4           :-                                  
 outerSrcIPv6           :-                                  
 outerDstIPv6           :-
 RoCEv2 Qpair           :-
 NVME Namespace ID      :-
 
<HUAWEI> display latency-event flow-cache ipv4 slot 1
------------------------------------------------------------
Number                  :3                                  
 Latency packet Count   :1                                  
 Latency Byte Count     :124                                
 Latency Peak           :1376329803                         
 Latency Last           :1376329803                         
 Source MAC             :0000-c055-0107                     
 Destination MAC        :0000-0000-0077                     
 PE-VLAN                :0                                  
 CE-VLAN                :0                                  
 Source IPv4            :11.1.1.1                           
 Destination IPv4       :10.1.1.1                           
 Source IPv6            :-                                  
 Destination IPv6       :-                                  
 ProtocolId             :253                                
 L4 Source Port         :0                                  
 L4 Destination Port    :0                                  
 Outer TTL              :64                                 
 Inner TTL              :64                                 
 Tos                    :0                                  
 VNI ID                 :0                                  
 Queue                  :48                                 
 Start Timestamp        :2022-10-10 09:58:33  
 Last Timestamp         :2022-10-10 09:58:33           
 In Interface           :25GE1/0/1                         
 Out Interface          :-                                  
 causeID                :8191                               
 outerSrcIPv4           :-                                  
 outerDstIPv4           :-                                  
 outerSrcIPv6           :-                                  
 outerDstIPv6           :-
 RoCEv2 Qpair           :-
 NVME Namespace ID      :-

```

**Table 1** Description of the **display latency-event flow-cache** command output
| Item | Description |
| --- | --- |
| Latency packet Count | Number of latency packets. |
| Latency Byte Count | Number of latency bytes.  A hyphen (-) indicates that this parameter is not supported. |
| Latency Peak | Peak latency. |
| Latency Last | Valley latency.  A hyphen (-) indicates that this parameter is not supported. |
| Last Timestamp | End timestamp. |
| Source MAC | Source MAC address.  A hyphen (-) indicates that this parameter is not supported. |
| Source IPv4 | Source IPv4 address. |
| Source IPv6 | Source IPv6 address. |
| Destination MAC | Destination MAC address.  A hyphen (-) indicates that this parameter is not supported. |
| Destination IPv4 | Destination IPv4 address. |
| Destination IPv6 | Destination IPv6 address. |
| PE-VLAN | PE VLAN.  A hyphen (-) indicates that this parameter is not supported. |
| CE-VLAN | CE VLAN.  A hyphen (-) indicates that this parameter is not supported. |
| ProtocolId | Protocol ID. |
| L4 Source Port | Layer 4 source port. |
| L4 Destination Port | Layer 4 destination port. |
| Outer TTL | Outer TTL. |
| Inner TTL | Inner TTL. |
| Tos | TOS. |
| VNI ID | VNI ID. |
| Queue | Queue. |
| Start Timestamp | Start timestamp. |
| In Interface | Inbound interface. |
| Out Interface | Outbound interface. |
| causeID | Cause ID.  The cause ID of the latency is fixed to 8191. |
| outerSrcIPv4 | Outer source IPv4 address of a VXLAN packet.  A hyphen (-) indicates that this parameter is not supported. |
| outerDstIPv4 | Outer destination IPv4 address of a VXLAN packet.  A hyphen (-) indicates that this parameter is not supported. |
| outerSrcIPv6 | Outer source IPv6 address of a VXLAN packet.  A hyphen (-) indicates that this parameter is not supported. |
| outerDstIPv6 | Outer destination IPv6 address of a VXLAN packet.  A hyphen (-) indicates that this parameter is not supported. |
| RoCEv2 Qpair | Queue pair information in RoCEv2 packets. |
| NVME Namespace ID | Namespace ID information in an NVMe packet. |