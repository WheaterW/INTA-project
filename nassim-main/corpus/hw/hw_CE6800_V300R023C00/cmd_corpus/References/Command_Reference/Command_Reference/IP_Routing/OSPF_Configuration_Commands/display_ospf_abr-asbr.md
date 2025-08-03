display ospf abr-asbr
=====================

display ospf abr-asbr

Function
--------



The **display ospf abr-asbr** command displays information about the ABRs and ASBRs of OSPF.




Format
------

**display ospf** [ *process-id* ] **abr-asbr** [ *router-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | process-id Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |
| *router-id* | Specifies the router ID of an ABR or ASBR. | Dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

An ABR can belong to two or more areas, and one of the areas must be a backbone area. An ABR is used to connect the backbone area and non-backbone areas. It can be physically or logically connected to the backbone area.An ASBR exchanges routing information with other ASs. An ASBR may not reside at the boundary of an AS. It can be an internal router or an ABR. If an OSPF device imports external routes, the router is an ASBR.To view information about the ABRs and ASBRs of OSPF, run the display ospf abr-asbr command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the ABRs and ASBRs of OSPF.
```
<HUAWEI> display ospf abr-asbr
OSPF Process 1 with Router ID 10.1.1.1
                  Routing Table to ABR and ASBR

 Type        Destination     Area            Cost       NextHop         RtType  
 INTRA-AREA  10.1.1.2        0.0.0.1         1          10.3.1.2        ABR/ASBR

```

**Table 1** Description of the **display ospf abr-asbr** command output
| Item | Description |
| --- | --- |
| Type | Intra-area or inter-area router. |
| Destination | IP address of the ABR or ASBR. |
| Area | Area ID. |
| Cost | Cost of the route from the local router to the ABR or ASBR. |
| NextHop | IP address of the next hop through which packets are transmitted to the ABR or ASBR. |
| RtType | ABR or ASBR. |