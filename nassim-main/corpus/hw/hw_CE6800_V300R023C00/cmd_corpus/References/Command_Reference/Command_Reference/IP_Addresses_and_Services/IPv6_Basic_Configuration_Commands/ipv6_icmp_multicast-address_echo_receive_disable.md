ipv6 icmp multicast-address echo receive disable
================================================

ipv6 icmp multicast-address echo receive disable

Function
--------



The **ipv6 icmp multicast-address echo receive disable** command disables a device from responding to received ICMPv6 multicast Echo messages.

The **undo ipv6 icmp multicast-address echo receive disable** command restores the default configuration.



By default, a device responds to received ICMPv6 multicast Echo messages.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 icmp multicast-address echo receive disable**

**undo ipv6 icmp multicast-address echo receive disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a routing device receives a large number of ICMPv6 multicast Echo messages, responding to these messages consumes performance. To disable a device from responding to received ICMPv6 multicast Echo messages, run the **ipv6 icmp multicast-address echo receive disable** command.


Example
-------

# Disable a device from responding to received ICMPv6 multicast Echo messages.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 icmp multicast-address echo receive disable

```