reset bridge-domain statistics
==============================

reset bridge-domain statistics

Function
--------



The **reset bridge-domain statistics** command clears traffic statistics of a BD.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset bridge-domain** *bd-id* **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *bd-id* | Specifies the ID of a bridge domain. | The value is an integer  ranging from 1 to 16777215. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before you collect traffic statistics within a specified period for a BD, run the **reset bridge-domain statistics** command to clear existing statistics so that traffic statistics can be collected again, ensuring that the statistics are correct.

**Prerequisites**

A bridge domain has been created using the **bridge-domain** command.

**Precautions**



Traffic statistics of a BD are cleared and cannot be restored. Exercise caution when running the **reset bridge-domain statistics** command.




Example
-------

# Clear packet statistics in bridge domain 10.
```
<HUAWEI> reset bridge-domain 10 statistics

```