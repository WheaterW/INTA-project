display dcb pfc
===============

display dcb pfc

Function
--------



The **display dcb pfc** command displays PFC statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dcb pfc** [ **interface** { *interface-name* | *interface-type* *interface-num* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** | Indicates an interface. | - |
| *interface-name* | Specifies an interface name. | - |
| *interface-type* | Specifies an interface type. | - |
| *interface-num* | Specifies an interface number. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

When diagnosing and locating PFC faults, you need to obtain PFC statistics in a specified period.Before recalculating PFC statistics, run the **reset dcb pfc** command to clear existing PFC statistics and then run the **display dcb pfc** command to view the PFC statistics.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on PFC frames on 100GE1/0/1.
```
<HUAWEI> display dcb pfc interface 100ge 1/0/1
-----------------------------------------------------------------------------------------
Interface         Queue         Received(Frames)        ReceivedRate(pps)     DeadlockNum
                             Transmitted(Frames)     TransmittedRate(pps)     RecoveryNum
-----------------------------------------------------------------------------------------
100GE1/0/1             5                       0                        0               0
                                               0                        0               0
-----------------------------------------------------------------------------------------

```

**Table 1** Description of the **display dcb pfc** command output
| Item | Description |
| --- | --- |
| Interface | Name of the interface where statistics on PFC frames need to be checked. |
| Queue | Priority queue. |
| Received(Frames) | Number of PFC frames received in a queue. |
| ReceivedRate(pps) | Rate of PFC frames received in a queue. |
| DeadlockNum | Number of detected PFC deadlocks. |
| Transmitted(Frames) | Number of PFC frames sent from a queue. |
| TransmittedRate(pps) | Rate of PFC frames sent from a queue. |
| RecoveryNum | Number of recovery times after PFC deadlocks occur. |