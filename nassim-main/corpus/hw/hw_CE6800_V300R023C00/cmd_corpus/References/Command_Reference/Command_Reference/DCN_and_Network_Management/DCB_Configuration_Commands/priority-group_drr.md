priority-group drr
==================

priority-group drr

Function
--------



The **priority-group drr** command sets the Deficit Round Robin (DRR) weight for a priority group.

The **undo priority-group drr** command restores the default DRR weight for a priority group.



For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM, the DRR weights of PG0 and PG1 are both 50 by default.

For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ, by default, the scheduling mode of the CIR token bucket based on PG0 and PG1 is PQ, and the scheduling mode of the EIR token bucket based on PG0 and PG1 is DRR with the weight being 50.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**priority-group** *pg-group-value* **drr** **weight** *weight-value*

**undo priority-group** *pg-group-value* **drr** **weight** *weight-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pg-group-value* | Specifies the value of a priority group. | Enumerated type. The values are as follows:   * 0:PG0 * 1:PG1 * 2:PG2 * 3:PG3 * 4:PG4 * 5:PG5 * 6:PG6 * 7:PG7 |
| **weight** *weight-value* | Specifies the DRR weight of a queue or some queues participating in DRR scheduling. | The value is an integer that ranges from 1 to 100. |



Views
-----

ETS view of the DCB


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In ETS, priority groups except PG15 use DRR scheduling. You can run the priority-group drr command to set the DRR weight for each priority group so that the system schedules each priority group based on weights in turn.In DRR scheduling, the weight indicates the percentage of resources that a queue can obtain. You can configure the DRR weight according to the actual networking.

**Prerequisites**

Run the **priority-group** command to create a priority group.

**Precautions**



For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ:The default scheduling mode of the CIR token bucket based on priority groups is PQ and the rate is not limited by default. The priority groupâbased scheduling mode configured for the CIR token bucket does not take effect. The configured scheduling mode and the default configuration of PG0 and PG1 using DRR scheduling with their respective weight being 50 take effect only for the EIR (EIR = PIR â CIR) token bucket.




Example
-------

# Set the DRR weight of PG1 to 80.
```
<HUAWEI> system-view
[~HUAWEI] dcb ets-profile myets
[*HUAWEI-ets-myets] priority-group 1 drr weight 80

```