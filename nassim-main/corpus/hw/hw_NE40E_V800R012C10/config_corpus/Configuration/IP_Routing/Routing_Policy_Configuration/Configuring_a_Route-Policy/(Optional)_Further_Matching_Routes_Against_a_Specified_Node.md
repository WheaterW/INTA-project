(Optional) Further Matching Routes Against a Specified Node
===========================================================

A route-policy can be configured to match routes against two or more nodes.

#### Context

The relationship between the matching rules of nodes in the same route-policy is OR. Specifically, if a route matches a node, it matches the route-policy and is no longer matched against other nodes. If you need to match the route against two or more nodes, configure a route-policy and use it to match the route against a specified node after the route matches the current node.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **permit** | **deny** } **node** *node*
   
   
   
   The route-policy view is displayed.
3. Run [**goto next-node**](cmdqueryname=goto+next-node) [ *node* ]
   
   
   
   The route-policy is configured to further match routes against a specified node after the routes match the current node.
   
   If *node* is not specified in the command, the route will be further matched against the next node of the current node by default.
   
   
   
   If the *node* specified in the command does not exist, the route will be further matched against the next node of the specified node by default. If the next node of the specified node does not exist either, the route fails to match the route-policy, and no **apply** clause will be applied to the route.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.