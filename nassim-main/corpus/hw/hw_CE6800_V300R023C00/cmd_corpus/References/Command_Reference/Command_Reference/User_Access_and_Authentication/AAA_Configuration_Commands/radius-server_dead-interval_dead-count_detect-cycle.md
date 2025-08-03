radius-server dead-interval dead-count detect-cycle
===================================================

radius-server dead-interval dead-count detect-cycle

Function
--------

The **radius-server dead-interval dead-count detect-cycle** command configures the RADIUS server detection interval, number of times the detection interval cycles, and maximum number of consecutive unacknowledged packets in each detection interval.

The **undo radius-server dead-interval dead-count detect-cycle** command restores the default settings.

By default, the RADIUS server detection interval is 5 seconds, the number of times the detection interval cycles is 2, and the maximum number of consecutive unacknowledged packets in each detection interval is 2.



Format
------

**radius-server** { **dead-interval** *dead-interval* | **dead-count** *dead-count* | **detect-cycle** *detect-cycle* }

**undo radius-server** { **dead-interval** | **dead-count** | **detect-cycle** }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dead-interval* | Specifies the RADIUS server detection interval. | The value is an integer that ranges from 1 to 300, in seconds. |
| *dead-count* | Specifies the maximum number of consecutive unacknowledged packets in each detection interval. | The value is an integer that ranges from 1 to 65535. |
| *detect-cycle* | Specifies the number of times the detection interval cycles. | The value is an integer that ranges from 1 to 5. |




Views
-----

System view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

After the system starts, the RADIUS server status detection timer runs. The device sets the RADIUS server status to Up. When the device sends a RADIUS request packet to the RADIUS server, if the conditions for setting the RADIUS server status to Down are met, the device sets the RADIUS server status to Down; if the conditions are not met, the RADIUS server status remains to be Up.

If the device does not receive any response packet from the RADIUS server after sending the first RADIUS Access-Request packet to the server and the condition that the number of times the device does not receive any response packet from the server (n) is greater than or equal to the maximum number of consecutive unacknowledged packets (dead-count) is met in a detection interval, a communication interruption is recorded. If the device still does not receive any response packet from the RADIUS server, the device sets the RADIUS server status to Down when recording the communication interruption for the same times as the detection interval cycles.

**Precautions**

If the device has reported a RADIUS server Up alarm and needs to report a RADIUS server Down alarm, the device will send the Down alarm 10 seconds after the Up alarm is sent, even if the RADIUS server Down detection interval is shorter than 10 seconds (for example, the value of dead-interval is set to 4 seconds, and the RADIUS server Down detection interval is 8 seconds). This function prevents frequent alarm sending.



Example
-------

# Set the RADIUS server detection interval to 10 seconds, number of times the detection interval cycles to 2, and maximum number of consecutive unacknowledged packets in each detection interval to 2.
```
<HUAWEI> system-view
[~HUAWEI] radius-server dead-interval 10
[*HUAWEI] radius-server dead-count 2
[*HUAWEI] radius-server detect-cycle 2

```