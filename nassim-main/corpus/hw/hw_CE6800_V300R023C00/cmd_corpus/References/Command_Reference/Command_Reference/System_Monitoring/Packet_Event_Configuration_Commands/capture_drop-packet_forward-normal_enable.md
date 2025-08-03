capture drop-packet forward-normal enable
=========================================

capture drop-packet forward-normal enable

Function
--------



The **capture drop-packet forward-normal enable** command enables the packet loss visualization function for packets that are expected to be discarded during forwarding.

The **undo capture drop-packet forward-normal enable** command disables the packet loss visualization function for packets that are expected to be discarded during forwarding.



By default, the packet loss visualization function for the packets that are expected to be discarded during forwarding is disabled.


Format
------

**capture drop-packet forward-normal enable**

**undo capture drop-packet forward-normal enable**


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

A packet loss visualization-enabled device can match a flow whose packets are expected to be discarded during forwarding based on ACL rules, and generate a flow entry to analyze the flow to obtain its detailed information such as the packet discarding reason, number of packets, and port number.


Example
-------

# Enable the packet loss visualization function for the packets that are expected to be discarded during forwarding.
```
<HUAWEI> system-view
[~HUAWEI] packet event monitor
[*HUAWEI-packet-event-monitor] capture drop-event
[*HUAWEI-packet-event-monitor-drop-event] capture drop-packet forward-normal enable

```