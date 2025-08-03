capture drop-event
==================

capture drop-event

Function
--------



The **capture drop-event** command displays the packet loss visualization view.

The **undo capture drop-event** command deletes the packet loss visualization view.



By default, the packet loss visualization view is not displayed.


Format
------

**capture drop-event**

**undo capture drop-event**


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

To analyze discarded packets for traffic passing through a device, you can run the capture drop-event command to enter the packet loss visualization view and enable the packet loss visualization function.


Example
-------

# Enter the packet loss visualization view.
```
<HUAWEI> system-view
[~HUAWEI] packet event monitor
[*HUAWEI-packet-event-monitor] capture drop-event

```