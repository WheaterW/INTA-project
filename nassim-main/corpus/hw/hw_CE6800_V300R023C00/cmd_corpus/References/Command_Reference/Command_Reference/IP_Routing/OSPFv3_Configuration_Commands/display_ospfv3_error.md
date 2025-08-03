display ospfv3 error
====================

display ospfv3 error

Function
--------



The **display ospfv3 error** command displays OSPFv3 errors.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3 error**

**display ospfv3** *process-id* **error**

**display ospfv3** [ *process-id* ] **error** **lsa**

**display ospfv3 error interface** { *interface-name* | *interface-type* *interface-number* }

**display ospfv3** *process-id* **error** **interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an OSPFv3 process ID. If no process ID is specified, errors of all OSPFv3 processes are displayed. | The value is an integer ranging from 1 to 4294967295. |
| **lsa** | Displays OSPFv3 LSA errors. | - |
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

While analyzing the faults of OSPFv3, you can obtain information of errors using the command. You can then diagnose the faults of OSPFv3 according to information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display LSA errors.
```
<HUAWEI> display ospfv3 error lsa
OSPFV3 Process  1  with Router ID 10.1.1.14

 Last Received Bad LSA Header
    LS Age             : 36
    Link State Type    : 0x0008
    Link State ID      : 0.0.1.66
    Advertising Router : 10.2.2.22
    LS Sequence Number : 0x80000002
    LS Checksum        : 0x00bd2e
    Length             : 96
    Interface          : 100GE1/0/1
    Recv Time          : 2010-11-15 16:37:17

```

# Display OSPFv3 errors.
```
<HUAWEI> display ospfv3 error

          OSPFv3 Process 1 with Router ID 1.1.1.1
                  OSPFV3 Error Statistics

General Packet Errors:
 0          : Bad packet                    0          : Bad version
 0          : Bad area ID                   0          : Bad virtual link
 0          : Packet too small              0          : Transmit error
 0          : Bad Instance ID               0          : Interface down
 0          : Unknown neighbor              0          : Authentication failure
 0          : AuthSeqNum mismatch           0          : AuthKeyId mismatch
 0          : IPv6: received my own packet  0          : Bad Checksum
 0          : TTL error                     0          : Packet too long
 0          : Packet size > ipv6 length     0          : Invalid Source Address
 0          : Bad destination address
 0          : Packet received from silent interface

Hello Packet Errors:
 0          : Hello timer mismatch          0          : Dead timer mismatch
 0          : Extern option mismatch        0          : Router ID confusion
 0          : Virtual neighbor unknown      0          : Invalid DR
 0          : DR/BDR mismatch               0          : Neighbor reach limit
 0          : Hold down state               0          : Memory overload
 0          : CPU overload

DD Packet Errors:
 0          : Neighbor state low            0          : Extern option mismatch
 0          : Unknown LSA Type              0          : MTU option mismatch
 0          : Router ID confusion           0          : CPU overload
 0          : Exchange neighbor limit

LS ACK Packet Errors:
 0          : Neighbor state low            0          : Unknown LSA type

LS REQ Packet Errors:
 0          : Neighbor state low            0          : Bad request
 0          : Empty Request

LS UPD Packet Errors:
 0          : Neighbor state low            0          : LSA checksum bad
 0          : Received less recent LSA      0          : Unknown LSA type
 0          : Newer self-generate LSA       0          : Ignore receive LSA
 0          : Received LSA within LSA Arrival interval

Receive Grace LSA Errors:
 0          : Number of invalid LSAs
 0          : Number of policy failed LSAs
 0          : Number of wrong period LSAs

```

