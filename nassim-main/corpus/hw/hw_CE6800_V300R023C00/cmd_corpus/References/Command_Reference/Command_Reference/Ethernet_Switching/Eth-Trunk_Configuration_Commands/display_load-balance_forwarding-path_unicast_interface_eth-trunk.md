display load-balance forwarding-path unicast interface eth-trunk
================================================================

display load-balance forwarding-path unicast interface eth-trunk

Function
--------



The **display load-balance forwarding-path unicast interface eth-trunk** command displays the outbound interface that is calculated by the software based on the input 5-tuple information and source and destination MAC addresses.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display load-balance forwarding-path unicast interface eth-trunk** *trunk-id* **src-interface** *interface-type* *interface-name* { **ethtype** *eth-type-number* | **vlan** *vlan-id* | [ [ **src-ip** *src-ip-data* | **dst-ip** *dst-ip-data* ] \* | [ **src-ipv6** *src-ipv6-data* | **dst-ipv6** *dst-ipv6-data* ] \* ] | **src-mac** *src-mac-data* | **dst-mac** *dst-mac-data* | **protocol** { *protocol-number* | **icmp** | **igmp** | **ip** | **ospf** | **tcp** [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* | **udp** [ **l4-src-port** *src-port-data* | **l4-dst-port** *dst-port-data* ] \* } } \* **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *trunk-id* | Specifies the ID of an Eth-Trunk. | The value is an integer in the range from 0 to 1023. |
| **src-interface** *interface-type* *interface-name* | Specifies the source interface of packets. | The value must be set according to the device configuration. |
| **ethtype** *eth-type-number* | Specifies the Ethernet frame type. | The value ranges from 0 to ffff, in hexadecimal notation. The default value is 0800. |
| **vlan** *vlan-id* | Specifies the ID of a VLAN. | The value is an integer ranging from 1 to 4094. |
| **src-ip** *src-ip-data* | Specifies the source IPv4 address.  You can use either an IPv4 address or an IPv6 address. | The value is in dotted decimal notation. |
| **dst-ip** *dst-ip-data* | Specifies the destination IPv4 address.  You can use either an IPv4 address or an IPv6 address. | The value is in dotted decimal notation. |
| **src-ipv6** *src-ipv6-data* | Specifies the source IPv6 address.  You can use either an IPv4 address or an IPv6 address. | The address is a 32-digit hexadecimal number, in the format X:X:X:X:X:X:X:X. |
| **dst-ipv6** *dst-ipv6-data* | Specifies the destination IPv6 address.  You can use either an IPv4 address or an IPv6 address. | The address is a 32-digit hexadecimal number, in the format X:X:X:X:X:X:X:X. |
| **src-mac** *src-mac-data* | Specifies the source MAC address. | The value is in H-H-H format. An H is a hexadecimal number of 1 to 4 digits. |
| **dst-mac** *dst-mac-data* | Specifies the destination MAC address. | The value is in H-H-H format. An H is a hexadecimal number of 1 to 4 digits. |
| **protocol** *protocol-number* | Specifies the protocol number or type.  protocol-number specifies the protocol number. | The value is an integer that ranges from 0 to 255.  The protocol type is as follows:   * ICMP * IGMP * IP * OSPF * TCP * UDP |
| **l4-src-port** *src-port-data* | Specifies the source port number. | The value is an integer that ranges from 0 to 65535. |
| **l4-dst-port** *dst-port-data* | Specifies the destination port number. | The value is an integer that ranges from 0 to 65535. |
| **slot** *slot-id* | Specifies the slot ID in which the source interface of packets resides. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The 5-tuple information contains the source/destination IP addresses, source/destination port numbers in TCP or UDP packets, and protocol type. Traffic often carries different 5-tuple information and source and destination MAC addresses. You can run this command to check the outbound interface that is calculated by the software based on the 5-tuple information and source and destination MAC addresses. Then you can learn the forwarding path of specified traffic.

**Prerequisites**

An Eth-Trunk has been created.

**Precautions**

When using this command to check the outbound interface calculated through the hash algorithm on an Eth-Trunk, pay attention to the following points:

* You can use either an IPv4 address or an IPv6 address.
* The outbound interface can be queried on an Eth-Trunk Layer 3 sub-interface.
* If an Eth-Trunk member interface is bound to an independent VLAN, the outbound interface that is calculated using this command is incorrect.
* The outbound interface of known unicast packets can be queried only. The 5-tuple information, source MAC address, and destination MAC address cannot be specified to query the outbound interfaces of tunneling packets.
* The outbound interface of known Layer 2 unicast packets can be queried on an Eth-Trunk. It is recommended that src-mac, dst-mac, and vlan be specified.
* The outbound interface of known Layer 3 unicast packets can be queried on an Eth-Trunk. It is recommended that src-ip, dst-ip, src-ipv6, dst-ipv6, src-mac, and dst-mac be specified. If the source interface of packets is the VLANIF interface or Layer 3 sub-interface, it is recommended that the VLAN ID be specified to query the outbound interface.
* If TCP or UDP is specified to query the outbound interface that is calculated by the software, you are advised to specify the source and destination port numbers.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the outbound interface that is calculated by the software based on the input 5-tuple information and source and destination MAC addresses.
```
<HUAWEI> display load-balance forwarding-path unicast interface eth-trunk 2 src-interface 100GE1/0/1 dst-mac 00e0-fc12-3456 src-mac 00e0-fc12-3478 src-ip 172.16.1.1 dst-ip 172.16.1.2 vlan 100 slot 1

Packet HashField for calculate: 

--------------------------------------------------------------------------------
               dst-mac : 00e0-fc12-3456 
               src-mac : 00e0-fc12-3478 
               vlan    : 100 
               ethtype : 0x800 
               dst-ip  : 172.16.1.2 
               src-ip  : 172.16.1.1

--------------------------------------------------------------------------------
Out Interface: 100GE1/0/3 
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display load-balance forwarding-path unicast interface eth-trunk** command output
| Item | Description |
| --- | --- |
| dst-mac | Destination MAC address. |
| src-mac | Source MAC address. |
| src-ip | Source IP address. |
| dst-ip | Destination IP address. |
| vlan | VLAN ID. |
| Packet HashField for calculate | Factor used in hash calculation. |
| ethtype | Ethernet frame type. |
| Out Interface | Outbound interface of packets that contain the specified 5-tuple information. |