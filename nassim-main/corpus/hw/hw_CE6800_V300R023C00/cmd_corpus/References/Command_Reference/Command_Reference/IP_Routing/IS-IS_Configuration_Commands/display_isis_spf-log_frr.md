display isis spf-log frr
========================

display isis spf-log frr

Function
--------



The **display isis spf-log frr** command displays the SPF calculation log of IS-IS.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display isis spf-log** [ *process-id* ] **frr** [ **ipv6** | [ **level-1** | **level-2** ] ] \*

For CE6885-LL (low latency mode):

**display isis spf-log** [ *process-id* ] **frr** [ **level-1** | **level-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |
| **frr** | Indicates the FRR calculation log. | - |
| **ipv6** | Indicates the SPF calculation log in the IPv6 topology.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **level-1** | Indicates the SPF calculation log in a Level-1 area. | - |
| **level-2** | Indicates the SPF calculation log in a Level-2 area. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When an error occurs in the IS-IS SPF calculation, run the **display isis spf-log** command to diagnose the fault. The command can be used to view the SPF calculation log of IS-IS, such as the start time, duration, number of nodes, and events that trigger the SPF calculation. You can check which event causes the error of the SPF calculation by the start time.Check the StartTime field first. If the SPF calculation is performed repeatedly at short intervals, flapping may have occurred. Then check the Last Trigger LSP and Trigger Event fields for further analysis.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the FRR calculation log.
```
<HUAWEI> display isis spf-log frr

                        SPF Log information for ISIS(1)
                        -------------------------------

                            ISIS(1) Level-1 FRR Log
                            -----------------------

 StartTime  Duration  Nodes  Count  Last Trigger LSP      Trigger Event        
-------------------------------------------------------------------------------
2019-08-10  0         1      1      NULL                  L1_IFRR_CIRC_METRIC_C
08:28:14.99                                               HANGE                
6                                                                              
2019-08-10  1         1      1      NULL                  L1_IFRR_CIRC_METRIC_C
08:12:34.75                                               HANGE                
7

```

**Table 1** Description of the **display isis spf-log frr** command output
| Item | Description |
| --- | --- |
| StartTime | Start time for SPF calculation. |
| Duration | Time taken for SPF calculation, the value rounds down the actual duration, in milliseconds. In most cases, the value is less than 1 ms. Therefore, it is displayed as 0. |
| Nodes | Number of nodes calculated by SPF. |
| Count | Number of events triggering the SPF calculation. |
| Last Trigger LSP | LSP that triggers the last SPF calculation. |
| Trigger Event | Event that triggers the last SPF calculation. |