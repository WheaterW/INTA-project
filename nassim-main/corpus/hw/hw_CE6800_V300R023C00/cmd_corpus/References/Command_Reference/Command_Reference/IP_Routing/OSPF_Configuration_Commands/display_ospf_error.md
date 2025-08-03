display ospf error
==================

display ospf error

Function
--------



The **display ospf error** command displays OSPF error information.




Format
------

**display ospf** *process-id* **error**

**display ospf** [ *process-id* ] **error** **lsa**

**display ospf error**

**display ospf** *process-id* **error** **interface** { *interface-name* | *interface-type* *interface-number* }

**display ospf error interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process.  If no OSPF process ID is specified, error information about all OSPF processes is displayed. | The value ranges from 1 to 4294967295. |
| **lsa** | Display the OSPF LSA errors. | - |
| **interface** *interface-name* | Specifies the name of an interface. | - |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies an interface number. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When locating OSPF faults, you can run the display ospf error command to obtain OSPF error information. You can then analyze OSPF faults according to the OSPF error information.If error statistics keep increasing rapidly, locate the fault based on the error type.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display LSA errors.
```
<HUAWEI> display ospf error lsa
OSPF Process  1  with Router ID 10.1.1.14

 Last Received Bad LSA Header
    LS Age             : 36
    Link State Type    : 0x0008
    Link State ID      : 10.0.1.66
    Advertising Router : 10.2.2.22
    LS Sequence Number : 0x80000002
    LS Checksum        : 0x00bd2e
    Length             : 96
    Interface          : 100GE1/0/1
    Recv Time          : 2011-05-27 14:37:17

```

# Display OSPF error information.
```
<HUAWEI> display ospf error
OSPF Process 1 with Router ID 10.1.1.1
                  OSPF error statistics

General packet errors:
 0           : IP: received my own packet     113         : Bad packet
 0           : Bad version                    0           : Bad checksum
 0           : Bad area id                    0           : Drop on unnumbered interface
 0           : Bad virtual link               0           : Bad authentication type
 0           : Bad authentication key         0           : Packet too small
 1           : Packet size > ip length        0           : Transmit error
 7           : Interface down                 1           : Unknown neighbor
 0           : Bad authentication sequence number 
 15          : TTL error                      0           : Packet too long
 3           : Bad network segment            2           : Bad RouterId
 1           : Bad destination address        0           : Packet received from silent interface

HELLO packet errors:
 1           : Netmask mismatch               50          : Hello timer mismatch
 0           : Dead timer mismatch            0           : Extern option mismatch
 0           : Router id confusion            0           : Virtual neighbor unknown
 0           : NBMA neighbor unknown          0           : Invalid Source Address
 1           : Invalid DR                     0           : LSDB overflow
 147         : DR/BDR mismatch                0           : Neighbor reach limit
 0           : Hold down state                0           : memory overload
 0           : CPU overload

DD packet errors:
 534         : Neighbor state low             0           : Router id confusion
 0           : Extern option mismatch         0           : Unknown LSA type
 0           : MTU option mismatch            0           : CPU overload
 0           : Exchange neighbor limit

LS ACK packet errors:
 1           : Neighbor state low             0           : Unknown LSA type

LS REQ packet errors:
 0           : Neighbor state low             0           : Empty request
 0           : Bad request

LS UPD packet errors:
 0           : Neighbor state low             17          : Newer self-generate LSA
 0           : LSA checksum bad               12          : Received less recent LSA
 2           : Unknown LSA type               0           : Ignore receive LSA
 7           : Received LSA within LSA Arrival interval

Opaque errors:  
 0           : 9-out of flooding scope        32          : 10-out of flooding scope
 13          : 11-out of flooding scope       0           : Unknown TLV type
 12          : RI LSA TLV ERROR               25          : RI LSA Sub TLV ERROR
 19          : ExtendPrefix LSA TLV ERROR     0           : ExtendPrefix LSA Sub TLV ERROR
 8           : ExtendLink LSA TLV ERROR       0           : ExtendLink LSA Sub TLV ERROR
 0           : EIA-ASBR LSA TLV ERROR         0           : EIA-ASBR TLV ERROR
 0           : EIA-ASBR Sub TLV ERROR

SR TLV errors:
 1           : Bad SR-Algorithm TLV           3           : Bad SID/Label Range TLV
 2           : Bad SID/Label Sub TLV          1           : Bad Extended Prefix  TLV
 1           : Bad Prefix-SID Sub TLV         1           : Bad Extended Prefix Range TLV
 3           : Bad LAN Adj-SID Sub TLV        2           : Bad Adj-SID Sub TLV 
 1           : Bad Extended Link TLV          0           : Bad Flex-Algo Definition TLV
 0           : Bad Exclude AG Sub TLV         0           : Bad Include-Any AG Sub TLV
 0           : Bad Include-All AG Sub TLV     0           : Bad FAD Flags Sub TLV
 0           : Bad ASLA Sub TLV               0           : Bad TE Metric Sub TLV
 0           : Bad Link Delay Sub TLV         0           : Bad Extended AG Sub TLV
 0           : Bad AG Sub TLV                 0           : Bad FAPM Sub TLV
 0           : Bad FAAM Sub TLV

Retransmission for packet over Limitation errors:
 0           : Number for DD Packet           0           : Number for Update Packet
 0           : Number for Request Packet

Receive Grace LSA errors:
 0           : Number of invalid LSAs         0           : Number of policy failed LSAs
 0           : Number of wrong period LSAs

Configuration errors:
 0           : Tunnel cost mistake
 1           : The network type of the neighboring interface is not consistent

```

