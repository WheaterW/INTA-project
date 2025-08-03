display ospfv3 peer
===================

display ospfv3 peer

Function
--------



The **display ospfv3 peer** command displays specified OSPFv3 neighbors.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] [ **area** { *area-id* | *area-idIpv4* } ] **peer** [ { *neighbor-id* | **hostname** *hostnamestr* } | *interfaceName* | *interfaceType* *interfaceNum* ] [ **verbose** ]

**display ospfv3** [ *process-id* ] **peer** **last-nbr-down**

**display ospfv3** [ *process-id* ] [ **area** { *area-id* | *area-idIpv4* } ] **peer** [ *neighbor-id* | *interfaceName* | *interfaceType* *interfaceNum* ] **resolve-hostname** [ **verbose** ]

**display ospfv3** [ *process-id* ] [ **area** { *area-id* | *area-idIpv4* } ] **peer** { *neighbor-id* **dns-hostname** | **dns-hostname** [ *hostnamestr* ] | *interfaceType* *interfaceNum* | *interfaceName* } [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an process ID of OSPFv3. | The value is an integer ranging from 1 to 4294967295. |
| **area** *area-id* | Specifies an area ID. | The value is an integer that ranges from 0 to 4294967295. |
| **area** *area-idIpv4* | Specifies an area ID. | The value is in dotted decimal notation. |
| *neighbor-id* | Specifies router ID of a neighbor. | The value is in dotted decimal notation. |
| **hostname** *hostnamestr* | Specifies a dynamic hostname. | The value is a string of characters ranging from 1 to 255 characters. |
| *interfaceName* | Specifies an interface name. | - |
| *interfaceType* | Specifies an interface type. | - |
| *interfaceNum* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **verbose** | Displays detailed information of neighbors of each area. | - |
| **last-nbr-down** | Displays brief information about the neighbors that go down the last in an OSPFv3 process. Brief information about a maximum of ten such neighbors can be displayed for each process. | - |
| **resolve-hostname** | Displays information about resolved dynamic hostnames. | - |
| **dns-hostname** *hostnamestr* | Displays information about neighbors with a specified static hostname. | The value is a string of characters ranging from 1 to 255 characters. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command displays OSPFv3 neighbor information, which helps you diagnose OSPFv3 faults and verify the configuration of OSPFv3 neighbors.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the detailed neighbor information of OSPFv3 process 100 on 100GE 1/0/1.
```
<HUAWEI> display ospfv3 100 peer 100GE 1/0/1 verbose

OSPFv3 Process (100)
 OSPFv3 Area (0.0.0.0)

 Neighbor 1.1.1.1, interface address FE80::3D43:0:8C14:1
    In the area 0.0.0.1 via interface 100GE1/0/1
    DR is 0.0.0.0 BDR is 0.0.0.0
    Options is 0x000013 (-|R|-|-|E|V6)
    Dead timer due in 00:00:29
    Neighbour is up for 01:08:17
    Neighbour Up Time : 2018-06-08 01:41:57
    Link State Request List 0
    Link State Retransmission List 0
    Neighbour Event: 7
    Neighbour If Id : 0x04

```

# Display neighbor information about OSPFv3 process 1.
```
<HUAWEI> display ospfv3 1 peer
OSPFv3 Process (1)
Total number of peer(s): 1       
 Peer(s) in full state: 1       
OSPFv3 Area (0.0.0.0)
Neighbor ID      Pri State            Dead Time  Interface          Instance ID
2.2.2.2            1 Full/Backup      00:00:35   Vlanif100             0

```

# Display neighbor information about OSPFv3 process 1 on 100GE 1/0/1.
```
<HUAWEI> display ospfv3 1 peer 100GE 1/0/1
OSPFv3 Process (1)
OSPFv3 Area (0.0.0.0)
Neighbor ID     Pri   State           Dead Time   Interface                Instance ID
1.1.1.1           1   Full/ -         00:00:30    100GE1/0/1              0

```

# Display the information about the last neighbor that goes Down in an OSPFv3 process.
```
<HUAWEI> display ospfv3 100 peer last-nbr-down
          OSPFv3 Process 100 with Router ID 1.1.1.1

                         Last Down OSPFv3 Peer

  Neighbor Area   Id  : 0.0.0.1
  Neighbor Router Id  : 2.2.2.2
  Interface           : 100GE1/0/1 (6)
  Instance        Id  : 1
  Immediate Reason    : Neighbor Down Due to AdjOK?
  Primary Reason      : Router State Change from DR or BDR to DROTHER
  Down Time           : 2010-12-22 07:49:21

  Neighbor Area   Id  : 0.0.0.1
  Neighbor Router Id  : 2.2.2.2
  Interface           : 100GE1/0/1 (27)
  Instance        Id  : 1
  Immediate Reason    : Neighbor Down Due to Kill Neighbor
  Primary Reason      : OSPF Process Reset
  Down Time           : 2010-12-22 07:49:16

```

**Table 1** Description of the **display ospfv3 peer** command output
| Item | Description |
| --- | --- |
| OSPFv3 Process | OSPFv3 process. |
| OSPFv3 Area | OSPFv3 area ID. |
| Neighbor ID | Neighbor ID or hostname. |
| Neighbor Area Id | Area to which the last OSPFv3 neighbor that goes Down belongs. |
| Neighbor Router Id | Router ID of the last OSPFv3 neighbor that goes Down. |
| Neighbor x.x.x.x | Router ID of the neighbor: x.x.x.x. |
| interface address | IP address of the neighbor interface. |
| In the area 0.0.0.1 via interface | Interface of the neighbor is in area xxx. |
| DR | Designated router. |
| BDR | Backup Designated Router (BDR). |
| Options | Options of the neighbor. |
| Dead Time | Dead timer of the neighbor. |
| Dead timer due in | Dead timer of the neighbor. |
| Neighbour is up for | Duration that the neighbor has been Up. |
| Neighbour Up Time | Time when the neighbor relationship went Up. |
| Neighbour Event | Neighboring device event. |
| Neighbour If Id | Index of the neighbor interface. |
| Link State Retransmission List | Number of LSAs in the retransmission list of the neighbor. |
| Link State Request List | Number of LSAs in the neighbor request list. |
| State | Neighbor status (Down/Attempt/Init/2 Way/ExStart/Exchange/Loading/Full). |
| Pri | Priority of the neighbor. |
| Interface | Interface that connects to the neighbor. |
| Instance ID | ID of the instance to which a neighbor belongs. |
| Total number of peer(s) | Total information of neighbors. |
| Peer(s) in full state | Number of entries with the neighbor state Full. |
| Router ID | Route ID of the current router. |
| Last Down OSPFv3 Peer | Latest OSPFv3 neighbor that goes Down. |
| Down Time | Period during which a neighbor is in the Down state. |
| Immediate Reason | Direct reason why the neighbor becomes Down. |
| Primary Reason | Root reason why the neighbor becomes Down. |