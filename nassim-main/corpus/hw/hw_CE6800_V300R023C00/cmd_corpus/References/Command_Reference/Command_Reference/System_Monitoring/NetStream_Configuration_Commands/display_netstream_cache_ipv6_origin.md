display netstream cache ipv6 origin
===================================

display netstream cache ipv6 origin

Function
--------



The **display netstream cache ipv6 origin** command displays details about IPv6 original flow statistics on a device.




Format
------

**display netstream cache ipv6 origin** [ [ { **inbound** | **outbound** } | **source** **interface** { *interface-name* | *interface-type* *interface-number* } | **source** **port** *port-number* | **source** **ipv6** *ipv6-address* | **destination** **interface** { *interface-name* | *interface-type* *interface-number* } | **destination** **port** *port-number* | **destination** **ipv6** *ipv6-address* | **tos** *tos-num* | **protocol** *protocol-num* | **flowlabel** *flowlabel-num* ] \* ] **slot** *slot-id* [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **inbound** | Specify inbound information to match. | - |
| **outbound** | Specify outbound information to match. | - |
| **source** | Specify source information to match. | - |
| **interface** *interface-type* *interface-number* | Specifies the interface of packets. | - |
| *interface-name* | The specified interface name. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **port** *port-number* | Specifies the port number of packets. | The value is an integer that ranges from 0 to 65535. |
| **ipv6** *ipv6-address* | Specifies the IPv6 address of packets. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **destination** | Specify destination information to match. | - |
| **tos** *tos-num* | Specifies the ToS value of packets. | The value is an integer that ranges from 0 to 255. |
| **protocol** *protocol-num* | Specifies the protocol type of packets. | The value is an integer that ranges from 0 to 255. |
| **flowlabel** *flowlabel-num* | Specifies the flow label of packets. | The value is an integer that ranges from 0 to 1048575. |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **verbose** | Verbose Information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

This command displays real-time statistics on flows on the device.

**Precautions**

This command must be executed before the flows age out; otherwise, no information will be displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about IPv6 original flow statistics on the device.
```
<HUAWEI> display netstream cache ipv6 origin slot 1 verbose
NOTE:
  L4 Info: SourcePort,DestinationPort,Protocol
  TCP Flags: URG,ACK,PSH,RST,SYN,FIN
Last time when cache information were cleared: 2022-2-11 20:20:36
NetStream cache information:
-------------------------------------------------------------------------------
SrcIf                                   SrcVlan          TCP Flags
DstIf                                   DstVlan          L4 Info
SrcIP                                   ToS              FlowLabel
DstIP                                   Octets           Packets
Direction
-------------------------------------------------------------------------------
100GE1/0/5                              20               1,0,0,0,0,0
-                                       0                0,0,6
2001:db8:1::1	                        0                0
2001:db8:1::2                           4211184256       32899877
Inbound

100GE1/0/5                              20               0,0,0,0,0,0
-                                       0                0,0,59
2001:db8:1::3                           0                0
2001:db8:1::2                           4235529984       33090078
Inbound

-------------------------------------------------------------------------------

```

# Display detailed information about IPv6 original flow statistics on the device.
```
<HUAWEI> display netstream cache  ipv6 origin  slot 1
NOTE: 
  L4 Info: SourcePort,DestinationPort
Last time when cache information were cleared: 2022-2-11 20:20:36
NetStream cache information:
--------------------------------------------------------------------------
SrcIP                                     Direction         Protocol            
DstIP                                     ToS               L4 Info             
Interface                                 Flowlabel         
--------------------------------------------------------------------------
2001:db8:2::1                  Outbound          59                  
2001:db8:2::2                  0                 0,0                 
100GE1/0/5                                0                 

------------------------------------------------------------------------

```

**Table 1** Description of the **display netstream cache ipv6 origin** command output
| Item | Description |
| --- | --- |
| L4 Info | Transport layer information about packets.  When detailed information is displayed, the format is source port number, destination port number, protocol type.  When non-detailed information is displayed, the format is source port number, destination port number. |
| TCP Flags | TCP flag of packets. The format is URG,ACK,PSH,RST,SYN,FIN. |
| Last time when cache information were cleared | Last time when flow table information was cleared. |
| NetStream cache information | NetStream flow table information. |
| SrcIf | Source interface of packets.  If this field displays - when inbound packet sampling is performed, the source interface of packets does not exist. |
| SrcVlan | Source VLAN of packets. |
| DstIf | Destination interface of packets.  If this field displays - when inbound packet sampling is performed, the source interface of packets does not exist. |
| DstVlan | Destination VLAN of packets. |
| SrcIP | Source IPv6 address of packets. |
| ToS | Service type of packets. |
| FlowLabel | IPv6 flow label. |
| DstIP | Destination IPv6 address of packets. |
| Octets | Number of octets in packets. |
| Packets | Number of packets. |
| Direction | Packet sampling direction:   * Inbound: inbound direction. * Outbound: outbound direction. |
| Protocol | Protocol number. |
| NOTE | Description. |