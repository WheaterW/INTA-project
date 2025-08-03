capture latency-event
=====================

capture latency-event

Function
--------



The **capture latency-event** command displays the latency visualization view.

The **undo capture latency-event** command deletes the latency visualization view.



By default, the latency visualization view is not displayed.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**capture latency-event**

**undo capture latency-event**


Parameters
----------

None

Views
-----

packet-event-monitor view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To analyze long-latency packets for traffic passing through a device, you can run the capture latency-event command to enter the latency visualization view and enable the latency visualization function.

**Precautions**

IOAM and latency visualization cannot be configured at the same time.Before configuring latency visualization, enable 1588v2.


Example
-------

# Enter the latency visualization view.
```
<HUAWEI> system-view
[~HUAWEI] packet event monitor
[*HUAWEI-packet-event-monitor] capture latency-event

```