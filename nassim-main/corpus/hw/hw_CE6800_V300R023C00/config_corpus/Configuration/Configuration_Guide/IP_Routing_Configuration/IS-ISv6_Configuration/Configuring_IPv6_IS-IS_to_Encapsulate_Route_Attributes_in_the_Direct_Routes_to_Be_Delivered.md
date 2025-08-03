Configuring IPv6 IS-IS to Encapsulate Route Attributes in the Direct Routes to Be Delivered
===========================================================================================

Configuring IPv6 IS-IS to Encapsulate Route Attributes in the Direct Routes to Be Delivered

#### Context

After IPv6 IS-IS is enabled on directly connected interfaces, it delivers a direct route to the forwarding table for each of the interfaces. By default, the interface cost and administrative tag of each direct route that IPv6 IS-IS delivers are both 0. To ensure that the direct routes to be delivered inherit the interface cost and administrative tag configured on the involved IPv6 IS-IS interface, configure IPv6 IS-IS to encapsulate route attributes in these routes.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an IS-IS process, and enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Configure IS-IS to use IS-IS attributes when it delivers direct routes.
   
   
   ```
   [direct-routes protocol-attribute-update](cmdqueryname=direct-routes+protocol-attribute-update)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```