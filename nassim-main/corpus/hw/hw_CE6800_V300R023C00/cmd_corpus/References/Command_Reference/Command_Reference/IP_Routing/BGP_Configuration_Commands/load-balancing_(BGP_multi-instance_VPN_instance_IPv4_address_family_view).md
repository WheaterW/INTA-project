load-balancing (BGP multi-instance VPN instance IPv4 address family view)
=========================================================================

load-balancing (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **load-balancing as-path-ignore** command configures a router not to compare the AS\_Path attributes of routes that are to be used for load balancing.

The **undo load-balancing as-path-ignore** command cancels the configuration.

The **load-balancing as-path-relax** command configures BGP to compare only the AS\_Path attribute lengths of the routes to be used for load balancing. Routes with different AS-Path attributes can form equal-cost routes as long as the AS-Path attribute lengths of the routes are the same.

The **undo load-balancing as-path-relax** command cancels the configuration.



By default, a router compares the AS\_Path attributes of the routes to be used for load balancing.


Format
------

**load-balancing** { **as-path-ignore** | **as-path-relax** }

**undo load-balancing** { **as-path-ignore** | **as-path-relax** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **as-path-ignore** | Ignores AS\_Path attribute comparison. | - |
| **as-path-relax** | Ignores the comparison of the AS\_Path attributes with the same AS\_Path length. | - |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When load balancing is performed among routes, the device processes the AS\_Path attribute as follows:

* Load balancing can be implemented only when the AS\_Path attributes are the same.
* Ignores the AS\_Path attributes. You can run the **load-balancing as-path-ignore** command to configure the device to ignore the AS\_Path attributes. After this command is run, the device does not compare the AS\_Path attributes (including the AS\_Path length and content) of routes when selecting the routes used for load balancing. That is, load balancing can be performed even if the AS\_Path attributes of the routes are different. This changes the conditions for load balancing. Therefore, exercise caution when running this command.
* Ignores the AS\_Path content and compares only the AS\_Path lengths. You can run the **load-balancing as-path-relax** command to configure the device to compare the AS\_Path lengths. After this command is run, the device compares only the AS\_Path lengths of the routes to be used for load balancing. Load balancing can be implemented as long as the AS\_Path lengths are the same. If the AS\_Path lengths are different, load balancing cannot be implemented. For example, the AS\_Path attribute of route A is 10 and that of route B is 10 20. The AS\_Path lengths of route A and route B are different. In this case, load balancing cannot be implemented.The **load-balancing as-path-relax** command is mainly used in BGP route load balancing scenarios. Exercise caution when running this command because it will change the conditions for load balancing.

**Precautions**



The load-balancing as-path-ignore and **bestroute as-path-ignore** commands are mutually exclusive. That is, the **load-balancing as-path-ignore** command cannot be configured after the **bestroute as-path-ignore** command is configured.If you run both the load-balancing as-path-relax and **load-balancing as-path-ignore** commands, the latest configuration overrides the previous one.If the load-balancing as-path-ignore or **load-balancing as-path-relax** command is run but as-path-ignore or as-path-relax is not specified in the **peer load-balancing** command, the load-balancing as-path-ignore or **load-balancing as-path-relax** command takes effect. If as-path-ignore or as-path-relax is specified in the **peer load-balancing** command, the configuration specified in the **peer load-balancing** command takes effect.Running the load-balancing as-path-ignore or **load-balancing as-path-relax** command may cause BGP routing loops.




Example
-------

# Configure a device not to compare the AS\_Path attributes of the routes to be used for load balancing.
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
[*HUAWEI-bgp-instance-a-vpna] load-balancing as-path-ignore

```

# Configure a device not to compare the AS\_Path attributes of the same length when selecting routes for load balancing.
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
[*HUAWEI-bgp-instance-a-vpna] load-balancing as-path-relax

```