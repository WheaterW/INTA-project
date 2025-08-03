Overview of RIP
===============

Overview of RIP

#### Definition

Routing Information Protocol (RIP) is a simple Interior Gateway Protocol (IGP).

RIP employs the hop count to measure the distance to a destination. The distance is called the metric value. In RIP, the default hop count from a routing device to its directly connected network is 0, and the hop count from a routing device to a network that is reachable through another routing device is 1. The rest can be deduced by analogy. The hop count (metric value) equals the number of routing devices along the path from the local network to the destination network. To restrict the convergence time, RIP requires that the metric value be an integer between 0 and 15. A metric value greater than or equal to 16 is defined as infinite, which means the destination network or host is unreachable. As such, RIP is not suitable for large-scale networks.


#### Purpose

RIP is one of the earliest IGPs and is designed for small- and medium-sized networks using the same technology. RIP is still widely used because it is easier to implement, configure, and maintain than OSPF and IS-IS.