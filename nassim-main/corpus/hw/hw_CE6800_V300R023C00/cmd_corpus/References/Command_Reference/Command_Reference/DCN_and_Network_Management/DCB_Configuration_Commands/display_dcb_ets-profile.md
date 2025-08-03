display dcb ets-profile
=======================

display dcb ets-profile

Function
--------



The **display dcb ets-profile** command displays the ETS profile configuration.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dcb ets-profile** [ *name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *name* | Displays the configuration of a specified ETS profile.  If this parameter is not specified, the configurations of all ETS profiles are displayed. | The ETS profile must have been created. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After configuring an ETS profile, you can run the display eTS-profile command to view the ETS profile configuration.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about all ETS profiles.
```
<HUAWEI> display dcb ets-profile
Q:Queue    SCH:Schedule    RN:Renumber                                          
ETS Maximum: 8                                                                  
Total: 1                                                                        
ETS Profile: default                                                            
------------------------------------------------------------------------------- 
PG(RN)  Q  SCH    Weight              CIR/PIR(kbps)            CBS/PBS(kbytes)  
------------------------------------------------------------------------------- 
 0(0)   -  DRR    50(50)                -/-                      -/-            
        0  PQ          -                -/-                      -/-            
        1  PQ          -                -/-                      -/-            
        2  PQ          -                -/-                      -/-            
        4  PQ          -                -/-                      -/-            
        5  PQ          -                -/-                      -/-            
 1(1)   -  DRR    50(50)                -/-                      -/-            
        3  PQ          -                -/-                      -/-            
15(15)  -  PQ          -                -/-                      -/-            
        6  PQ          -                -/-                      -/-            
        7  PQ          -                -/-                      -/-            
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display dcb ets-profile** command output
| Item | Description |
| --- | --- |
| ETS Maximum | Maximum number of ETS profiles can be configured. |
| ETS Profile | ETS profile name. |
| PG(RN) | Priority group (redefined group ID). |
| Q | Queue. |
| SCH | Scheduling mode of a queue or priority group:   * DRR: indicates that the scheduling mode is DRR. * PQ: indicates that the scheduling mode is PQ. * LPQ: indicates that the scheduling mode is LPQ.   The scheduling modes of priority groups are fixed. Specifically, the scheduling modes of PG0 and PG1 are fixed as DRR, and the scheduling mode of PG15 is fixed as PQ. The scheduling modes of queues can be configured using the queue { pq | lpq | drr } command. |
| Weight | DRR weight of a queue or priority group.  To set the DRR weight for a priority group, run the priority-group drr command. To set the DRR weight for a queue, run the queue { pq | drr } command.  Assume that A is the configured value, the sum of configured values of priority groups can exceed 100, B is the actual value after calculation, and the sum of actual values of priority groups is 100. During scheduling, B is used. |
| CIR/PIR(kbps) | CIR and PIR of a queue or priority group.  To set traffic shaping parameters for a queue, run the queue shaping command. To set traffic shaping parameters for a priority group, run the priority-group shaping command. |
| CBS/PBS(kbytes) | CBS and PBS of a queue or priority group.  To set traffic shaping parameters for a queue, run the queue shaping command. To set traffic shaping parameters for a priority group, run the priority-group shaping command. |
| Total | Total number of ETS profiles. |