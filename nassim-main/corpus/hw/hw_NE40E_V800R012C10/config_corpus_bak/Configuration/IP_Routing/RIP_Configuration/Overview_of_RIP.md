Overview of RIP
===============

RIP protocol can implement the interworking of small and
medium-sized networks.

#### Definition

Routing Information Protocol (RIP) is a simple Interior Gateway Protocol (IGP). RIP is used in small-scale networks, such as campus networks and simple regional networks.

As a distance-vector routing protocol, RIP exchanges routing information through User Datagram Protocol (UDP) packets with port number 520.

RIP employs the hop count as the metric to measure the distance to the destination. In RIP, by default, the number of hops from the Router to its directly connected network is 0; the number of hops from the Router to a network that is reachable through another Router is 1, and so on. The hop count (the metric) equals the number of Routers along the path from the local network to the destination network. To speed up route convergence, RIP defines the hop count as an integer that ranges from 0 to 15. A hop count that is greater than or equal to 16 is classified as infinite, indicating that the destination network or host is unreachable. Due to the hop limit, RIP is not applicable to large-scale networks.

RIP has two versions:

* RIP version 1 (RIP-1), a classful routing protocol
* RIP version 2 (RIP-2), a classless routing protocol

RIP supports split horizon, poison reverse, and triggered update, which improves the performance and prevents routing loops.


#### Purpose

As the earliest IGP, RIP is used in small and medium-sized networks. Its implementation is simple, and the configuration and maintenance of RIP are easier than those of Open Shortest Path First (OSPF) and Intermediate System-to-Intermediate System (IS-IS). Therefore, RIP is widely used on live networks.