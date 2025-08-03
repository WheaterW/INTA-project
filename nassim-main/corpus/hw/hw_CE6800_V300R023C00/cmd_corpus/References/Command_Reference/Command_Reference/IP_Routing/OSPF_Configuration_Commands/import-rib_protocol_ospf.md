import-rib protocol ospf
========================

import-rib protocol ospf

Function
--------



The **import-rib protocol ospf** command imports public network or other VPN instance routes to a VPN instance routing table.

The **undo import-rib protocol ospf** command restores the default configuration.



By default, public network or other VPN instance routes are not imported to VPN instance routing tables.


Format
------

**import-rib vpn-instance** *vpn-instance-name* **protocol** **ospf** *process-id* [ **valid-route** ] [ **route-policy** *route-policy-name* ]

**import-rib public protocol ospf** *process-id* [ **valid-route** ] [ **route-policy** *route-policy-name* ]

**undo import-rib vpn-instance** *vpn-instance-name* **protocol** **ospf** *process-id* [ **valid-route** ] [ **route-policy** *route-policy-name* ]

**undo import-rib public protocol ospf** *process-id* [ **valid-route** ] [ **route-policy** *route-policy-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ospf** *process-id* | Imports OSPF routes from the specified process (process-id). | The value is an integer ranging from 1 to 4294967295. |
| **valid-route** | Imports valid routes of the corresponding route type. | - |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **public** | Imports routes from the public network BGP routing table. | - |



Views
-----

VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In VPN networking, users in a VPN instance can communicate with users in another VPN instance only if the two VPN instances have matching VPN targets, but cannot communicate with public network users. To enable a VPN to communicate with the public network, you have to ensure that the VPN and public network users can obtain routes to each other. To import public network routes to a VPN instance, run the **import-rib public** command.In VPN networking, users of a VPN instance can communicate with users of another VPN instance only if the two VPN instances have matching VPN targets. To enable users in different VPN instances to communicate with each other, ensure that users in different VPN instances can obtain routes from each other. To import routes from another VPN instance to a specified VPN instance, run the **import-rib vpn-instance** command.In an intelligent traffic control scenario, traffic of different users are distributed to different VPNs. To enable the traffic to reach the public network, run the **import-rib public** command to import public network routes to each VPN instance routing table.When VLAN tag termination sub-interfaces are used to import routes between VPN and public network instances, traffic forwarding depends on direct routes (Vlink direct routes) generated based on user entries. However, the direct routes imported between VPN and public network instances do not contain Vlink direct routes. As a result, traffic fails to be forwarded. To solve this problem, route import between VPN and public network instances newly supports import of Vlink direct routes.

**Configuration Impact**

If a VPN instance needs to import public network routes or routes of another VPN instance, you are advised to paln it in advance and configure a route-policy to prevent loops caused by manual configurations.

**Precautions**



If you run the **import-rib public** command without specifying valid-route, the system imports all routes of the specified type from the public network instance to the corresponding VPN instance's routing table. If these routes can be preferentially selected, they are advertised to other devices in the VPN instance and sent to the private IPv4 routing table to guide traffic forwarding.If the valid-route parameter is specified, the system imports valid routes of the specified type from the public network to the VPN routing table of the corresponding type. If these routes can be preferentially selected, they are advertised to other devices on the VPN and sent to the private IPv4 routing table to guide traffic forwarding.A VPN instance imports public network routes or routes of other VPN instances. You are advised to plan the routes in advance and configure a routing policy to prevent loops caused by manual configurations.




Example
-------

# Configure the device to import valid public network OSPF routes to the VPN instance vrf1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv4-family
[*HUAWEI-vpn-instance-vrf1-af-ipv4] import-rib public protocol ospf 1 valid-route

```