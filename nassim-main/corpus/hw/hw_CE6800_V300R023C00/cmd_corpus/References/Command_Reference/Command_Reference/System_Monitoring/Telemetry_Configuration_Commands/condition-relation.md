condition-relation
==================

condition-relation

Function
--------



The **condition-relation** command configures a logical operation mode between filter criteria in a filter.

The **undo condition-relation** command restores the default configuration.



The default logical operation mode between filter criteria in a filter is AND.


Format
------

**condition-relation** { **or** | **and** }

**undo condition-relation** [ **and** | **or** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **or** | Indicates that the logical operation mode between filter criteria is OR. | - |
| **and** | Indicates that the logical operation mode between filter criteria is AND. | - |



Views
-----

Telemetry filter view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Multiple filter criteria can be configured for the same filter of a sampling path. The final filter criteria can be determined only after logical operations are performed between these filter criteria. To perform logical operations between multiple filter criteria, you must run the condition-relation command to configure a logical operation mode between these filter criteria.

**Prerequisites**

A filter has been created using the **filter** command.


Example
-------

# Set a logical operation mode between filter criteria in a filter named abc to OR.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] sensor-group 1
[*HUAWEI-telemetry-sensor-group-1] sensor-path huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info self-defined-event
[*HUAWEI-telemetry-sensor-group-1-self-defined-event-path] filter abc
[*HUAWEI-telemetry-sensor-group-1-self-defined-event-path-filter-abc] condition-relation or

```