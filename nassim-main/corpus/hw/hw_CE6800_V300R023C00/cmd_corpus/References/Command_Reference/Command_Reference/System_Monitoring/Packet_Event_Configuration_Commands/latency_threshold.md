latency threshold
=================

latency threshold

Function
--------



The **latency threshold** command configures the latency threshold for latency visualization.

The **undo latency threshold** command cancels the latency threshold configuration for latency visualization.



By default, no latency threshold is configured for latency visualization.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**latency threshold** *threshold-value*

**undo latency threshold** [ *threshold-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *threshold-value* | Specifies a latency threshold for latency visualization. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer in the range from 768 to 1000000, in ns. The value must be 768 + 64n (n = 0, 1, 2...).  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM:The value is an integer in the range from 800 to 1000000, in ns. The value must be 800 + 32n (n = 0, 1, 2...). |



Views
-----

packet-event-monitor-latency-event view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When the latency of packets passing through a device exceeds the specified threshold, the device considers the packets as long-latency packets. The device creates a latency visualization flow entry for the flow to obtain high-precision information such as the peak latency, number of packets, and inbound and outbound interfaces.


Example
-------

# Set the latency threshold for latency visualization to 800 ns.
```
<HUAWEI> system-view
[~HUAWEI] packet event monitor
[*HUAWEI-packet-event-monitor] capture latency-event
[*HUAWEI-packet-event-monitor-latency-event] latency threshold 800

```

# Set the latency threshold for latency visualization to 768 ns.
```
<HUAWEI> system-view
[~HUAWEI] packet event monitor
[*HUAWEI-packet-event-monitor] capture latency-event
[*HUAWEI-packet-event-monitor-latency-event] latency threshold 768

```