**Table 1** Description of the **display ospf error** command output
| Item | Description |
| --- | --- |
| Router id confusion | The router IDs on the two ends are the same. |
| Last Received Bad LSA Header | Last received LSA. |
| Received less recent LSA | The LSA older than the local LSA is received. |
| Received LSA within LSA Arrival interval | An LSA is received within the LSA arrival interval. |
| Bad packet | The parsed packet is incorrect, including the checksum of the length field. |
| Bad version | The OSPF version is incorrect (not version 2). |
| Bad checksum | The OSPF checksum is incorrect. |
| Bad area id | The area ID in the received packet does not match the local area ID. (Vlink can receive packets from area 0. Area ID inconsistency in other cases is considered an error.). |
| Bad virtual link | V-link receives illegal packets. |
| Bad authentication type | Packet authentication is incorrect. |
| Bad authentication key | Packet authentication key is incorrect. |
| Bad authentication sequence number | Indicates bad authentication sequence number errors. |
| Bad request | Error request. |
| Bad network segment | The source address in the Hello packet does not match the network segment of the local interface address. |
| Bad RouterId | The router ID in the non-Hello packet is different from the router ID of the neighbor. |
| Bad destination address | A non-DR/BDR interface receives a packet with the destination address 224.0.0.6, or the destination address is not the local interface address or the multicast address 224.0.0.5 or 224.0.0.6, the vlink/sham link/NBMA interface and the v3 P2MP non-broadcast interface receive multicast packets with destination addresses 224.0.0.5 and 224.0.0.6. |
| Bad SR-Algorithm TLV | The length of the algorithm TLV of the RI LSA is incorrect. |
| Bad SID/Label Range TLV | The range TLV length of the device LSA is incorrect. |
| Bad SID/Label Sub TLV | The length of the SID sub TLV of the RI LSA is incorrect. |
| Bad Extended Prefix TLV | The length of the extend prefix TLV in the extend prefix LSA is incorrect. |
| Bad Prefix-SID Sub TLV | The length of the prefix SID sub-TLV in the extend prefix LSA is incorrect. |
| Bad Extended Prefix Range TLV | The length of the range TLV in the extended prefix LSA is incorrect. |
| Bad LAN Adj-SID Sub TLV | The length of the lan adj sid sub TLV in the extended link LSA is incorrect. |
| Bad Adj-SID Sub TLV | Failed to check the length of adj sid sub tlv in the extended link LSA. |
| Bad Extended Link TLV | An error occurred when checking the TLV length of the extended link in the extended link LSA. |
| Bad Flex-Algo Definition TLV | The Flex-Algo definition TLV is incorrect. |
| Bad Exclude AG Sub TLV | The Exclude extended admin group sub-TLV is incorrect. |
| Bad Include-Any AG Sub TLV | The Include-Any extended admin group sub-TLV is incorrect. |
| Bad Include-All AG Sub TLV | The Include-All extended management group sub-TLV is incorrect. |
| Bad FAD Flags Sub TLV | The FAD flag sub-TLV is incorrect. |
| Bad ASLA Sub TLV | The sub-TLV of the specific application link attribute is incorrect. |
| Bad TE Metric Sub TLV | The TE Metric sub-TLV is incorrect. |
| Bad Link Delay Sub TLV | The link delay sub-TLV is incorrect. |
| Bad Extended AG Sub TLV | The extended admin group sub-TLV is incorrect. |
| Bad AG Sub TLV | Administrative group sub-TLV error. |
| Bad FAPM Sub TLV | FAPM sub-TLV error. |
| Bad FAAM Sub TLV | FAAM sub-TLV error. |
| LSA checksum bad | LSA checksum error. |
| LS ACK packet errors | LS Ack packet errors. |
| LS REQ packet errors | LSR packet errors. |
| LS UPD packet errors | LSU packet errors. |
| LS Age | Aging time of the LSA. |
| LS Sequence Number | Sequence number in the LSA header. |
| LS Checksum | LSA checksum. |
| Link State Type | LSA type. |
| Link State ID | LSA state ID. |
| Advertising Router | Advertising router. |
| Number for DD Packet | Number of times that retransmitting DD packets expires. |
| Number for Update Packet | Number of times that retransmitting Update packets expires. |
| Number for Request Packet | Number of times that retransmitting count of Request packets excceds the limit. |
| Number of invalid LSAs | Total number of invalid LSAs. |
| Number of policy failed LSAs | Total number of LSAs rejected by a policy. |
| Number of wrong period LSAs | Total number of wrong period LSAs. |
| Length | Length of the LSA. |
| Interface down | Number of times that the OSPF interface goes Down. |
| Interface | Interface that receives the LSA. |
| Recv Time | LSA receiving time. |
| General packet errors | General packet errors. |
| IP: received my own packet | The interface receives the packet sent by itself. |
| Drop on unnumbered interface | The unnumbered interface receives packets (the interface must be of the P2P type). |
| Packet too small | The length of the received packet does not equal the sum of the IP header length and the packet length. |
| Packet size > ip length | The length of the OSPF packet is greater than the permitted length of the IP packet. |
| Packet too long | The packet length exceeds 65535 bytes. |
| Packet received from silent interface | Packets are received from the silent interface. |
| Transmit error | Transmitting packets to socket fails. |
| Unknown neighbor | OSPF packets are received from non-OSPF neighbors on NBMA networks, virtual links, and sham links. |
| Unknown LSA type | The router receives unknown LSAs. |
| TTL error | The TTL value in the packet is 0. |
| HELLO packet errors | Hello packet errors. |
| Netmask mismatch | The address mask does not match the local address mask. |
| Hello timer mismatch | The Hello intervals on the two ends are inconsistent. |
| Dead timer mismatch | The Dead intervals on the two ends are inconsistent. |
| Extern option mismatch | The extension attributes of the Hello packet are not consistent. |
| Virtual neighbor unknown | The router ID of the packet is inconsistent with that of the neighbor that is configured for the virtual link. |
| NBMA neighbor unknown | The status of the NBMA neighbor is not active. |
| Invalid DR | Statistics about Hello packets with non-zero DR priorities received by a P2P interface. |
| LSDB overflow | Number of received Hello packets when the OSPF LSDB is overloaded. |
| Neighbor state low | Following situations:   * A DD packet is received, but its neighbor status is lower than 2-way. * An LSR packet is received, but its neighbor status is lower than Exchange. * An LSU packet is received, but its neighbor status is lower than Exchange. * An LSAck packet is received, but its neighbor status is lower than Exchange. |
| Neighbor reach limit | The number of neighbors exceeds the upper limit. |
| Hold down state | The neighbor is in the holddown state. |
| memory overload | The received packets are ignored due to memory overload. |
| CPU overload | The received packets are ignored because the CPU is overloaded. |
| DD packet errors | Database description (DD) packet errors. |
| MTU option mismatch | The MTU check of the OSPF interface is enabled, and the MTU of the DD packet received by the interface is greater than the MTU of the interface. |
| Exchange neighbor limit | The number of neighbors in the Exchange state exceeds the upper limit, and the establishment of neighbors is controlled. |
| Empty request | Empty LSR packets. |
| Newer self-generate LSA | Number of new self-generated LSAs. This field is reserved for future use. |
| Ignore receive LSA | The sum of received LSA ignored. |
| Opaque errors | Opaque errors. |
| 9-out of flooding scope | Number of Type 9 LSAs that exceed the flooding scope. |
| 10-out of flooding scope | Number of Type 10 LSAs that exceed the flooding scope. |
| 11-out of flooding scope | Number of Type 11 LSAs that exceed the flooding scope. |
| RI LSA TLV ERROR | The length of the main TLV in the RI LSA is incorrect. |
| RI LSA Sub TLV ERROR | The length of the sub TLV in the RI LSA is incorrect. |
| ExtendPrefix LSA TLV ERROR | The length of the main TLV in the extend prefix LSA is incorrect. |
| ExtendPrefix LSA Sub TLV ERROR | The length of the sub TLV in the Extend prefix LSA is incorrect. |
| ExtendLink LSA TLV ERROR | An error occurred when checking the length of the main TLV of the extended link LSA. |
| ExtendLink LSA Sub TLV ERROR | The length of the sub TLV of the extended link LSA is incorrect. |
| EIA-ASBR LSA TLV | EIA-ASBR LSA error. |
| EIA-ASBR TLV ERROR | EIA-ASBR TLV error. |
| EIA-ASBR Sub TLV ERROR | EIA-ASBR sub-TLV error. |
| SR TLV errors | segment-routing TLV error. |
| Retransmission for packet over Limitation errors | Indicates the number of times that the number of retransmitted packets exceeds the threshold. |
| Receive Grace LSA errors | Number of received incorrect Grace LSAs. |
| Configuration errors | Configuration errors. |
| Tunnel cost mistake | Number of times that the cost of the OSPF tunnel interface is smaller than 1. This count increases by one each time the cost of the OSPF tunnel interface is smaller than one. If the cost is smaller than one, the cost is calculated as one. |
| The network type of the neighboring interface is not consistent | Network types of the neighboring interfaces are different. |