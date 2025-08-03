sensor-group (Telemetry view)
=============================

sensor-group (Telemetry view)

Function
--------



The **sensor-group** command creates one or more sampling sensor groups in the Telemetry view and enters the Sensor-group view.

The **undo sensor-group** command deletes one or more sampling sensor groups in the Telemetry view.



By default, no sampling sensor group is created in the Telemetry view.


Format
------

**sensor-group** *sensor-name*

**undo sensor-group** *sensor-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *sensor-name* | Specifies the name of a sampling sensor group. | The value is a string of 1 to 64 case-sensitive characters containing letters and digits. Spaces are not supported between letters or digits. |



Views
-----

Telemetry view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To sample the data collected, run the **sensor-group** command to create one or more sampling sensor groups first.

**Precautions**



A maximum of 128 sampling sensor groups can be created using this command.




Example
-------

# Create a sampling sensor group named infodata.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] sensor-group infodata

```