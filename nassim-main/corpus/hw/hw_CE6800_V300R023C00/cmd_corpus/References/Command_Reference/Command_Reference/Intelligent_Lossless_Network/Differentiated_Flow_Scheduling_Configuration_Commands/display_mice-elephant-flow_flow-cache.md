display mice-elephant-flow flow-cache
=====================================

display mice-elephant-flow flow-cache

Function
--------



The **display mice-elephant-flow flow-cache** command is used to query flow table statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**display mice-elephant-flow flow-cache ipv4** [ **sip** *ipv4-sip-address* | **dip** *ipv4-dip-address* | **srcport** *srcport-number* | **dstport** *dstport-number* | **protocol** *protocol-number* | **vpn-instance** *vpn-instance-name* | **vni** *vni-id* ] \* **slot** *slot-id*

**display mice-elephant-flow flow-cache ipv6** [ **sip** *ipv6-sip-address* | **dip** *ipv6-dip-address* | **srcport** *srcport-number* | **dstport** *dstport-number* | **protocol** *protocol-number* | **vpn-instance** *vpn-instance-name* | **vni** *vni-id* ] \* **slot** *slot-id*

For CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ:

**display mice-elephant-flow flow-cache ipv4** [ **sip** *ipv4-sip-address* | **dip** *ipv4-dip-address* | **srcport** *srcport-number* | **dstport** *dstport-number* | **protocol** *protocol-number* | **vpn-instance** *vpn-instance-name* ] \* **slot** *slot-id*

**display mice-elephant-flow flow-cache ipv6** [ **sip** *ipv6-sip-address* | **dip** *ipv6-dip-address* | **srcport** *srcport-number* | **dstport** *dstport-number* | **protocol** *protocol-number* | **vpn-instance** *vpn-instance-name* ] \* **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **sip** *ipv4-sip-address* | Specifies the source IPv4 address. | The value is in dotted decimal notation. |
| **sip** *ipv6-sip-address* | Specifies a source IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **dip** *ipv4-dip-address* | Specifies a destination IPv4 address. | The value is in dotted decimal notation. |
| **dip** *ipv6-dip-address* | Specifies the destination IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **srcport** *srcport-number* | Specifies the source port number. | The value is an integer in the range of 0 to 65535. |
| **dstport** *dstport-number* | Specifies the destination port number. | The value is an integer in the range of 0 to 65535. |
| **protocol** *protocol-number* | Specifies the protocol type. | The value is an integer ranging from 1 to 255. |
| **vpn-instance** *vpn-instance-name* | Displays information about a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **vni** *vni-id* | Specifies a VNI.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | The value is an integer in the range from 0 to 16777215. |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **ipv6** | Specifies an IPv6 address. | - |
| **ipv4** | Specifies an IPv4 address. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After differentiated flow scheduling is enabled and a flow table is created, you can run this command to view information about the flow table for differentiated flow scheduling in a specified slot in real time.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the flow table for differentiated flow scheduling. (CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ)
```
<HUAWEI> display mice-elephant-flow flow-cache ipv4 sip 192.168.1.2 slot 1
------------------------------------------------------------------        
SIP                     : 192.168.1.2                      
DIP                     : 10.1.1.1                         
SrcPort                 : 0                                 
DstPort                 : 0                                 
Protocol                : 6                                                              
VPN Instance            : _public_                                                          
Packet Counter          : 334044756                         
In Interface Name       : 10GE1/0/1                         
In Interface ID         : 14                                                            
------------------------------------------------------------------

```

# Display information about the flow table for differentiated flow scheduling. (CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, and CE6820S)
```
<HUAWEI> display mice-elephant-flow flow-cache ipv4 sip 192.168.1.2 slot 1
------------------------------------------------------------------
Start Timestamp         : 2022-03-29 15:21:20               
Last Timestamp          : 2022-03-29 15:43:50               
SIP                     : 192.168.1.2                      
DIP                     : 10.1.1.1                         
SrcPort                 : 0                                 
DstPort                 : 0                                 
Protocol                : 6                                 
VNI                     : --                                
VPN Instance            : _public_                          
Tunnel Flag             : False                             
Flow ID                 : 3999                              
Stat ID                 : 35631                             
Byte Counter            : 334044756                         
In Interface Name       : 10GE1/0/1                         
In Interface ID         : 14                                
Out Interface Name      : 10GE1/0/2                        
Out Interface ID        : 61                                
------------------------------------------------------------------

```

**Table 1** Description of the **display mice-elephant-flow flow-cache** command output
| Item | Description |
| --- | --- |
| Start Timestamp | Timestamp when a flow table is created. |
| Last Timestamp | Timestamp of the last flow table update. |
| SIP | Source IP address. |
| DIP | Destination IP address. |
| SrcPort | Source port. |
| DstPort | Destination port number. |
| Protocol | Protocol type. |
| VNI | VNI. |
| VPN Instance | VPN instance. This parameter is displayed only for Layer 3 traffic. |
| Tunnel Flag | VXLAN tunnel status. |
| Flow ID | Flow ID. |
| Stat ID | Statistical ID. |
| Byte Counter | Number of bytes. |
| In Interface Name | Inbound interface name. |
| In Interface ID | Inbound interface index. |
| Out Interface Name | Outbound interface name. |
| Out Interface ID | Outbound interface index. |
| Packet Counter | Number of packets. |