maximum load-balancing mixed (BGP-VPN instance IPv6 address family view)
========================================================================

maximum load-balancing mixed (BGP-VPN instance IPv6 address family view)

Function
--------

By default, the maximum number of equal-cost BGP routes for load balancing with routes of other protocols is 0, and load balancing is not implemented.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**maximum load-balancing mixed** *number*

**undo maximum load-balancing mixed**

**undo maximum load-balancing mixed** *number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the maximum number of equal-cost BGP routes for load balancing with routes of other protocols. | The value is an integer ranging from 1 to 128. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **maximum load-balancing mixed** command is used in the scenario where traffic is transmitted between different VNFs in the symmetric telco cloud. To set the maximum number of equal-cost BGP routes for load balancing with routes of other protocols, run this command so that the BGP routes and routes of other protocols can implement load balancing.NOTE:BGP routes can be generated into equal-cost BGP routes only if all the following conditions are met:

* Original next-hop addresses are different.
* PrefVal values are the same.
* Local\_Pref attributes are the same.
* All BGP routes are summarized or non-summarized routes.
* AS\_path lengths are the same.
* Origin types (IGP, EGP, or Incomplete) are the same.
* Multi\_Exit Discriminator (MED) values are the same.
* AS\_Path attributes are the same.Equal-cost BGP routes can load-balance traffic with routes of another protocol in the IP routing table only if all the following conditions are met:
* The BGP routes are optimal or sub-optimal.
* The BGP routes and routes of other protocols have the same preference.For BGP routes with the same prefix in a routing table:
* If the optimal route and the routes selected for load balancing are all labeled routes, the number of routes used for load balancing depends on the **maximum load-balancing ingress-lsp** or **maximum load-balancing transit-lsp** command configuration.
* If the optimal route and the routes selected for load balancing are all non-labeled routes, the number of routes used for load balancing depends on the **maximum load-balancing mixed** command configuration.If BGP labeled routes implement load balancing and the ingress LSP creation criteria are met, ingress LSPs are created for the labeled routes. If BGP labeled routes implement load balancing and the transit LSP creation criteria are met, transit LSPs are created for the labeled routes.

**Configuration Impact**

If the command is run more than once, the latest configuration overrides the previous one.

**Precautions**

After this command is run, EBGP and IBGP routes can load-balance traffic, and leaked routes and non-leaked routes can also load-balance traffic.


Example
-------

# Set the maximum number of equal-cost BGP routes for load balancing with routes of other protocols to 3.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] vpn-target 1:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-vpna] maximum load-balancing mixed 3

```