Configuring Routing Policies on a BGP Route Receiver
====================================================

This section describes how to configure routing policies on a BGP route receiver.

#### Context

Perform the following operations on a BGP route receiver:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* *matchMode* **node** *node*
   
   
   
   The node of a routing policy is created, and the view of the routing policy is displayed.
3. Run one of the following commands as needed to configure a filtering rule for the routing policy on the BGP route receiver.
   
   
   * To match an AS\_Path list, run the [**if-match as-path-filter**](cmdqueryname=if-match+as-path-filter) *as-path-acl-number* &<1-16> command.
   * To match a community attribute list, run the [**if-match community-filter**](cmdqueryname=if-match+community-filter) { *basic-comm-filter-num* [ **whole-match** ] | *ext-comm-filter-num* } &<1-16> command.
   * To match a route cost, run the [**if-match cost**](cmdqueryname=if-match+cost) *value* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The route attribute configured for a BGP route must be the same as that of the route advertised by a BGP route sender.
4. Perform the following steps as required:
   
   
   * Run the [**apply qos-local-id**](cmdqueryname=apply+qos-local-id) *qos-local-id* command to apply a QoS policy to the route that meets the matching rule in the routing policy.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When the QoS policy ID, configured by **apply qos-local-id** *qos-local-id*, is applied to QPPB, the ID can be configured within the range of the QoS policy ID using **qos-local-id** *qos-local-id* **behavior** *behavior-name*.
   * Run the [**apply ip-precedence**](cmdqueryname=apply+ip-precedence) *ip-precedence* command to apply IP precedence to the route that meets the matching rule in the routing policy.
   
   A routing policy consists of multiple nodes. Each node comprises multiple **if-match** and **apply** clauses. The **if-match** clauses define matching rules of a node. The **apply** clauses define QoS behaviors to be performed on the routes that match the matching rule.
   
   You can configure multiple **if-match** clauses for a node. The relationship between these rules is "AND". This means that a route passes the filtering only when it meets all the matching rules.
   
   The relationship between routing policy nodes is "OR". That is, if a route matches a node of a routing policy, it matches the routing policy. If none of the routing policy nodes is matched, the route does not match the routing policy.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   BGP is enabled and the BGP view is displayed.
7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name* **import**
   
   
   
   The routing policy is applied to the routes sent from the peer (route sender).
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Ensure that BGP peer relationships have been set up before the routing policy is applied.
8. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
   
   
   
   The BGP-IPv6 unicast address family view is displayed.
9. Run [**ipv6 qppb**](cmdqueryname=ipv6+qppb)
   
   
   
   The import policy of a BGP peer is enabled to support the IPv6 QPPB attribute.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After this step is performed, the BGP IPv6 routes delivered to the RM module carry QoS attributes and support functions such as traffic statistics collection.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.