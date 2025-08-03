sensor-path
===========

sensor-path

Function
--------



The **sensor-path self-defined-event** command configures a Telemetry customized event.

The **undo sensor-path self-defined-event** command deletes a Telemetry customized event.



By default, no sampling path or Telemetry customized event is configured.


Format
------

**sensor-path** *path*

**sensor-path** *path* **self-defined-event**

**undo sensor-path** *path*

**undo sensor-path** *path* **self-defined-event**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *path* | Specifies a sampling path name.  For a sampling path that contains an interface name, Telemetry can add the filtering field [name=interface-type interface-number] to the sampling path, for example, huawei-ifm:ifm/interfaces/interface[name="GigabitEthernet1/0/1"].   * name is the filtering field. A maximum of five filter criteria can be configured for a path. * The filtering field must be of the key type in a node. * The filtering field is added at the interface level instead of the last level of the sampling path.   Telemetry also supports fuzzy match for an interface name in a sampling path. An interface name must end with an asterisk (\*) and contain only one asterisk (\*). For example:   * GigabitEthernet1/0/\*: indicates all interfaces with the prefix of GigabitEthernet1/0/. * GigabitEthernet1/\*: indicates all interfaces with the prefix of GigabitEthernet1/. * GigabitEthernet\*: indicates all interfaces with the prefix of GigabitEthernet. * GigabitEt\*: indicates all interfaces with the prefix of GigabitEt. * \*: indicates all device interfaces supported by the service corresponding to the sampling path.   The preceding interface types are for reference only. For details, see the interface types supported by the device. | The value is a string of 1 to 511 case-sensitive characters. |
| **self-defined-event** | Specifies a Telemetry customized event. | - |



Views
-----

Sensor group view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



You can run the sensor-path <path> self-defined-event command to configure a Telemetry customized event. If a performance indicator of a resource object that telemetry monitors exceeds the user-defined threshold, the customized event is reported to the collector in time for service policy determination.



**Precautions**



You can configure only the sampling paths on which you have the read permission.A maximum of 64 sampling paths can be configured for a sampling sensor group, including sampling paths configured using the sensor-path and sensor-path <path> self-defined-event commands. When the number of sampling paths reaches the upper limit, the device displays a message indicating that the maximum number of paths is reached.A sampling path name can be configured in a maximum of 10 sampling sensor groups at the same time. When the number of sampling paths reaches the upper limit, the device displays a message indicating that the maximum number of paths is reached.




Example
-------

# Configure a Telemetry sampling sensor path.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] sensor-group test
[*HUAWEI-telemetry-sensor-group-test] sensor-path huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info

```

# Configure a Telemetry customized event.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] sensor-group test
[*HUAWEI-telemetry-sensor-group-test] sensor-path huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info self-defined-event

```