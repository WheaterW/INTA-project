sensor-group sample-adaptive
============================

sensor-group sample-adaptive

Function
--------



The **sensor-group sample-adaptive** command configures adaptive sampling for static subscription and displays the sample-adaptive view.




Format
------

**sensor-group** *sensor-group-name* **sample-adaptive**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *sensor-group-name* | Specifies the name of a sampling sensor group. | The value is a string of 1 to 64 case-sensitive characters containing letters, digits, or a combination of letters and digits. Spaces are not supported between letters or digits. The value must be the name of a sampling sensor group that has been created in the telemetry view. |



Views
-----

Subscription view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Generally, a small sampling interval is set for an analyzer to obtain more accurate data for analysis. However, a large amount of redundant data is generated when a small sampling interval is used. The data requires a large amount of storage space and is inconvenient for data management. If adaptive sampling is configured, telemetry dynamically adjusts the sampling interval based on preset conditions. When the monitoring indicators are normal, telemetry reduces the sampling interval. When the monitoring indicators reach the threshold, telemetry automatically adjusts the sampling interval based on the configuration to report collected data at a higher frequency, reducing the amount of data on the analyzer.The **sensor-group sample-adaptive** command associates a sampling sensor group with a subscription and displays the sample-adaptive view.

**Follow-up Procedure**

After the **sensor-group sample-adaptive** command is run, run the **sample-interval** command in the sample-adaptive view to configure the interval and conditions for adaptive sampling.

**Precautions**

Adaptive sampling can be configured only when the sampling sensor group meets the following conditions:

1. There is only one sampling path in the group, and the path is a container or list that contains leaf nodes. The path cannot be a pure container node.
2. The type of the sampling path in the group is not OnChange, alarm, or event.
3. The minimum sampling interval of the sampling paths in the group is greater than or equal to 1000 ms.

After the sampling mode is set to adaptive sampling, the sampling path cannot be added to or deleted from the associated sampling sensor group.


Example
-------

# Configure adaptive sampling for sampling sensor group S associated with subscription A.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] sensor-group S
[*HUAWEI-telemetry-sensor-group-S] sensor-path huawei-cpu-memory:cpu-memory/board-cpu-core-infos/board-cpu-core-info
[*HUAWEI-telemetry-sensor-group-S-path] subscription A
[*HUAWEI-telemetry-subscription-A] sensor-group S sample-adaptive
[*HUAWEI-telemetry-subscription-A-sensor-group-S-sample-adaptive]

```