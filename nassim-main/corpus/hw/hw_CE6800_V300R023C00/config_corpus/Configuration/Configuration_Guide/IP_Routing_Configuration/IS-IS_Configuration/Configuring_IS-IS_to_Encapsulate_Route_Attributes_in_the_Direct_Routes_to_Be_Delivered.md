Configuring IS-IS to Encapsulate Route Attributes in the Direct Routes to Be Delivered
======================================================================================

Configuring IS-IS to Encapsulate Route Attributes in the Direct Routes to Be Delivered

#### Context

After IS-IS is enabled on directly connected interfaces, it delivers a direct route to the forwarding table for each of the interfaces. By default, the interface cost and administrative tag of each direct route that IS-IS delivers are both 0. To ensure that the direct routes to be delivered inherit the interface cost and administrative tag configured on the involved IS-IS interface, configure IS-IS to encapsulate route attributes in these routes.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an IS-IS process, and enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ] [ vpn-instance vpn-instance-name ]
   ```
3. Configure IS-IS to encapsulate route attributes in the direct routes to be delivered.
   
   
   ```
   [direct-routes protocol-attribute-update](cmdqueryname=direct-routes+protocol-attribute-update)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```