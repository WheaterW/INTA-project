Route Establishment
===================

Route Establishment

#### Route Classification

There are multiple available forwarding paths between the source and destination nodes of a packet. Different routes indicate different forwarding paths. The following table provides the classification of routes.

**Table 1** Classification of routes in adaptive routing
| Route Type | Forwarding Path | Cost Value Range | Description |
| --- | --- | --- | --- |
| Direct route | - | 0 | Direct route, which is generated on an access port. |
| Local min route | Intra-group shortest path | 1 | A route generated when the egress node advertises a direct route to other network nodes in the group. The cost of the route increments by 1 each time the route is advertised to a new hop. To ensure low latency, packets forwarded within a group can pass through no more than two local links. |
| Local non-min route | Intra-group non-shortest path | [2,1000) |
| Global min route | Inter-group shortest path | [1000,2000) | A route generated when a local route is advertised to a node in a directly connected group through a global link. The cost of the route increments by 1000 when the route is advertised through the global link. |
| Global non-min route | Inter-group non-shortest path | [2000,3000) | A route generated when a global min route is advertised to other groups, except the directly connected group, through a global link. The cost of the route increments by 1000 when the route is advertised through the global link. To ensure low latency, packets forwarded between groups can pass through no more than two global links, and packets in each group can pass through no more than one local link. |



#### Route Configuration

The adaptive routing function is implemented based on BGP. Each group is considered to be an AS and allocated an AS number. EBGP runs between groups, and IBGP runs within a group. Each network node has three types of ports: access port, global port, and local port. Each pair of nodes that are connected between groups establishes a BGP session through the global port. Each pair of nodes that are connected within a group establishes two BGP sessions through the two Layer 3 sub-interfaces of the local port to advertise the shortest path routes and non-shortest path routes, respectively.

Three routing tables are maintained on each network node: a public network routing table, a routing table of a Non-min VPN instance, and a routing table of a Mix VPN instance.

* Public network routing table: contains the routing information of the shortest path.
* Routing table of a Non-min VPN instance: contains the routing information of the non-shortest paths.
* Routing table of a Mix VPN instance: contains the routing information of both the shortest and non-shortest paths.

When configuring route establishment rules, you can configure VPN instances, interface types, routing policies, and BGP route processing to control route advertisement and generate routing tables that comply with the rules on network nodes. In this way, routes for packet forwarding are established on the entire network.

**Table 2** Classification of ports on network nodes
| Port Type | Connected Node | Layer 3 Sub-Interface | Bound VPN Instance |
| --- | --- | --- | --- |
| Access port | Compute node connected to the local device | None | Mix VPN instance |
| Global port | Network nodes in different groups | None | None  It uses the public network routing table to guide packet forwarding. |
| Local port | Network nodes in the same group | Min sub-interface | None  It uses the public network routing table to guide packet forwarding. |
| Non-min sub-interface | Non-min VPN instance |



#### Route Advertisement

After route establishment rules are configured, routing table information is generated through route advertisement. Using route advertisement from the compute node D to compute node S as an example, the processes of route advertisement for different paths are as follows:

* **Intra-group shortest path****Figure 1** Route advertisement for the intra-group shortest path  
  ![](figure/en-us_image_0000001513030470.png)
  1. The access port of Node4 generates direct route information, which is then imported from the routing table of the Mix VPN instance to the public network routing table, with a cost of 0.
  2. Node4 advertises the route to the public network routing tables on Node1, Node2, and Node3, and the cost of the route increments by 1.
  3. The route is imported from the public network routing tables on Node1, Node2, and Node3 to the routing tables of the Mix VPN and Non-min VPN instances on these nodes.
  
  **Table 3** Cost value of the destination node D in the routing table of each involved node
  | Routing Table | Node1 | Node2 | Node3 | Node4 |
  | --- | --- | --- | --- | --- |
  | Public network routing table | Cost = 1 | Cost = 1 | Cost = 1 | Cost = 0 |
  | Routing table of the Non-min VPN instance | Cost = 1 | Cost = 1 | Cost = 1 | - |
  | Routing table of the Mix VPN instance | Cost = 1 | Cost = 1 | Cost = 1 | Cost = 0 |
* **Intra-group non-shortest path****Figure 2** Route advertisement for an intra-group non-shortest path  
  ![](figure/en-us_image_0000001513030462.png)
  1. The access port of Node4 generates direct route information, which is then imported from the routing table of the Mix VPN instance to the public network routing table, with a cost of 0.
  2. Node4 advertises the route to the public network routing tables on Node2 and Node3, and the cost of the route increments by 1.
  3. The route is imported from the public network routing tables on Node2 and Node3 to the routing tables of the Mix VPN and Non-min VPN instances on these nodes.
  4. Node2 and Node3 advertise the route to the public network routing table and routing table of the Non-min VPN instance on Node1, and the cost of the route increments by 1.
  5. The route is imported from the routing table of the Non-min VPN instance on Node1 to the routing table of the Mix VPN instance on Node1.
  
  **Table 4** Cost value of the destination node D in the routing table of each involved node
  | Routing Table | Node1 | Node2 | Node3 | Node4 |
  | --- | --- | --- | --- | --- |
  | Public network routing table | Cost = 2 | Cost = 1 | Cost = 1 | Cost = 0 |
  | Routing table of the Non-min VPN instance | Cost = 2 | Cost = 1 | Cost = 1 | - |
  | Routing table of the Mix VPN instance | Cost = 2 | Cost = 1 | Cost = 1 | Cost = 0 |
