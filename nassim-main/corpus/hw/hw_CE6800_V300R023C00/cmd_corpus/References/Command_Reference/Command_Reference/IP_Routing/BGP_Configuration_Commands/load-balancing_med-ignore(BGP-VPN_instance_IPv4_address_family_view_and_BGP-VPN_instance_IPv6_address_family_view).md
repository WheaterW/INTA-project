load-balancing med-ignore(BGP-VPN instance IPv4 address family view/BGP-VPN instance IPv6 address family view)
==============================================================================================================

load-balancing med-ignore(BGP-VPN instance IPv4 address family view/BGP-VPN instance IPv6 address family view)

Function
--------



The **load-balancing med-ignore** command configures a device not to compare the MEDs of routes when selecting routes for load balancing.

The **undo load-balancing med-ignore** command restores the default configuration.



By default, a router compares the MED attributes of the routes to be used for load balancing.


Format
------

**load-balancing med-ignore**

**undo load-balancing med-ignore**


Parameters
----------

None

Views
-----

BGP-VPN instance IPv4 address family view,BGP-VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the **load-balancing med-ignore** command is run, a device does not compare the MED attributes of the routes to be used for load balancing. Exercise caution when using the command because the execution of this command will change the conditions of load balancing.When routes are used for load balancing, the device processes the MED attribute as follows:

* Load balancing can be implemented only when the MEDs of routes are the same.
* Ignores the MED attribute if the **load-balancing med-ignore** command is run. After this command is run, the device does not compare MEDs. That is, load balancing can be performed among routes with different MED attributes.The **load-balancing med-ignore** command applies to BGP route load balancing scenarios. Exercise caution when running this command because it will change the conditions of load balancing.

Example
-------

# Disable a router from comparing the MED attributes of the routes to be used for load balancing.
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
[*HUAWEI-bgp-vpna] load-balancing med-ignore

```