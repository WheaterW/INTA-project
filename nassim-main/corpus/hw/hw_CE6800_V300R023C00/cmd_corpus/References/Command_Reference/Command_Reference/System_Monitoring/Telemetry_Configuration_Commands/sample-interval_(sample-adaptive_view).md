sample-interval (sample-adaptive view)
======================================

sample-interval (sample-adaptive view)

Function
--------



The **sample-interval** command configures the interval and conditions for adaptive sampling.

The **undo sample-interval** command cancels the configuration of the interval and conditions for adaptive sampling.



By default, adaptive sampling is not configured.


Format
------

**sample-interval** *interval* **op-field** *field* **op-type** { **eq** | **gt** | **ge** | **lt** | **le** } **op-value** *value*

**undo sample-interval** *interval* **op-field** *field* **op-type** { **eq** | **gt** | **ge** | **lt** | **le** } **op-value** *value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the adaptive sampling interval. | The value is an integer in the range of 1000 to 1800000, in milliseconds. Currently, only 1000, 5000, 10000, 30000, 60000, 180000, 300000, 900000, and 1800000 are supported. |
| **op-field** *field* | Specifies a field contained in the data to be sampled. | The value is a string of 1 to 64 case-sensitive characters. The value must be the name of a leaf node in the sampling path and must be an integer or an enumerated value. |
| **op-type** | Specifies the adaptive sampling relational operator. | - |
| **eq** | Equal to. | - |
| **gt** | Greater than. | - |
| **ge** | Greater than or equal to. | - |
| **lt** | Less than. | - |
| **le** | Less than or equal to. | - |
| **op-value** *value* | Specifies a value involved in operation. | The value is an integer in the range of 0-9223372036854775807. The actual value depends on the device.  If the value of op-field (leaf node) is of the enumerated type, the value of op-value will be converted to an integer. The meaning of this integer can be checked by entering "?" in the CLI to check the help information or checking the enumeration type definition of the leaf node in the YANG file. |



Views
-----

sample-adaptive view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **sample-interval** command to specify the interval and conditions for adaptive sampling. If the conditions are met, data is sampled based on the specified sampling interval. If the command is run multiple times, only the latest configuration takes effect.

**Precautions**

If the value of op-field (leaf node) is of the enumerated type, the value of op-value will be converted to an integer. The meaning of this integer can be checked by entering "?" in the CLI to check the help information or checking the enumeration type definition of the leaf node in the YANG file.


Example
-------

# Configure adaptive sampling. Under normal circumstances, the sampling interval is 30s. When the CPU usage of the device is greater than 45%, the sampling interval is automatically adjusted to 10s.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] sensor-group S
[*HUAWEI-telemetry-sensor-group-S] sensor-path huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info
[*HUAWEI-telemetry-sensor-group-S-path] subscription A
[*HUAWEI-telemetry-subscription-A] sensor-group S sample-interval 30000
[*HUAWEI-telemetry-subscription-A] sensor-group S sample-adaptive
[*HUAWEI-telemetry-subscription-A-sensor-group-S-sample-adaptive] sample-interval 10000 op-field system-cpu-usage op-type gt op-value 45

```