Understanding IPv6 Static Routes
================================

A routing device forwards data packets over routes. The routes can be manually configured or automatically calculated using a dynamic routing algorithm. Static routes are manually configured. Compared with using dynamic routes, using static routes consumes less bandwidth and does not consume device resources to calculate, analyze, and update routes.

Compared with dynamic routes, static routes have the disadvantage that if a network fault occurs or the topology changes, static routes can only be manually adjusted but cannot automatically change.

A static route may contain the destination address, mask length, outbound interface name, and next-hop address.

#### Destination Address and Mask Length

The destination address in an IPv6 static route is a 32-digit hexadecimal number. The mask length is the number of consecutive 1s in the mask and ranges from 0 to 128.


#### Outbound Interface and Next-Hop IP Address

When configuring a static route, you can specify an outbound interface only, a next-hop IP address only, or both. Actually, a next-hop IP address must be explicitly specified for each route. Before sending a packet, a device searches its routing table for a route matching the destination IP address in the packet by following the longest match rule. The corresponding link-layer address can be found and packets can be forwarded only after a next-hop IP address is specified. Rules for specifying an outbound interface are as follows:

* When a P2P interface is specified as an outbound interface, this operation also implicitly specifies a next-hop IP address. This is because the IP address of the interface directly connected to the outbound interface is used as the next-hop IP address.
* Non-Broadcast Multiple-Access (NBMA) interfaces apply to point-to-multipoint (P2MP) networks. In addition to IP routes, mappings between IP and link-layer addresses must be established. In this case, next-hop IP addresses must be specified.

* When configuring a static route, you are recommended not to specify a broadcast interface (for example, an Ethernet interface) as an outbound interface. Because broadcasting involves multiple next hops, using such an outbound interface leads to difficulty in determining a correct next hop. In applications, if a broadcast interface (for example, an Ethernet interface) must be used as an outbound interface, a next-hop IP address must also be specified.