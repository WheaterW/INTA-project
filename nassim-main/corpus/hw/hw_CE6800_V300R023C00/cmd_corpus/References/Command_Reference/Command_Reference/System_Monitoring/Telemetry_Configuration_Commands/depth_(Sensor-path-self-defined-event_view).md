depth (Sensor-path-self-defined-event view)
===========================================

depth (Sensor-path-self-defined-event view)

Function
--------



The **depth** command configures a sampling depth for the sampling path of a telemetry sensor.

The **undo depth** command restores the default configuration.



The default sampling depth for the sampling path of a telemetry sensor is 1.


Format
------

**depth** *depth-value*

**undo depth** [ *depth-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *depth-value* | Specifies a sampling depth. | The value is an integer ranging from 1 to 3. |



Views
-----

Sensor path view,Sensor-path-self-defined-event view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After configuring a sampling path on a device, you can run the **depth** command to configure a sampling depth for the sampling path. The device collects data of some or all nodes in the path based on the sampling depth.

* If the sampling depth is set to 1, only the data of the specified path is sampled.
* If the sampling depth is set to 2, the data of the specified path and all its child nodes is sampled.
* If the sampling path depth is set to 3, the data of the specified path and all its child and grandchild nodes is sampled.

Example
-------

# Set a sampling depth to 1 for a Telemetry customized event sampling path named huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] sensor-group sen1
[*HUAWEI-telemetry-sensor-group-sen1] sensor-path huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info self-defined-event
[*HUAWEI-telemetry-sensor-group-sen1-self-defined-event-path] depth 1

```