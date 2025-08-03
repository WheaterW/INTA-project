import-rib protocol direct
==========================

import-rib protocol direct

Function
--------



The **import-rib protocol direct** command imports public network or other VPN instance routes to a VPN instance routing table.

The **undo import-rib protocol direct** command restores the default configuration.



By default, public network or other VPN instance routes are not imported to VPN instance routing tables.


Format
------

**import-rib** { **vpn-instance** *vpn-instance-name* | **public** } **protocol** **direct** [ **route-policy** *route-policy-name* ]

**undo import-rib** { **vpn-instance** *vpn-instance-name* | **public** } **protocol** **direct**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **public** | Indicates the public network instance. | - |
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



In a L3VPN scenario, one VPN can communicate with another VPN if they have matching VPN targets, but VPNs cannot communicate with the public network. To enable a VPN to communicate with the public network, you have to ensure that the VPN and public network can obtain routes to each other. To import public network routes to a VPN instance, run the **import-rib public** command.In an intelligent traffic control scenario, traffic of different users are distributed to different VPNs. To enable the traffic to reach the public network, run the **import-rib public** command to import public network routes to each VPN instance routing table.Traffic forwarding relies on direct routes (Vlink direct routes) generated based on user entries.



**Precautions**



If you run the **import-rib public** command without specifying the valid-route keyword, the device imports all routes of a specified type from the public network instance to the routing table of the corresponding VPN instance. If these routes can be preferentially selected, they are advertised to other devices in the VPN instance and delivered to the IPv4 routing table of the VPN instance to guide traffic forwarding.If the valid-route keyword is specified, the device imports valid routes of the specified type from the public network instance to the VPN routing table of the corresponding type. If these routes can be preferentially selected, they are advertised to other devices in the VPN instance and delivered to the IPv4 routing table of the VPN instance to guide traffic forwarding.If the routes imported using the import-rib command are imported by other routing protocols, routing loops may occur. For details, see the precautions for IGP or BGP route import commands.When a route-policy is specified to filter routes, if the address family of the route does not match the address family of the if-match clause in the route-policy, the default matching result depends on whether the **route-policy address-family mismatch-deny** command is configured. For details, see the precautions for the **route-policy address-family mismatch-deny** command and the scenario description and precautions for the route-policy command.When a route-policy is specified to filter routes, if the next hop-based matching rule is configured in the route-policy node, this command is not supported, and the matching result is Permit.When a route-policy is specified to filter routes, the IPv4 destination address ACL, IPv4 destination address prefix list, route cost, route modulo, route preference, route tag, and outbound interface attributes can be matched. If the referenced route-policy contains an unsupported attribute matching behavior, unexpected results may occur.When a route-policy is specified to filter routes, the route cost, route preference, and route tag attributes can be set. If the referenced route-policy contains unsupported attributes, unexpected results may occur.




Example
-------

# Configure the device to import public direct routes to the VPN instance vrf1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv4-family
[*HUAWEI-vpn-instance-vrf1] import-rib public protocol direct

```