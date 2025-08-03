display ip statistics verbose
=============================

display ip statistics verbose

Function
--------



The **display ip statistics verbose** command displays statistics about IP packets by protocol types, such as ICMP, IGMP, PIM, VRRP, OSPF, TCP, UDP, and others.




Format
------

**display ip statistics verbose** [ **protocol** { *protocol-id* | **icmp** | **igmp** | **ospf** | **pim** | **rsvp** | **tcp** | **udp** | **vrrp** } ]

**display ip statistics verbose** [ **protocol** { *protocol-id* | **icmp** | **igmp** | **ospf** | **pim** | **rsvp** | **tcp** | **udp** | **vrrp** } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **protocol** | Displays statistics about IP packets of a specific protocol. | - |
| *protocol-id* | Specify the protocol ID. | The value is an integer ranging from 1 to 255.  The value can be 1(ICMP), 2(IGMP), 6(TCP), 17(UDP), 46(RSVP), 89(OSPF), 103(PIM), or 112(VRRP). If the protocol ID specified is none of the preceding values, the protocol is displayed as "Others". |
| **icmp** | Displays statistics about IP packets of ICMP protocol. | - |
| **igmp** | Displays statistics about IP packets of IGMP protocol. | - |
| **ospf** | Displays statistics about IP packets of OSPF protocol. | - |
| **pim** | Displays statistics about IP packets of PIM protocol. | - |
| **rsvp** | Displays statistics about IP packets of RSVP protocol. | - |
| **tcp** | Displays statistics about IP packets of TCP protocol. | - |
| **udp** | Displays statistics about IP packets of UDP protocol. | - |
| **vrrp** | Displays statistics about IP packets of VRRP protocol. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check statistics about IP packets, including sent, received, fragmented, and reassembled packets, run the command. The received packets displayed also include the packets carrying the Source Route options that are received and then discarded.During packet transmission, if the source fragments packets, run the command on the source to check the number of successfully fragmented packets and the number of sent fragmented packets, and then run the display ip statistics command on the destination to check whether the same number of fragmented packets are received.To view detailed IP traffic statistics, run the **display ip statistics verbose** command. The command output helps you locate packet loss problems during packet sending and receiving of a specific application. For example, when BGP fails to be established, you can check whether the value of the bad checksum field increases.

**Precautions**

If the "bad protocol" and "no route" field values displayed are large, the local device receives a large number of packets of unknown protocols and IP packets for which no routes can be found. In this case, check whether the local device is attacked by the connected device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display IP packet statistics verbose.
```
<HUAWEI> display ip statistics verbose
Input:
-------------------------------------------------------------------------
Application        : ICMP                                   
Format error       : 0           Checksum error      : 0          
Option error       : 0           No route            : 0          
Reassembly timeout : 0           Sent to upper-layer : 0          

Application        : OSPF                                   
Format error       : 0           Checksum error      : 0          
Option error       : 0           No route            : 0          
Reassembly timeout : 0           Sent to upper-layer : 3814281    

Application        : RSVP                                   
Format error       : 0           Checksum error      : 0          
Option error       : 0           No route            : 0          
Reassembly timeout : 0           Sent to upper-layer : 0          

Application        : TCP                                    
Format error       : 0           Checksum error      : 0          
Option error       : 0           No route            : 0          
Reassembly timeout : 0           Sent to upper-layer : 0          

Application        : UDP                                    
Format error       : 0           Checksum error      : 0          
Option error       : 0           No route            : 0          
Reassembly timeout : 0           Sent to upper-layer : 0          

Application        : IGMP                                   
Format error       : 0           Checksum error      : 0          
Option error       : 0           No route            : 0          
Reassembly timeout : 0           Sent to upper-layer : 0          

Application        : PIM                                    
Format error       : 0           Checksum error      : 0          
Option error       : 0           No route            : 0          
Reassembly timeout : 0           Sent to upper-layer : 0                

Application        : VRRP                                   
Format error       : 0           Checksum error      : 0          
Option error       : 0           No route            : 0          
Reassembly timeout : 0           Sent to upper-layer : 0          
                
Application        : Others                                 
Format error       : 0           Checksum error      : 0          
Option error       : 0           No route            : 0          
Reassembly timeout : 0           Sent to upper-layer : 0          

-------------------------------------------------------------------------

Output:
-------------------------------------------------------------------------
Application        : ICMP                                   
No route           : 0           Port selection failures : 0      
Dropped Packets    : 0           Path Invalid            : 0      

Application        : OSPF                                   
No route           : 0           Port selection failures : 0      
Dropped Packets    : 0           Path Invalid            : 0      

Application        : RSVP                                   
No route           : 0           Port selection failures : 0      
Dropped Packets    : 0           Path Invalid            : 0      

Application        : TCP                                    
No route           : 0           Port selection failures : 0      
Dropped Packets    : 0           Path Invalid            : 0      

Application        : UDP                                    
No route           : 0           Port selection failures : 0      
Dropped Packets    : 0           Path Invalid            : 0      

Application        : IGMP                                   
No route           : 0           Port selection failures : 0      
Dropped Packets    : 0           Path Invalid            : 0      

Application        : PIM                                    
No route           : 0           Port selection failures : 0      
Dropped Packets    : 0           Path Invalid            : 0      

Application        : VRRP                                   
No route           : 0           Port selection failures : 0      
Dropped Packets    : 0           Path Invalid            : 0      

Application        : Others                                 
No route           : 0           Port selection failures : 0      
Dropped Packets    : 0           Path Invalid            : 0      

-------------------------------------------------------------------------

```

**Table 1** Description of the **display ip statistics verbose** command output
| Item | Description |
| --- | --- |
| Application | Protocol type. |
| Format error | Number of packets with incorrect formats. |
| Checksum error | Number of packets with incorrect checksums. |
| Option error | Number of packets with incorrect options. |
| No route | The number of correctly routed packets cannot be found in the received packets. |
| No route | Number of packets for which no correct route can be found, including the packets sent and forwarded by the local device. |
| Reassembly timeout | Number of fragmented packets that fail to be reassembled due to timeouts. |
| Sent to upper-layer | Number of packets sent to the upper-layer protocol. |
| Port selection failures | Number of packets that failed to select a port. |
| Dropped Packets | Number of discarded packets. |
| Path Invalid | Number of packets with invalid PATH entries. |
| Input | Received packet statistics. |
| Output | Number of sent packets. |