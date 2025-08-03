import-rib (BGP-VPN instance IPv4 address family view)
======================================================

import-rib (BGP-VPN instance IPv4 address family view)

Function
--------



The **import-rib** command imports public network BGP routes or BGP routes in a specified VPN instance into a BGP-VPN instance routing table.

The **undo import-rib** command cancels the configuration.



By default, a device does not import public network BGP routes or BGP routes in a VPN instance into a BGP-VPN instance routing table.


Format
------

**import-rib** { **public** | [ **instance** *instance-name* ] **vpn-instance** *vpn-instance-name* } [ **include-label-route** ] [ **valid-route** ] [ **route-policy** *route-policy-name* ]

**undo import-rib** { **public** | [ **instance** *instance-name* ] **vpn-instance** *vpn-instance-name* } [ **include-label-route** ] [ **valid-route** ] [ **route-policy** *route-policy-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **public** | Imports routes from the public network BGP routing table. | - |
| **instance** *instance-name* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **include-label-route** | Includes labeled routes received from peers as well as leaked VPN routes. | - |
| **valid-route** | Imports valid routes of a specified type. Valid routes include optimal routes, routes for load balancing, FRR routes, and reachable routes that are not selected for packet forwarding. If this parameter is not specified, only optimal routes, load balancing routes, and FRR routes can be imported. | - |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To configure a device to import public network BGP routes into a VPN instance routing table, run the **import-rib public** command in the BGP-VPN instance IPv4 address family view.To configure a device to import BGP routes from a specified VPN instance into a VPN instance routing table, run the **import-rib vpn-instance vpn-instance-name** command in the BGP-VPN instance IPv4 address family view.To import BGP routes from a specified VPN instance in the BGP multi-instance to the VPN routing table, run the **import-rib instance instance-name vpn-instance vpn-instance-name** command in the BGP-VPN instance IPv4 address family view.



**Precautions**



If the source of the invalid routes imported using the **import-rib** command belongs to the same instance and address family as those in which the **routing-table rib-only** command is run, the two commands are mutually exclusive.If route-policy-name is specified in the command, the **if-match interface**, **if-match route-type**, or **if-match protocol** command configured in the route-policy does not take effect.Route import between VPN and public network instances may cause BGP routing loops.




Example
-------

# Configure a device to import valid BGP routes from the public network instance to a VPN instance's BGP routing table.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] vpn-target 100:1 both
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] import-rib public valid-route

```