level (Sensor-path-self-defined-event view)
===========================================

level (Sensor-path-self-defined-event view)

Function
--------



The **level** command configures a level for a customized event.

The **undo level** command restores the default configuration.



The default level of a customized event is 0.


Format
------

**level** *level-value*

**undo level** [ *level-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *level-value* | Specifies a level for a customized event. | The value is an integer ranging from 0 to 255. |



Views
-----

Sensor-path-self-defined-event view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To ensure normal network and service running, specify a customized threshold for a performance indicator of a resource object that telemetry monitors, and configure a customized event. If the performance indicator exceeds the customized threshold, the system automatically reports the customized event to the collector for service policy determination.To specify a level for a customized event, run the level command. You can define the meaning of level-value. For example, the larger the level value, the greater the impact of the event. After the level of a customized event is configured, the data packet sent to the collector contains the level value when the customized event is reported. You can determine the severity of the event based on the level value and take measures accordingly.


Example
-------

# Set a level to 20 for the customized event associated with the sampling path huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] sensor-group 1
[*HUAWEI-telemetry-sensor-group-1] sensor-path huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info self-defined-event
[*HUAWEI-telemetry-sensor-group-1-self-defined-event-path] level 20

```