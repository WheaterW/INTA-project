display telemetry sensor
========================

display telemetry sensor

Function
--------



The **display telemetry sensor** command displays sampling sensor group information.




Format
------

**display telemetry sensor** [ *sensor-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *sensor-name* | Specifies the name of a sampling sensor group. | The value is a string of 1 to 64 case-sensitive characters containing letters and digits. Spaces are not supported between letters or digits. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view the name, subscription information, and subscription status of a sensor group, run the display telemetry sensor command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all sampling sensor groups.
```
<HUAWEI> display telemetry sensor
----------------------------------------------------------
Sensor-name     Path-state Sensor-type          Path
----------------------------------------------------------
group1          NA         yang                 huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info
----------------------------------------------------------

```

# Display information about sampling sensor group group1.
```
<HUAWEI> display telemetry sensor group1
----------------------------------------------------------------------------------------
Sensor-name:group1
 1. Sensor-path : huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info
    Sensor-type : self-defined-event
    Path-state  : NA
    Op-field    : interval
      Op-type1  : eq
      Op-value1 : 10
      Relation  : and
      Op-type2  : invalid
      Op-value2 : 0
    Self defined event  :
      Level             : -
      Suppress-period   : -
      Description       : -
    Depth       : 1

----------------------------------------------------------------------------------------

```

**Table 1** Description of the **display telemetry sensor** command output
| Item | Description |
| --- | --- |
| Sensor-name | Name of a sampling sensor group.   * -: The sensor-path is not configured. |
| Path-state | Sampling sensor path status:   * RESOLVED: subscribed. * NA: not subscribed. * -: The sensor-path is not configured. |
| Sensor-type | Sampling type.   * probe: probe sampling. * yang: YANG modelâbased sampling. * event: event sampling. * alarm: alarm sampling. * self-defined-event: customized event sampling. * alarm-or-event: alarm or event sampling. * OnChange: immediate sampling. * -: The sensor path is not configured. |
| Path | Sampling sensor path. |
| Sensor-path | Sampling sensor path. |
| Op-field | Fields contained in the data reported. |
| Op-type1 | Operator 1. |
| Op-value1 | Value 1 after operation. |
| Relation | Operation relationship. |
| Op-type2 | Operator 2. |
| Op-value2 | Value 2 after operation. |
| Depth | Sampling path depth. |
| Self defined event | Customized event. |
| Level | Level of a customized event. |
| Suppress-period | Suppression period of a customized event. |
| Description | Description of a customized event. |