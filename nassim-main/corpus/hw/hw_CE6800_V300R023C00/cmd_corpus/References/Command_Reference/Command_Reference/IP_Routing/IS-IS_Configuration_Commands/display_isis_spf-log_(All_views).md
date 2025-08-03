display isis spf-log (All views)
================================

display isis spf-log (All views)

Function
--------



The **display isis spf-log** command displays the SPF and PRC calculation log of IS-IS.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display isis spf-log** [ *process-id* ] **spf** [ **ipv6** | [ **level-1** | **level-2** ] ] \*

**display isis spf-log** [ *process-id* ] **prc** [ **ipv6** ] \*

For CE6885-LL (low latency mode):

**display isis spf-log** [ *process-id* ] **spf** [ **level-1** | **level-2** ]

**display isis spf-log** [ *process-id* ] **prc**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |
| **spf** | Indicates the SPF calculation log. | - |
| **ipv6** | Indicates the SPF calculation log in the IPv6 topology.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **level-1** | Indicates the SPF calculation log in a Level-1 area. | - |
| **level-2** | Indicates the SPF calculation log in a Level-2 area. | - |
| **prc** | Indicates the PRC calculation log. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When an error occurs in the IS-IS SPF or PRC calculation, run the **display isis spf-log** command to diagnose the fault. The command can be used to view the SPF calculation log of IS-IS, such as the start time, duration, number of nodes, and events that trigger the SPF calculation. You can check which event causes the error of the SPF or PRC calculation by the start time.Check the StartTime field first. If the SPF or PRC calculation is performed repeatedly at short intervals, flapping may have occurred. Then check the Last Trigger LSP and Trigger Event fields for further analysis.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the PRC calculation log.
```
<HUAWEI> display isis spf-log prc

                        SPF Log information for ISIS(1)
                        -------------------------------

                            ISIS(1) PRC Log
                            -----------------------

 StartTime  Duration  Routes Count  Last Trigger LSP      Trigger Event        
-------------------------------------------------------------------------------
2019-08-10  0         2      3      NULL                  ICRM_SC_FULL_CALC    
08:28:31.50                                                                    
8                                                                              
2019-08-10  0         1      1      NULL                  ICRM_SC_PREFIX       
08:26:34.59                                                                    
6                                                                              
2019-08-10  0         1      1      NULL                  ICRM_SC_PREFIX       
08:25:36.80                                                                    
2                                                                              
2019-08-10  1         1      1      NULL                  ICRM_SC_PREFIX       
08:25:09.35                                                                    
1                                                                              
2019-08-10  0         1      1      NULL                  ICRM_SC_PREFIX       
08:13:53.47                                                                    
8                                                                              
2019-08-10  0         0      2      NULL                  ICRM_SC_FRR_NODE     
08:13:14.04                                                                    
3                                                                              
2019-08-10  1         2      3      NULL                  ICRM_SC_FULL_CALC    
08:13:12.25                                                                    
1                                                                              
2019-08-10  0         1      1      NULL                  ICRM_SC_PREFIX       
08:05:21.39                                                                    
8                                                                              
2019-08-10  0         2      2      NULL                  ICRM_SC_PREFIX       
07:25:05.55                                                                    
7                                                                              
2019-08-10  0         0      1      NULL                  ICRM_SC_AREA         
07:22:54.02                                                                    
7                                                                              
2019-08-10  0         1      1      NULL                  ICRM_SC_PREFIX       
02:19:58.36                                                                    
2                                                                              
2019-08-10  0         0      2      NULL                  ICRM_SC_STALE_SPT    
02:09:04.94                                                                    
6                                                                              
2019-08-10  0         0      3      NULL                  ICRM_SC_AREA         
02:09:03.91                                                                    
0

```

# Display the SPF calculation log in a Level-1 area.
```
<HUAWEI> display isis spf-log spf level-1

                        SPF Log information for ISIS(1)
                        -------------------------------

                            ISIS(1) Level-1 SPF Log
                            -----------------------

 StartTime  Duration  Nodes  Count  Last Trigger LSP      Trigger Event        
-------------------------------------------------------------------------------
2019-08-10  0         2      3      NULL                  L1_ISPT_ADJ_NEXTHOP_C
07:52:52.51                                               HANGE                
5

```

**Table 1** Description of the **display isis spf-log (All views)** command output
| Item | Description |
| --- | --- |
| StartTime | Start time for SPF calculation. |
| Duration | Time taken for SPF calculation, the value rounds down the actual duration, in milliseconds. In most cases, the value is less than 1 ms. Therefore, it is displayed as 0. |
| Count | Number of events triggering the SPF calculation. |
| Last Trigger LSP | LSP that triggers the last SPF calculation. |
| Trigger Event | Event that triggers the last SPF calculation. |
| Nodes | Number of nodes calculated by SPF. |