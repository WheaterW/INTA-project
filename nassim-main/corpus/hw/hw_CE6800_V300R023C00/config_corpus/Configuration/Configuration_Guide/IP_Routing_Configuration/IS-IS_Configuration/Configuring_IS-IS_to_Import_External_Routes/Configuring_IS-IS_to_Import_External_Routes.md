Configuring IS-IS to Import External Routes
===========================================

Configuring IS-IS to Import External Routes

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Configure IS-IS to import external routes.
   
   
   * Configure IS-IS to import external routes and set a cost for the imported routes.
     ```
     [import-route](cmdqueryname=import-route) { direct | static | { ospf | rip | isis } [ process-id ] | bgp } [ cost-type { external | internal } | cost cost | tag tag | { route-policy route-policy-name } | [ level-1 | level-2 | level-1-2 ] ] *
     ```
   * Configure IS-IS to import external routes and retain the original cost of each imported route.
     ```
     [import-route](cmdqueryname=import-route) { { ospf | rip | isis } [ process-id ] | bgp | direct } inherit-cost [ { level-1 | level-2 | level-1-2 } | tag tag | route-policy route-policy-name ] *
     ```
     
     The protocol from which routes are imported cannot be **static**.
4. (Optional) Configure IS-IS to advertise only some imported external routes to the IS-IS routing domain.
   
   
   
   By default, IS-IS advertises all imported external routes to an IS-IS routing domain. To advertise only some imported external routes to the IS-IS routing domain, perform this step.
   
   
   
   ```
   [filter-policy](cmdqueryname=filter-policy) { acl-number | acl-name acl-name-string | ip-prefix ip-prefix-name | route-policy route-policy-name } export [ direct | static | rip process-id | bgp | ospf process-id | isis process-id ] 
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```