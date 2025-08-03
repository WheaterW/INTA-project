Creating a Route-Policy
=======================

By applying a route-policy, you can set attributes for the imported routes as required.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **permit** | **deny** } **node** *node*
   
   
   
   A route-policy node is created, and the route-policy view is displayed.
   
   
   
   Either of the following parameters can be used to define a matching mode:
   
   * **permit**: configures the permit mode for the node. If a route matches the **if-match** clauses of the node in permit mode, the **apply** clauses of the node are executed, and the route will not be matched against a next node. If the route does not match the **if-match** clauses of the node, the device continues to match the route against a next node.
   * **deny**: configures the deny mode for the node. In deny mode, **apply** clauses are not executed. If a route matches all **if-match** clauses of the node in deny mode, the route is rejected and is not matched against a next node. If the route does not match **if-match** clauses of the node, the device continues to match the route against a next node.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   By default, the NE40E considers that each route that does not match a route-policy is rejected by the route-policy. If more than one node is defined in a route-policy, at least one should be set to permit mode.
   
   When a route-policy is used to filter routes, if a route does not match the matching rules of all nodes in the route-policy, the route is rejected by the route-policy. If all nodes in a route-policy are in deny mode, all routes are rejected by the route-policy.
   
   When a route-policy is used to filter routes, the node with the smallest node ID is matched against first.
3. (Optional) Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. (Optional) Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* **address-family** **mismatch-deny**
   
   
   
   The device is configured to deny routes if the address family that the routes belong to does not match that specified in an **if-match** clause of the route-policy.
   
   
   
   By default, if the address family that a route belongs to does not match that specified in an **if-match** clause of a route-policy, the route matches the route-policy. Take a route-policy node in permit mode (permit node for short) as an example. If no **if-match** clause is configured for the permit node, all IPv4 and IPv6 routes are considered to match this node. If the permit node is configured with **if-match** clauses for filtering IPv4 routes only, IPv4 routes that match the **if-match** clauses and all IPv6 routes are considered to match this node. If the permit node is configured with **if-match** clauses for filtering IPv6 routes only, IPv6 routes that match the **if-match** clauses and all IPv4 routes are considered to match this node. This implementation also applies to a deny node. When the default configuration is used, you are not advised to use the same route-policy to filter both IPv4 and IPv6 routes. Otherwise, services may be interrupted.
   
   If you want to use the same route-policy to filter both IPv4 and IPv6 routes, you can run the [**route-policy address-family mismatch-deny**](cmdqueryname=route-policy+address-family+mismatch-deny) command to change the default behavior of the route-policy in order to prevent a potential service interruption. After this configuration completes, if the address family that a route belongs to does not match that specified in an **if-match** clause of the route-policy, the route fails to match the route-policy. Take a permit node as an example. If no **if-match** clause is configured for the permit node, all IPv4 and IPv6 routes are considered to match this node. If the permit node is configured with **if-match** clauses for filtering IPv4 routes only, only IPv4 routes that match the **if-match** clauses are considered to match this node, and no IPv6 routes match this node. If the permit node is configured with **if-match** clauses for filtering IPv6 routes only, only IPv6 routes that match the **if-match** clauses are considered to match this node, and no IPv4 routes match this node. This implementation also applies to a deny node.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.