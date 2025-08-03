display load-balance forwarding-path unicast interface ecmp
===========================================================

display load-balance forwarding-path unicast interface ecmp

Function
--------



The **display load-balance forwarding-path unicast interface ecmp** command displays the ECMP outbound interface obtained through simulated calculation after the specified 5-tuple information, source MAC address, and destination MAC addresses are input.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display load-balance forwarding-path unicast interface ecmp src-interface** { *iftype* *ifnum* | *src-interface-name* } { **vlan** *vlanid* | **vpn-instance** *vpn-instance-name* | **src-ip** *src-ip-data* | **dst-ip** *dst-ip-data* | [ [ **inner-src-ip** *inner-src-ip* | **inner-dst-ip** *inner-dst-ip* ] \* | [ **inner-src-ipv6** *inner-src-ipv6* | **inner-dst-ipv6** *inner-dst-ipv6* ] \* ] | **protocol** { *protocol-number* [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* | **inner-l4-src-port** *inner-src-port-data* | **inner-l4-dst-port** *inner-dst-port-data* ] \* | **icmp** | **igmp** | **ip** | **ospf** | **tcp** [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* | **udp** [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* } } \* **slot** *slot-id*

**display load-balance forwarding-path unicast interface ecmp src-interface** { *iftype* *ifnum* | *src-interface-name* } { **vlan** *vlanid* | **vpn-instance** *vpn-instance-name* | **src-ipv6** *src-ipv6-data* | **dst-ipv6** *dst-ipv6-data* | [ [ **inner-src-ip** *inner-src-ip* | **inner-dst-ip** *inner-dst-ip* ] \* | [ **inner-src-ipv6** *inner-src-ipv6* | **inner-dst-ipv6** *inner-dst-ipv6* ] \* ] | **flow-label** *flow-label* | **protocol** { *protocol-number* [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* | **inner-l4-src-port** *inner-src-port-data* | **inner-l4-dst-port** *inner-dst-port-data* ] \* | **icmp** | **igmp** | **ip** | **ospf** | **tcp** [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* | **udp** [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* } } \* **slot** *slot-id*

For CE6885-LL (low latency mode):

**display load-balance forwarding-path unicast interface ecmp src-interface** { *iftype* *ifnum* | *src-interface-name* } { **vlan** *vlanid* | **vpn-instance** *vpn-instance-name* | **src-ip** *src-ip-data* | **dst-ip** *dst-ip-data* | **protocol** { *protocol-number* [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* | **icmp** | **igmp** | **ip** | **ospf** | **tcp** [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* | **udp** [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* } } \* **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *iftype* | Specifies the physical source interface of packets. | The value is a string of 1 to 256 case-sensitive characters, spaces not supported. |
| *ifnum* | Specifies the physical source interface of packets. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **vlan** *vlanid* | Specifies a VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **src-ip** *src-ip-data* | Specifies a source IP address. | The value is in dotted decimal notation. |
| **dst-ip** *dst-ip-data* | Specifies a destination IP address. | The value is in dotted decimal notation. |
| **inner-src-ip** *inner-src-ip* | Inner Source IP.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is in dotted decimal notation. |
| **inner-dst-ip** *inner-dst-ip* | Inner Destination IP Address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is in dotted decimal notation. |
| **inner-src-ipv6** *inner-src-ipv6* | Inner Source IPv6 Address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number in the format X:X:X:X:X:X:X:X. |
| **inner-dst-ipv6** *inner-dst-ipv6* | Inner Destination IPv6 Address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number in the format X:X:X:X:X:X:X:X. |
| **protocol** *protocol-number* | Specifies a protocol number or type.  protocol-number specifies a protocol number. | The value is an integer ranging from 0 to 255.  The protocol type can be:   * ICMP * IGMP * IP * OSPF * TCP * UDP |
| **l4-src-port** *src-port-data* | Specifies a source port number. | The value is an integer in the range of 0 to 65535. |
| **l4-dst-port** *dst-port-data* | Specifies a destination port number. | The value is an integer in the range of 0 to 65535. |
| **inner-l4-src-port** *inner-src-port-data* | Inner Source L4 Port Number.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer in the range of 0 to 65535. |
| **inner-l4-dst-port** *inner-dst-port-data* | Inner Destination L4 Port Number.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer in the range of 0 to 65535. |
| **icmp** | Indicates the ICMP protocol. | - |
| **igmp** | Indicates the IGMP protocol. | - |
| **ip** | Indicates the IP protocol. | - |
| **ospf** | Indicates the OSPF protocol. | - |
| **tcp** | Indicates the TCP protocol. | - |
| **udp** | Indicates the UDP protocol. | - |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |
| **src-interface** *src-interface-name* | Specifies a source interface name. | The value is a string of 1 to 256 case-sensitive characters, spaces not supported. |
| **src-ipv6** *src-ipv6-data* | Source IPv6 address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number in the format X:X:X:X:X:X:X:X. |
| **dst-ipv6** *dst-ipv6-data* | Destination IPv6 address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number in the format X:X:X:X:X:X:X:X. |
| **flow-label** *flow-label* | Specifies the flow label.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 0 to 1048575. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. "\_public\_" is reserved and cannot be used as a VPN instance name. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The 5-tuple information of packets includes the source IP address, destination IP address, source port number, destination port number, and protocol type. Traffic transmitted on devices often carries different 5-tuple information, source MAC addresses, and destination MAC addresses. You can run the display load-balance forwarding-path unicast interface ecmp command to check the ECMP outbound interface obtained through software-simulated calculation after the specified 5-tuple information is input.

**Configuration Impact**

When running this command to check the ECMP outbound interface, pay attention to the following points:

* An IPv4 address and IPv6 address cannot both be specified.
* This command can display only the outbound interface of known IPv4 and IPv6 packets based on the specified 5-tuple information.
* This command can display the outbound interface of known Layer 3 unicast packets. You are advised to check the outbound interface based on the load balancing mode configured in the current load balancing profile.
* The ECMP outbound interface of packets cannot be obtained through simulated calculation based on the next hop of the tunnel type.
* When adaptive-routing enable is configured, the ECMP outbound interface of packets cannot be obtained through simulated calculation.
* When load-balance ecmp rail-group enable is configured, the ECMP outbound interface of packets cannot be obtained through simulated calculation.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the ECMP outbound interface obtained through simulated calculation after the specified 5-tuple information is input.
```
<HUAWEI> display load-balance forwarding-path unicast interface ecmp src-interface 10GE1/0/1 src-ip 10.1.1.1 dst-ip 172.16.1.1 protocol udp l4-dst-port 10 l4-src-port 20 vlan 1 slot 1

Packet HashField for calculate:
-------------------------------------------------------------------------------- 
  SrcInterface :10ge1/0/1        
        VlanId :1                
       SrcAddr :10.1.1.1          
       DstAddr :172.16.1.1         
  ProtocolType :17               
     L4SrcPort :20               
     L4DstPort :10               
--------------------------------------------------------------------------------
Out Interface: 10GE1/0/2   
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display load-balance forwarding-path unicast interface ecmp** command output
| Item | Description |
| --- | --- |
| Packet HashField for calculate | Indicates the hash factor used for calculation. |
| SrcInterface | Physical source interface. |
| VlanId | VLAN ID. |
| SrcAddr | Source IP address. |
| DstAddr | Destination IP address. |
| ProtocolType | Protocol type. |
| L4SrcPort | Transport-layer source interface. |
| L4DstPort | Transport-layer destination interface. |
| Out Interface | ECMP outbound interface of packets with the specified 5-tuple information. |