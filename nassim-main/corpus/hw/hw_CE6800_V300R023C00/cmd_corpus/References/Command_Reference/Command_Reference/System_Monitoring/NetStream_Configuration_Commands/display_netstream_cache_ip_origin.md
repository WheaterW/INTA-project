display netstream cache ip origin
=================================

display netstream cache ip origin

Function
--------



The **display netstream cache ip origin** command displays details about IPv4 original flow statistics on a device.




Format
------

**display netstream cache ip origin** [ [ { **inbound** | **outbound** } | **source** **interface** { *interface-name* | *interface-type* *interface-number* } | **source** **port** *port-number* | **source** **ip** *ip-address* | **destination** **interface** { *interface-name* | *interface-type* *interface-number* } | **destination** **port** *port-number* | **destination** **ip** *ip-address* | **tos** *tos-num* | **protocol** *protocol-num* ] \* ] **slot** *slot-id* [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **inbound** | Specifies incoming packets. | - |
| **outbound** | Specifies outgoing packets. | - |
| **source** | Specifies the source information of packets. | - |
| **interface** *interface-type* *interface-number* | Specifies the interface of packets. | - |
| *interface-name* | Specifies the interface name of packets. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **port** *port-number* | Specifies the port number of packets. | The value is an integer that ranges from 0 to 65535. |
| **ip** *ip-address* | Specifies the IPv4 address of packets. | The value is in dotted decimal notation. |
| **destination** | Specifies the destination information of packets. | - |
| **tos** *tos-num* | Specifies the ToS value of packets. | The value is an integer that ranges from 0 to 255. |
| **protocol** *protocol-num* | Specifies the protocol type of packets. | The value is an integer that ranges from 0 to 255. |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **verbose** | Displays detailed information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

This command displays real-time statistics on IPv4 original flows on the device.

**Precautions**

This command must be executed before the flows age out; otherwise, no information will be displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display details about IPv4 original flow statistics on the device.
```
<HUAWEI> display netstream cache ip origin slot 1
NOTE:
  L4 Info: SourcePort,DestinationPort,Protocol
  TCP Flags: URG,ACK,PSH,RST,SYN,FIN
Last time when cache information were cleared: 2022-2-11 20:20:36
NetStream cache information:
-------------------------------------------------------------------------------
SrcIf                                   SrcVlan          TCP Flags
DstIf                                   DstVlan          L4 Info
SrcIP                                   ToS              Direction
DstIP                                   Octets           Packets
------------------------------------------------------------------------
100GE1/0/5                               77               -,-,-,-,-,-
-                                       -                0,0,253
192.168.1.2                              0                Inbound
192.168.1.1                              170502420        1550022


------------------------------------------------------------------------

```

# Display details about IPv4 original flow statistics on the device.
```
<HUAWEI> display netstream cache ip origin slot 1 verbose
NOTE:
  L4 Info: SourcePort,DestinationPort,Protocol
  TCP Flags: URG,ACK,PSH,RST,SYN,FIN
Last time when cache information were cleared: 2021-12-11 20:20:36
NetStream cache information:
-------------------------------------------------------------------------------
SrcIf                      SrcVlan         SrcIP               Octets
DstIf                      DstVlan         DstIP               Packets
TCP Flags                  Direction       L4 Info             ToS
MPLS Label1                MPLS Label2     MPLS Label3         MPLS Label4
-------------------------------------------------------------------------------
100GE1/0/5                 20              192.168.1.3         414512512
-                          0               192.168.1.1         3238379
0,0,0,0,0,0                Inbound         0,0,253             0
0                          0               0                   0

100GE1/0/5                 20              192.168.1.2         1007323776
-                          0               192.168.1.1         7869717
0,0,0,0,0,0                Inbound         1024,4789,17        0
0                          0               0                   0

100GE1/0/5                 20              192.168.1.2         415422336
-                          0               192.168.1.1         3245487
0,0,0,0,0,0                Inbound         0,0,253             0
0                          0               0                   0

-------------------------------------------------------------------------------

```

**Table 1** Description of the **display netstream cache ip origin** command output
| Item | Description |
| --- | --- |
| L4 Info | Transport layer information about packets, in the format of source port number, destination port number, protocol type. |
| TCP Flags | TCP flag of packets. The format is URG,ACK,PSH,RST,SYN,FIN. |
| Last time when cache information were cleared | Last time when flow table information was cleared. |
| NetStream cache information | NetStream flow table information. |
| SrcIf | Source interface of packets.  If this field displays - when inbound packet sampling is performed, the source interface of packets does not exist. |
| SrcVlan | Source VLAN of packets. |
| DstIf | Destination interface of packets.  If this field displays - when inbound packet sampling is performed, the source interface of packets does not exist. |
| DstVlan | Destination VLAN of packets. |
| SrcIP | Source IP address of packets. |
| ToS | Service type of packets. |
| Direction | Packet sampling direction:  * Inbound: inbound direction. * Outbound: outbound direction. |
| DstIP | Destination IP address of packets. |
| Octets | Number of octets in packets. |
| Packets | Number of packets. |
| MPLS Label1 to MPLS Label4 | MPLS label of packets. |
| NOTE | Description. |