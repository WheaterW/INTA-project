tc-protection threshold
=======================

tc-protection threshold

Function
--------



The **tc-protection threshold** command sets the maximum number of topology change notification messages that can be processed during the topology change protection interval.

The **undo tc-protection threshold** command restores the default maximum number of topology change notification messages that can be processed during the topology change protection interval.



By default, an ERPS ring processes three topology change notification messages during the topology change protection interval.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**tc-protection threshold** *threshold-value*

**undo tc-protection threshold**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *threshold-value* | Specifies the maximum number of TC BPDUs that a device processes within a specified period. | The value is an integer ranging from 1 to 255. |



Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

* After a device on an ERPS ring network receives topology change notification messages, the device updates MAC and ARP entries. However, frequent updates will cause a high CPU usage.
* To prevent frequent MAC and ARP entry updates, run the tc-protection threshold command to set the maximum number of topology change notification messages that can be processed during the topology change protection interval specified in the **tc-protection interval** command. Then, during the topology change protection interval, the device processes only the specified maximum number of topology change notification messages. If there are excess messages, the device processes all the excess messages for once after the topology change protection interval elapses. For example, if the time is set to 10 seconds and the maximum number is set to 5, when a device receives topology change notification messages, the device processes only the first 5 topology change notification messages within 10 seconds and processes the subsequent topology change notification messages only after the time elapses. This prevents the device from frequently deleting MAC and ARP entries.

Example
-------

# Specify the maximum number of topology change notification messages that ERPS ring 5 can process during the topology change protection interval to 5.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 5
[*HUAWEI-erps-ring5] tc-protection threshold 5

```