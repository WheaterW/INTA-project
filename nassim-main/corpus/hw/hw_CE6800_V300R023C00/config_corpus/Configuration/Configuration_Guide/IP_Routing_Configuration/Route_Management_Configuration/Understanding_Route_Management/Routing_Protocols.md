Routing Protocols
=================

Route selection and packet forwarding are the main functions of a routing device. To implement the two functions, routing protocols are required. Routing protocols are necessary to implement these two functions, and they are rules used by routing devices to discover and add routes, as well as maintain routing tables for packet forwarding.

#### Differences Between Static and Dynamic Routes

Routes are classified into the following types according to their origins:

* Direct route: discovered by a data link layer protocol
* Static route: manually configured
* Dynamic route: discovered by a dynamic routing protocolDynamic and static routes have their own advantages and disadvantages. You can determine whether to use static or dynamic routes based on real-world situations. [Table 1](#EN-US_CONCEPT_0000001130622776__table12718927578) describes the advantages and disadvantages of static and dynamic routes.
  
  **Table 1** Advantages and disadvantages of static and dynamic routes
  | Route Type | Advantage | Disadvantage |
  | --- | --- | --- |
  | Static route | Poses low system requirements and is applicable to small-scale networks with simple and stable topologies. | Static routes cannot dynamically adapt to network topology changes; therefore, manual intervention is required. |
  | Dynamic route | Has its own routing algorithm and can automatically adapt to network topology changes. Dynamic routes are applicable to networks with a large number of Layer 3 devices. | In addition to consuming network and system resources, dynamic routes have complex configurations, and they pose higher system requirements than static routes. |


#### Classification of Dynamic Routing Protocols

Dynamic routing protocols are classified based on application ranges and algorithms.

Based on the application range, dynamic routing protocols are classified into the following types:

* Interior Gateway Protocols (IGPs): run within an autonomous system (AS). Common IGPs include the Routing Information Protocol (RIP), Open Shortest Path First (OSPF), and Intermediate System to Intermediate System (IS-IS).
* Exterior Gateway Protocols (EGPs): run between ASs. Border Gateway Protocol (BGP) is the most commonly used EGP.

Based on the type of algorithm used, routing protocols are classified as follows:

* Distance-vector protocols: include RIP and BGP. BGP is also called a path-vector protocol.
* Link-state protocols: include OSPF and IS-IS.

The preceding algorithms mainly differ in route discovery and calculation methods.