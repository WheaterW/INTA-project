import-rib route next-hop-invariable (BGP multi-instance VPN instance IPv4 address family view)
===============================================================================================

import-rib route next-hop-invariable (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **import-rib route next-hop-invariable** command configures a VPN instance to retain the original next hops of imported routes when advertising these routes to its IBGP peers.

The **undo import-rib route next-hop-invariable** command restores the default configuration.



By default, a VPN instance changes the next hops of imported routes to its own next hop when advertising these routes to its IBGP peers.


Format
------

**import-rib route next-hop-invariable**

**undo import-rib route next-hop-invariable**


Parameters
----------

None

Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To enable a VPN instance to retain the original next hops of imported routes when advertising these routes to its IBGP peers, run the **import-rib route next-hop-invariable** command for the VPN instance.




Example
-------

# Configure a VPN instance to retain the original next hops of imported routes when advertising these routes to its IBGP peers.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] import-rib route next-hop-invariable

```