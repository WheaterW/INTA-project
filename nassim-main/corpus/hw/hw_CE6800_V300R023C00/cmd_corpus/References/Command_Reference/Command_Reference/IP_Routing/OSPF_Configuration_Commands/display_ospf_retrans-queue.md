display ospf retrans-queue
==========================

display ospf retrans-queue

Function
--------



The **display ospf retrans-queue** command displays the OSPF retransmission list.




Format
------

**display ospf** [ *process-id* ] **retrans-queue** [ *InterfaceName* | *interfaceType* *interfaceNum* ] [ *neighbor-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |
| *InterfaceName* | Specifies the name of an interface. | - |
| *interfaceType* | Specifies the type of an interface. | - |
| *interfaceNum* | Specifies the interface number. | - |
| *neighbor-id* | The router ID of a neighbor. | The value is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view OSPF statistics, run the display ospf cumulative command. The command output can help you troubleshoot OSPF faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the OSPF retransmission list.
```
<HUAWEI> display ospf retrans-queue
OSPF Process 1 with Router ID 10.1.1.1
                  OSPF Retransmit List
 Area 0.0.0.0 interface 10.10.1.1 (100GE1/0/1)'s neighbors
  Retransmit list:
  Neighbor ID: 10.1.1.2
 Type             LinkState ID      AdvRouter         Sequence   Age
 1                10.1.1.1         10.1.1.1          8000000b     4
 5                10.1.1.0         10.1.1.1          80000001     4
 5                10.1.2.0         10.1.1.1          80000001     4
 5                10.1.3.0         10.1.1.1          80000001     4
 5                10.1.4.0         10.1.1.1          80000001     4
 5                10.1.5.0         10.1.1.1          80000001     4
 5                10.1.6.0         10.1.1.1          80000001     4
 5                10.1.7.0         10.1.1.1          80000001     4
 5                10.1.8.0         10.1.1.1          80000001     4
 5                10.1.9.0         10.1.1.1          80000001     4
 5                10.1.10.0        10.1.1.1          80000001     4

```

**Table 1** Description of the **display ospf retrans-queue** command output
| Item | Description |
| --- | --- |
| Router ID | Router ID of the current route. |
| Retransmit list | Retransmission list. |
| Area | Area ID. |
| interface | IP address of the interface. |
| Neighbor ID | Neighbor ID. |
| Type | LSA type. |
| LinkState ID | Link state ID in the LSA header. |
| AdvRouter | Advertising router in the LSA header. |
| Sequence | Sequence number in the LSA header. |
| Age | Aging time in the LSA header. |