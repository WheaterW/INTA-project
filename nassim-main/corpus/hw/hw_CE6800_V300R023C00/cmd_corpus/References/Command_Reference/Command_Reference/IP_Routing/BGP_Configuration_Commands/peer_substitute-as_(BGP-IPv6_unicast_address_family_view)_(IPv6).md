peer substitute-as (BGP-IPv6 unicast address family view) (IPv6)
================================================================

peer substitute-as (BGP-IPv6 unicast address family view) (IPv6)

Function
--------



The **peer substitute-as** command substitutes the local AS number for the AS number of a specified peer in the AS\_Path attribute in the advertisement direction.

The **undo peer substitute-as** command disables AS number substitution.



By default, AS number substitution is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **substitute-as**

**undo peer** *ipv6-address* **substitute-as**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In an L3VPN scenario, if the ASs where two VPN sites reside use private AS numbers, the AS numbers of the two VPN sites may be the same. If a CE in a VPN site sends a VPN route to the local PE through EBGP and the remote PE sends the route to the remote CE, the remote CE discards the route due to duplicate AS numbers. As a result, different sites in the same VPN cannot communicate with each other. In this case, you need to run the **peer substitute-as** command on the PE to enable AS number substitution in the advertisement direction. That is, when advertising the routes learned from the remote PE to its connected CE, the PE replaces the AS number of the VPN site where the CE in the received VPN site resides with the local AS number.In a BGP public network scenario, when two devices with the same AS number learn a BGP route from each other through the same EBGP peer, the route may be discarded because the AS\_Path attribute contains duplicate AS numbers. To prevent this problem, run the **peer substitute-as** command on this EBGP peer to enable AS number substitution in the advertisement direction.

**Prerequisites**

Enabling BGP AS number substitution may cause route loops in a CE multi-homing network. The **peer soo** command must be run to prevent a routing loop in a VPN site.On BGP public networks, if three or more BGP peers form a ring network, the **peer substitute-as** command cannot be run; otherwise, a routing loop may occur.

**Precautions**

If the **peer substitute-as** command is run, the AS number of the route is replaced, which may cause routing loops. To solve this problem, run the **peer soo** command to configure the SoO feature.


Example
-------

# Configure a device to replace the AS number of a specified peer in the AS\_Path of a route with the local AS number.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 200
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 enable
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 substitute-as

```