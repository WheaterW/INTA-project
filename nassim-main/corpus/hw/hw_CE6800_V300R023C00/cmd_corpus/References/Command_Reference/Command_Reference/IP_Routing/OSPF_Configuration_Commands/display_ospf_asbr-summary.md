display ospf asbr-summary
=========================

display ospf asbr-summary

Function
--------



The **display ospf asbr-summary** command displays information about OSPF route summarization.




Format
------

**display ospf** [ *process-id* ] **asbr-summary** [ *ip-address* *mask* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | process-id Specifies the ID of an OSPF process. | The value is an integer that ranges from 1 to 4294967295. |
| *ip-address* | Specifies the IP address.  If no IP address is specified, summarization information of all imported routes is displayed. | The value is in dotted decimal notation. |
| *mask* | Specifies the address mask for matching.  If an IP address is specified, a mask must be specified. | The value is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Route summarization reduces the amount of routing information transmitted between areas and the routing table size and improves routing performance.After route summarization is configured using the **asbr-summary** command, you can run the **display ospf asbr-summary** command to view the route summarization information, which facilitates troubleshooting.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about OSPF route summarization.
```
<HUAWEI> display ospf asbr-summary
OSPF Process 1 with Router ID 192.168.1.2
 Total summary address count: 1

 net         : 10.0.0.0
 mask        : 255.0.0.0
 tag         : 10
 status      : Advertise
 Cost        : 0 (Not Configured)
 Delay       : 30 (Configured)
 Number of routes : 2
 Destination     Net Mask        Proto      Process   Type     Metric

 10.1.0.0        255.255.0.0     Static     1         2        10
 10.2.0.0        255.255.0.0     Static     1         2        10

```

**Table 1** Description of the **display ospf asbr-summary** command output
| Item | Description |
| --- | --- |
| Process | Process ID. |
| Total summary address count | Number of routes that are summarized using the asbr-summary command. |
| net | Network address of the summarized route. |
| tag | Tag of the summarized route. |
| status | Advertisement status of the summarized route:   * Advertise: indicates that the summarized route is advertised. * DoNotAdvertise: indicates that the summarized route is not advertised. |
| Cost | Cost of the summarized route. |
| Delay | Delay for advertising a summary route. |
| Number of routes | Number of summarized routes. |
| Destination | Destination address of the routes that are summarized. |
| Net Mask | Mask of the routes that are summarized. |
| Mask | Network mask of the summarized route. |
| Proto | Protocol of the routes that are summarized. |
| Type | Type of the imported AS external route, Type 1 or Type 2. |
| Metric | Cost of the routes that are summarized. |