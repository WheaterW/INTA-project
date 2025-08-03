description (Sensor-path-self-defined-event view)
=================================================

description (Sensor-path-self-defined-event view)

Function
--------



The **description** command configures a description for a customized event.

The **undo description** command restores the default configuration.



By default, no description is configured for a customized event.


Format
------

**description** *event-description*

**undo description** [ *event-description* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *event-description* | Specifies a description for a customized event. | The value is a string of 1 to 55 case-sensitive characters. It cannot contain spaces. |



Views
-----

Sensor-path-self-defined-event view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When associating a sampling path with a customized event, you can run the description command to configure a description for the customized event. The description helps a controller determine the meaning or possible impact of the customized event.

**Prerequisites**

A customized event has been configured using the **sensor-path self-defined-event** command.


Example
-------

# Configure a description of event1 for a customized event.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] sensor-group 1
[*HUAWEI-telemetry-sensor-group-1] sensor-path huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info self-defined-event
[*HUAWEI-telemetry-sensor-group-1-self-defined-event-path] description event1

```