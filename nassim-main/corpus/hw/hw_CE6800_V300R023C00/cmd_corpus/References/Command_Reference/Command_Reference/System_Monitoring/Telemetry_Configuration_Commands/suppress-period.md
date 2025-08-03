suppress-period
===============

suppress-period

Function
--------



The **suppress-period** command configures a suppression period for a customized event.

The **undo suppress-period** command restores the default configuration.



The default suppression period of a customized event is 10 seconds.


Format
------

**suppress-period** *period*

**undo suppress-period** [ *period* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *period* | Specifies a suppression period for a customized event. | The value is an integer ranging from 0 to 3600, in seconds. |



Views
-----

Sensor-path-self-defined-event view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When the filter criteria in a filter are met, a customized event is repeatedly reported. To prevent such frequent reporting, run the suppress-period command to configure a suppression period for the customized event. After the command is run, the customized event is not repeatedly reported within the suppression period

**Prerequisites**

A customized event has been configured using the **sensor-path self-defined-event** command.


Example
-------

# Set a suppression period to 30 seconds for a customized event.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] sensor-group 1
[*HUAWEI-telemetry-sensor-group-1] sensor-path huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info self-defined-event
[*HUAWEI-telemetry-sensor-group-1-self-defined-event-path] suppress-period 30

```