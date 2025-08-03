multicast cpu-forward disable (VPN instance IPv4 address family view)
=====================================================================

multicast cpu-forward disable (VPN instance IPv4 address family view)

Function
--------



The **multicast cpu-forward disable** command disables soft forwarding for multicast packets.

The **undo multicast cpu-forward disable** command restores the default configuration.



By default, soft forwarding for multicast packets is enabled.


Format
------

**multicast cpu-forward disable**

**undo multicast cpu-forward disable**


Parameters
----------

None

Views
-----

VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In most cases, the Router forwards packets based on software before the hardware forwarding is completed. After that, the forwards packets based on hardware.Soft forwarding for multicast packets must be disabled on the router to prevent the low forwarding speed and first packet cache mechanism of soft forwarding from causing disorder of the first packet transmitted at a high speed.

**Prerequisites**

The **multicast routing-enable** command is run in the VPN instance view.


Example
-------

# Disable soft forwarding for multicast packets in the VPN IPv4 address family view.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance mytest
[*HUAWEI-vpn-instance-mytest] ipv4-family
[*HUAWEI-vpn-instance-mytest-af-ipv4] route-distinguisher 11:11
[*HUAWEI-vpn-instance-mytest-af-ipv4] multicast routing-enable
[*HUAWEI-vpn-instance-mytest-af-ipv4] multicast cpu-forward disable

```