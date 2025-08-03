(Optional) Further Matching Routes Against a Specified Node
===========================================================

(Optional) Further Matching Routes Against a Specified Node

#### Context

The relationship between the matching rules of nodes in the same route-policy is OR. Specifically, if a route matches a node, it matches the route-policy and is no longer matched against other nodes. If you need to match routes against two or more nodes in a route-policy, configure a route-policy and use it to match the routes against a specified node if the routes match an existing node.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the route-policy view.
   
   
   ```
   [route-policy](cmdqueryname=route-policy) route-policy-name matchMode node node
   ```
3. Configure the route-policy to further match routes against a specified node if the routes match an existing node.
   
   
   ```
   [goto next-node](cmdqueryname=goto+next-node) [ node ]
   ```
   
   
   
   If *node* is not specified in the command, the routes will be further matched against a node next to an existing node by default.
   
   If *node* specified in the command does not exist, the routes will be further matched against a node next to the specified node by default. If the next node of the specified node does not exist either, the routes fail to match the route-policy, and no apply clause will be executed for the routes.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```