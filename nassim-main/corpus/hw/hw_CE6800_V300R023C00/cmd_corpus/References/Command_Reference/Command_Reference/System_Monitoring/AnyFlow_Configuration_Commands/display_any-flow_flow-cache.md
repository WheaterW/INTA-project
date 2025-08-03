display any-flow flow-cache
===========================

display any-flow flow-cache

Function
--------



The **display any-flow flow-cache** command displays flow table statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display any-flow flow-cache** { **ipv4** | **ipv6** } **slot** *slot-id*

**display any-flow flow-cache sip** *ipv4-sip-address* **dip** *ipv4-dip-address* [ **srcport** *srcport-number* | **dstport** *dstport-number* | **protocol** *protocol-number* | **vpn-instance** *vpn-instance-name* | **vlan** *vlan-id* | **vni** *vni-id* | **rocev2** [ **dest-qp** *dest-qp-value* ] ] \* **slot** *slot-id*

**display any-flow flow-cache ipv6 sip** *ipv6-sip-address* **ipv6** **dip** *ipv6-dip-address* [ **srcport** *srcport-number* | **dstport** *dstport-number* | **protocol** *protocol-number* | **vpn-instance** *vpn-instance-name* | **vlan** *vlan-id* | **vni** *vni-id* | **rocev2** [ **dest-qp** *dest-qp-value* ] ] \* **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv4** | Displays the IPv4 flow table. | - |
| **ipv6** | Displays the IPv6 flow table. | - |
| **slot** *slot-id* | Specifies the slot ID of a board. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **sip** *ipv4-sip-address* | Specifies a source IPv4 address. | The value is in dotted decimal notation. |
| **sip** *ipv6-sip-address* | Specifies the source IPv6 address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **dip** *ipv4-dip-address* | Specifies a destination IPv4 address. | The value is in dotted decimal notation. |
| **dip** *ipv6-dip-address* | Sets a destination IPv6 address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **srcport** *srcport-number* | Specifies a source port number. | The value is an integer that ranges from 0 to 65535. |
| **dstport** *dstport-number* | Specifies a destination port number. | The value is an integer that ranges from 0 to 65535. |
| **protocol** *protocol-number* | Specifies the protocol type. | The value is an integer ranging from 1 to 255. |
| **vpn-instance** *vpn-instance-name* | Displays information about a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. \_public\_ cannot be used as the VPN instance name. If the string is enclosed in double quotation marks ("), spaces are allowed in the string.  Description:  \_public\_ indicates a public VPN instance. |
| **vlan** *vlan-id* | Specifies the VLAN ID. | The value is an integer ranging from 1 to 4094. |
| **vni** *vni-id* | Specifies an VNI. | The value is an integer that ranges from 1 to 16777215. |
| **rocev2** | Displays RoCEv2 flow table information. | - |
| **dest-qp** *dest-qp-value* | Specifies the value of RoCEv2 queue pair. | The value is an integer ranging from 0 to 16777215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After the Any-Flow function is enabled and a flow table is created, you can run this command to view entry content, statistics, packet forwarding information, and latency for flows on a specified card in real time.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display entries for flows whose source IPv6 address is 2001:db8:1::1, the destination IPv6 address is 2001:db8:2::1, and the VPN instance is vpn1 on the card in slot 1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:4
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:4
[*HUAWEI-vpn-instance-vpn1-af-ipv6] commit
[~HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[~HUAWEI-vpn-instance-vpn1] quit
[~HUAWEI] quit
<HUAWEI> display any-flow flow-cache ipv6 sip 2001:db8:1::1 ipv6 dip 2001:db8:2::1 vpn-instance vpn1 slot 1
------------------------------------------------------------
Start Timestamp         : 2020-06-17 15:07:27
Last Timestamp          : 2020-06-17 17:01:12
First Non-SYN TimeStamp : 2016131313180
SIP                     : 2001:db8:1::1                
DIP                     : 2001:db8:2::1
SrcPort                 : 20   
DstPort                 : 30
Protocol                : 17
VNI                     : --
VLAN                    : --
VPN Instance            : vpn1
Tunnel Flag             : false
Packet Size             : 1500
Packet Counter          : 500
Byte Counter            : 6500
Outer TTL               : 5
Inner TTL               : 5
In Interface Name       : 100GE 1/0/2
In Interface ID         : 80
Out Interface Name      : 100GE 1/0/1
Out Interface ID        : 50
Hardware Anomaly Flag   : 0x00000ff
Microcode Anomaly Flag  : 0x000ee
Overflow Flag           : False
RoCEv2 Qpair            : 0
------------------------------------------------------------

```

# Display the entries for all IPv6 flows on the card in slot 1.
```
<HUAWEI> display any-flow flow-cache ipv6 slot 1
Total: 1
----------------------------------------------------------------
SIP   :2001:db8:1::1                            SrcPort :20
DIP   :2001:db8:2::1                            DstPort :30
VRF   :_public_                                 Protocol:17
VNI   :--                                       VLAN    :--
Qpair :--
----------------------------------------------------------------

```

# Display the entries for all IPv4 flows on the card in slot 1.
```
<HUAWEI> display any-flow flow-cache ipv4 slot 1
Total: 1
----------------------------------------------------------------
SIP   :192.168.1.1                            SrcPort :20
DIP   :10.1.1.1                               DstPort :30
VRF   :_public_                               Protocol:17
VNI   :--                                     VLAN    :--
Qpair :--
----------------------------------------------------------------

```

# Display entries for flows whose source IPv4 address is 192.168.1.2, the destination IPv4 address is 10.0.0.2, and the VPN instance is vpn1 on the card in slot 1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:4
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:4
[*HUAWEI-vpn-instance-vpn1-af-ipv6] commit
[~HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[~HUAWEI-vpn-instance-vpn1] quit
[~HUAWEI] quit
<HUAWEI> display any-flow flow-cache sip 192.168.1.2 dip 10.1.1.1 vpn-instance vpn1 slot 1
------------------------------------------------------------
Start Timestamp         : 2020-06-17 15:07:27
Last Timestamp          : 2020-06-17 17:01:12
First Non-SYN TimeStamp : 2016131313180
SIP                     : 192.168.1.2                
DIP                     : 10.1.1.1
SrcPort                 : 20   
DstPort                 : 30
Protocol                : 17
VNI                     : --
VLAN                    : --
VPN Instance            : vpn1
Tunnel Flag             : false
Packet Size             : 1500
Packet Counter          : 500
Byte Counter            : 6500
Outer TTL               : 5
Inner TTL               : 5
In Interface Name       : 100GE 1/0/2
In Interface ID         : 80
Out Interface Name      : 100GE 1/0/1
Out Interface ID        : 50
Hardware Anomaly Flag   : 0x00000ff
Microcode Anomaly Flag  : 0x000ee
Overflow Flag           : False
RoCEv2 Qpair            : 0
------------------------------------------------------------

```

**Table 1** Description of the **display any-flow flow-cache** command output
| Item | Description |
| --- | --- |
| Start Timestamp | Timestamp when traffic enters the device. |
| Last Timestamp | Timestamp when traffic leaves the device. |
| First Non-SYN TimeStamp | Timestamp of the first non-SYN packet. |
| SIP | Source IP address. |
| DIP | Destination IP address. |
| SrcPort | Source Layer 4 port number. |
| DstPort | Destination Layer 4 port number. |
| Protocol | Protocol type. |
| VNI | VNI ID. |
| VLAN | ID of the VLAN. |
| VPN Instance | VPN instance. |
| Tunnel Flag | VXLAN tunnel status. |
| Packet Size | Packet size. |
| Packet Counter | Number of packets. |
| Byte Counter | Number of bytes. |
| Outer TTL | TTL in the outer IP header. |
| Inner TTL | TTL in the inner IP header. |
| In Interface Name | Inbound interface name. |
| In Interface ID | Inbound interface index. |
| Out Interface Name | Outbound interface name. |
| Out Interface ID | Outbound interface index. |
| Hardware Anomaly Flag | Hardware exception identifier. |
| Microcode Anomaly Flag | Microcode exception identifier. |
| Overflow Flag | Overload status identifier. |
| RoCEv2 Qpair | Queue pair information in RoCEv2 packets. |
| Qpair | Queue pair information in RoCEv2 packets. |
| VRF | Index of a VPN instance. |