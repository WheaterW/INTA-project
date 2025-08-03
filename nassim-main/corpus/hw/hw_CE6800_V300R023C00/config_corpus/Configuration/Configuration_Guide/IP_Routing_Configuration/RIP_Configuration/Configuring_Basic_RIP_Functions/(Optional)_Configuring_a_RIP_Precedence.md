(Optional) Configuring a RIP Precedence
=======================================

(Optional) Configuring a RIP Precedence

#### Context

When routes learned through multiple protocols exist, you can configure the RIP precedence for route selection.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIP process and enter the RIP view.
   
   
   ```
   [rip](cmdqueryname=rip) [ process-id ]
   ```
3. Configure the RIP preference.
   
   
   ```
   [preference](cmdqueryname=preference) { preference | route-policy route-policy-name }
   ```
   
   
   
   The [**preference**](cmdqueryname=preference) command can be used together with a route-policy to set the precedence for routes that match the route-policy.
   
   ![](public_sys-resources/notice_3.0-en-us.png) 
   
   If the RIP precedence is changed after RIP routing information is delivered to the routing management (RM) module, the RM module re-updates the routing table.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```