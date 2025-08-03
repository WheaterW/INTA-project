aging-time(packet-event-monitor-latency-event view)
===================================================

aging-time(packet-event-monitor-latency-event view)

Function
--------



The **aging-time** command configures the aging time for entries in the latency visualization flow table.

The **undo aging-time** command cancels the aging time configuration for the latency visualization flow table.



By default, the aging time for entries in the latency visualization flow table is 30 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**aging-time** *time-value*

**undo aging-time** [ *time-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time-value* | Specifies the aging time for entries in the latency visualization flow table.The value 0 indicates that the entries in the flow table are not aged out. | The value is an integer that ranges from 0 to 3600s. The default value is 30s. |



Views
-----

packet-event-monitor-latency-event view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Network traffic may burst intermittently and a large number of flows are generated in a short period of time. However, the capacity of the flow table is limited. Old flow entries in the table need to be deleted to release memory space for new flow entries. The process of deleting old flow entries is called aging.

Because the storage space of the device is limited, all flow entries generated in the flow table after latency visualization analysis must be aged out locally and reported to the collector for further processing.

When the inactive time (from the last packet receiving time to the current time) of a flow entry exceeds the specified aging time, the flow entry will be aged out locally and reported to the specified collector.


Example
-------

# Set the aging time for entries in the latency visualization flow table to 15s.
```
<HUAWEI> system-view
[~HUAWEI] packet event monitor
[*HUAWEI-packet-event-monitor] capture latency-event
[*HUAWEI-packet-event-monitor-latency-event] aging-time 15

```