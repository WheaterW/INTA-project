display ospf peer
=================

display ospf peer

Function
--------



The **display ospf peer** command displays information about neighbors in each OSPF area.




Format
------

**display ospf** [ *process-id* ] **peer** [ *interfaceName* | *interfaceType* *interfaceNum* | { *neighbor-id* | **hostname** *hostnamestr* } | **brief** | **last-nbr-down** ]

**display ospf** [ *process-id* ] **peer** { { *interfaceName* | *interfaceType* *interfaceNum* } { *neighbor-id* [ **resolve-hostname** ] | **hostname** *hostnamestr* } }

**display ospf** [ *process-id* ] **peer** [ *interfaceName* | *interfaceType* *interfaceNum* | *neighbor-id* | **brief** ] **resolve-hostname**

**display ospf** [ *process-id* ] **peer** [ *interfaceType* *interfaceNum* | *neighbor-id* | **brief** ] **dns-hostname**

**display ospf** [ *process-id* ] **peer** { *interfaceType* *interfaceNum* | *neighbor-id* [ **dns-hostname** ] | **dns-hostname** *hostnamestr* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | process-id Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |
| *interfaceName* | Specifies the name of an interface. | - |
| *interfaceType* | Specifies the type of an interface. | - |
| *interfaceNum* | Specifies the interface number. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *neighbor-id* | Specifies the router ID of a neighbor. | The value is in dotted decimal notation. |
| **hostname** *hostnamestr* | Specifies a dynamic hostname. | The value is a string of 1 to 255 characters. |
| **brief** | Displays summaries of OSPF neighbors in each area. | - |
| **last-nbr-down** | Displays brief information about the last neighbor that goes Down in the OSPF area. | - |
| **resolve-hostname** | Displays information about resolved dynamic hostnames. | - |
| **dns-hostname** *hostnamestr* | Displays information about neighbors with a specified static hostname. | The value is a string of 1 to 255 characters. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The command output can display information about OSPF neighbors, and help you troubleshoot OSPF faults, verify the configurations of OSPF neighbors, and check whether the neighbor performs Graceful Restart (GR).The command output includes such information as all OSPF interfaces, interface types, status, and attributes. If an OSPF neighbor relationship fails to be established or routes are incorrectly calculated, you can run the command to check whether OSPF interfaces are normal.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the OSPF neighbor that goes Down for the last time.
```
<HUAWEI> display ospf 1 peer last-nbr-down

          OSPF Process 1 with Router ID 10.1.1.1

                         Last Down OSPF Peer

         Neighbor Ip Address : 10.2.1.2
         Neighbor Area   Id  : 0.0.0.0
         Neighbor Router Id  : 10.1.1.2
         Interface           : 100GE1/0/1 (9)
         Immediate Reason    : Neighbor Down Due to Kill Neighbor
         Primary Reason      : Hello Not Seen
         Down Time           : 2010-02-11 06:50:23

```

# Display brief information about OSPF neighbors.
```
<HUAWEI> display ospf 1 peer brief
(M) Indicates MADJ interface
          OSPF Process 1 with Router ID 1.1.1.1
                   Peer Statistic Informations

  Total number of peer(s): 2
  Peer(s) in full state: 2

-------------------------------------------------------------------------
 Area Id         Interface      Neighbor id      State
 0.0.0.0         100GE1/0/7        1.1.1.2          Full
 0.0.0.1         100GE1/0/8        1.1.1.2          Full
-------------------------------------------------------------------------

```

# Display OSPF neighbor information.
```
<HUAWEI> display ospf peer
OSPF Process 1 with Router ID 1.1.1.1
 Area 0.0.0.0 interface 192.168.1.1 ( 100GE1/0/8 )'s neighbors
  Router ID: 2.2.2.2         Address : 192.168.1.2
  State    : 2-Way           Mode    : Nbr is  Slave   Priority: 1
  DR       : 192.168.1.4     BDR     : 192.168.1.3     MTU     : 0
  Dead timer due (in seconds) : 32
  Retrans timer interval      : 5
  Neighbor up time            : 00h04m14s
  Neighbor up time stamp      : 2020-06-08 01:41:57
  Authentication Sequence     : 0

```

**Table 1** Description of the **display ospf peer** command output
| Item | Description |
| --- | --- |
| OSPF Process 1 with Router ID 1.1.1.1 | OSPF process ID and router ID. |
| Router ID | Router ID of the neighbor. |
| Down Time | Time when the neighbor goes Down. |
| Neighbor up time stamp | Time when the peer went Up. |
| Neighbor id | Neighbor ID. |
| Neighbor Ip Address | Interface IP address of the neighbor. |
| Neighbor Area Id | Area to which the neighbor belongs. |
| Neighbor Router Id | Router ID of the neighbor. |
| Neighbor up time | Time when the peer went Up. |
| Address | Interface IP address of the neighbor. |
| Area | Area to which the neighbor belongs. |
| Area Id | Area to which the neighbor belongs. |
| Interface | Interface that connects to the neighbor. |
| Immediate Reason | Direct reason why the neighbor goes Down.   * Neighbor Down Due to Inactivity: The inactivity timer expires. * Neighbor Down Due to LL Down: The link is Down. For example, the interface goes Down or the IP address of the link is deleted. * Neighbor Down Due to Kill Neighbor: The Kill Neighbor event occurs on the neighbor state machine of the interface. * Neighbor Down Due to 1-Wayhello: The neighbor goes Down because only one end receives Hello packets. * Received: Neighbor Down Due to AdjOK?: An AdjOK? event occurs on the interface. * Neighbor Down Due to SequenceNum Mismatch: A Sequence Number Mismatch event occurs on the neighbor state machine of the interface. * Neighbor Down Due to BadLSreq: A BadLSreq event occurs on the neighbor state machine of the interface. |
| Primary Reason | Root cause of the neighbor down event.   * Hello Not Seen: No Hello packet is received. * Interface Parameter Mismatch: The parameters of the interfaces at both ends of the link do not match. * Logical Interface State Change: The status of the logical interface changes. * Link Fault or Interface Configuration Change: The link is faulty or the interface configuration is changed. * OSPF Process Reset: The OSPF process is restarted. * Area reset: The area is restarted because the area type changes. * Area Option Mis-match: The area options of the interfaces at both ends of the link do not match. * Vlink Peer Not Reachable: The neighbor on the virtual link is unreachable. * Sham-Link Unreachable: The sham link is unreachable. * Undo Network Command: The network command is deleted. * Undo NBMA Peer: indicates that the neighbor configuration on the NBMA interface is deleted. * Passive Interface Down: The neighbor relationship goes Down because the silent-interface command is run on the local end to disable the interface from receiving and sending OSPF packets. * Opaque Capability Enabled: The Opaque capability is enabled. * Opaque Capability Disabled: The opaque capability is disabled. * Virtual Interface State Change: The status of the virtual link interface changes. * BFD Session Down: The BFD session is Down. * Retransmission Limit Exceed: The retransmission limit is reached. * 1-Wayhello Received: Only one of the neighbors receives Hello packets. * Router State Change from DR or BDR to DROTHER: The interface state machine changes from DR or BDR to DROTHER. * Neighbor State Change from DR or BDR to DROTHER: The interface state machine changes from DR or BDR to DROTHER. * NSSA Area Configure Change: indicates that the NSSA area configuration changes. * Stub Area Configure Change: indicates that the configuration of the stub area changes. * Received Invalid DD Packet: indicates that invalid DD packets are received. * Not Received DD during RouterDeadInterval: No DD packet is received when the Dead timer starts. * M,I,MS bit or SequenceNum Incorrect: The M, I, and MS bits in the received DD packet do not comply with the protocol. * Unable Opaque Capability,Find 9,10,11 Type Lsa: LSAs of types 9, 10, and 11 are received, but the Opaque capability is not enabled. * Not NSSA,Find 7 Type Lsa in Summary List: indicates that the local area does not belong to the NSSA but Type 7 LSAs are found in the summary table. * LSrequest Packet,Unknown Reason: indicates that the LSR packet is received due to unknown reasons. * NSSA or STUB Area,Find 5 ,11 Type Lsa: indicates that the local area is an NSSA or a stub area but Type 5 and Type 11 LSAs are discovered. * LSrequest Packet,Request Lsa is Not in the Lsdb: The neighbor requests an LSA from the local process or area, but the LSA does not exist in the LSDB of the local process or area. * LSrequest Packet, exist same lsa in the Lsdb: indicates that the local process receives an LSA that already exists in the local LSDB and is in the request list of the neighbor. * LSrequest Packet, exist newer lsa in the Lsdb: indicates that the local process receives an updated LSA that already exists in the local LSDB and is in the request list of the neighbor. * Neighbor state was not full when LSDB overflow: When the LSDB exceeds the upper limit, the neighbor status changes to Down if the neighbor status does not reach Full. * Filter LSA configuration change: The LSA filter configuration changes. * ACL changed for Filter LSA: The ACL configuration of LSA filter changes. * Reset OSPF Peer: The OSPF neighbor is restarted. * Interface Reset: Restart the interface. * Undo OSPF Interface, Undo area, Undo network: disables interfaces, areas, and networks. * UNDO OSPF Area: The area is disabled. * CPU Overload: The CPU is overloaded. * Interface State Change to Standby: The interface changes to the standby state. * Undo Router-Id: The router ID is deleted. * Neighbor Router-Id changed or Ip Conflicted: The router ID of the neighbor changes or an IP address conflict occurs. * Component is in Implement stat: The component status is incomplete. * Seqeunce Number mismatched: The sequence number does not match. * I Bit Incorrect in DD: The I bit in the DD packet does not match. * MS Bit Incorrect in DD: indicates that the MS bit in the DD packet does not match. * Options Incorrect in DD: The option field of the DD packet does not match. * The MTU of the DD packet received by the Received MTU mismatched DD Packet does not match. * OSPF Process Shutdown: The OSPF process is shut down. * OSPF Max Nbr In Adj: The number of OSPF neighbors exceeds the maximum. * OSPF Dcn Intf Para MisMatch: OSPF DCN interface parameters do not match. * OSPF Gr Master ForceDown: " OSPF Gr forced shutdown. * DD retrans times upto limit: The number of retransmitted DD packets reaches the upper limit. * Neighbor state was not full when LSDB overflow: OSPF flow control. * Received DD packet without R bit in graceful-restart status: indicates that the DD packet received in the GR state does not carry the R bit. * Memory Overload: The memory is overloaded. * Undo OSPF Interface, Undo area: Delete an interface or an area. |
| (M) Indicates MADJ interface | Multi-area adjacency interface. |
| Total number of peer(s) | Total information of neighbors. |
| Peer(s) in full state | Number of entries with the neighbor state Full. |
| State | Neighbor status:   * Down: It is the initial status of the neighbor, indicating that the neighbor does not receive any information. On an NBMA network, when the neighbor is Down, Hello packets can still be transmitted at the poll interval, which is longer than the Hello interval. * Attempt: It exists only on an NBMA network, indicating that two ends are attempting to establish the neighbor relationship. The interval at which Hello packets are sent is the Hello interval, which is shorter than the poll interval. * Init: It indicates that the Hello packet has been received from the neighbor. * 2-Way: It indicates that the Hello packet has been received from the neighbor, and the neighbor list of the Hello packet contains the local router ID. That is, the two ends can interwork. * ExStart: It is the first step of establishing adjacencies. In this step, the master and slave relationship and Database Description (DD) sequence number are negotiated. * Exchange: It indicates that the LSDBs start to be synchronized. In this process, DD packets, Link Status Request (LSR) packets, and Link Status Update (LSU) packets are exchanged. * Loading: It indicates that the LSDBs are being synchronized. In this process, LSR packets and LSU packets are exchanged. * Full: It indicates that the LSDB of the neighbor has been synchronized, and the Full adjacency is established between both ends. |
| Mode | Master or slave in the process of exchanging DD packets:   * Nbr is Master: indicates that the neighbor is the master and actively sends DD packets. * Nbr is Slave: The neighbor is the slave and cooperates with the master to send DD packets. |
| DR | DR. |
| BDR | Backup designated router. |
| MTU | Maximum Transmission Unit (MTU) value of the neighboring interface. |
| Dead timer due in 32 sec | The Dead timer expires in x seconds. |
| Dead timer due (in seconds) | Remaining time (in seconds) of the Dead timer. |
| Retrans timer interval | Interval for retransmitting LSAs, in seconds. |
| Authentication Sequence | Authentication sequence number. |
| Priority | Priority of the neighbor. |