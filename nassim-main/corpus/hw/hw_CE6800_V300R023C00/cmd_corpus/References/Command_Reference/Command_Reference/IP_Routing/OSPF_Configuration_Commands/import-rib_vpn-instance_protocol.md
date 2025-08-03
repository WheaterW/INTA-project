import-rib vpn-instance protocol
================================

import-rib vpn-instance protocol

Function
--------



The **ip import-rib vpn-instance protocol** command imports routes in a VPN instance routing table to the public network routing table.

The **undo ip import-rib vpn-instance protocol** command restores the default configuration.

The **ipv6 import-rib vpn-instance protocol** command enables a device to import IPv6 routes from a VPN instance to the public network instance's IPv6 routing table.

The **undo ipv6 import-rib vpn-instance protocol** command disables a device from importing IPv6 routes from a VPN instance to the public network instance's IPv6 routing table.



By default, routes in VPN instance routing tables are not imported to the public network routing table.

By default, a device does not import IPv6 routes from a VPN instance to the public network instance's IPv6 routing table.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**ip import-rib vpn-instance** *vpn-instance-name* **protocol** **ospf** *process-id* [ **valid-route** ] [ **route-policy** *route-policy-name* ]

**undo ip import-rib vpn-instance** *vpn-instance-name* **protocol** **ospf** *process-id* [ **valid-route** ] [ **route-policy** *route-policy-name* ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**ipv6 import-rib vpn-instance** *vpn-instance-name* **protocol** **ospfv3** *process-id* [ **valid-route** ] [ **route-policy** *route-policy-name* ]

**undo ipv6 import-rib vpn-instance** *vpn-instance-name* **protocol** **ospfv3** *process-id* [ **valid-route** ] [ **route-policy** *route-policy-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, which do not contain spaces. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **protocol** | Specifies the type of routes to be imported. | - |
| **ospf** *process-id* | Imports OSPF routes from the specified process (process-id). | The value is an integer ranging from 1 to 4294967295. |
| **valid-route** | Imports valid routes of the corresponding route type. | - |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **ospfv3** *process-id* | Imports OSPFv3 routes. process-id specifies the ID of an OSPFv3 process.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In a VPN scenario, one VPN can communicate with another VPN if they have matching VPN targets, but VPNs cannot communicate with the public network. To enable a VPN to communicate with the public network, you have to ensure that the VPN and public network can obtain routes to each other. To import the VPN instance routes to public network, run the **ip import-rib vpn-instance** command.In an intelligent traffic control scenario, traffic of different users are distributed to different VPNs. To enable public-network traffic to reach the VPNs, run the **ip import-rib vpn-instance** command to import routes in each VPN instance routing table to the public network routing table.Traffic forwarding relies on direct routes (Vlink direct routes) generated based on user entries. When VLAN tag termination sub-interfaces are used for route import between VPN and public network, Vlink direct routes cannot be imported. As a result, traffic forwarding is interrupted. To solve this problem, route import between VPN and public network newly supports import of Vlink direct routes.



In a VPN scenario, one VPN can communicate with another VPN if they have matching VPN targets, but VPNs cannot communicate with the public network. To enable a VPN to communicate with the public network, you have to ensure that the VPN and public network can obtain routes to each other. To import the VPN instance routes to public network, run the **ip import-rib vpn-instance** command.In an intelligent traffic control scenario, traffic of different users are distributed to different VPNs. To enable public-network traffic to reach the VPNs, run the **ip import-rib vpn-instance** command to import routes in each VPN instance routing table to the public network routing table.Traffic forwarding relies on direct routes (Vlink direct routes) generated based on user entries. When VLAN tag termination sub-interfaces are used for route import between VPN and public network, Vlink direct routes cannot be imported. As a result, traffic forwarding is interrupted. To solve this problem, route import between VPN and public network newly supports import of Vlink direct routes.In an IPv6 VPN networking, IPv6 users of two VPNs with matching VPN targets can communicate, but IPv6 VPN users cannot communicate with IPv6 public network users. To enable IPv6 VPN users to communicate with IPv6 public network users, you must configure IPv6 route import between VPN and public network instances. To enable a device to import IPv6 routes from a VPN instance to the public network instance, run the **ipv6 import-rib vpn-instance** command.Traffic forwarding relies on direct routes (Vlink direct routes) generated based on user entries. When VLAN tag termination sub-interfaces are used for route import between VPN and public network, Vlink direct routes cannot be imported. As a result, traffic forwarding is interrupted. To solve this problem, route import between VPN and public network newly supports import of Vlink direct routes.



**Configuration Impact**

To import VPN routes to the public network, you are advised to make a plan in advance and configure routing policies to prevent loops caused by manual configurations.

**Precautions**



If you run the **ip import-rib vpn-instance** command without specifying the valid-route parameter, the system imports the optimal routes of the specified type in the VPN instance to the corresponding public network IPv4 routing table. If these routes can be preferentially selected, they are advertised to other devices on the public network and sent to the public network IPv4 routing table to guide traffic forwarding.If valid-route is specified, the system imports valid routes of the specified type in the VPN instance to the public network IPv4 routing table of the corresponding type. If these routes can be selected, they are advertised to other devices on the public network and sent to the public network IPv4 routing table to guide traffic forwarding.To import VPN routes to the public network, you are advised to plan the routes in advance and configure routing policies to prevent loops caused by manual configurations.



If you run the **ip import-rib vpn-instance** command without specifying the valid-route parameter, the system imports the optimal routes of the specified type in the VPN instance to the corresponding public network IPv4 routing table. If these routes can be preferentially selected, they are advertised to other devices on the public network and sent to the public network IPv4 routing table to guide traffic forwarding.If valid-route is specified, the system imports valid routes of the specified type in the VPN instance to the public network IPv4 routing table of the corresponding type. If these routes can be selected, they are advertised to other devices on the public network and sent to the public network IPv4 routing table to guide traffic forwarding.If you run the **ipv6 import-rib vpn-instance** command without specifying the valid-route parameter, the system imports the optimal routes of the specified type in the VPN instance to the public network instance's IPv6 routing table. If these routes can be selected, they are advertised to other devices on the public network and sent to the public network IPv6 routing table to guide traffic forwarding.If valid-route is specified, the system imports valid routes of the specified type in the VPN instance to the public network IPv6 routing table of the corresponding type. If these routes can be preferentially selected, they are advertised to other devices on the public network and sent to the public network IPv6 routing table to guide traffic forwarding.To import VPN routes to the public network, you are advised to plan the routes in advance and configure routing policies to prevent loops caused by manual configurations.




Example
-------

# Configure the device to import OSPF routes in the routing table of the VPN instance vrf1 to the public network routing table.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv4-family
[*HUAWEI-vpn-instance-vrf1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vrf1-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vrf1-af-ipv4] quit
[*HUAWEI-vpn-instance-vrf1] quit
[*HUAWEI] ip import-rib vpn-instance vrf1 protocol ospf 1 valid-route

```