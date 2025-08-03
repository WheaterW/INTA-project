filter (Sensor-path view and Sensor-path-self-defined-event view)
=================================================================

filter (Sensor-path view and Sensor-path-self-defined-event view)

Function
--------



The **filter** command creates a filter for a sampling path and displays the filter view.

The **undo filter** command deletes a filter configured for a sampling path.



By default, no filter is created for a sampling path.


Format
------

**filter** *filter-name*

**undo filter** *filter-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *filter-name* | Specifies the name of a filter. | Specifies the name of a filter.  The value is a string of 1 to 8 case-sensitive characters. It cannot contain spaces. |



Views
-----

Sensor path view,Sensor-path-self-defined-event view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When configuring a sampling path, you can specify filter criteria so that the data that meets the filter criteria can be collected and reported. Filter criteria can be configured only in the filter view. Therefore, before configuring filter criteria, run the filter command to create a filter and enter the filter view.

**Precautions**

Only one filter can be configured for a sampling path.If a sampling sensor group has been subscribed to and the sensor-group command has been run in the subscription view to configure a heartbeat interval or redundancy suppression, no filter can be configured for sampling paths in the sampling sensor group.


Example
-------

# Configure a filter named abc for the telemetry sampling path.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] sensor-group 1
[*HUAWEI-telemetry-sensor-group-1] sensor-path huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info self-defined-event
[*HUAWEI-telemetry-sensor-group-1-self-defined-event-path] filter abc

```