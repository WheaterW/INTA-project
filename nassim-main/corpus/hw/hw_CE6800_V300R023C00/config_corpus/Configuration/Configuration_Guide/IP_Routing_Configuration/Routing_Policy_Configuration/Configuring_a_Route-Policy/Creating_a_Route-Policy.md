Creating a Route-Policy
=======================

Creating a Route-Policy

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a route-policy node and enter the route-policy view.
   
   
   ```
   [route-policy](cmdqueryname=route-policy) route-policy-name matchMode node node
   ```
   
   
   
   Either of the following parameters can be used to define a matching mode:
   
   * **permit**: configures the permit mode for the node. If a route matches the node, the device performs actions defined by the apply clauses and the matching is complete. If a route does not match the node, the route is matched against the next node.
   * **deny**: configures the deny mode for the node. In deny mode, apply clauses are not executed. If the route matches all if-match clauses of the node, the route is rejected and is not matched against a next node. If a route fails to match any if-match clause of the node, the route is matched against a next node.![](public_sys-resources/note_3.0-en-us.png) 
   
   By default, all unmatched routes are rejected by the route-policy. If more than one node is defined in a route-policy, at least one of them must be in permit mode.
   
   For a route-policy used to filter routes, if a route does not match any node, a route is rejected. If all nodes in a route-policy are in deny mode, all routes are rejected.
   
   When a route-policy is used to filter routes, a node with a smaller value is used first.
3. (Optional) Configure the device to deny routes if the address family of these routes does not match that corresponding to an **if-match** clause of the route-policy.
   
   
   ```
   [route-policy](cmdqueryname=route-policy) route-policy-name address-family mismatch-deny
   ```
   
   
   
   By default, if the address family of routes does not match that corresponding to an **if-match** clause of a route-policy, these routes match the route-policy. Take a route-policy node in permit mode (permit node for short) as an example. If no if-match clause is configured for the permit node, all IPv4 and IPv6 routes are considered to match this node. If the permit node is configured with if-match clauses for filtering IPv4 routes only, IPv4 routes that match the if-match clauses and all IPv6 routes are considered to match this node. If the permit node is configured with if-match clauses for filtering IPv6 routes only, IPv6 routes that match the if-match clauses and all IPv4 routes are considered to match this node. This implementation also applies to a deny node. When the default configuration is used, you are not advised to use the same route-policy to filter both IPv4 and IPv6 routes. Otherwise, services may be interrupted.
   
   If you want to use the same route-policy to filter both IPv4 and IPv6 routes, you can run the [**route-policy address-family mismatch-deny**](cmdqueryname=route-policy+address-family+mismatch-deny) command to change the default behavior of the route-policy. After this configuration completes, if the address family of routes does not match that corresponding to an **if-match** clause of the route-policy, the routes fail to match the route-policy. Take a permit node as an example. If no if-match clause is configured for the permit node, all IPv4 and IPv6 routes are considered to match this node. If the permit node is configured with if-match clauses for filtering IPv4 routes only, only IPv4 routes that match the if-match clauses are considered to match this node, and no IPv6 routes match this node. If the permit node is configured with if-match clauses for filtering IPv6 routes only, only IPv6 routes that match the if-match clauses are considered to match this node, and no IPv4 routes match this node. This implementation also applies to a deny node.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```