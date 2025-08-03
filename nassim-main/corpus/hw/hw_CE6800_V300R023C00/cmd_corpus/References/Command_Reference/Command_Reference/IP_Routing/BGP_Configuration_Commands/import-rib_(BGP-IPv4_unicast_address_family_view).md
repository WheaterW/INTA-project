import-rib (BGP-IPv4 unicast address family view)
=================================================

import-rib (BGP-IPv4 unicast address family view)

Function
--------



The **import-rib** command imports public network BGP routes or BGP routes in a specified VPN instance into the public network BGP routing table.

The **undo import-rib** command cancels the configuration.



By default, a device does not import public network BGP routes or BGP routes in a VPN instance into the public network BGP routing table.


Format
------

**import-rib** [ **instance** *instance-name* ] **vpn-instance** *vpn-instance-name* [ **valid-route** ] [ **route-policy** *route-policy-name* ]

**import-rib** [ **instance** *instance-name* ] **vpn-instance** *vpn-instance-name* **include-label-route** [ **valid-route** ] [ **route-policy** *route-policy-name* ]

**undo import-rib** [ **instance** *instance-name* ] **vpn-instance** *vpn-instance-name* [ **valid-route** ] [ **route-policy** *route-policy-name* ]

**undo import-rib** [ **instance** *instance-name* ] **vpn-instance** *vpn-instance-name* **include-label-route** [ **valid-route** ] [ **route-policy** *route-policy-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-name* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **valid-route** | Imports valid routes of a specified type. Valid routes include optimal routes, routes for load balancing, FRR routes, and reachable routes that are not selected for packet forwarding. If this parameter is not specified, only optimal routes, load balancing routes, and FRR routes can be imported. | - |
| **route-policy** *route-policy-name* | Specifies a route-policy to filter routes to be imported. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **include-label-route** | Includes labeled routes received from peers as well as leaked VPN routes. | - |



Views
-----

BGP-IPv4 unicast address family view,BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To configure a device to import BGP routes from a specified VPN instance into the public network BGP routing table, run the **import-rib vpn-instance** command in the BGP view or BGP-IPv4 unicast address family view.To import BGP routes from a specified VPN instance in the BGP multi-instance to the VPN routing table, run the **import-rib instance instance-name vpn-instance vpn-instance-name** command in the BGP-VPN instance IPv4 address family view.



**Precautions**



If the source of the non-valid-route routes imported using the **import-rib** command matches the instance and address family to which the **routing-table rib-only** command belongs, the two commands are mutually exclusive.If route-policy-name is specified in the command, the if-match interface or if-match route-type command configured in the routie-policy does not take effect.BGP IPv4 route import between VPN and public network instances does not take effect on non-labeled routes that are remotely or locally leaked, or routes imported in import or network mode.Route import between VPN and public network instances may cause BGP routing loops.




Example
-------

# Configure a device to import BGP routes from a VPN instance named vpna to a public network's BGP routing table.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] import-rib vpn-instance vpna

```