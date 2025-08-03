import-rib protocol isis
========================

import-rib protocol isis

Function
--------



The **import-rib protocol isis** command imports public network or other VPN instance routes to a VPN instance routing table.

The **undo import-rib protocol isis** command restores the default configuration.



By default, public network or other VPN instance routes are not imported to VPN instance routing tables.


Format
------

**import-rib** { **public** | **vpn-instance** *vpn-instance-name* } **protocol** **isis** *process-id* [ **valid-route** ] [ **route-policy** *route-policy-name* ]

**undo import-rib** { **public** | **vpn-instance** *vpn-instance-name* } **protocol** **isis** *process-id* [ **valid-route** ] [ **route-policy** *route-policy-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **public** | Indicates the public network instance. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **protocol** | Specifies a protocol type of route to be imported to a VPN instance routing table. | - |
| **isis** *process-id* | Imports IS-IS routes of the specified process. | The value is an integer ranging from 1 to 4294967295. |
| **valid-route** | Imports valid routes of the corresponding route type. | - |
| **route-policy** *route-policy-name* | Specifies a route-policy to filter routes to be imported. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



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

Exercise caution when importing public network routes or routes of other VPN instances to a specified VPN instance to prevent loops caused by manual configurations.After a policy for importing routes is configured using the route-policy parameter in the command, only the network segment routes that meet the policy can be imported to the specified VPN instance. This prevents the device from passively importing unnecessary routes. If no policy is specified for importing routes, a large number of unexpected routes may be imported. As a result, the number of routes exceeds the upper limit or the memory is overloaded.

**Precautions**



If you run the **import-rib public** command without specifying valid-route, the system imports all routes of the specified type from the public network instance to the corresponding VPN instance's routing table. If these routes are preferentially selected, they are advertised to other devices in the VPN instance and delivered to the private IPv4 routing table to guide traffic forwarding.If the valid-route parameter is specified, the system imports valid routes of the specified type from the public network to the VPN routing table of the corresponding type. If these routes are preferentially selected, they are advertised to other devices on the VPN and delivered to the private IPv4 routing table to guide traffic forwarding.When configuring route-policy route-policy-name, you can run this command to match the outbound interface, ACL list of the next hop address of IP routing information, ACL list of the next hop address of IP routing information, route cost, route type, route tag, route protocol type, and route priority. You cannot set the behavior.If the referenced policy contains unsupported attribute matching or setting behavior, unexpected results may occur.




Example
-------

# Configure the device to import public network IS-IS routes to the VPN instance vrf1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv4-family
[*HUAWEI-vpn-instance-vrf1] import-rib public protocol isis 1 valid-route

```