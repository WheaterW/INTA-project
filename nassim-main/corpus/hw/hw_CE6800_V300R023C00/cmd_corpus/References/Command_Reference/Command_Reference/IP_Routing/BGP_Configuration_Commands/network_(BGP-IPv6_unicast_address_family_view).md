network (BGP-IPv6 unicast address family view)
==============================================

network (BGP-IPv6 unicast address family view)

Function
--------



The **network** command imports routes to the BGP routing table and advertises them to peers.

The **undo network** command cancels the configuration.



By default, BGP does not import routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**network** *ipv6-address* *prefix-length* [ **route-policy** *route-policy-name* ]

**undo network** *ipv6-address* *prefix-length*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a route to be imported by BGP. | The format is X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the mask length of an IPv6 address. If no mask length is specified, the IP address is considered as a classful address. | It is an integer ranging from 0 to 128. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy that is used for route advertisement. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP itself cannot discover routes. Instead, it imports routes discovered by other protocols (such as an IGP or static routes) to the BGP routing table. These imported routes then are transmitted within an AS or between ASs. Before adding routes to the BGP routing table, BGP can filter them based on the routing protocol. Alternatively, if routes in the local routing table need to be manually added to the BGP routing table and then advertised, you can use the **network** command.The Origin attribute of the routes imported to the BGP routing table using the **network** command is IGP.If a route with a specific prefix or mask is added to the BGP routing table using the **network** command, this route is the optimal route selected from all types of protocol routes. Unlike the **network** command, the **import-route** command is used to add all routes of a specified protocol, such as RIP, OSPF, IS-IS, static routes, or direct routes to the BGP routing table.

**Precautions**



Using the **network** command, you can advertise exactly matched routes. That is, routes can be correctly advertised only when the specified destination address and prefix length are the same as those in the local IP routing table. If the network mask is not specified, routes are exactly matched based on the natural network segment.When running the **undo network** command to delete the existing configuration, you need to specify the correct mask.If load balancing routes need to be imported, only the first route in the IP routing table can be imported.If the same route is imported between different protocols, the loop prevention attribute of the route is lost, causing loops. To prevent this problem, you are advised to specify a routing policy when importing routes.If **route-policy** *route-policy-name*is configured, the following items can be matched: IPv4 ACLs, AS\_Path filters, route costs, destination addresses, outbound interfaces, MPLS labels, next hop addresses, next hop addresses of IPv6 routes, next-hop prefix list of routing information, next-hop prefix list based on IPv6 routing information, route preference, destination prefix list of IP routing information, destination prefix list of IPv6 routing information, route modulo operation, RD attribute filter, route source IP address ACL list, route source IPv6 address ACL list, route source IP address prefix list, route source IPv6 address prefix list, routing protocol type, route type, and route tag. The following attributes can be set: BGP Large-Community attribute, AIGP value, AS\_Path attribute, BGP community attribute, MED of BGP routes, color extended community attribute of BGP routes, SoO extended community attribute of BGP routes, MPLS label, local preference of BGP routes, route origin, and the preferred value of BGP routes.If the referenced policy contains unsupported attribute matching or setting behaviors, unexpected results may occur. For some attribute matching behaviors, the device may display warning-level messages.




Example
-------

# Configure BGP to advertise the local route 2001:DB8:1::1/64.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] network 2001:DB8:1::1 64

```