import-rib protocol static
==========================

import-rib protocol static

Function
--------



The **import-rib protocol static** command imports public network or other VPN instance routes to a VPN instance routing table.

The **undo import-rib protocol static** command restores the default configuration.



By default, public network or other VPN instance routes are not imported to VPN instance routing tables.


Format
------

**import-rib** { **vpn-instance** *vpn-instance-name* | **public** } **protocol** **static** [ **valid-route** ] [ **route-policy** *route-policy-name* ]

**undo import-rib** { **vpn-instance** *vpn-instance-name* | **public** } **protocol** **static**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **public** | Indicates the public network instance. | - |
| **protocol** | Specifies a protocol type of route to be imported to a VPN instance routing table. | - |
| **static** | Imports static routes. | - |
| **valid-route** | Imports valid routes. | - |
| **route-policy** *route-policy-name* | Specifies a route-policy to filter routes to be imported. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In the VPN scenario, one VPN can communicate with another VPN if they have matching VPN targets, but VPNs cannot communicate with the public network. To enable a VPN to communicate with the public network, you have to ensure that the VPN and public network can obtain routes to each other. To import public network routes to a VPN instance, run the **import-rib public** command.In an intelligent traffic control scenario, traffic of different users are distributed to different VPNs. To enable the traffic to reach the public network, run the **import-rib public** command to import public network routes to each VPN instance routing table.Traffic forwarding relies on direct routes (Vlink direct routes) generated based on user entries. When VLAN tag termination sub-interfaces are used for route import between VPN and public network, Vlink direct routes cannot be imported. As a result, traffic forwarding is interrupted. To solve this problem, route import between VPN and public network newly supports import of Vlink direct routes.

**Precautions**



If you run the **import-rib public** command on a device without adding the valid-route keyword, the device will import all routes of the specified type from the public network instance's corresponding routing table to the specified VPN instance. If an imported route is preferred in this routing table, the device will advertise the route to other devices and deliver the route to the VPN IPv4 routing table to guide traffic forwarding.If you run the command with the valid-route parameter, the device will import valid routes of the specified type in the public network routing table to the specified VPN instance. If imported routes are preferred in the VPN instance, the device will advertise the routes to other devices and deliver these routes to the VPN IPv4 routing tables of the devices to guide traffic forwarding.If the routes imported using the import-rib command are imported by other routing protocols, routing loops may occur. For details, see the precautions for IGP or BGP route import commands.When a route-policy is specified to filter routes, if the address family of the route does not match the address family of the if-match clause in the route-policy, the default matching result depends on whether the **route-policy address-family mismatch-deny** command is configured. For details, see the precautions for the **route-policy address-family mismatch-deny** command and the scenario description and precautions for the route-policy command.When a route-policy is specified to filter routes, the IPv4 destination address ACL list, IPv4 destination address prefix list, IPv4 next hop ACL list, IPv4 next hop prefix list, IPv6 next hop ACL list, IPv6 next hop prefix list, route cost, route modulo, route preference, and route tag can be matched. If the referenced route-policy contains an unsupported attribute matching behavior, unexpected results may occur.When a route-policy is specified to filter routes, the route cost, route preference, and route tag attributes can be set. If the referenced route-policy contains an unsupported attribute setting behavior, unexpected results may occur.




Example
-------

# Configure the device to import static routes to the VPN instance vrf1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv4-family
[*HUAWEI-vpn-instance-vrf1] import-rib public protocol static

```