Configuring a Route-Policy Related to the Large-Community Attribute
===================================================================

Before configuring the Large-Community attribute for routes, configure a route-policy in which the Large-Community attribute is applied.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**route-policy**](cmdqueryname=route-policy+node) *route-policy-name* *matchMode* **node** *node*
   
   
   
   A route-policy with a node is created, and the route-policy view is displayed.
3. (Optional) Configure filtering conditions (if-match clauses) for the route-policy. Large-Community values can be added only to the BGP routes that pass the filtering, and the Large-Community values of only these routes can be modified.
   
   
   
   For details, see [(Optional) Configuring an if-match Clause](dc_vrp_route-policy_cfg_0009.html).
4. Run [**apply large-community**](cmdqueryname=apply+large-community+additive+overwrite+delete) { *aa:bb:cc* } &<1-16> { **additive** | **overwrite** | **delete** } or [**apply large-community-list**](cmdqueryname=apply+large-community-list+additive+overwrite+delete) *large-community-list-name* { **additive** | **overwrite** | **delete** }
   
   
   
   Large-Community values are configured for BGP routes.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.