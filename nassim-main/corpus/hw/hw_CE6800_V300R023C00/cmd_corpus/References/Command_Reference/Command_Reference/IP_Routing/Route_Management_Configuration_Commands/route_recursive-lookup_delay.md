route recursive-lookup delay
============================

route recursive-lookup delay

Function
--------



The **route recursive-lookup delay disable** command disables route or tunnel recursion suppression in case of flapping.

The **undo route recursive-lookup delay disable** command restores the default configuration.

The **route recursive-lookup delay** command configures suppression periods for route or tunnel recursion, including the initial suppression period, incremental suppression period since the second suppression, and the maximum suppression period.

The **undo route recursive-lookup delay** command restores the default configuration.



By default, route or tunnel recursion suppression in case of flapping is enabled. The initial suppression period, incremental suppression period since the second suppression, and the maximum suppression period are 500 ms, 1000 ms, and 30000 ms, respectively.


Format
------

**route recursive-lookup delay disable**

**route recursive-lookup delay start-time** *start-time* **increase-time** *increase-time* **max-time** *max-time*

**undo route recursive-lookup delay disable**

**undo route recursive-lookup delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **start-time** *start-time* | Specifies the initial suppression period for route or tunnel recursion suppression. | The value is an integer ranging from 500 to 2000, in ms. |
| **increase-time** *increase-time* | Specifies the incremental suppression period since the second route or tunnel recursion suppression. | The value is an integer ranging from 1000 to 5000, in ms. |
| **max-time** *max-time* | Specifies the maximum suppression period for route or tunnel recursion suppression. | The value is an integer ranging from 5000 to 60000, in ms. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In route or tunnel recursion scenarios, if a route or tunnel flaps frequently, services that depend on the route or tunnel perform recursion frequently, causing frequent route updates. As a result, the CPU usage of the system keeps increasing. To solve the problem, enable route or tunnel recursion suppression in case of flapping. The suppression reduces the route update frequency and the CPU usage. To disable route or tunnel recursion suppression in case of flapping, run the **route recursive-lookup delay disable** command.To configure suppression periods for route or tunnel recursion, including the initial suppression period, incremental suppression period since the second suppression, and the maximum suppression period, run the **route recursive-lookup delay** command.The initial suppression period is determined by start-time. The suppression period since the second suppression is increase-time \* 2 (n - 1). When the value (increase-time \* 2(n - 1)) reaches max-time, the maximum suppression period is used.



**Precautions**



Route or tunnel recursion suppression in case of flapping must be enabled using the **undo route recursive-lookup delay disable** command; otherwise, the **route recursive-lookup delay** command does not take effect.




Example
-------

# Disable route recursion or tunnel recursion suppression in case of flapping.
```
<HUAWEI> system-view
[~HUAWEI] route recursive-lookup delay disable

```

# Set the initial suppression period, incremental suppression period since the second suppression, and the maximum suppression period to 600 ms, 2000 ms, and 6000 ms, respectively.
```
<HUAWEI> system-view
[~HUAWEI] route recursive-lookup delay start-time 600 increase-time 2000 max-time 6000

```