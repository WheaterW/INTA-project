sensor-group (Subscription view)
================================

sensor-group (Subscription view)

Function
--------



The **sensor-group** command associates a sampling sensor group and configures a sampling interval, redundancy suppression, and a heartbeat interval for the sensor group.

The **undo sensor-group** command cancels the association of a sampling sensor group.



By default, no sampling sensor group is associated.


Format
------

**sensor-group** *sensor-name* [ **sample-interval** *sample-interval* { [ **suppress-redundant** ] | [ **heartbeat-interval** *heartbeat-interval* ] } \* ]

**undo sensor-group** *sensor-name* [ **sample-interval** *sample-interval* { [ **suppress-redundant** ] | [ **heartbeat-interval** *heartbeat-interval* ] } \* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *sensor-name* | Specifies the name of a sampling sensor group to be associated. | The value is a string of 1 to 64 characters. The value must be the name of a sampling sensor group created in the telemetry view. |
| **sample-interval** *sample-interval* | Specifies a sampling interval. | The value is an integer ranging from 0 to 1800000, in milliseconds. Currently, only 0, 100, 500, 1000, 5000, 10000, 30000, 60000, 180000, 300000, 900000, and 1800000 are supported. The default value is 60000. If the value is set to 0, real-time sampling is performed. |
| **suppress-redundant** | Indicates that redundancy suppression is enabled for sampling. If the data remains unchanged during a heartbeat interval after the data is sent last time, no more data is sent. | - |
| **heartbeat-interval** *heartbeat-interval* | Specifies a heartbeat interval. | The value is an integer that ranges from 1 to 60, in seconds. The value of heartbeat-interval must be an integer multiple of the value of sample-interval in the same dimension. The default value is 60. |



Views
-----

Subscription view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

A sampling sensor group created in the telemetry view must be associated in the subscription view to perform sampling tasks.A maximum of five sampling sensor groups can be associated for each subscription using this command.

**Precautions**

* When the sampling path type is alarm, the sampling interval, redundancy suppression, and heartbeat interval configurations do not take effect.
* When the sampling type is OnChange or OnChange+, the sampling is performed immediately. The sampling interval takes effect only when it is set to 0 ms. The redundancy suppression and heartbeat interval configurations are mutually exclusive with the OnChange or OnChange+ sampling.
* When the sampling interval is set to 0 ms, periodic sampling and user-defined sampling do not take effect.
* You can run the **display telemetry sensor-path** command to check the sampling paths and types supported by the device.
* The sampling sensor group to be associated must have been successfully created in the Telemetry view. Otherwise, the association fails.
* If the sampling path configured in a sampling sensor group to be associated contains threshold filtering conditions, redundancy suppression and a heartbeat interval cannot be configured. That is, the threshold filtering configuration is mutually exclusive with the redundancy suppression and heartbeat interval configurations.
* If the configured sampling interval is less than the minimum sampling precision of the sampling path (not involved in sampling paths of alarm and event types), the device reports data based on the minimum sampling precision. If the configured sampling interval is greater than the minimum sampling precision but not an integer multiple of the minimum sampling precision, the device reports data based on the round-down multiple of the minimum sampling precision. For example, the minimum sampling precision of the sampling path huawei-devm:devm/cpuInfos/cpuInfo is 1000. If sample-interval is set to 100 using the **sensor-group** command, the device reports data at an interval of 1000 ms.
* You are advised to configure a sampling interval based on the following formula: Sampling interval = Total number of sampling instances/Number of sampling instances in the minimum sampling period x Minimum sampling period.


Example
-------

# Associate a sampling sensor group and configure a sampling interval, redundancy suppression, and a heartbeat interval for the sensor group.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] sensor-group 1
[*HUAWEI-telemetry-sensor-group-1] quit
[*HUAWEI-telemetry] subscription test
[*HUAWEI-telemetry-subscription-test] sensor-group 1 sample-interval 100 suppress-redundant heartbeat-interval 30

```