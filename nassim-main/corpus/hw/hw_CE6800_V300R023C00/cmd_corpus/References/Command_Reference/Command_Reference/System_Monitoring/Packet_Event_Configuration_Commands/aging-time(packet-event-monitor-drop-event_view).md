aging-time(packet-event-monitor-drop-event view)
================================================

aging-time(packet-event-monitor-drop-event view)

Function
--------



The **aging-time** command configures the aging time for entries in the packet loss visualization flow table.

The **undo aging-time** command cancels the aging time configuration for entries in the packet loss visualization flow table.



By default, the aging time for entries in the packet loss visualization flow table is 30 seconds.


Format
------

**aging-time** *time-value*

**undo aging-time** [ *time-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time-value* | Specifies the aging time for entries in the packet loss visualization flow table. The value 0 indicates that the entries in the flow table are not aged out. | The value is an integer that ranges from 0 to 3600, in seconds. The default value is 30. |



Views
-----

packet-event-monitor-drop-event view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Network traffic may burst intermittently and a large number of flows are generated in a short period of time. However, the capacity of the flow table is limited. Old flow entries in the table need to be aged out locally to release memory space for new flow entries. The process of deleting old flow entries is called aging.

Because the storage space of the device is limited, all flow entries generated in the flow table after packet loss visualization analysis must be aged out locally and reported to a specified collector for further processing.

When the inactive time (from the last packet receiving time to the current time) of a flow entry exceeds the specified aging time, the flow entry will be aged out locally and reported to the specified collector.


Example
-------

# Set the aging time for entries in the packet loss visualization flow table to 15s.
```
<HUAWEI> system-view
[~HUAWEI] packet event monitor
[*HUAWEI-packet-event-monitor] capture drop-event
[*HUAWEI-packet-event-monitor-drop-event] aging-time 15

```