summary automatic (BGP multi-instance VPN instance IPv4 address family view)
============================================================================

summary automatic (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **summary automatic** command enables automatic aggregation for the locally-imported routes.

The **undo summary automatic** command disables automatic aggregation for the locally-imported routes.



By default, the locally-imported routes are not aggregated automatically.


Format
------

**summary automatic**

**undo summary automatic**


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



Using the **summary automatic** command, you can summarize the routes imported by BGP. The routes can be direct routes, static routes, RIP routes, OSPF routes, or IS-IS routes. After this command is run, BGP summarizes routes based on the natural network segment (for example, 10.1.1.1/32 and 10.2.1.1/32 are summarized to 10.0.0.0/8, a Class A address), and sends only the summary route to peers. This reduces the amount of routing information.



**Configuration Impact**



BGP route aggregation is classified into manual aggregation and automatic aggregation. The command is used to implement automatic aggregation. Manual aggregation takes precedence over automatic aggregation.



**Precautions**



The **summary automatic** command is invalid for the routes imported by using the **network** command.When some summary routes are withdrawn, black holes may occur on the summary routes, causing traffic loss.




Example
-------

# Enable automatic aggregation for imported routes.
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
[*HUAWEI-bgp-instance-a-vpna] summary automatic

```