ipv6 icmp hop-limit-exceeded source-address ingress-interface
=============================================================

ipv6 icmp hop-limit-exceeded source-address ingress-interface

Function
--------



The **ipv6 icmp hop-limit-exceeded source-address ingress-interface** command forcibly configures the IPv6 address of the inbound interface for forwarding packets as the source address of an ICMPv6 Time Exceeded message.

The **undo ipv6 icmp hop-limit-exceeded source-address ingress-interface** command restores the default configuration.



By default, the IPv6 address of the inbound interface for forwarding packets is not forcibly configured as the source address of an ICMPv6 Time Exceeded message.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 icmp hop-limit-exceeded source-address ingress-interface**

**undo ipv6 icmp hop-limit-exceeded source-address ingress-interface**


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

**Usage Scenario**

Tracert is used to test the path through which a packet is sent from a host to the destination. After receiving the packet, an intermediate device sends an ICMPv6 Time Exceeded message to the host. The host then identifies the device according to the source IPv6 address of the ICMPv6 Time Exceeded message. To easily observe the inbound interface of a device along the path, you can forcibly configure the IPv6 address of the inbound interface for forwarding packets as the source address of an ICMPv6 Time Exceeded message.

**Precautions**

If both the ipv6 icmp hop-limit-exceeded source-address ingress-interface and **ipv6 icmp hop-limit-exceeded source-address** commands are run, the **ipv6 icmp hop-limit-exceeded source-address** command takes precedence over the **ipv6 icmp hop-limit-exceeded source-address ingress-interface** command.


Example
-------

# Configure the IPv6 address of the inbound interface for forwarding packets as the source address of an ICMPv6 Time Exceeded message.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 icmp hop-limit-exceeded source-address ingress-interface

```