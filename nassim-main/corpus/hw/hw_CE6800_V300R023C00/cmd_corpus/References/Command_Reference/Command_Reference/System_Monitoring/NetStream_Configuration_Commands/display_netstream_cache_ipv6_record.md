display netstream cache ipv6 record
===================================

display netstream cache ipv6 record

Function
--------



The **display netstream cache ipv6 record** command displays details about IPv6 flexible flow statistics on a device.




Format
------

**display netstream cache ipv6 record** *record-name* [ [ { **inbound** | **outbound** } | **source** **interface** { *interface-name* | *interface-type* *interface-number* } | **source** **port** *port-number* | **source** **ipv6** *ipv6-address* | **destination** **interface** { *interface-name* | *interface-type* *interface-number* } | **destination** **port** *port-number* | **destination** **ipv6** *ipv6-address* | **tos** *tos-num* | **protocol** *protocol-num* | **flowlabel** *flowlabel-num* ] \* ] **slot** *slot-id* [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *record-name* | Specifies the name of a flexible flow statistics template. | The value must be the name of an existing template on the device. |
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
| **verbose** | Verbose information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

This command displays real-time statistics on IPv6 flexible flows on the device.

**Precautions**

This command must be executed before the flows age out; otherwise, no information will be displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about IPv6 flexible flow statistics on the device.
```
<HUAWEI> display netstream cache ipv6 record r slot 1 verbose
NOTE:
  L4 Info: SourcePort,DestinationPort,Protocol
  TCP Flags: URG,ACK,PSH,RST,SYN,FIN
Last time when cache information were cleared: 2022-2-11 20:20:36
NetStream cache information:
-------------------------------------------------------------------------------
SrcIP                                   SrcMac            EthType
DstIP                                   DstMac            Vlan
SrcIf                                   L4 Info           Octets
DstIf                                   TCP Flags         Packets
Direction                               ToS               FlowLabel
-------------------------------------------------------------------------------
2001:db8:1::1                           00e0-fc12-3456    -
-                                       -                 -
100GE1/0/5                              -,-,-             3192135168
-                                       0,0,0,0,0,0       24938556
Inbound                                 -                 -

-------------------------------------------------------------------------------

```

# Display detailed information about IPv6 flexible flow statistics on the device.
```
<HUAWEI> display netstream cache ipv6  record  bbb slot 1
NOTE: 
  L4 Info: Source Port,Destination Port
Last time when cache information were cleared: 2022-2-11 20:20:36
NetStream cache information:
-------------------------------------------------------------------------------
SrcIP                                   SrcIf                  SrcMac           
DstIP                                   DstIf                  DstMac           
EthType                                 L4 Info                Direction        
Vlan                                    Protocol               ToS              
------------------------------------------------------------------------
2001:db8:2::1                -                      00e0-fc12-3456    
2001:db8:2::2                100GE1/0/5             ffff-ffff-ffff    
0x86DD                                  0,0                    Outbound         
77                                      59                     0                
 
------------------------------------------------------------------------

```

**Table 1** Description of the **display netstream cache ipv6 record** command output
| Item | Description |
| --- | --- |
| L4 Info | Transport layer information about packets.  When detailed information is displayed, the format is source port number, destination port number, protocol type.  When non-detailed information is displayed, the format is source port number, destination port number. |
| TCP Flags | TCP flag of packets. The format is URG,ACK,PSH,RST,SYN,FIN. |
| Last time when cache information were cleared | Last time when flow table information was cleared. |
| NetStream cache information | NetStream flow table information. |
| SrcIP | Source IPv6 address of packets. |
| SrcMac | Source MAC address of packets. |
| EthType | Ethernet type of packets. |
| DstIP | Destination IPv6 address of packets. |
| DstMac | Destination MAC address of packets. |
| Vlan | Vlan ID of packets. |
| SrcIf | Inbound interface of packets.  If this field displays - when inbound packet sampling is performed, the source interface of packets does not exist.  If a physical interface that has been added to an Eth-Trunk and configured with the sampling function is switched to another Eth-Trunk, the interface information in the flow table is still that of the original Eth-Trunk. If the sampling function is also configured on the Eth-Trunk after the switchover, the interface information in the flow table is updated to the new Eth-Trunk after the flow table is aged out. |
| Octets | Number of octets in packets. |
| DstIf | Outbound interface of packets.  If this field displays - when inbound packet sampling is performed, the source interface of packets does not exist.  If a physical interface that has been added to an Eth-Trunk and configured with the sampling function is switched to another Eth-Trunk, the interface information in the flow table is still that of the original Eth-Trunk. If the sampling function is also configured on the Eth-Trunk after the switchover, the interface information in the flow table is updated to the new Eth-Trunk after the flow table is aged out. |
| Packets | Number of packets. |
| Direction | Packet sampling direction:  * Inbound: inbound direction. * Outbound: outbound direction. |
| ToS | ToS value of packets. |
| FlowLabel | IPv6 flow label. |
| Protocol | Protocol. |
| NOTE | Description. |