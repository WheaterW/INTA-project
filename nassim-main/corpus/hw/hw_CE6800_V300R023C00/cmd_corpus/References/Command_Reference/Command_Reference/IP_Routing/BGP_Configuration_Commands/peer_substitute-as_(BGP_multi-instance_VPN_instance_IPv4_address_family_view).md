peer substitute-as (BGP multi-instance VPN instance IPv4 address family view)
=============================================================================

peer substitute-as (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **peer substitute-as** command substitutes the local AS number for the AS number of a specified peer in the AS\_Path attribute in the advertisement direction.

The **undo peer substitute-as** command disables AS number substitution.



By default, AS number substitution is disabled.


Format
------

**peer** *ipv4-address* **substitute-as**

**undo peer** *ipv4-address* **substitute-as**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In a BGP public network scenario, when two devices with the same AS number learn a BGP route from each other through the same EBGP peer, the route may be discarded because the AS\_Path attribute contains duplicate AS numbers. To prevent this problem, run the **peer substitute-as** command on this EBGP peer to enable AS number substitution in the advertisement direction.



**Prerequisites**



Enabling BGP AS number substitution may cause route loops in a CE multi-homing network. The **peer soo** command must be run to prevent a routing loop in a VPN site.On BGP public networks, if three or more BGP peers form a ring network, the **peer substitute-as** command cannot be run; otherwise, a routing loop may occur.



**Precautions**



If the **peer substitute-as** command is run, the AS number of the route is replaced, which may cause routing loops. To solve this problem, run the **peer soo** command to configure the SoO feature.




Example
-------

# Configure a device to replace the AS number of a specified peer in the AS\_Path of a route with the local AS number.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] peer 10.1.1.1 as-number 200
[*HUAWEI-bgp-instance-a-vpna] peer 10.1.1.1 substitute-as

```