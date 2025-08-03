display ospf topology
=====================

display ospf topology

Function
--------



The **display ospf topology** command displays information about the topology based on which OSPF routes are calculated.




Format
------

**display ospf** [ *process-id* ] **topology** [ **area** { *area-id* | *area-ipv4* } ] [ **statistics** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |
| **area** *area-id* | Specifies the ID of an OSPF area. | The value is an integer ranging from 0 to 4294967295. |
| *area-ipv4* | Specifies the ID of an OSPF area in IP address format. | The value is in the format of an IPv4 address. |
| **statistics** | Displays statistics about the topology based on which OSPF routes are calculated. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view information about the topology based on which OSPF routes are calculated, including the cause of route calculation, and the number of changed routes, run the **display ospf topology** command. The command output helps you diagnose OSPF route flapping.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the topology based on which OSPF routes are calculated.
```
<HUAWEI> display ospf topology
OSPF Process 1 with Router ID 10.9.9.9
 Bits :
 B - ABR    E - ASBR    V - VIRTUAL    NT - NSSA translator

 OSPF Area 0.0.0.0 topology
 Type  ID            Bits    Metric    Next-Hop        Interface
 Rtr   10.8.8.8      B       1         10.11.11.1      100GE1/0/8.1
 Rtr   10.9.9.9      E       1         -               -
 Net   10.11.11.1    B       1         10.11.11.2      100GE1/0/8.1

```

**Table 1** Description of the **display ospf topology** command output
| Item | Description |
| --- | --- |
| ID | Route advertiser. |
| Bits | Device type. |
| B - ABR | Area border router. |
| E - ASBR | Autonomous system boundary router. |
| V - VIRTUAL | Virtual link device. |
| NT - NSSA translator | ABR in an NSSA that translates LSAs. |
| Type | LSA type. |
| Metric | Cost of the route. |
| Next-Hop | Router ID of the next hop. |
| Interface | Interface of the next hop. |