display ospfv3 topology verbose
===============================

display ospfv3 topology verbose

Function
--------



The **display ospfv3 topology verbose** command displays information about the detailed information of the topology in an OSPFv3 area.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **topology** [ **area** { *area-id* | *area-ipv4* } ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies a process ID of OSPFv3. | The value ranges from 1 to 4294967295. |
| **area** *area-id* | Specifies the OSPF area ID. | The value is an integer that ranges from 0 to 4294967295. |
| **area** *area-ipv4* | Specifies the OSPF area ID. | The value is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information about the topology in an OSPFv3 area, run the display ospfv3 topology command. The command output shows information about nodes on the topology, including the type and attribute of each node and cost, outbound interface, and next hop IP address of the path to each node. Such information helps OSPFv3 troubleshooting.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the topology of OSPFv3 area 1.
```
<HUAWEI> display ospfv3 topology verbose
2019-08-13 19:47:13.254 

OSPFv3 Process (1)
Bits :
B - ABR    E - ASBR    V - VIRTUAL    NT - NSSA translator

Shortest Path Tree for Area: 0.0.0.0

Node: Router    10.11.1.2    Cost: 1 Cost(tunnel): 0
    BitFlags : B
    Neighbors: 1 (Children:(0) Parents:(1))
    Neighbor List:
        router  10.10.10.10, Parent, cost: 0
    Nexthop List:
        10.11.1.2        10GE1/0/1.1

```

**Table 1** Description of the **display ospfv3 topology verbose** command output
| Item | Description |
| --- | --- |
| Bits | Device type:   * B bit: ABR. * E bit: ASBR. |
| Shortest Path Tree for Area | Display detailed information about the topology based on which OSPFv3 routes are calculated in a specified area. |
| BitFlags | Route Type ID. |
| Neighbor List | Neighbor of the path to the node. |
| Nexthop List | Next hop of the path to the node. |
| Cost | Cost of the route. |
| Neighbors | Neighbor of the node. |
| Node | Node Information. |