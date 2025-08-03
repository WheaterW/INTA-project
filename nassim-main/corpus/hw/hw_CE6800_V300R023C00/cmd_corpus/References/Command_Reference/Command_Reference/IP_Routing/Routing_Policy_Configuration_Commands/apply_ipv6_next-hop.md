apply ipv6 next-hop
===================

apply ipv6 next-hop

Function
--------



The **apply ipv6 next-hop** command configures an IPv6 next hop address for a BGP route using a route-policy.

The **undo apply ipv6 next-hop** command cancels the configuration.



By default, IPv6 next hop addresses of BGP routes are not configured using a route-policy.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**apply ipv6 next-hop** { *address* | **peer-address** | **blackhole** }

**undo apply ipv6 next-hop** { *address* | **peer-address** | **blackhole** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *address* | Specifies the IPv6 next hop address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **peer-address** | If the apply ipv6 next-hop peer-address command is run in a route-policy that is used as an export route-policy on a device, the device sets the next hop address of a route to be advertised to a peer to its own IPv6 address.  If the command is run in a route-policy that is used as an import route-policy, the device sets the next hop address of a filtered route that has been received from the peer to the peer's IPv6 address. | - |
| **blackhole** | Adds a black-hole flag to a route. | - |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **apply ipv6 next-hop** command configures an IPv6 next hop address for a BGP route.In BGP, an import or export policy can be used to change the next hop addresses of matched routes. Even if the next hop address configured in the policy is unreachable, the device adds the route to the BGP routing table, but the route is invalid (the route is not added to the IPv6 routing table).To add a blackhole flag to a route, run the **apply ipv6 next-hop blackhole** command.

**Prerequisites**



A route-policy has been configured using the route-policy command.



**Configuration Impact**



After a BGP route matches a route-policy, the IPv6 next hop address of the BGP route is changed.



**Precautions**



When a route-policy is specified in the import-route and network commands, the apply ipv6 next-hop clause in the route-policy does not take effect.




Example
-------

# Set 2001:db8:2001::1 as the next hop address.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] apply ipv6 next-hop 2001:db8:2001::1

```