network (BGP view/BGP-IPv4 unicast address family view)
=======================================================

network (BGP view/BGP-IPv4 unicast address family view)

Function
--------



The **network** command imports routes to the BGP routing table and advertises them to peers.

The **undo network** command cancels the configuration.



By default, BGP does not import routes.


Format
------

**network** { *ipv4-address* [ *mask* | *mask-length* ] } [ **route-policy** *route-policy-name* ]

**undo network** { *ipv4-address* [ *mask* | *mask-length* ] }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a route to be imported by BGP. | The value is in the dotted decimal format. |
| *mask* | Specifies an IP address mask. If no mask is specified, the IP address is considered as a classful address. | It is in dotted decimal notation. |
| *mask-length* | Specifies the mask length of an IP address. If no mask length is specified, the IP address is considered as a classful address. | The value is an integer in the range from 0 to 32. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy that is used for route advertisement. | The value is a string of 1 to 200 case-sensitive characters. It cannot contain spaces. If spaces are used, the string must start and end with double quotation marks ("). |



Views
-----

BGP-IPv4 unicast address family view,BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP itself cannot discover routes and needs to import routes discovered by other protocols, such as IGP routes or static routes, into the BGP routing table. These imported routes can be transmitted within an AS or between ASs. When importing routes, you can filter routes based on different routing protocols. When you need to statically add the routes in the local routing table to the BGP routing table and advertise the routes to the peer, run the **network** command.The Origin attribute of the routes that are added to the BGP routing table through the **network** command is IGP.A route with the specified prefix and mask is added to the BGP routing table using the **network** command. This route is the optimal route selected from the routes of various routing protocols. The **import-route** command is used to add routes of a specified protocol, such as RIP routes, OSPF routes, IS-IS routes, static routes, or direct routes, to the BGP routing table.If the same route is imported between different protocols, the loop prevention attribute of the route is lost, which may lead to routing loops. To prevent this problem, you are advised to specify a route-policy when importing routes.

**Precautions**

Using the **network** command, you can advertise exactly matched routes. That is, routes can be correctly advertised only when the specified destination address and prefix length are the same as those in the local IP routing table. If the network mask is not specified, routes are exactly matched based on the natural network segment.When running the **undo network** command to delete the existing configuration, you need to specify the correct mask.If load balancing routes need to be imported, only the first route in the IP routing table can be imported.If the same route is imported between different protocols, the loop prevention attribute of the route is lost, causing loops. To prevent this problem, you are advised to specify a routing policy when importing routes.If **route-policy** *route-policy-name*is configured, the following items can be matched: IPv4 ACLs, AS\_Path filters, route costs, destination addresses, outbound interfaces, MPLS labels, next hop addresses, next hop addresses of IPv6 routes, next-hop prefix list of routing information, next-hop prefix list based on IPv6 routing information, route preference, destination prefix list of IP routing information, destination prefix list of IPv6 routing information, route modulo operation, RD attribute filter, route source IP address ACL list, route source IPv6 address ACL list, route source IP address prefix list, route source IPv6 address prefix list, routing protocol type, route type, and route tag. The following attributes can be set: BGP Large-Community attribute, AIGP value, AS\_Path attribute, BGP community attribute, MED of BGP routes, color extended community attribute of BGP routes, SoO extended community attribute of BGP routes, MPLS label, local preference of BGP routes, route origin, and the preferred value of BGP routes.If the referenced policy contains unsupported attribute matching or setting behaviors, unexpected results may occur. For some attribute matching behaviors, the device may display warning-level messages.


Example
-------

# Configure BGP to import the local route 10.0.0.0/16.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] network 10.0.0.0 255.255.0.0

```