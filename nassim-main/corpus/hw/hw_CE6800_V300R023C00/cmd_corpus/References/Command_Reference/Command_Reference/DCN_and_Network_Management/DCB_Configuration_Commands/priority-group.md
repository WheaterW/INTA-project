priority-group
==============

priority-group

Function
--------



The **priority-group** command creates a priority group.

The **undo priority-group** command deletes a priority group.



By default, an ETS profile defines three priority groups: PG0, PG1, and PG15.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**priority-group** *pg-group-value*

**undo priority-group** *pg-group-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pg-group-value* | Specifies the value of a priority group. | Enumerated type. The values are as follows:   * 0:PG0 * 1:PG1 * 2:PG2 * 3:PG3 * 4:PG4 * 5:PG5 * 6:PG6 * 7:PG7 * 15:PG15 |



Views
-----

ETS view of the DCB


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

ETS provides CoSs based on the priority group. A priority group is a group of queues with the same interface priority. You can run the priority-group command to create a priority group. Queues in the same priority group share the same CoS such as the low latency and no packet loss.

**Precautions**

An ETS profile can define a maximum of eight priority groups.The default priority groups PG0, PG1, and PG15 cannot be deleted.When you run the **undo priority-group pg-value** command to delete a priority group, the default setting of queues in the priority group is restored.


Example
-------

# Create PG5.
```
<HUAWEI> system-view
[~HUAWEI] dcb ets-profile myets
[*HUAWEI-ets-myets] priority-group 5

```