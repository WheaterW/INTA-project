display ospf interface
======================

display ospf interface

Function
--------



The **display ospf interface** command displays OSPF interface information.




Format
------

**display ospf** [ *process-id* ] **interface** [ *interface-name* | *interface-type* *interface-number* | **all** ] [ **verbose** ]

**display ospf** [ *process-id* ] **interface** **no-peer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | process-id Specifies the ID of an OSPF process. | The value ranges from 1 to 4294967295. |
| *interface-type* | Interface type. | - |
| *interface-number* | Specifies the number of an interface based on which information about VLANs in which users go online dynamically is to be displayed. | - |
| **all** | Displays information about all OSPF interfaces. | - |
| **verbose** | Displays detailed information about OSPF interfaces. | - |
| **no-peer** | Specifies to display the interfaces whose states are Up but have no neighbors. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check the configuration and operating status of OSPF, run the display ospf interface command. The command output helps you locate faults and verify configurations.The command output includes such information as all OSPF interfaces, interface types, status, and attributes. If an OSPF neighbor relationship fails to be established or routes are incorrectly calculated, you can run the command to check whether OSPF interfaces are normal.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display OSPF interface information.
```
<HUAWEI> display ospf interface
OSPF Process 1 with Router ID 1.1.1.1
                  
 Area: 0.0.0.0             MPLS TE : Disabled
 Interface                IP Address      Type      State    Cost    Pri
 100GE1/0/1               192.168.1.1     P2P       P-2-P    1       100

```

# Display information about OSPF interfaces that have no neighbors.
```
<HUAWEI> display ospf interface no-peer
OSPF Process 1 with Router ID 172.16.6.185
                  Interfaces

 Area: 0.0.0.0          (MPLS TE not enabled)
 Interface             IP Address      Type         State    Cost    Pri  
 Loop2147483647        172.16.6.185    P2P          P-2-P    0       1

```

# Display information about the specified OSPF interface.
```
<HUAWEI> display ospf interface 100GE1/0/1
OSPF Process 1 with Router ID 1.1.1.1
                  Interfaces

 Area: 0.0.0.0               MPLS TE : Disabled
 Interface: 192.168.1.1 ( 100GE1/0/1 ) --> 192.168.1.2
 Cost: 1       State: P-2-P         Type: P2P            MTU: 1500
 Timers: Hello 10 , Dead 40 , Wait 40 , Poll 120 , Retransmit 5 , Transmit Delay 1

```

**Table 1** Description of the **display ospf interface** command output
| Item | Description |
| --- | --- |
| OSPF Process 1 with Router ID 1.1.1.1 | OSPF process ID and router ID. |
| MPLS TE not enabled | MPLS TE is not enabled. |
| MPLS TE | Whether the MPLS TE function is enabled. |
| Interface | Name of an interface. |
| IP Address | IP address allocated to the interface. |
| Type | Interface type, which can be P2P, P2MP, broadcast, or NBMA. |
| State | Status of the interface, which is determined by the OSPF interface state machines:   * Down: The status of the interface is Down. If an interface is Down, the interface is unavailable and cannot be used to transmit traffic. * Loopback: The interface connecting to the network on the router is in the Loopback state. The loopback interface cannot be used to transmit data but can collect interface information through ICMP ping operations or bit error detection. * Waiting: The router is determining the DR and BDR on the network. The DR or BDR election mechanism is not implemented until the waiting period ends. This prevents unnecessary changes in the DR and BDR roles. * P-2-P: The interface is connected to the P2P network or a virtual link. * DROther: The router itself is not elected as the BDR. Instead, another router connecting to the broadcast network or NBMA network is elected as the DR. The router starts to set up adjacency with the DR and BDR (if existing). * BDR: The router functions as the BDR on the network, and will turn into a DR when the current DR fails. The router sets up adjacency with other routers that access the network. * DR: The router functions as the DR on the network. The router sets up adjacency with other routers that access the network. |
| Cost | Cost of the interface. |
| Pri | Priority of an interface during DR and BDR election. The greater the value, the higher the priority. |
| Hello | Interval at which Hello packets are sent, which can be set using the ospf timer hello command. |
| Dead | OSPF neighbor dead interval, which can be set using the ospf timer dead command. |
| Wait | The wait timer on an OSPF interface, which can be set using the ospf timer wait command. |
| Poll | Interval at which poll Hello packets are sent on NBMA networks, which can be set using the ospf timer poll command. |
| Retransmit | Interval at which LSAs are retransmitted, which can be set using the ospf timer retransmit command. |
| Transmit Delay | LSA transmission delay, which can be set using the ospf trans-delay command. |
| Area | ID of the area to which the interface belongs. |
| MTU | MTU value of the interface. |
| Timers | Timers, including:   * Hello: interval at which Hello packets are sent. To set the interval at which Hello packets are sent, run the ospf timer hello command. * Dead: interval of the Dead timer. You can run the ospf timer dead command to set the dead interval of OSPF neighbors. * Wait: interval of the Wait timer. You can run the ospf timer wait command to set the interval of the Wait timer on an OSPF interface. * Poll: interval at which poll Hello packets are sent on an NBMA network. To set the poll interval, run the ospf timer poll command. * Retransmit: interval at which an interface retransmits LSAs, which can be set using the ospf timer retransmit command. * Transmit Delay: indicates the delay for transmitting LSAs on the interface. You can run the ospf trans-delay command to set the delay for transmitting LSAs on the interface. |