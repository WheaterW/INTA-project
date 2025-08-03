load-balancing eibgp(BGP-VPN instance IPv4 address family view)
===============================================================

load-balancing eibgp(BGP-VPN instance IPv4 address family view)

Function
--------

By default, load balancing can be performed only among IBGP or EBGP routes, and the IGP metrics of the routes to be used for load balancing are compared.


Format
------

**load-balancing** { **eibgp** | **igp-metric-ignore** }

**undo load-balancing** { **eibgp** | **igp-metric-ignore** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **eibgp** | Allows both EBGP and IBGP peers to support load balancing. | - |
| **igp-metric-ignore** | Ignores IGP metric values. | - |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To enable load balancing among EBGP and IBGP routes, run the **load-balancing eibgp** command.The **load-balancing eibgp** command applies to the scenario where both EBGP and IBGP routes exist on a device and load balancing needs to be performed between EBGP and IBGP routes. Running this command will change the conditions for load balancing. Therefore, exercise caution when running this command.After the **load-balancing igp-metric-ignore** command is run, the device does not compare IGP metrics of the routes to be used for load balancing.The **load-balancing igp-metric-ignore** command is used when routes with different IGP metrics exist on a device and load balancing needs to be performed among these routes. Running this command will change the conditions for load balancing. Therefore, exercise caution when running this command.


Example
-------

# Prevent a router from comparing IGP costs when selecting routes for load balancing.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 22:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 5:5 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] load-balancing igp-metric-ignore

```