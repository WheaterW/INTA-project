display netstream cache ip record
=================================

display netstream cache ip record

Function
--------



The **display netstream cache ip record** command displays details about IPv4 flexible flow statistics on a device.




Format
------

**display netstream cache ip record** *record-name* [ [ { **inbound** | **outbound** } | **source** **interface** { *interface-name* | *interface-type* *interface-number* } | **source** **port** *port-number* | **source** **ip** *ip-address* | **destination** **interface** { *interface-name* | *interface-type* *interface-number* } | **destination** **port** *port-number* | **destination** **ip** *ip-address* | **tos** *tos-num* | **protocol** *protocol-num* ] \* ] **slot** *slot-id* [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *record-name* | Specifies the name of a flexible flow statistics template. | The record-name must already exist. |
| **inbound** | Specify inbound information to match. | - |
| **outbound** | Specify outbound information to match. | - |
| **source** | Specify source information to match. | - |
| **interface** *interface-type* *interface-number* | Specifies the interface of packets. | - |
| *interface-name* | Specifies the interface name of packets. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **port** *port-number* | Specifies the port number of packets. | The value is an integer that ranges from 0 to 65535. |
| **ip** *ip-address* | Specifies the IPv4 address of packets. | The value is in dotted decimal notation. |
| **destination** | Specify destination information to match. | - |
| **tos** *tos-num* | Specifies the ToS value of packets. | The value is an integer that ranges from 0 to 255. |
| **protocol** *protocol-num* | Specifies the protocol type of packets. | The value is an integer that ranges from 0 to 255. |
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

This command displays real-time statistics on IPv4 flexible flows on the device.

**Precautions**

This command must be executed before the flows age out; otherwise, no information will be displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about IPv4 flexible flow statistics on the device.
```
<HUAWEI> display netstream cache ip record flex slot 1 verbose
NOTE:
  L4 Info: SourcePort,DestinationPort,Protocol
  TCP Flags: URG,ACK,PSH,RST,SYN,FIN
Last time when cache information were cleared: 2021-12-11 20:20:36
NetStream cache information:
-------------------------------------------------------------------------------
SrcIP           SrcIf                      SrcMac          L4 Info
DstIP           DstIf                      DstMac          TCP Flags
EthType         Vlan                       Octets          Packets
Direction       ToS
-------------------------------------------------------------------------------
192.168.1.2     100GE1/0/5                 -               -,-,-
-               -                          -               0,0,0,0,0,0
-               -                          172412416       1346972
Inbound         -

192.168.1.3     100GE1/0/5                 -               -,-,-
-               -                          -               0,0,0,0,0,0
-               -                          172339200       1346400
Inbound         -

-------------------------------------------------------------------------------

```

# Display detailed information about IPv4 flexible flow statistics on the device.
```
<HUAWEI> display netstream cache  ip record  aaa slot 1
NOTE: 
  L4 Info: SourcePort,DestinationPort 
Last time when cache information were cleared: 2021-12-11 20:20:36
NetStream cache information:
------------------------------------------------------------------------
SrcIP           SrcIf                      SrcMac          
DstIP           DstIf                      DstMac          
EthType         L4 Info                    Direction       
Vlan            Protocol                   Tos             
------------------------------------------------------------------------
192.168.1.2      100GE1/0/5                  00e0-fc12-3456      
192.168.1.1      -                          ffff-ffff-ffff   
0x0800          0,0                        Inbound         
77              253                        0               
 
------------------------------------------------------------------------

```

**Table 1** Description of the **display netstream cache ip record** command output
| Item | Description |
| --- | --- |
| L4 Info | Transport layer information about packets.  When detailed information is displayed, the format is source port number, destination port number, protocol type.  When non-detailed information is displayed, the format is source port number, destination port number. |
| TCP Flags | TCP flag of packets. The format is URG,ACK,PSH,RST,SYN,FIN. |
| Last time when cache information were cleared | Last time when flow table information was cleared. |
| NetStream cache information | NetStream flow table information. |
| SrcIP | Source IP address of packets. |
| SrcIf | Inbound interface of packets.  If this field displays - when inbound packet sampling is performed, the source interface of packets does not exist.  If a physical interface that has been added to an Eth-Trunk and configured with the sampling function is switched to another Eth-Trunk, the interface information in the flow table is still that of the original Eth-Trunk. If the sampling function is also configured on the Eth-Trunk after the switchover, the interface information in the flow table is updated to the new Eth-Trunk after the flow table is aged out. |
| SrcMac | Source MAC address of packets. |
| DstIP | Destination IP address of packets. |
| DstIf | Outbound interface of packets.  If this field displays - when inbound packet sampling is performed, the source interface of packets does not exist.  If a physical interface that has been added to an Eth-Trunk and configured with the sampling function is switched to another Eth-Trunk, the interface information in the flow table is still that of the original Eth-Trunk. If the sampling function is also configured on the Eth-Trunk after the switchover, the interface information in the flow table is updated to the new Eth-Trunk after the flow table is aged out. |
| DstMac | Destination MAC address of packets. |
| EthType | Ethernet type of packets. |
| Vlan | Vlan ID of packets. |
| Octets | Number of octets in packets. |
| Packets | Number of packets. |
| Direction | Packet sampling direction:  * Inbound: inbound direction. * Outbound: outbound direction. |
| ToS | ToS value of packets. |
| Protocol | Protocol. |
| NOTE | Description. |