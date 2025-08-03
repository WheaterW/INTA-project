capture drop-packet acl-deny enable
===================================

capture drop-packet acl-deny enable

Function
--------



The **capture drop-packet acl-deny enable** command enables the packet loss visualization function for packets that are discarded due to the deny action in ACL rules.

The **undo capture drop-packet acl-deny enable** command disables the packet loss visualization function for packets that are discarded due to the deny action in ACL rules.



By default, the packet loss visualization function for the packets that are discarded due to the deny action in ACL rules is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**capture drop-packet acl-deny enable**

**undo capture drop-packet acl-deny enable**


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

A packet loss visualization-enabled device can capture a flow whose packets that are discarded due to the deny action in ACL rules, and generate a flow entry to analyze the flow to obtain its detailed information such as the packet discarding reason, number of packets, and port number.


Example
-------

# Enable the packet loss visualization function for the packets that are discarded due to the deny action in ACL rules.
```
<HUAWEI> system-view
[~HUAWEI] packet event monitor
[*HUAWEI-packet-event-monitor] capture drop-event
[*HUAWEI-packet-event-monitor-drop-event] capture drop-packet acl-deny enable

```