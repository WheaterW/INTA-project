Overview of Routing Policies
============================

Routing policies can be used to control route advertisement and acceptance.

#### Definition

Routing policies are used to filter routes and control how routes are received and advertised. If route attributes, such as reachability, are changed, the path along which network traffic passes changes accordingly.


#### Purpose

When advertising, receiving, and importing routes, the Router implements certain routing policies based on actual networking requirements to filter routes and change the route attributes. Routing policies serve the following purposes:

* Control route advertising
  
  Only routes that match the rules specified in a policy are advertised.
* Control route receiving
  
  Only the required and valid routes are received, which reduces the routing table size and improves network security.
* Filter and control imported routes
  
  A routing protocol may import routes discovered by other routing protocols. Only routes that satisfy certain conditions are imported to meet the requirements of the protocol.
* Modify attributes of specified routes
  
  To enrich routing information, a routing protocol may import routing information discovered by other routing protocols. Only the routing information that satisfies the conditions is imported. Some attributes of the imported routing information are changed to meet the requirements of the routing protocol.

#### Benefits

Routing policies have the following benefits:

* Control the routing table size, saving system resources.
* Control route receiving and advertising, improving network security.
* Modify attributes of routes for proper traffic planning, improving network performance.


#### Differences Between the Routing Policy and Policy-based Routing

Unlike the routing mechanism that searches the forwarding table for matching routes based on the destination addresses of IP packets, policy-based routing (PBR) is based on the user-defined routing policies. PBR selects routes based on the user-defined routing policies, with reference to the source IP addresses and lengths of incoming packets. PBR can be used to improve security and implement load balancing.

A routing policy and PBR have different mechanisms. [Table 1](#EN-US_CONCEPT_0172366529__en-us_concept_0172354517_tab_feature_000399236701) shows the differences between them.

**Table 1** Differences between the routing policy and PBR
| Routing Policy | Policy-based Routing |
| --- | --- |
| Forwards packets based on destination addresses in the routing table. | Forwards packets based on the policy. The device searches the routing table for packet forwarding only after packets fail to be forwarded based on the policy. |
| Based on the control plane, serves routing protocols and routing tables. | Based on the forwarding plane, serves forwarding. |
| Combines with a routing protocol to form a policy. | Needs to be configured hop by hop to ensure that packets are forwarded based on the policies. |
| Is configured using the **route-policy** command. | Is configured using the **policy-based-route** command. |