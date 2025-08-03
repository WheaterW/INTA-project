Configuring a Device to Compare Costs of Inherited Routes for IPv4 Static Route Selection
=========================================================================================

Configuring a Device to Compare Costs of Inherited Routes for IPv4 Static Route Selection

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a device to compare costs of inherited routes for static route selection.
   
   
   ```
   [ip route-static selection-rule compare-inherit-cost](cmdqueryname=ip+route-static+selection-rule+compare-inherit-cost)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```