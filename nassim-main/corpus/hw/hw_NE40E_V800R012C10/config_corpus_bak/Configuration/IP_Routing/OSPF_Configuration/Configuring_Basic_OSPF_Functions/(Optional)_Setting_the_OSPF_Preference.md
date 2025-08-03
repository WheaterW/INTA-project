(Optional) Setting the OSPF Preference
======================================

When multiple routing protocols discover routes to the same destination address, you can set the OSPF preference to control the route selection result.

#### Context

If a Router runs multiple dynamic routing protocols at the same time, routing information may be shared and selected among the routing protocols. The system sets a priority for each routing protocol. When multiple routing protocols are used to select routes, the route selected by the routing protocol with a higher priority takes effect.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**preference**](cmdqueryname=preference) [ **ase** | **inter** | **intra** ] { *preference* | { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* } } \*
   
   
   
   A preference is set for OSPF.
   
   
   
   * **ase**: indicates the AS external routes for which a preference is set.
   * **inter**: indicates the inter-area routes for which a preference is set.
   * **intra**: indicates the intra-area routes for which a preference is set.
   * *preference*: specifies a preference value for OSPF routes. The smaller the value, the higher the priority.
   * *route-policy-name*: specifies a route-policy to filter routes so that the preset preference is applied to the matched routes.
   * *route-filter-name*: specifies a route-filter to filter routes so that the preset preference is applied to the matched routes.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.