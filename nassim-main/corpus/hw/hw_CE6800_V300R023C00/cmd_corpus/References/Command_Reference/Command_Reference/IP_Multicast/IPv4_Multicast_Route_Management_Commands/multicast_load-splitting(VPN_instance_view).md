multicast load-splitting(VPN instance view)
===========================================

multicast load-splitting(VPN instance view)

Function
--------



The **multicast load-splitting** command configures a multicast load splitting policy.

The **undo multicast load-splitting** command restores the default configuration.



By default, the load splitting among multicast routes is disabled.


Format
------

**multicast load-splitting** { **group** | **source** | **source-group** | **stable-preferred** | **balance-ucmp** }

**undo multicast load-splitting**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **group** | Indicates group address-based load splitting. This policy is applicable to the scenario of one source to multiple groups. | - |
| **source** | Indicates source address-based load splitting. This policy is applicable to the scenario of multiple sources to one group. | - |
| **source-group** | Indicates source and group addresses-based load splitting. This policy is applicable to the scenario of multiple sources to multiple groups. | - |
| **stable-preferred** | Indicates stable-preferred load splitting. This policy is applicable to the stable multicast networking. | - |
| **balance-ucmp** | Indicates link bandwidth-based load splitting. This policy is applicable to the scenario in which links have different bandwidth. | - |



Views
-----

VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If multiple equal-cost routes exist over the network, you can run the **multicast load-splitting** command to realize load splitting among the equal-cost routes. The Router selects equal-cost routes from unicast and multicast static routing tables, and determines the routing table for creating multicast routing entries based on the mask lengths and preferences of routes. All equal cost routes in the determined routing table can then take part in load splitting. The Router supports load splitting among the routes in only one routing table.

**Prerequisites**

The **multicast routing-enable** command is run.

**Configuration Impact**

The four load splitting policies are mutually exclusive. You are advised to adopt a fixed multicast load splitting policy based on the actual networking.

* If stable-preferred is specified, the Router automatically adjusts and balances the entries when equal-cost routes are added or deleted; however, when multicast routing entries are deleted, the Router does not automatically adjust the entries on the equal-cost routes.
* If group, source, or source-group is specified, fixed algorithms are used for load splitting. In case that multicast routing entries and network configurations are stable, Reverse Path Forwarding (RPF) interfaces and RPF neighbors keep unchanged.
* If balance-ucmp is specified, the Router automatically adjusts and balances traffic based on link bandwidth, implementing unequal load splitting.

**Precautions**

Multicast load-splitting and Rpf ecmp non-reverse are mutually exclusive.


Example
-------

# Configure stable-preferred load splitting in the VPN instance.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] ip vpn-instance mytest
[*HUAWEI-vpn-instance-mytest] ipv4-family
[*HUAWEI-vpn-instance-mytest-af-ipv4] route-distinguisher 100:100
[*HUAWEI-vpn-instance-mytest-af-ipv4] multicast routing-enable
[*HUAWEI-vpn-instance-mytest-af-ipv4] quit
[*HUAWEI-vpn-instance-mytest] multicast load-splitting stable-preferred

```