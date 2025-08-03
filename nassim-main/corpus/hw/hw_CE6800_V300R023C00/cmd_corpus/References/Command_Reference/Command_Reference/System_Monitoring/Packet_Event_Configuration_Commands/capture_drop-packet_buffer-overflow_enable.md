capture drop-packet buffer-overflow enable
==========================================

capture drop-packet buffer-overflow enable

Function
--------



The **capture drop-packet buffer-overflow enable** command enables the packet loss visualization function for packets that are discarded due to a full buffer.

The **undo capture drop-packet buffer-overflow enable** command disables the packet loss visualization function for packets that are discarded due to a full buffer.



By default, the packet loss visualization function for the packets that are discarded due to a full buffer is disabled.


Format
------

**capture drop-packet buffer-overflow enable**

**undo capture drop-packet buffer-overflow enable**


Parameters
----------

None

Views
-----

packet-event-monitor-drop-event view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A packet loss visualization-enabled device can capture a flow whose packets that are discarded due to a full buffer, and generate a flow entry to analyze the flow to obtain its detailed information such as the packet discarding reason, number of packets, and port number.


Example
-------

# Enable the packet loss visualization function for the packets that are discarded due to a full buffer.
```
<HUAWEI> system-view
[~HUAWEI] packet event monitor
[*HUAWEI-packet-event-monitor] capture drop-event
[*HUAWEI-packet-event-monitor-drop-event] capture drop-packet buffer-overflow enable

```