capture drop-packet forward-exception enable
============================================

capture drop-packet forward-exception enable

Function
--------



The **capture drop-packet forward-exception enable** command enables the packet loss visualization function for packets that are discarded due to a forwarding exception.

The **undo capture drop-packet forward-exception enable** command disables the packet loss visualization function for packets that are discarded due to a forwarding exception.



By default, the packet loss visualization function for the packets that are discarded due to a forwarding exception is disabled.


Format
------

**capture drop-packet forward-exception enable**

**undo capture drop-packet forward-exception enable**


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

A packet loss visualization-enabled device can match a flow whose packets that are discarded due to a forwarding exception based on ACL rules, and generate a flow entry to analyze the flow to obtain its detailed information such as the packet discarding reason, number of packets, and port number.


Example
-------

# Enable the packet loss visualization function for the packets that are discarded due to a forwarding exception.
```
<HUAWEI> system-view
[~HUAWEI] packet event monitor
[*HUAWEI-packet-event-monitor] capture drop-event
[*HUAWEI-packet-event-monitor-drop-event] capture drop-packet forward-exception enable

```