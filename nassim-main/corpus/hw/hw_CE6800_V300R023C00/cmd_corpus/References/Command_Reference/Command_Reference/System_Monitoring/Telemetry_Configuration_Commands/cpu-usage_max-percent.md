cpu-usage max-percent
=====================

cpu-usage max-percent

Function
--------



The **cpu-usage max-percent** command configures a maximum usage for the main control board's CPU used when telemetry collects data.

The **undo cpu-usage max-percent** command restores the default maximum usage for the main control board's CPU used when telemetry collects data.



By default, the maximum usage of the main control board's CPU used when telemetry collects data is 5%.


Format
------

**cpu-usage max-percent** *usage*

**undo cpu-usage max-percent** [ *usage* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *usage* | Specifies a maximum usage for the main control board's CPU used. | The value is an integer ranging from 1 to 50, in percentage. |



Views
-----

Telemetry view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When telemetry collects data, the main control board's CPU is consumed. When the CPU usage reaches a certain percentage, other services may be affected. To prevent other services from being affected, run the cpu-usage max-percent command to configure a maximum usage for the main control board's CPU used when telemetry collects data. If the CPU usage exceeds the configured maximum usage, telemetry stops sending sampled data. After the CPU usage falls below the maximum usage, telemetry continues to send sampled data.


Example
-------

# Set a maximum usage to 20% for the main control board's CPU used when telemetry collects data.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] cpu-usage max-percent 20

```