* **Inter-group shortest path****Figure 3** Route advertisement for the inter-group shortest path  
  ![](figure/en-us_image_0000001512671310.png)
  1. Route advertisement in the destination group:
     1. The access port of the egress node Node8 generates direct route information, which is then imported from the routing table of the Mix VPN instance to the public network routing table, with a cost of 0.
     2. Node8 advertises the route to the public network routing tables on Node5, Node6, and Node7, and the cost of the route increments by 1.
     3. The route is imported from the public network routing tables on Node5, Node6, and Node7 to the routing tables of the Mix VPN and Non-min VPN instances on these nodes.
  2. Route advertisement in the source group:
     1. Node5 advertises the route to the public network routing table on Node2, and the cost of the route increments by 1000.
     2. The route is imported from the public network routing table on Node2 to the routing table of the Mix VPN instance on Node2.
     3. Node2 advertises the route to the public network routing tables on Node1, Node3, and Node4, and the cost of the route increments by 1.
     4. The route is imported from the public network routing tables on Node1, Node3, and Node4 to the routing tables of the Mix VPN instances on these nodes.
  
  **Table 5** Cost value of the destination node D in the routing table of each involved node
  | Routing Table | Node1 | Node2 | Node3 | Node4 | Node5 | Node6 | Node7 | Node8 |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | Public network routing table | Cost = 1002 | Cost = 1001 | Cost = 1002 | Cost = 1002 | Cost = 1 | Cost = 1 | Cost = 1 | Cost = 0 |
  | Routing table of the Non-min VPN instance | - | - | - | - | Cost = 1 | Cost = 1 | Cost = 1 | - |
  | Routing table of the Mix VPN instance | Cost = 1002 | Cost = 1001 | Cost = 1002 | Cost = 1002 | Cost = 1 | Cost = 1 | Cost = 1 | Cost = 0 |
* **Inter-group non-shortest path**

**Figure 4** Route advertisement for an inter-group non-shortest path  
![](figure/en-us_image_0000001563870421.png)

1. Route advertisement in the destination group:
   1. The access port of the egress node Node12 generates direct route information, which is then imported from the routing table of the Mix VPN instance to the public network routing table, with a cost of 0.
   2. Node12 advertises the route to the public network routing tables on Node9, Node10, and Node11, and the cost of the route increments by 1.
   3. The route is imported from the public network routing tables on Node9, Node10, and Node11 to the routing tables of the Mix VPN and Non-min VPN instances on these nodes.
2. Route advertisement in the transit group:
   1. Node11 advertises the route to the public network routing table on Node6, and the cost of the route increments by 1000.
   2. The route is imported from the public network routing table on Node6 to the routing table of the Mix VPN instance on Node6.
   3. Node6 advertises the route to the public network routing tables on Node5, Node7, and Node8, and the cost of the route increments by 1.
   4. The route is imported from the public network routing tables on Node5, Node7, and Node8 to the routing tables of the Mix VPN instances on these nodes.
3. Route advertisement in the source group:
   1. Node5 advertises the route to the public network routing table on Node4, and the cost of the route increments by 1000.
   2. The route is imported from the public network routing table on Node4 to the routing tables of the Mix VPN and Non-min VPN instances on Node4.
   3. Node4 advertises the route to the routing tables of the Non-min VPN instances on Node1, Node2, and Node3, and the cost of the route increments by 1.
   4. The route is imported from the routing tables of the Non-min VPN instances on Node1, Node2, and Node3 to the routing tables of the Mix VPN instances on these nodes.

**Table 6** Cost value of the destination node D in the routing table of each involved node
| Routing Table | Node1 | Node2 | Node3 | Node4 | Node5 | Node6 | Node7 | Node8 | Node9 | Node10 | Node11 | Node12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Public network routing table | - | - | - | Cost = 2002 | Cost = 1002 | Cost = 1001 | Cost = 1002 | Cost = 1002 | Cost = 1 | Cost = 1 | Cost = 1 | Cost = 0 |
| Routing table of the Non-min VPN instance | Cost = 2003 | Cost = 2003 | Cost = 2003 | Cost = 2002 | - | - | - | - | Cost = 1 | Cost = 1 | Cost = 1 | - |
| Routing table of the Mix VPN instance | Cost = 2003 | Cost = 2003 | Cost = 2003 | Cost = 2002 | Cost = 1002 | Cost = 1001 | Cost = 1002 | Cost = 1002 | Cost = 1 | Cost = 1 | Cost = 1 | Cost = 0 |