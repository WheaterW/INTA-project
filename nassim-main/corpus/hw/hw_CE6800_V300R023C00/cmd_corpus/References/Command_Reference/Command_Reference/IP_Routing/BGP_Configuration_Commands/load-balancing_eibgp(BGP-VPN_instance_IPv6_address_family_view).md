load-balancing eibgp(BGP-VPN instance IPv6 address family view)
===============================================================

load-balancing eibgp(BGP-VPN instance IPv6 address family view)

Function
--------

By default, load balancing can be performed only among IBGP or EBGP routes, and the IGP metrics of the routes to be used for load balancing are compared.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



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

BGP-VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To enable load balancing among EBGP and IBGP routes, run the **load-balancing eibgp** command.The **load-balancing eibgp** command applies to the scenario where both EBGP and IBGP routes exist on a device and load balancing needs to be performed between EBGP and IBGP routes. Running this command will change the conditions for load balancing. Therefore, exercise caution when running this command.After the **load-balancing igp-metric-ignore** command is run, the device does not compare IGP metrics of the routes to be used for load balancing.The **load-balancing igp-metric-ignore** command is used when routes with different IGP metrics exist on a device and load balancing needs to be performed among these routes. Running this command will change the conditions for load balancing. Therefore, exercise caution when running this command.


Example
-------

# Enable load balancing among EBGP and IBGP routes.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] load-balancing eibgp

```

# Configure a device not to compare the IGP metrics of the routes to be used for load balancing.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] load-balancing igp-metric-ignore

```