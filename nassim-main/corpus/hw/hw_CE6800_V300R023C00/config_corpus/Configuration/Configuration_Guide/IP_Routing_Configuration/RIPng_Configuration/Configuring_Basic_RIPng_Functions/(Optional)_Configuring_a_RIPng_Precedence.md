(Optional) Configuring a RIPng Precedence
=========================================

(Optional) Configuring a RIPng Precedence

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIPng process and enter the RIPng view.
   
   
   ```
   [ripng](cmdqueryname=ripng) [ process-id ]
   ```
3. Configure a RIPng precedence.
   
   
   ```
   [preference](cmdqueryname=preference) { preference | route-policy route-policy-name }
   ```
   
   
   
   The [**preference**](cmdqueryname=preference) command can be used together with a route-policy to set the precedence for policy-based routes.
   
   If the RIPng precedence is changed after RIPng routing information is delivered to the routing management (RM) module, the RM module will update its routing table.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```