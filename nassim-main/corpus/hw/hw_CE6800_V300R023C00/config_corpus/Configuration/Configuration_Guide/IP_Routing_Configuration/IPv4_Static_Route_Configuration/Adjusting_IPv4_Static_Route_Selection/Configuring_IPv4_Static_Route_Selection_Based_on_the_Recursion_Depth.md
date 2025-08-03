Configuring IPv4 Static Route Selection Based on the Recursion Depth
====================================================================

Configuring IPv4 Static Route Selection Based on the Recursion Depth

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure static route selection based on the recursion depth.
   
   
   ```
   [ip route-static selection-rule relay-depth](cmdqueryname=ip+route-static+selection-rule+relay-depth)
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   A route whose recursion depth is greater than 10 is inactive. Recursion depth is the number of route lookups involved during route recursion. The recursion depth increments by one each time a recursive route lookup is performed.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```