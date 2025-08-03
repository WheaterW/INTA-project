priority-group pq
=================

priority-group pq

Function
--------



The **priority-group pq** command configures PQ scheduling for a priority group.



By default, priority-group mode is PQ.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**priority-group** *pg-group-value* **pq**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pg-group-value* | Specifies the value of a priority group. | The value must be 15. |



Views
-----

ETS view of the DCB


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The priority-group pq command configures PQ scheduling for a priority group.

**Precautions**

The scheduling mode of each priority group cannot be changed.


Example
-------

# Configure PQ scheduling for PG15.
```
<HUAWEI> system-view
[~HUAWEI] dcb ets-profile myets
[*HUAWEI-ets-myets] priority-group 15 pq

```