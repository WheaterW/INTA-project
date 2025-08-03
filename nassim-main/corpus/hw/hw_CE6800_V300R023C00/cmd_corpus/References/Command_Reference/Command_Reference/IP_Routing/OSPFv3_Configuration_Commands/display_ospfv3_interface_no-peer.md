display ospfv3 interface no-peer
================================

display ospfv3 interface no-peer

Function
--------



The **display ospfv3 interface no-peer** command displays the interfaces whose states are Up but have no neighbors.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **interface** **no-peer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the OSPFv3 process ID. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display ospfv3 interface command output displays the configuration and operating status of OSPFv3, which facilitates fault location and configuration verification.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the interfaces whose states are Up but have no neighbors.
```
<HUAWEI> display ospfv3 interface no-peer

          OSPFV3 Process 1 with Router ID 1.1.1.1
                  Interfaces

 Area: 0.0.0.0          MPLS TE not enabled

 Interface                    IP Address              Type         State    Cost    Pri
 100GE1/0/1                      ::                      Broadcast    Down     1       1

```

**Table 1** Description of the **display ospfv3 interface no-peer** command output
| Item | Description |
| --- | --- |
| OSPFV3 Process | OSPFv3 process ID. |
| Router ID | Router ID. |
| Interface | Interface address. |
| State | State of the interface:   * Down: The status of the interface is Down. If an interface is Down, the interface is unavailable and cannot be used to transmit traffic. * Loopback: The interface connecting to the network on the router is in the Loopback state. The loopback interface cannot be used to transmit data but can collect interface information through ICMP ping operations or bit error detection. * Waiting: The router is determining the DR and BDR on the network. The DR or BDR election mechanism is not implemented until the waiting period ends. This prevents unnecessary changes in the DR and BDR roles. * P-2-P: The interface is connected to the P2P network or a virtual link. * DROther: The router itself is not elected as the BDR. Instead, another router connecting to the broadcast network or NBMA network is elected as the DR. The router starts to set up adjacency with the DR and BDR (if existing). * BDR: The router functions as the BDR on the network, and will turn into a DR when the current DR fails. The router sets up adjacency with other routers that access the network. * DR: The router functions as the DR on the network. The router sets up adjacency with other routers that access the network. |
| Cost | Cost of the interface. |
| Pri | Priority of the interface. |
| Area | Area to which the interface belongs. |