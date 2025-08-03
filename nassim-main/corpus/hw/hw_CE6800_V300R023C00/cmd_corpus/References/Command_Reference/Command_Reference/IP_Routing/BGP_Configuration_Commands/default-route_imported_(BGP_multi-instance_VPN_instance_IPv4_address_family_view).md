default-route imported (BGP multi-instance VPN instance IPv4 address family view)
=================================================================================

default-route imported (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **default-route imported** command imports default routes to the BGP routing table.

The **undo default-route imported** command restores the default configuration.



By default, default routes are not imported to the BGP routing table.


Format
------

**default-route imported**

**undo default-route imported**


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
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vrf1
[*HUAWEI-bgp-instance-a-vrf1] default-route imported

```