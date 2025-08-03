ipv6 import-rib vpn-instance protocol static
============================================

ipv6 import-rib vpn-instance protocol static

Function
--------



The **ipv6 import-rib vpn-instance protocol static** command enables a device to import IPv6 routes from a VPN instance to the public network instance's IPv6 routing table.

The **undo ipv6 import-rib vpn-instance protocol static** command disables a device from importing IPv6 routes from a VPN instance to the public network instance's IPv6 routing table.



By default, a device does not import IPv6 routes from a VPN instance to the public network instance's IPv6 routing table.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 import-rib vpn-instance** *vpn-instance-name* **protocol** **static** [ **valid-route** ] [ **route-policy** *route-policy-name* ]

**undo ipv6 import-rib vpn-instance** *vpn-instance-name* **protocol** **static**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **protocol** | Specifies the type of routes to be imported. | - |
| **static** | Imports static routes. | - |
| **valid-route** | Imports only the valid routes of the specified route type. | - |
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

In the VPN networking, IPv6 users of two VPNs with matching VPN targets can communicate, but IPv6 VPN users cannot communicate with IPv6 public network users. To enable IPv6 VPN users to communicate with IPv6 public network users, you must configure IPv6 route import between VPN and public network instances. To enable a device to import IPv6 routes from a VPN instance to the public network instance, run the **ipv6 import-rib vpn-instance protocol static** command.

**Precautions**



If you run the **ipv6 import-rib vpn-instance** command without adding the valid-route keyword, the device will import the optimal IPv6 route of the specified type from the specified VPN instance to the public network instance's corresponding routing table. If the imported route is preferred in this routing table, the device will advertise the route to other devices and deliver the route to the public network IPv6 routing table to guide traffic forwarding.If you run the **ipv6 import-rib vpn-instance** command with the valid-route keyword added, the device will import the valid IPv6 routes of the specified type from the specified VPN instance to the public network instance's corresponding routing table. If the imported routes are preferred in this routing table, the device will advertise these routes to other devices and deliver these routes to the public network IPv6 routing table to guide traffic forwarding.If the routes imported using the import-rib command are imported by other routing protocols, routing loops may occur. For details, see the precautions for IGP or BGP route import commands.When a route-policy is specified to filter routes, if the address family of the route does not match the address family of the if-match clause in the route-policy, the default matching result depends on whether the **route-policy address-family mismatch-deny** command is configured. For details, see the precautions for the **route-policy address-family mismatch-deny** command and the scenario description and precautions for the route-policy command.When a route-policy is specified to filter routes, the IPv6 destination address ACL list, IPv6 destination address prefix list, IPv6 next hop ACL list, IPv6 next hop prefix list, route cost, route modulo, route preference, and route tag can be matched. If the referenced route-policy contains an unsupported attribute matching behavior, unexpected results may occur.When a route-policy is specified to filter routes, the route cost, route preference, and route tag attributes can be set. If the referenced route-policy contains an unsupported attribute setting behavior, unexpected results may occur.




Example
-------

# Configure a device to import static direct routes from a VPN instance named vrf1 to the public network instance's IPv6 routing table.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv6-family
[*HUAWEI-vpn-instance-vrf1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vrf1-af-ipv6] quit
[*HUAWEI-vpn-instance-vrf1] quit
[*HUAWEI] ipv6 import-rib vpn-instance vrf1 protocol static

```