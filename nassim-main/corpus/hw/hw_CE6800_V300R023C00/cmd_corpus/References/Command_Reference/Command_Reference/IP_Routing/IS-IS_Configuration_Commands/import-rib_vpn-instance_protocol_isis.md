import-rib vpn-instance protocol isis
=====================================

import-rib vpn-instance protocol isis

Function
--------



The **ip import-rib vpn-instance protocol isis** command imports routes in a VPN instance routing table to the public network routing table.

The **undo ip import-rib vpn-instance protocol isis** command restores the default configuration.

The **ipv6 import-rib vpn-instance protocol isis** command enables a device to import IPv6 routes from a VPN instance to the public network instance's IPv6 routing table.

The **undo ipv6 import-rib vpn-instance protocol isis** command disables a device from importing IPv6 routes from a VPN instance to the public network instance's IPv6 routing table.



By default, routes in VPN instance routing tables are not imported to the public network routing table.

By default, a device does not import IPv6 routes from a VPN instance to the public network instance's IPv6 routing table.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

{ **ip** | **ipv6** } **import-rib** **vpn-instance** *vpn-instance-name* **protocol** **isis** *process-id* [ **valid-route** ] [ **route-policy** *route-policy-name* ]

**undo** { **ip** | **ipv6** } **import-rib** **vpn-instance** *vpn-instance-name* **protocol** **isis** *process-id* [ **valid-route** ] [ **route-policy** *route-policy-name* ]

For CE6885-LL (low latency mode):

**undo ip import-rib vpn-instance** *vpn-instance-name* **protocol** **isis** *process-id* [ **valid-route** ] [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **protocol** | Specifies the type of routes to be imported. | - |
| **isis** *process-id* | Imports IS-IS routes of an IS-IS process with the specified ID. | The value is an integer ranging from 1 to 4294967295. |
| **valid-route** | Imports valid routes of the corresponding route type. | - |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **route-filter** *route-filter-name* | Specifies the name of a route-filter.  NOTE:  This parameter is supported only on the CE6885-LL (low latency mode). | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). If parameters are included in the referenced route-filter, specify values for them in the format of (var1, var2, ...var8) behind the route-filter name. Each value ranges from 1 to 200 characters. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In the VPN scenario, one VPN can communicate with another VPN if they have matching VPN targets, but VPNs cannot communicate with the public network. To enable a VPN to communicate with the public network, you have to ensure that the VPN and public network can obtain routes to each other. To import the VPN instance routes to public network, run the **ip import-rib vpn-instance** command.In an intelligent traffic control scenario, traffic of different users are distributed to different VPNs. To enable public-network traffic to reach the VPNs, run the **ip import-rib vpn-instance** command to import routes in each VPN instance routing table to the public network routing table.Traffic forwarding relies on direct routes (Vlink direct routes) generated based on user entries. When VLAN tag termination sub-interfaces are used for route import between VPN and public network, Vlink direct routes cannot be imported. As a result, traffic forwarding is interrupted. To solve this problem, route import between VPN and public network newly supports import of Vlink direct routes.In the IPv6 VPN networking, IPv6 users of two VPNs with matching VPN targets can communicate, but IPv6 VPN users cannot communicate with IPv6 public network users. To enable IPv6 VPN users to communicate with IPv6 public network users, you must configure IPv6 route import between VPN and public network instances. To enable a device to import IPv6 routes from a VPN instance to the public network instance, run the **ipv6 import-rib vpn-instance** command.Traffic forwarding relies on direct routes (Vlink direct routes) generated based on user entries. When VLAN tag termination sub-interfaces are used for route import between VPN and public network, Vlink direct routes cannot be imported. As a result, traffic forwarding is interrupted. To solve this problem, route import between VPN and public network newly supports import of Vlink direct routes.

**Configuration Impact**

Exercise caution when importing routes in a VPN instance to the public network routing table or importing IPv6 routes in a VPN instance to the public network IPv6 routing table to prevent routing loops caused by manual configurations.After the route-policy parameter is specified in the command, only the network segment routes that meet the specified conditions can be imported to the public network routing table. This prevents the device from passively importing unnecessary routes. If no policy is specified for importing routes, a large number of unexpected routes may be imported. As a result, the number of routes exceeds the upper limit or the memory is overloaded.

**Precautions**

If you run the **ip import-rib vpn-instance** command without specifying the valid-route parameter, the system imports the optimal routes of the specified type in the VPN instance to the corresponding public network IPv4 routing table. If these routes can be preferentially selected, they are advertised to other devices on the public network and sent to the public network IPv4 routing table to guide traffic forwarding.If valid-route is specified, the system imports valid routes of the specified type in the VPN instance to the public network IPv4 routing table of the corresponding type. If these routes can be selected, they are advertised to other devices on the public network and sent to the public network IPv4 routing table to guide traffic forwarding.If you run the **ipv6 import-rib vpn-instance** command without specifying the valid-route parameter, the system imports the optimal routes of the specified type in the VPN instance to the public network instance's IPv6 routing table. If these routes can be selected, they are advertised to other devices on the public network and sent to the public network IPv6 routing table to guide traffic forwarding.If valid-route is specified, the system imports valid routes of the specified type in the VPN instance to the public network IPv6 routing table of the corresponding type. If these routes can be preferentially selected, they are advertised to other devices on the public network and sent to the public network IPv6 routing table to guide traffic forwarding.If route-policy route-policy-name is specified in this command, the following items can be matched: the outbound interface, next hop address ACL list of IP routing information, next hop address prefix list of IP routing information, route cost, route type, route tag, IPv6 route next-hop address ACL list, IPv6 route next-hop address prefix list, routing protocol type, and route priority. The route cost, route tag, and route priority can be set.If the referenced policy contains unsupported attribute matching or setting an action, unexpected results may occur.


Example
-------

# Configure the device to import IS-IS routes in the routing table of the VPN instance vrf1 to the public network routing table.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv4-family
[*HUAWEI-vpn-instance-vrf1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vrf1-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vrf1-af-ipv4] quit
[*HUAWEI-vpn-instance-vrf1] quit
[*HUAWEI] ip import-rib vpn-instance vrf1 protocol isis 1 valid-route

```