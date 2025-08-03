display ospf topology verbose
=============================

display ospf topology verbose

Function
--------



The **display ospf topology verbose** command displays the SPF tree information depending on process and area for OSPFv2.




Format
------

**display ospf** [ *process-id* ] **topology** [ **area** { *area-id* | *area-ipv4* } ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |
| **area** *area-id* | Specifies the ID of an OSPF area. | The value is an integer ranging from 0 to 4294967295. |
| *area-ipv4* | Specifies the ID of an OSPF area in IP address format. | The value is in the format of an IPv4 address. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The **display ospf topology** command displays topology information about route calculation in an OSPF process, including the time when route calculation occurs, causes, and number of changed routes. To check the cause of OSPF route flapping, you can run this command to obtain information about OSPF route calculation and diagnose OSPF route flapping based on the information.

**Prerequisites**



To view information about the topology based on which OSPF routes are calculated, including the time when route calculation is performed, cause of route calculation, and the number of changed routes, run the **display ospf topology** command. The command output helps you diagnose OSPF route flapping.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the topology based on which OSPF routes are calculated.
```
<HUAWEI> display ospf topology verbose

          OSPF Process 1 with Router ID 1.1.1.1
Bits :
B - ABR    E - ASBR    V - VIRTUAL    NT - NSSA translator

Shortest Path Tree for Area: 0.0.0.0

Node: Router    1.1.1.1    Cost: 0 Cost(tunnel): 0
    BitFlags : B
    Neighbors: 1 (Children:(1) Parents:(0))
    Neighbor List:
        router  6.6.6.6, Child, cost: 100

```

**Table 1** Description of the **display ospf topology verbose** command output
| Item | Description |
| --- | --- |
| Bits | Device type. |
| B - ABR | Area border router. |
| E - ASBR | Autonomous system boundary router. |
| V - VIRTUAL | Virtual link device. |
| NT - NSSA translator | ABR in an NSSA that translates LSAs. |
| Shortest Path Tree for Area | Display detailed information about the topology based on which OSPF routes are calculated in a specified area. |
| BitFlags | Device type. |
| Neighbor List | Neighbor router ID list. |
| cost | Cost of the route. |
| Neighbors | Neighbor quantity. |
| Node | Node Type. |