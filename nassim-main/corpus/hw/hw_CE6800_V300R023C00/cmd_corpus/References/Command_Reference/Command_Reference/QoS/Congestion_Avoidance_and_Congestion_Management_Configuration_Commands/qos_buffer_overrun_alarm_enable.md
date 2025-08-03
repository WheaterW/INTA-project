qos buffer overrun alarm enable
===============================

qos buffer overrun alarm enable

Function
--------



The **qos buffer overrun alarm enable** command enables the device to generate an alarm when the queue buffer exceeds the threshold.

The **undo qos buffer overrun alarm enable** command disables the device from generating an alarm when the queue buffer exceeds the threshold.



By default, the device is disabled from generating an alarm when the queue buffer exceeds the threshold.


Format
------

**qos buffer overrun alarm enable**

**undo qos buffer overrun alarm enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The interface bandwidth is fixed. When the traffic rate exceeds the interface bandwidth and the used queue buffer exceeds the configured threshold, the device discards excess traffic. You can run the **qos buffer overrun threshold** command to set the threshold for the percentage of device traffic to the maximum queue buffer and run the **qos buffer overrun alarm enable** command to enable the device to generate an alarm when the queue buffer exceeds the threshold. When the traffic rate exceeds the threshold, "QoS\_1.3.6.1.4.1.2011.5.25.32.4.1.11.21 hwXQOSQueueBufferOverrunAlarm" is generated. When the queue buffer is restored, "QoS\_1.3.6.1.4.1.2011.5.25.32.4.1.11.22 hwXQOSQueueBufferOverrunResume" is generated.


Example
-------

# Enable the device to generate an alarm when the queue buffer exceeds the threshold.
```
<HUAWEI> system-view
[~HUAWEI] qos buffer overrun alarm enable

```