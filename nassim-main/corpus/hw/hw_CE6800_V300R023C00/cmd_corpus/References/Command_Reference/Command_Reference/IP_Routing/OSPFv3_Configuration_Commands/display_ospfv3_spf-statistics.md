display ospfv3 spf-statistics
=============================

display ospfv3 spf-statistics

Function
--------



The **display ospfv3 spf-statistics** command displays OSPFv3 route calculation statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **spf-statistics** [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an OSPFv3 process ID. | The value is an integer that ranges from 1 to 4294967295. |
| **verbose** | Displays the detailed statistics. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display ospfv3 spf-statistics** command displays OSPFv3 route calculation statistics, which includes the time and cause of the route calculation and the number of changed routes. The command output helps you troubleshoot OSPFv3 faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the OSPFv3 SPF statistics.
```
<HUAWEI> display ospfv3 1 spf-statistics
OSPFv3 Process 1 with Router ID 5.5.5.5
Routing table change statistics:
      Date          Time         Intra        Inter        External     Reason
    2011-06-14    11:06:08     0            0            0            LSA     
    2011-06-14    11:06:08     0            0            0            LSA   
    2011-06-14    11:06:08     0            0            0            LSA   
    2011-06-14    11:06:08     0            0            0            LSA   
    2011-06-14    11:06:08     0            0            0            LSA   
    2011-06-14    11:06:09     0            0            0            LSA

```

**Table 1** Description of the **display ospfv3 spf-statistics** command output
| Item | Description |
| --- | --- |
| Routing table change statistics | Statistics about routing table changes. |
| Date | Date when route calculation occurs. |
| Time | Time when the route calculation was triggered. |
| Intra | Intra-area route. |
| Inter | Number of inter-area routes in the routing table which are changed because of route calculation. |
| External | External route. |
| Reason | Trigger reason:   * Other: The route calculation is triggered by a cause that is neither a topology change nor an LSA change. * Topo: The route calculation is triggered by a topology change. * LSA: The route calculation is triggered by an LSA change. |