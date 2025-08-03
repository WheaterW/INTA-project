default-route imported (BGP-VPN instance IPv6 address family view)
==================================================================

default-route imported (BGP-VPN instance IPv6 address family view)

Function
--------



The **default-route imported** command imports default routes to the BGP routing table.

The **undo default-route imported** command restores the default configuration.



By default, default routes are not imported to the BGP routing table.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**default-route imported**

**undo default-route imported**


Parameters
----------

None

Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To import default routes to the BGP routing table, run the **default-route imported** command. After a default route of another routing protocol is added to the BGP routing table, packets can be transmitted over the default route when no matched route is available in the routing table, preventing packet loss.

**Follow-up Procedure**



When a device needs to advertise default routes to a peer or peer group and no default route exists in the local routing table, run the **peer default-route-advertise** command.



**Precautions**



The **default-route imported** command imports default routes to the BGP routing table and changes the PrefVal of the default routes to 32768. To import default routes, the **default-route imported** command needs to be used together with the **import-route** command. Using only the **import-route** command cannot import default routes, and using only the **default-route imported** command imports the default routes that exist in the local routing table. In addition, you can run the network 0.0.0.0 command to import default routes.




Example
-------

# Import default routes to the BGP routing table.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] default-route imported
[*HUAWEI-bgp-6-vpna] import-route ospf 1

```