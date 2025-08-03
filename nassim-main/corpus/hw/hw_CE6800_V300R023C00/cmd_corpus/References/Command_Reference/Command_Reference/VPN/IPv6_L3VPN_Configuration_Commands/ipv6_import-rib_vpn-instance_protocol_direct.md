ipv6 import-rib vpn-instance protocol direct
============================================

ipv6 import-rib vpn-instance protocol direct

Function
--------



The **ipv6 import-rib vpn-instance protocol direct** command enables a device to import IPv6 routes from a VPN instance to the public network instance's IPv6 routing table.

The **undo ipv6 import-rib vpn-instance protocol direct** command disables a device from importing IPv6 routes from a VPN instance to the public network instance's IPv6 routing table.



By default, a device does not import IPv6 routes from a VPN instance to the public network instance's IPv6 routing table.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 import-rib vpn-instance** *vpn-instance-name* **protocol** **direct** [ **route-policy** *route-policy-name* ]

**undo ipv6 import-rib vpn-instance** *vpn-instance-name* **protocol** **direct**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **protocol** | Specifies the type of routes to be imported. | - |
| **direct** | Imports direct routes. | - |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In IPv6 VPN networking, a VPN instance can communicate only with other VPN instances that have matching VPN targets, but cannot communicate with public network users. If you want the public network and VPN to communicate with each other, ensure that VPN users and public network users can obtain routes from each other. You can run the **ipv6 import-rib vpn-instance protocol direct** command to import IPv6 routes from a VPN instance to the public network IPv6 routing table so that public network IPv6 users can obtain routes to access the IPv6 VPN.

**Precautions**

If the routes imported using the import-rib command are imported by other routing protocols, routing loops may occur. For details, see the precautions for IGP or BGP route import commands.When a route-policy is specified to filter routes, if the address family of the route does not match the address family of the if-match clause in the route-policy, the default matching result depends on whether the **route-policy address-family mismatch-deny** command is configured. For details, see the precautions for the **route-policy address-family mismatch-deny** command and the scenario description and precautions for the route-policy command.When a route-policy is specified to filter routes, if the next hop-based matching rule is configured in the route-policy node, this command is not supported, and the matching result is Permit.When a route-policy is specified to filter routes, the IPv6 destination address ACL, IPv6 destination address prefix list, route cost, route modulo, route preference, route tag, and outbound interface attributes can be matched. If the referenced route-policy contains an unsupported attribute matching behavior, unexpected results may occur.When a route-policy is specified to filter routes, the route cost, route preference, and route tag can be set. If the referenced route-policy contains unsupported attributes, unexpected results may occur.


Example
-------

# Configure a device to import IPv6 direct routes from a VPN instance named vrf1 to the public network instance's IPv6 routing table.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv6-family
[*HUAWEI-vpn-instance-vrf1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vrf1-af-ipv6] quit
[*HUAWEI-vpn-instance-vrf1] quit
[*HUAWEI] ipv6 import-rib vpn-instance vrf1 protocol direct

```