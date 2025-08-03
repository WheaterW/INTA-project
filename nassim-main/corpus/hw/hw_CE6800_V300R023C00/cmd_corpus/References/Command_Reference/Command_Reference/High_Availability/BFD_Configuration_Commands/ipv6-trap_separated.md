ipv6-trap separated
===================

ipv6-trap separated

Function
--------



The **ipv6-trap separated** command configures alarms of the BFD IPv4 and IPv6 sessions to be reported by different trap messages when the session state changes.

The **undo ipv6-trap separated** command disables alarms of the BFD IPv4 and IPv6 sessions from being reported by different trap messages when the session state changes.



By default, the BFD IPv4 and IPv6 sessions use the same trap messages to report alarms.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6-trap separated**

**undo ipv6-trap separated**


Parameters
----------

None

Views
-----

BFD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, the BFD IPv4 and IPv6 sessions use the same trap messages to report alarms. If both BFD IPv4 and IPv6 sessions exist on a link and the traffic is heavy, trap suppression is triggered. When the session link status changes, only the IPv4 or IPv6 trap messages are reported. As a result, alarms are lost.The **ipv6-trap separated** command adds trap messages for the BFD IPv6 session. When the BFD IPv6 session state changes between Up and Down, new trap messages are used to report alarms. The BFD IPv4 session uses the original trap messages for reporting alarms. In this manner, alarms for the BFD IPv4 and IPv6 sessions are separated, preventing alarms from being lost during traffic suppression.


Example
-------

# Configure alarms of the BFD IPv4 and IPv6 sessions to be reported by different trap messages when the session state changes.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] ipv6-trap separated

```