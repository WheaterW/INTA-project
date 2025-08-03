Route Summarization
===================

Route Summarization

#### Context

On large-scale networks, the RIPng routing table of each device contains a large number of routing entries, which consumes lots of system resources. In addition, if a specific link connected to a device within an IP address range frequently alternates between up and down, route flapping occurs.

RIPng route summarization was introduced to address these problems, enabling a device to summarize routes destined for different subnets of a network segment into one route destined for one network segment and then advertise the summary route to other network segments. RIPng route summarization reduces the number of routes in the routing table, minimizes system resource consumption, and prevents route flapping.


#### Implementation

RIPng route summarization is implemented on interfaces. After RIPng route summarization is enabled on an interface, the interface summarizes routes based on the longest matching rule and the metric of the summary route is the minimum metric among all the original routes.

For example, RIPng can advertise two routes, 2001:db8:11::24 (metric = 2) and 2001:db8:12::34 (metric = 3), through an interface. After route summarization is configured on the interface, both routes can be summarized into one: 2001:db8::0/16 (metric = 2).