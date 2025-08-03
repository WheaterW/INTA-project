ip import-rib vpn-instance protocol static
==========================================

ip import-rib vpn-instance protocol static

Function
--------



The **ip import-rib vpn-instance protocol static** command imports routes in a VPN instance routing table to the public network routing table.

The **undo ip import-rib vpn-instance protocol static** command restores the default configuration.



By default, routes in VPN instance routing tables are not imported to the public network routing table.


Format
------

**ip import-rib vpn-instance** *vpn-instance-name* **protocol** **static** [ **valid-route** ] [ **route-policy** *route-policy-name* ]

**undo ip import-rib vpn-instance** *vpn-instance-name* **protocol** **static**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **protocol** | Specifies a protocol type of route to be imported to the public network routing table. | - |
| **static** | Imports static routes. | - |
| **valid-route** | Imports only the valid routes of the specified route type. | - |
| **route-policy** *route-policy-name* | Specifies a route-policy to filter routes to be imported. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In the VPN scenario, one VPN can communicate with another VPN if they have matching VPN targets, but VPNs cannot communicate with the public network. To enable a VPN to communicate with the public network, you have to ensure that the VPN and public network can obtain routes to each other. To import the VPN instance routes to public network, run the **ip import-rib vpn-instance protocol static** command.In an intelligent traffic control scenario, traffic of different users are distributed to different VPNs. To enable public-network traffic to reach the VPNs, run the **ip import-rib vpn-instance protocol static** command to import routes in each VPN instance routing table to the public network routing table.Traffic forwarding relies on direct routes (Vlink direct routes) generated based on user entries. When VLAN tag termination sub-interfaces are used for route import between VPN and public network, Vlink direct routes cannot be imported. As a result, traffic forwarding is interrupted. To solve this problem, route import between VPN and public network newly supports import of Vlink direct routes.

**Precautions**



If you run the **ip import-rib vpn-instance** command without adding the valid-route keyword, the device will import the optimal route of the specified type from the specified VPN instance to the public network instance's corresponding IPv4 routing table. If the imported route is preferred in this routing table, the device will advertise the route to other devices and deliver the route to the public network IPv4 routing table to guide traffic forwarding.If you run the command with the valid-route keyword added, the device will import the valid IP routes of the specified type from the specified VPN instance to the public network instance's corresponding IPv4 routing table. If the imported routes are preferred in this routing table, the device will advertise these routes to other devices and deliver these routes to the public network IPv4 routing table to guide traffic forwarding.If the routes imported using the import-rib command are imported by other routing protocols, routing loops may occur. For details, see the precautions for IGP or BGP route import commands.When a route-policy is specified to filter routes, if the address family of the route does not match the address family of the if-match clause in the route-policy, the default matching result depends on whether the **route-policy address-family mismatch-deny** command is configured. For details, see the precautions for the **route-policy address-family mismatch-deny** command and the scenario description and precautions for the route-policy command.When a route-policy is specified to filter routes, the IPv4 destination address ACL list, IPv4 destination address prefix list, IPv4 next hop ACL list, IPv4 next hop prefix list, IPv6 next hop ACL list, IPv6 next hop prefix list, route cost, route modulo, route preference, and route tag can be matched. If the referenced route-policy contains an unsupported attribute matching behavior, unexpected results may occur.When a route-policy is specified to filter routes, the route cost, route preference, and route tag attributes can be set. If the referenced route-policy contains an unsupported attribute setting behavior, unexpected results may occur.




Example
-------

# Configure the device to import static routes in the routing table of the VPN instance vrf1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv4-family
[*HUAWEI-vpn-instance-vrf1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vrf1-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vrf1-af-ipv4] quit
[*HUAWEI-vpn-instance-vrf1] quit
[*HUAWEI] ip import-rib vpn-instance vrf1 protocol static

```