**Table 1** Description of the **display ospfv3 error** command output
| Item | Description |
| --- | --- |
| Router ID confusion | Number of received packets with the same route ID or with the same router ID. |
| Router ID | Router ID of the device. |
| Last Received Bad LSA Header | Error information about the last received LSA. |
| Received less recent LSA | Number of LSAs received less recently. |
| Received LSA within LSA Arrival interval | Number of LSAs received within the LSA arrival interval. |
| Bad packet | The parsed packet is incorrect, including the checksum of the length field. |
| Bad version | The OSPFv3 version is incorrect (not version 3). |
| Bad area ID | The area IDs in the received packets are different from the local area ID, except area 0, and other area IDs are considered incorrect. |
| Bad virtual link | V-link receives illegal packets. |
| Bad Checksum | Number of packets for which checksum calculation failed. |
| Bad request | BadRequest event in the protocol. |
| Bad Instance ID | Number of packets with incorrect instance IDs. |
| Bad destination address | A non-DR/BDR interface receives a packet with the destination address ff02::6, the destination address is not the link-local address of the local interface, or the destination address is not ff02::5 or ff02::6. |
| LSA checksum bad | Number of received packets with incorrect LSA checksums. |
| LS ACK Packet Errors | Title bar: LS ACK packet errors. |
| LS REQ Packet Errors | Title bar: LS REQ packet errors. |
| LS UPD Packet Errors | Title bar: LS UPD packet error. |
| LS Age | Aging time of the LSA. |
| LS Sequence Number | Sequence number in the LSA header. |
| LS Checksum | LSA checksum. |
| Link State Type | LSA type. |
| Link State ID | LSA state ID. |
| Advertising Router | Advertising Device. |
| Number of invalid LSAs | Number of invalid LSAs. |
| Number of policy failed LSAs | Number of LSAs that failed to match a policy. |
| Number of wrong period LSAs | Number of LSAs with incorrect periods. |
| Length | LSA length. |
| Interface down | Number of times that the OSPFv3 interface goes Down. |
| Interface | Interface that receives the LSA. |
| Recv Time | Time when the LSA was received. |
| General Packet Errors | General packet errors. |
| Packet too small | Length of the received packet is not equal to the sum of length of IP header and the length of the packet. |
| Packet too long | The packet length exceeds 65535 bytes. |
| Packet size > ipv6 length | The length of the OSPF packet is greater than the permitted length of the IPv6 packet. |
| Packet received from silent interface | Packets are received from the silent interface. |
| Transmit error | Transmitting packets to socket fails. |
| Unknown neighbor | OSPFv3 packets are received from non-OSPFv3 neighbors on NBMA networks, virtual links, and sham links. |
| Unknown LSA Type | The router receives unknown LSAs. |
| Authentication failure | Number of packets that fail to be authenticated. |
| AuthSeqNum mismatch | Number of bad authentication sequence number errors. |
| AuthKeyId mismatch | Number of packets with key IDs different from the local one. |
| IPv6: received my own packet | Number of IPv6 packets received from itself. |
| TTL error | The TTL value in the packet is 0. |
| Invalid DR | Statistics about Hello packets with non-zero DR priorities received by a P2P interface. |
| Invalid Source Address | The source address of LSA is invalid. |
| Hello Packet Errors | Hello packet errors exist. |
| Hello timer mismatch | The Hello interval is not consistent. |
| Dead timer mismatch | The Dead interval is not consistent. |
| Extern option mismatch | The extension attributes of the Hello packets were inconsistent, or the options of the DD packets did not match. |
| Virtual neighbor unknown | The router ID of the packet is inconsistent with that of the V-link neighbor. |
| DR/BDR mismatch | Number of received packets with DR/BDR errors. |
| Neighbor state low | Number of received packets with low neighbor status.  An error is reported in the following scenarios:   * A DD packet is received but its neighbor status is lower than 2-way. * The LSR packet is received but the neighbor state is lower than Exchange. * The LSU packet is received but the neighbor state is lower than Exchange. * The ACK packet is received but the neighbor status is lower than Exchange. |
| Neighbor reach limit | The number of neighbors exceeds the upper limit. |
| Hold down state | The neighbor is in the holddown state. |
| Memory overload | The received packets are ignored due to memory overload. |
| CPU overload | The received packets are ignored because the CPU is overloaded. |
| DD Packet Errors | Title bar: DD packet errors. |
| MTU option mismatch | The MTU value of the DD packet that is received on the interface is greater than that of this interface. |
| Exchange neighbor limit | The number of neighbors in the Exchange state exceeds the upper limit, and the establishment of neighbors is controlled. |
| Empty Request | Number of received packets with empty requests. |
| Newer self-generate LSA | Number of received LSAs that have been generated by the local device but are newer than the local ones. |
| Ignore receive LSA | The sum of received LSA ignored. |
| Receive Grace LSA Errors | Number of received incorrect Grace LSAs. |