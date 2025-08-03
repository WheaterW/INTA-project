load-balancing adaptive-routing(BGP-VPN instance IPv4 address family view)
==========================================================================

load-balancing adaptive-routing(BGP-VPN instance IPv4 address family view)

Function
--------



The **load-balancing adaptive-routing** command configures load balancing for adaptive routing.

The **undo load-balancing adaptive-routing** command restores the default configuration.



By default, load balancing for adaptive routing is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**load-balancing adaptive-routing**

**undo load-balancing adaptive-routing**


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



In a direct topology, to automatically adjust forwarding paths based on network topology and traffic load changes, you can configure load-balancing adaptive-routing on a node where BGP is deployed to implement load balancing for adaptive routing.



**Precautions**



The load-balance ecmp stateful enable and **load-balancing adaptive-routing** commands cannot be both configured.The vxlan-overlay local-preference enable and **load-balancing adaptive-routing** commands cannot be both configured.The load-balance ecmp rail-group enable and **load-balancing adaptive-routing** commands cannot be both configured.




Example
-------

# Configure load balancing for adaptive routing.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] load-balancing adaptive-routing

```