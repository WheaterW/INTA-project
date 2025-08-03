(Optional) Setting the OSPFv3 Preference
========================================

(Optional) Setting the OSPFv3 Preference

#### Context

Routing protocols may share and select the same routing information if a device runs multiple dynamic routing protocols at the same time. In this case, you can adjust the preferences of some specific routing protocols, so that when multiple routing protocols discover the same route, the route discovered by the routing protocol with the highest preference is selected.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Set the OSPFv3 preference.
   
   
   ```
   [preference](cmdqueryname=preference) [ ase ] { preference | route-policy route-policy-name } *
   ```
   * **ase**: indicates the AS external routes for which a preference is set.
   * **preference**: specifies a preference value for OSPFv3 routes. The smaller the value, the higher the preference.
   * **route-policy** *route-policy-name*: specifies a route-policy to filter routes so that the set preference is applied to the filtered routes.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```