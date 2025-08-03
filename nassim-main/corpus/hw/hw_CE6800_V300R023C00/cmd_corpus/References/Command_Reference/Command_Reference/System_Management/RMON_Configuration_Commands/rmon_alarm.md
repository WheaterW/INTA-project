rmon alarm
==========

rmon alarm

Function
--------



The **rmon alarm** command configures RMON threshold alarm function.

The **undo rmon alarm** command disables RMON threshold alarm function.



By default, the RMON threshold alarm function is disabled.


Format
------

**rmon alarm** *entry-number* *alarm-OID* *sampling-time* { **delta** | **absolute** | **changeratio** } **rising-threshold** *threshold-value1* *event-entry1* **falling-threshold** *threshold-value2* *event-entry2* [ **startup-alarm** { **falling** | **rising** | **risingorfalling** } ] [ **owner** *owner-name* ]

**undo rmon alarm** *entry-number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *entry-number* | Specifies the index number of an alarm MIB entry. | The value is an integer ranging from 1 to 65535. |
| *alarm-OID* | Specifies the OID of a monitored object. | The name is a string of 1 to 256 case-sensitive characters, spaces not supported. |
| *sampling-time* | Specifies the sampling interval. | The value is an integer ranging from 5 to 65535, in seconds. |
| **delta** | Sets the sampling type to the delta value. Specifically, the delta value of the variable in the sampling interval is extracted when the sampling time expires. | - |
| **absolute** | Specifies the sampling type as absolute. Specifically, the variable value is directly extracted once when the sampling time expires. | - |
| **changeratio** | Sets the sampling type to the changing ratio. Specifically, the ratio of the delta value to the sampling interval is extracted when the sampling time expires. | - |
| **rising-threshold** *threshold-value1* | Specifies an upper threshold for the sampled value. | The value is an integer ranging from -2147483648 to 2147483647. |
| *event-entry1* | Specifies the event index number mapped to the upper threshold. | The value is an integer ranging from 1 to 65535. |
| **falling-threshold** *threshold-value2* | Specifies a lower threshold for the sampled value. | The value is an integer ranging from -2147483648 to 2147483647. |
| *event-entry2* | Specifies the event index number mapped to the lower threshold. | The value is an integer ranging from 1 to 65535. |
| **startup-alarm** | Indicates the type of alarm generated when a valid alarm table was sampled for the first time. | - |
| **falling** | Indicates the lower-threshold-related alarm. | - |
| **rising** | Indicates the upper-threshold-related alarm. | - |
| **risingorfalling** | Indicates the upper- or lower-threshold-related alarm. | - |
| **owner** *owner-name* | Specifies the owner creating the alarm function. | The name is a string of 1 to 127 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure the RMON threshold alarm function to monitor key states during system operating, run the rmon alarm command. After the RMON threshold alarm function is configured, the system will obtain the value of a monitored alarm object based on the defined interval and trigger corresponding events after performing comparison between this value and the specified threshold. A log is recorded or trap messages are sent to the NMS.


Example
-------

# Monitor the alarm threshold of linkdown (1.3.6.1.6.3.1.1.5.3) and sample the absolute value with an interval of 30 seconds. When the sampled value is greater than or equal to the upper threshold 500, event 1 is triggered. When the sampled value is less than or equal to the lower threshold 100, event 2 is triggered. The creator parameter indicates the owner that creates the event.
```
<HUAWEI> system-view
[~HUAWEI] rmon event 1 trap public
[~HUAWEI] rmon event 2 trap public
[~HUAWEI] rmon alarm 1 1.3.6.1.6.3.1.1.5.3 30 absolute rising-threshold 500 1 falling-threshold 100 2 owner creator

```