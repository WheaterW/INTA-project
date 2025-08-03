reset hwtacacs-server statistics
================================

reset hwtacacs-server statistics

Function
--------



The **reset hwtacacs-server statistics** command clears the statistics on HWTACACS authentication, accounting, and authorization.




Format
------

**reset hwtacacs-server statistics** { **accounting** | **all** | **authentication** | **authorization** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **accounting** | Clears the statistics on HWTACACS accounting. | - |
| **all** | Clears all the statistics. | - |
| **authentication** | Clears the statistics on HWTACACS authentication. | - |
| **authorization** | Clears the statistics on HWTACACS authorization. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If statistics about HWTACACS authentication, accounting, and authorization need to be collected in a specified period of time, clear the original statistics first and then run the **display hwtacacs-server template verbose** command to view statistics on HWTACACS authentication, accounting, and authorization.

**Precautions**

* After the **reset hwtacacs-server statistics** command is run, all the statistics about HWTACACS authentication, accounting, and authorization is cleared. In addition, the statistics cannot be restored once being cleared. Therefore, exercise caution when you decide to run this command.- You can run the **display hwtacacs-server template verbose** command to check statistics about HWTACACS authentication, accounting, and authorization in the specified server template.

Example
-------

# Clear all the statistics.
```
<HUAWEI> reset hwtacacs-server statistics all

```