nexthop recursive-lookup default-route (BGP-VPN instance IPv4 address family view)
==================================================================================

nexthop recursive-lookup default-route (BGP-VPN instance IPv4 address family view)

Function
--------



The **nexthop recursive-lookup default-route** command enables BGP route recursion to the default route.

The **undo nexthop recursive-lookup default-route** command restores the default configuration.



By default, BGP route recursion to the default route is disabled.


Format
------

**nexthop recursive-lookup default-route**

**undo nexthop recursive-lookup default-route**


Parameters
----------

None

Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The next hop of a BGP route may not be directly reachable. In this case, route recursion is required. To allow BGP routes to be recursed to the default IP route in the BGP-VPN instance IPv4 address family view, run the **nexthop recursive-lookup default-route** command.

**Precautions**

After this command is run, BGP routes can be recursed to the default route. Therefore, the actual forwarding path of data traffic may change.This command takes effect only for routes learned from VPN peers.


Example
-------

# Enable the function to send packets over a default route when the recursive next-hop IP address is unavailable.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] nexthop recursive-lookup default-route

```