bestroute med-none-as-maximum (BGP multi-instance VPN instance IPv4 address family view)
========================================================================================

bestroute med-none-as-maximum (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **bestroute med-none-as-maximum** command configures BGP to assign the maximum MED (4294967295) to a route without MED in route selection.

The **undo bestroute med-none-as-maximum** command restores the default configuration.



By default, BGP assigns 0 to a route without MED.


Format
------

**bestroute med-none-as-maximum**

**undo bestroute med-none-as-maximum**


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



The **bestroute med-none-as-maximum** command takes effect during BGP route selection and is used only when no MED is carried by BGP routes. If no MED is carried and the **bestroute med-none-as-maximum** command is not run, the system cannot select the desired route as the optimal route.



**Configuration Impact**



During BGP route selection, if the **bestroute med-none-as-maximum** command is run, a route without MED is assigned the maximum MED (4294967295).




Example
-------

# Configure BGP to assign the maximum MED (4294967295) to a route without MED in route selection.
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
[*HUAWEI-bgp-instance-a-vrf1] bestroute med-none-as-maximum

```