adaptive-routing bandwidth
==========================

adaptive-routing bandwidth

Function
--------



The **adaptive-routing bandwidth** command configures the upper and lower thresholds for the bandwidth utilization level in a dragonfly profile.

The **undo adaptive-routing bandwidth** command restores the default upper and lower thresholds for the bandwidth utilization level in a dragonfly profile.



By default, the upper threshold is 6 and the lower threshold is 3.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**adaptive-routing bandwidth high-threshold** *high-threshold-value* **low-threshold** *low-threshold-value*

**undo adaptive-routing bandwidth high-threshold** *high-threshold-value* **low-threshold** *low-threshold-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **low-threshold** *low-threshold-value* | Specifies the lower threshold for the bandwidth utilization level. | The value is an integer ranging from 1 to 7. The default value is 3. high-threshold-value must be greater than low-threshold-value. |
| **high-threshold** *high-threshold-value* | Specifies the upper threshold for the bandwidth utilization level. | The value is an integer ranging from 1 to 7. The default value is 6. high-threshold-value must be greater than low-threshold-value. |



Views
-----

Dragonfly-profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If the bandwidth utilization level of a device is higher than the upper threshold, the device is congested. If the bandwidth utilization level of a device is lower than the lower threshold, the device is idle. The device adjusts routes based on the congestion level to prevent network congestion.


Example
-------

# Set the upper threshold to 7 and lower threshold to 3 for the bandwidth usage level in the default dragonfly profile.
```
<HUAWEI> system-view
[~HUAWEI] dragonfly profile default
[~HUAWEI-dragonfly-profile-default] adaptive-routing bandwidth high-threshold 7 low-threshold 3

```