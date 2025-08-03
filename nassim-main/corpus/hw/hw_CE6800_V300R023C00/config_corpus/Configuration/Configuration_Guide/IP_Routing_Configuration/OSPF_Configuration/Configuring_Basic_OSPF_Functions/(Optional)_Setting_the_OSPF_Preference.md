(Optional) Setting the OSPF Preference
======================================

(Optional) Setting the OSPF Preference

#### Context

Routing protocols may share and select the same routing information if a device runs multiple dynamic routing protocols at the same time. Therefore, the system sets a preference for each routing protocol. Then, when multiple routing protocols discover the same route, the route discovered by the routing protocol with the highest preference is selected.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
3. Set the OSPF preference.
   
   
   ```
   [preference](cmdqueryname=preference) [ ase | inter | intra ] { preference | route-policy route-policy-name } *
   ```
   
   The default OSPF preference is 10. Parameters in this command are described as follows:
   
   * **ase**: indicates the AS external routes for which a preference is set. If **ase** is specified, the default preference of AS external routes is 150.
   * **inter**: indicates the inter-area routes for which a preference is set.
   * **intra**: indicates the intra-area routes for which a preference is set.
   * *preference*: specifies a preference value for OSPF routes. The smaller the value, the higher the preference.
   * *route-policy-name*: specifies a route-policy to filter routes so that the preset preference is applied to the filtered routes.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```