import-rib(BGP multi-instance VPN instance IPv4 address family view)
====================================================================

import-rib(BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **import-rib vpn-instance** command imports BGP routes from a VPN instance into a BGP multi-instance VPN instance routing table.

The **undo import-rib vpn-instance** command cancels the configuration.



By default, a device does not import BGP routes from a VPN instance into a BGP multi-instance VPN instance routing table.


Format
------

**import-rib** { **base-instance** { **public** | **vpn-instance** *vpn-instance-name* } | **vpn-instance** *vpn-instance-name* } [ **include-label-route** ] [ **valid-route** ] [ **route-policy** *route-policy-name* ]

**undo import-rib** { **base-instance** { **public** | **vpn-instance** *vpn-instance-name* } | **vpn-instance** *vpn-instance-name* } [ **include-label-route** ] [ **valid-route** ] [ **route-policy** *route-policy-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **base-instance** | Indicates the BGP base-instance. | - |
| **public** | Imports routes from the public network BGP routing table. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **include-label-route** | Includes labeled routes received from peers as well as leaked VPN routes. | - |
| **valid-route** | Imports valid routes of a specified type. Valid routes include optimal routes, routes for load balancing, FRR routes, and reachable routes that are not selected for packet forwarding. If this parameter is not specified, only optimal routes, load balancing routes, and FRR routes can be imported. | - |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To configure a device to import BGP routes from a specified VPN instance into a BGP multi-instance VPN instance IPv4 routing table, run the **import-rib vpn-instance** command in the BGP multi-instance VPN instance IPv4 address family view.If the valid-route parameter is specified in the **import-rib vpn-instance** command, all valid BGP routes in the specified VPN instance are imported. If the valid-route parameter is not specified, only active BGP routes among valid BGP routes are imported.If you want newly imported BGP routes to be preferentially selected, specify the route-policy route-policy-name parameter so that the BGP attribute values in the filtered routes to be imported can be changed using the specified route-policy.

If base-instance is specified in the **import-rib vpn-instance** command, routes can be imported from the VPN instance of the BGP base instance. If base-instance is not specified, routes are imported only from the current BGP multi-instance.



**Precautions**



If the source of the non-valid-route routes imported using the **import-rib** command matches the instance and address family to which the **routing-table rib-only** command belongs, the two commands are mutually exclusive.If route-policy-name is specified in the command, the if-match interface or if-match route-type command configured in the routie-policy does not take effect.BGP IPv4 route import between VPN and public network instances does not take effect on non-labeled routes that are remotely or locally leaked, or routes imported in import or network mode.Route import between VPN and public network instances may cause BGP routing loops.




Example
-------

# Configure a device to import valid BGP routes from the public network instance to a VPN instance's BGP routing table.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] ip vpn-instance vpnb
[*HUAWEI-vpn-instance-vpnb] ipv4-family
[*HUAWEI-vpn-instance-vpnb-af-ipv4] route-distinguisher 100:2
[*HUAWEI-vpn-instance-vpnb-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpnb-af-ipv4] quit
[*HUAWEI-instance-vpnb] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] import-rib vpn-instance vpnb

```