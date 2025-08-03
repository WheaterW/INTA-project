ntp unsync max-poll-interval
============================

ntp unsync max-poll-interval

Function
--------



The **ntp unsync max-poll-interval** command sets the maximum polling interval in unsynchronized mode and the step to be decreased in the actual polling interval.

The **undo ntp unsync max-poll-interval** command restores the default maximum polling interval in unsynchronized mode and the step to be decreased in the actual polling interval.



By default, the maximum polling interval in unsynchronized mode and the step length to be decreased in the actual polling interval is no set.


Format
------

**ntp unsync max-poll-interval** *poll-interval-value* **dec-step** *step-value*

**undo ntp unsync max-poll-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *poll-interval-value* | Specifies the maximum polling interval in unsynchronized mode. | The value is an integer ranging from 6 to 10, expressed in the Nth power of 2 seconds. |
| **dec-step** *step-value* | Specifies the step length to be decreased in the actual polling interval. | The value is an integer ranging from 1 to 6, expressed in the Nth power of 2 seconds.  If the value of poll-interval-value is 10, step-value can be set to 6 only. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Network Time Protocol (NTP) is an application-layer protocol in the TCP/IP suite. It synchronizes time among a set of distributed time servers and clients. An NTP client sends NTP clock synchronization packets to the NTP server at a specified polling interval to request time synchronization. In unsynchronized mode, the polling interval increases by the Nth power of 2. If time synchronization is always not achieved, the interval increases to 2^10s (1024s) at most. To set a fixed polling interval in unsynchronized mode, run the **ntp unsync max-poll-interval** command.

* If the actual polling interval is greater than the polling interval configured using the **ntp unsync max-poll-interval** command, the actual polling interval decreases by the configured step length until it becomes the same as the configured polling interval.
* If the actual polling interval is less than the polling interval configured using the **ntp unsync max-poll-interval** command, the actual polling interval increases by the Nth power of 2 until it becomes the same as the configured polling interval.

**Precautions**

This command takes effect only for client/server and peer modes.


Example
-------

# Set the maximum polling interval in unsynchronized mode and the step length to be decreased in the actual polling interval to 128s and 64s, respectively.
```
<HUAWEI> system-view
[~HUAWEI] ntp unsync max-poll-interval 7 dec-step 6

```