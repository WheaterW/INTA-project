mtu check enable
================

mtu check enable

Function
--------



The **mtu check enable** command enables MTU check.

The **undo mtu check enable** command disables MTU check.



By default, MTU check is disabled for a GRE tunnel.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mtu check enable**

**undo mtu check enable**


Parameters
----------

None

Views
-----

Tunnel interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The MTU value determines the maximum number of bytes that can be sent by a sender at a time. If the MTU value exceeds the maximum value allowed by a receiver or a transit device, packets are fragmented or even discarded, which increases the network transmission load.After the MTU check function is enabled for a GRE tunnel, the device checks whether the length of a packet encapsulated with a GRE header exceeds the MTU of the corresponding GRE tunnel before transmitting the packet over the GRE tunnel. If the packet size exceeds the MTU, the device sends an ICMP Packet Too Big message to the sender (source IP address of the packet) to notify the sender that the packet size exceeds the MTU and provide a basis for the sender to determine the TCP packet fragment size.


Example
-------

# Enable MTU check on Tunnel1.
```
<HUAWEI> system-view
[~HUAWEI] interface tunnel 1
[*HUAWEI-Tunnel1] tunnel-protocol gre
[*HUAWEI-Tunnel1] mtu check enable

```