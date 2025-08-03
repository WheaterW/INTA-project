display ospf request-queue
==========================

display ospf request-queue

Function
--------



The **display ospf request-queue** command displays the OSPF request list.




Format
------

**display ospf** [ *process-id* ] **request-queue** [ *InterfaceName* | *interfaceType* *interfaceNum* ] [ *neighbor-id* ]


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


# Display the OSPF request list.
```
<HUAWEI> display ospf request-queue
OSPF Process 1 with Router ID 1.1.1.1
OSPF Request List
The Router's Neighbor is Router ID 4.4.4.4         Address 10.1.4.2
Interface 10.1.4.1        Area 0.0.0.2
Request list:
Type       LinkState ID      AdvRouter         Sequence   Age
Router     1.1.1.1           1.1.1.1           8000001b   677

```

**Table 1** Description of the **display ospf request-queue** command output
| Item | Description |
| --- | --- |
| Router ID | Router ID of the current route. |
| Request list | Request list. |
| The Router's Neighbor is Router ID | Router ID of the neighbor. |
| Address | IP address of the neighboring interface. |
| Interface | IP address of an interface. |
| Area | Area to which the local router belongs. |
| Type | LSA type:  Router LSA, network LSA, network summary LSA, ASBR summary LSA, AS external LSA, or opaque LSA. |
| LinkState ID | Link state ID in the LSA header. |
| AdvRouter | Advertising router in the LSA header. |
| Sequence | Sequence number in the LSA header. |
| Age | Aging time in the LSA header. |