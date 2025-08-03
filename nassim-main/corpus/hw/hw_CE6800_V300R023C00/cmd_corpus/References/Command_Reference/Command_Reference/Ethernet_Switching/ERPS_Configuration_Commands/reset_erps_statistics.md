reset erps statistics
=====================

reset erps statistics

Function
--------



The **reset erps statistics** command clears packet statistics in an ERPS ring.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**reset erps** [ **ring** *ring-id* ] **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ring** *ring-id* | Clears packet statistics in a specific ERPS ring. | The value is an integer ranging from 1 to 255. |



Views
-----

All views


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Before traffic statistics on a specific interface within a certain period is collected, the existing traffic statistics of this interface needs to be cleared. Running the reset erps statistics command ensures that existing packet statistics in the ERPS ring can be cleared.


Example
-------

# Clear packet statistics in ERPS ring 2.
```
<HUAWEI> reset erps ring 2 statistics

```