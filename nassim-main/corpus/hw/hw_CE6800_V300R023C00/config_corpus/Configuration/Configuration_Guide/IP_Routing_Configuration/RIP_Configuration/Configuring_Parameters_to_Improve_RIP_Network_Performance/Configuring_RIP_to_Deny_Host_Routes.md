Configuring RIP to Deny Host Routes
===================================

Configuring RIP to Deny Host Routes

#### Context

Routing devices on the live network may receive a large number of host routes from the same network segment. While such routes do not have a major effect on routing and addressing, they consume a large amount of network resources. After RIP is configured to deny host routes, a routing device can reject the received host routes.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIP process and enter the RIP view.
   
   
   ```
   [rip](cmdqueryname=rip) [ process-id ]
   ```
3. Configure RIP to deny host routes.
   
   
   ```
   [undo host-route](cmdqueryname=undo+host-route)
   ```
   
   
   
   By default, a device is allowed to accept host routes.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```