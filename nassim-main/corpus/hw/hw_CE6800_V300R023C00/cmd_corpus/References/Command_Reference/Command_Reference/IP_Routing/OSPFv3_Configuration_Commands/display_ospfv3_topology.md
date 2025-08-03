display ospfv3 topology
=======================

display ospfv3 topology

Function
--------



The **display ospfv3 topology** command displays information about the topology in an OSPFv3 area.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **topology** [ **area** { *area-id* | *area-ipv4* } ] [ **statistics** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the OSPFv3 process ID. | The value is an integer ranging from 1 to 4294967295. |
| **area** *area-id* | Specifies the OSPF area ID. | The value is an integer that ranges from 0 to 4294967295. |
| **area** *area-ipv4* | Specifies the OSPF area ID. | The value is in dotted decimal notation. |
| **statistics** | Displays the statistics of the OSPFv3 topology. | - |



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


# Display the topology in OSPFv3 area 1.
```
<HUAWEI> display ospfv3 topology area 1
OSPFv3 Process (1)
 Bits :
 B - ABR    E - ASBR    V - VIRTUAL    NT - NSSA translator
 
 OSPFv3 Area (0.0.0.1) topology
 Type  ID (If-Index)       Bits      Metric    Next-Hop        Interface
 Rtr   1.1.1.1                      --
 Rtr   2.2.2.2                      1         2.2.2.2         100GE1/0/1
 Net   2.2.2.2 (268435842)          1         0.0.0.0         100GE1/0/1

```

**Table 1** Description of the **display ospfv3 topology** command output
| Item | Description |
| --- | --- |
| Bits | Device type:   * B bit: ABR. * E bit: ASBR. |
| Type | SPF type:   * Rtr: Router. * Net: Network. |
| ID (If-Index) | Router ID. If-Index is the interface ID of the DR in the network type. |
| Metric | Cost of the path to the node. |
| Next-Hop | Next hop of the path to the node. |
| Interface | Outbound interface of the path to the node. |