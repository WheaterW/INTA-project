Understanding the Route-Policy
==============================

A route-policy is used to match routes or route attributes, and to change route attributes when matching conditions are met. Matching conditions can be ACLs, IP prefix lists, AS\_Path filters, Community filters, Extcommunity filters, or RD filters. They can match certain attributes of specified routes or change the attributes of routes when the matching conditions are met.

A route-policy consists of multiple nodes. Each node consists of one or multiple clauses:

* **if-match** clauses: define the matching rules that are used in a route-policy to match certain route attributes.
* **apply** clauses: specify actions taken to modify some attributes of matching routes.
* **goto next-node** clauses: further match routes against a specified node if the routes match an existing node.

#### Composition of a Route-Policy

As shown in [Figure 1](#EN-US_CONCEPT_0000001176663527__fig877514305618), a route-policy consists of the node ID, matching mode, if-match clause, apply clause, and goto next-node clause.**Figure 1** Composition of a route-policy  
![](figure/en-us_image_0000001176743445.png)

1. **Node ID**: A route-policy can consist of multiple nodes and filter routes based on either of the following rules:
   * Sequential match: A device checks entries in ascending order by node ID. Specifying the node IDs in a required order is recommended.
   * Unique match: The relationship among the nodes of a route-policy is "OR". If a route matches one node, the route matches the route-policy and will not be matched against a next node.
2. **Matching mode**: Either permit or deny mode can be used.
   * **permit**: indicates the permit mode of a node. If a route matches the if-match clauses of the node in permit mode, the apply clauses of the node are executed, and the route will not be matched against a next node. If the route does not match the if-match clauses of the node, the device continues to match the route against a next node.
   * **deny**: indicates the deny mode of a node. In deny mode, apply clauses are not executed. If a route matches all if-match clauses of the node, the route is rejected and is not matched against a next node. If the entry does not match if-match clauses of the node, the device continues to match the route against a next node.![](public_sys-resources/note_3.0-en-us.png) 
   
   To allow other routes to pass through, a route-policy that contains no if-match or apply clause in the permit mode is usually configured for a node after multiple nodes in the deny mode are configured.
3. **if-match** clause: defines some matching conditions.
   
   Each node of a route-policy can comprise multiple or none **if-match** clauses. By default, if the address family that a route belongs to does not match that specified in an if-match clause of a route-policy, the route matches the route-policy. Take a route-policy node in permit mode (permit node for short) as an example. If no if-match clause is configured for the permit node, all IPv4 and IPv6 routes are considered to match this node. If the permit node is configured with if-match clauses for filtering IPv4 routes only, IPv4 routes that match the if-match clauses and all IPv6 routes are considered to match this node. If the permit node is configured with if-match clauses for filtering IPv6 routes only, IPv6 routes that match the if-match clauses and all IPv4 routes are considered to match this node. This implementation also applies to a deny node.
   
   When the default configuration is used, you are not advised to use the same route-policy to filter both IPv4 and IPv6 routes. Otherwise, services may be interrupted in the following scenarios:
   
   * For the same route-policy, some nodes apply only to IPv4 routes and some nodes apply only to IPv6 routes.
   * A route-policy applies only to IPv4 routes but is used by IPv6 protocols.
   * A route-policy applies only to IPv6 routes but is used by IPv4 protocols.
   
   If you want to use the same route-policy to filter both IPv4 and IPv6 routes, you can run the **route-policy address-family mismatch-deny** command to change the default behavior of the route-policy. After this configuration completes, if the address family that a route belongs to does not match that specified in an if-match clause of the route-policy, the route fails to match the route-policy. Take a permit node as an example. If no **if-match** clause is configured for the permit node, all IPv4 and IPv6 routes are considered to match this node. If the permit node is configured with only an **if-match** clause for filtering IPv4 routes, only IPv4 routes that match the **if-match** clause are considered to match this node, and no IPv6 routes match this node. If the permit node is configured with only an **if-match** clause for filtering IPv6 routes, only IPv6 routes that match the **if-match** clause are considered to match this node, and no IPv4 routes match this node. This implementation also applies to a deny node.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If an **if-match** clause of a node matches routes based on information such as the next hop address or direct source of a route, the node compares the address family corresponding to the next hop address or direct source of the route with that corresponding to the **if-match** clause.
4. **apply** clause: specifies an action. When a route matches a route-policy, a device sets some attributes for the route based on the apply clause.
   
   Each node of a route-policy can contain multiple apply clauses or no apply clause at all. No apply clause needs to be configured if routes are to be filtered but their attributes do not need to be set.
5. **goto next-node clause**: further matches routes against a specified node if the routes match an existing node.


#### Matching Results of a Route-Policy

The matching results of a route-policy are obtained based on the following:

* Matching mode (permit or deny) of a node
* Matching rules (either permit or deny) contained in the if-match clause (such as ACLs or IP prefix lists)

[Table 1](#EN-US_CONCEPT_0000001176663527__tab_dc_vrp_route-policy_feature_001402) describes matching results.

**Table 1** Matching results of a route-policy
| Rule (Contained in if-match Clauses) | Mode (Matching Mode of a Node) | Matching Result |
| --- | --- | --- |
| **permit** | **permit** | * Once routes match the if-match clauses of a node, the routes match the route-policy, indicating that the matching is complete. * If routes do not match the if-match clauses of a node, a device continues to match the routes against a next node in the route-policy. |
| **deny** | * Once routes match the if-match clauses of a node, the routes are rejected, indicating that the matching is complete. * If routes do not match the if-match clauses of a node, a device continues to match the routes against a next node in the route-policy. |
| **deny** | **permit** | Routes are matched against a next node of the route-policy, regardless of whether the routes match an existing node.  NOTE:  If all if-match clauses and nodes of the route-policy are in the deny mode, all routes are rejected. |
| **deny** |


![](public_sys-resources/note_3.0-en-us.png) 

By default, all unmatched routes are rejected by the route-policy. If more than one node is defined in a route-policy, at least one of them must be in permit mode, preventing the following problems:

* If a route fails to match any of nodes in a route-policy, the route is rejected.
* If all nodes in the route-policy are in deny mode, all routes are rejected.