ipv6 icmp rate-limit packet-too-big disable
===========================================

ipv6 icmp rate-limit packet-too-big disable

Function
--------



The **ipv6 icmp rate-limit packet-too-big disable** command disables the suppression of ICMPv6 Packet Too Big messages.

The **undo ipv6 icmp rate-limit packet-too-big disable** command enables the suppression of ICMPv6 Packet Too Big messages.



By default, a device is enabled with the suppression of ICMPv6 Packet Too Big messages.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 icmp rate-limit packet-too-big disable**

**undo ipv6 icmp rate-limit packet-too-big disable**


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

If the size of an IPv6 packet sent by the source node exceeds the link MTU of the outbound interface on a network node, the network node replies with an ICMPv6 Packet Too Big message that contains the MTU value of the outbound interface on the network node.If the source node receives excessive ICMPv6 Packet Too Big messages, much memory will be used, and the system performance will be affected. By default, the system is enabled with the suppression of ICMPv6 Packet Too Big messages by processing only 50 ICMPv6 Packet Too Big messages within 1 second. If a large number of path MTU requests exist within a short period of time, run the **ipv6 icmp rate-limit packet-too-big disable** command to disable the suppression of ICMPv6 Packet Too Big messages.


Example
-------

# Enable the suppression of ICMPv6 Packet Too Big messages.
```
<HUAWEI> system-view
[~HUAWEI] undo ipv6 icmp rate-limit packet-too-big disable

```