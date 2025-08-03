import-rib (BGP-IPv6 unicast address family view)
=================================================

import-rib (BGP-IPv6 unicast address family view)

Function
--------



The **import-rib vpn-instance** command imports BGP routes from a specified VPN instance into the public network BGP routing table.

The **undo import-rib vpn-instance** command cancels the configuration.



By default, a device does not import BGP routes from a VPN instance into the public network BGP routing table.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**import-rib vpn-instance** *vpn-instance-name* [ **valid-route** ] [ **route-policy** *route-policy-name* ]

**undo import-rib vpn-instance** *vpn-instance-name* [ **valid-route** ] [ **route-policy** *route-policy-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **valid-route** | Imports all valid BGP routes from a VPN instance. | - |
| **route-policy** *route-policy-name* | Specifies a route-policy to filter routes to be imported. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To enable a device to import BGP routes from a specified VPN instance to the BGP IPv6 public network routing table, run the **import-rib vpn-instance** command in the BGP-IPv6 unicast address family view.If the **import-rib vpn-instance** command is run with valid-route specified, all valid BGP routes in the VPN instance are imported. If valid-route is not specified, only active valid BGP routes are imported.If you run the **import-rib vpn-instance** command with include-label-route specified, the device can import labeled routes that are received from peers and leaked to VPN instances.If you want the imported routes to be preferentially selected, configure route-policy route-policy-name to modify the attributes of the BGP routes so that the routes can be preferentially selected.



**Precautions**



If the source of the non-valid-route routes imported using the **import-rib** command matches the instance and address family to which the **routing-table rib-only** command belongs, the two commands are mutually exclusive.If route-policy-name is specified in the command, the if-match interface or if-match route-type command configured in the routie-policy does not take effect.BGP IPv4 route import between VPN and public network instances does not take effect on non-labeled routes that are remotely or locally leaked, or routes imported in import or network mode.Route import between VPN and public network instances may cause BGP routing loops.




Example
-------

# Configure a device to import BGP routes from a VPN instance named vpna to a public network's BGP routing table.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] import-rib vpn-instance vpna

```