reset gtsm statistics
=====================

reset gtsm statistics

Function
--------



The **reset gtsm statistics** command clears the GTSM statistics on a slot.




Format
------

**reset gtsm statistics** { *slot-id* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *slot-id* | Specifies a slot ID. | - |
| **all** | Clears the GTSM statistics on all slots. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Before collecting the GTSM statistics on a slot within a certain period, you need to clear the existing statistics.




Example
-------

# Clear the GTSM statistics on all boards.
```
<HUAWEI> reset gtsm statistics all

```