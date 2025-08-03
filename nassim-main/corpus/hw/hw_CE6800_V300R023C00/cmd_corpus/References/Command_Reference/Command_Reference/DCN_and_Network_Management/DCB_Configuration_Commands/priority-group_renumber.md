priority-group renumber
=======================

priority-group renumber

Function
--------



The **priority-group renumber** command redefines the priority group ID.

The **undo priority-group renumber** command cancels the configuration.



By default, the redefined value of each priority group in an ETS profile is the priority group ID.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**priority-group** *pg-id* **renumber** *new-pg-id*

**undo priority-group** *pg-id* **renumber** *new-pg-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pg-id* | Specifies a priority group. | Enumerated type. The values are as follows:   * 0 * 1 * 2 * 3 * 4 * 5 * 6 * 7 * 15 |
| *new-pg-id* | Specifies the priority group ID to be redefined. | The value is 15 or an integer that ranges from 0 to 7. |



Views
-----

ETS view of the DCB


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the device connects to a non-Huawei device, the negotiation may fail because the priority group ID is different in the ETS profile. You can run this command to redefine the priority group ID.

**Precautions**

The redefined priority group ID must be unique.


Example
-------

# Redefine PG1 into PG2.
```
<HUAWEI> system-view
[~HUAWEI] dcb ets-profile myets
[*HUAWEI-ets-myets] priority-group 1 renumber 2

```