qos buffer overrun threshold
============================

qos buffer overrun threshold

Function
--------



The **qos buffer overrun threshold** command sets the threshold for the percentage of device traffic to the maximum queue buffer.

The undo qos buffer overrun threshold command restores the default threshold for the percentage of device traffic to the maximum queue buffer.



By default, the threshold for the percentage of device traffic to the maximum queue buffer is 90%.


Format
------

**qos buffer overrun threshold** *percent*

**undo qos buffer overrun threshold** [ *percent* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *percent* | Specifies the threshold for the percentage of device traffic to the maximum queue buffer. | The value is an integer that ranges from 1 to 100. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The interface bandwidth is fixed. When the traffic rate exceeds the interface bandwidth and the used queue buffer exceeds the configured threshold, the device discards excess traffic. You can run the **qos buffer overrun threshold** command to set the threshold for the percentage of device traffic to the maximum queue buffer and run the **qos buffer overrun alarm enable** command to enable the device to generate an alarm when the queue buffer exceeds the threshold. When the traffic rate exceeds the threshold, an alarm is generated.


Example
-------

# Set the threshold for the percentage of device traffic to the maximum queue buffer to 60%.
```
<HUAWEI> system-view
[~HUAWEI] qos buffer overrun threshold 60

```