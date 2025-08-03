priority-group queue
====================

priority-group queue

Function
--------



The **priority-group queue** command adds an interface queue to a priority group.

The **undo priority-group queue** command deletes an interface queue from a priority group.



By default, queues 0, 1, 2, 4, and 5 belong to PG0, queue 3 belongs to PG1, and queues 6 and 7 belong to PG15.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**priority-group** *pg-group-value* **queue** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-8>

**undo priority-group** *pg-group-value* **queue** [ *start-queue-index* [ **to** *end-queue-index* ] ] &<0-8>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pg-group-value* | Specifies the value of a priority group. | Enumerated type. The values are as follows:   * 0:PG0 * 1:PG1 * 2:PG2 * 3:PG3 * 4:PG4 * 5:PG5 * 6:PG6 * 7:PG7 * 15:PG15 |
| *start-queue-index* | Specifies queue-start value. | The value is an integer that ranges from 0 to 7. |
| **to** *end-queue-index* | Specifies queue-end value.  end-queue-index must be larger than or equal to start-queue-index. start-queue-index and end-queue-index determine a range of queues. If to end-queue-index is not specified, the queue specified by start-queue-index joins a priority group. | The value is an integer that ranges from 0 to 7. |



Views
-----

ETS view of the DCB


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

ETS provides CoSs based on priority groups. A priority group is a group of queues with the same attributes on an interface. You can run the **priority-group queue** command to add queues with different priorities to a priority group.Queues in the same priority group share the same CoS such as low latency and lossless packets.

**Prerequisites**

Run the **priority-group** command to create a priority group.

**Precautions**

A queue can join only one priority group.If you run the **undo priority-group queue** command without any parameter specified, the default setting of queues is restored.


Example
-------

# Add queues 5, 6, and 7 to PG1.
```
<HUAWEI> system-view
[~HUAWEI] dcb ets-profile myets
[*HUAWEI-ets-myets] priority-group 1 queue 5 to 7

```