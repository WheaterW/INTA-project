export interval
===============

export interval

Function
--------



The **export interval** command configures the interval for reporting data in the packet loss visualization and latency visualization flow tables to the collector.

The **undo export interval** command cancels the interval configuration for reporting data in the packet loss visualization and latency visualization flow tables to the collector.



By default, the interval for sending flow table data of packet loss visualization and latency visualization to the collector is 10s.


Format
------

**export interval** *time-value*

**undo export interval** [ *time-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time-value* | Specifies the interval for reporting data in the packet loss visualization and latency visualization flow tables to the collector. | The value is an integer that ranges from 1 to 1800s. The default value is 10s. |



Views
-----

packet-event-monitor view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

All flow entries generated in the flow table after packet loss visualization analysis and latency visualization analysis must be aged out locally and reported to the collector for further processing.

When the inactive time (from the last packet receiving time to the current time) of a flow entry exceeds the specified aging time, the flow entry will be aged out locally and reported to the specified collector.


Example
-------

# Set the interval for reporting data in the packet loss visualization and latency visualization flow tables to the collector to 25s.
```
<HUAWEI> system-view
[~HUAWEI] packet event monitor
[*HUAWEI-packet-event-monitor] export interval 25

```