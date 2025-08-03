display ospfv3 statistics maxage-lsa
====================================

display ospfv3 statistics maxage-lsa

Function
--------



The **display ospfv3 statistics maxage-lsa** command displays information about MaxAge Router-LSAs.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **statistics** **maxage-lsa**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPFv3 process.  If no process ID is specified, information about MaxAge Router-LSAs in all OSPFv3 processes is displayed. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To query information about MaxAge Router-LSAs, run the **display ospfv3 statistics maxage-lsa** command. The command output helps troubleshooting route flapping.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about MaxAge Router-LSAs.
```
<HUAWEI> display ospfv3 statistics maxage-lsa

          OSPFV3 Process 1 with Router ID 1.1.1.1
                  Statistics of Router-LSAs
          ---------------------------------------------------

                          Area: 0.0.0.0
LinkState ID           MaxAge count        Last Five MaxAge Times
------------------------------------------------------------------
1.1.1.1                           1           2020-07-16 11:57:53

```

**Table 1** Description of the **display ospfv3 statistics maxage-lsa** command output
| Item | Description |
| --- | --- |
| LinkState ID | Link state ID in the LSA header. |
| MaxAge count | Number of times a Router-LSA reached the maximum aging time. |
| Last Five MaxAge Times | Time when a Router-LSA last reached the maximum aging time. |
| Area | OSPFv3 area. |