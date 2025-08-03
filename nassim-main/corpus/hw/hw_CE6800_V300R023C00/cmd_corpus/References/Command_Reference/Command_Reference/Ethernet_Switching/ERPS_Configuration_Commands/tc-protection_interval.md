tc-protection interval
======================

tc-protection interval

Function
--------



The **tc-protection interval** command sets the topology change protection interval at which topology change notification messages are sent.

The **undo tc-protection interval** command restores the default topology change protection interval.



By default, the topology change protection interval is 2s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**tc-protection interval** *interval-value*

**undo tc-protection interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval-value* | Specifies the topology change protection interval.  A longer interval ensures stable ERPS operation but may cause poor ring convergence performance. | The value is an integer ranging from 1 to 600, in seconds. |



Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

* If a user terminal connects to an upper-layer network through multiple ERPS rings and the ERPS ring closest to the user terminal has topology changes, the topology change notification messages will be twice multiplied each time they pass through a ring until they reach the upper-layer network. As a result, the upper-layer network will receive the same copy of topology change notification messages multiple times.
* To prevent this problem, run the **tc-protection interval** command to set a topology change protection interval at which the maximum number of topology change notification messages specified in the tc-protection threshold command are processed. Then, during the topology change protection interval, the device processes only the specified maximum number of topology change notification messages. If there are excess messages, the device processes all the excess messages for once after the topology change protection interval elapses. For example, if the time is set to 10 seconds and the maximum number is set to 5, when a device receives topology change notification messages, the device processes only the first 5 topology change notification messages within 10 seconds and processes the subsequent topology change notification messages only after the time elapses. This prevents the device from frequently deleting MAC and ARP entries.

Example
-------

# Set the topology change protection interval to 3s for ERPS ring 1.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 1
[*HUAWEI-erps-ring1] tc-protection interval 3

```