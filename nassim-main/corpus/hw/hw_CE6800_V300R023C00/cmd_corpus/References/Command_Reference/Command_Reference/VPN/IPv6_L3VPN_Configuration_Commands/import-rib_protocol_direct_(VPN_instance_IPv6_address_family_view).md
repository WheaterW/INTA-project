import-rib protocol direct (VPN instance IPv6 address family view)
==================================================================

import-rib protocol direct (VPN instance IPv6 address family view)

Function
--------



The **import-rib protocol direct** command imports public network or other VPN instance routes to a VPN instance routing table.

The **undo import-rib protocol direct** command restores the default configuration.



By default, public network or other VPN instance routes are not imported to VPN instance routing tables.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**import-rib** { **vpn-instance** *vpn-instance-name* | **public** } **protocol** **direct** [ **route-policy** *route-policy-name* ]

**undo import-rib** { **vpn-instance** *vpn-instance-name* | **public** } **protocol** **direct**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **public** | Imports public network routes. | - |
| **protocol** | Specifies a protocol type of route to be imported to a VPN instance routing table. | - |
| **direct** | Imports direct routes, excluding direct VLINK routes. | - |
| **route-policy** *route-policy-name* | Specifies a route-policy to filter routes to be imported. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a BGP IPv6 VPN scenario, one VPN can communicate with another VPN if they have matching VPN targets, but VPNs cannot communicate with the public network. To enable a VPN to communicate with the public network, you have to ensure that the VPN and public network can obtain routes to each other. To import public network routes to a VPN instance, run the **import-rib protocol direct** command.In an intelligent traffic control scenario, traffic of different users are distributed to different VPNs. To enable the traffic to reach the public network, run the **import-rib protocol direct** command to import public network routes to each VPN instance routing table.

**Precautions**

If the routes imported using the import-rib command are imported by other routing protocols, routing loops may occur. For details, see the precautions for IGP or BGP route import commands.When a route-policy is specified to filter routes, if the address family of the route does not match the address family of the if-match clause in the route-policy, the default matching result depends on whether the **route-policy address-family mismatch-deny** command is configured. For details, see the precautions for the **route-policy address-family mismatch-deny** command and the scenario description and precautions for the route-policy command.When a route-policy is specified to filter routes, if the next hop-based matching rule is configured in the route-policy node, this command is not supported, and the matching result is Permit.When a route-policy is specified to filter routes, the IPv6 destination address ACL, IPv6 destination address prefix list, route cost, route modulo, route preference, route tag, and outbound interface attributes can be matched. If the referenced route-policy contains an unsupported attribute matching behavior, unexpected results may occur.When a route-policy is specified to filter routes, the route cost, route preference, and route tag can be set. If the referenced route-policy contains unsupported attributes, unexpected results may occur.


Example
-------

# Configure the device to import public direct routes to the VPN instance vrf1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv6-family
[*HUAWEI-vpn-instance-vrf1-af-ipv6] import-rib public protocol direct

```