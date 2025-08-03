Configuring a Preference Value for IS-IS
========================================

Configuring a Preference Value for IS-IS

#### Context

If multiple routes to the same destination are discovered by different routing protocols running on the same device, the route discovered by the protocol with the highest preference is selected. For example, if both OSPF and IS-IS discover routes to the same network segment, the route discovered by OSPF is selected because OSPF has a higher preference than IS-IS by default. To configure the device to select the route discovered by IS-IS, you can increase the preference of IS-IS to be higher than that of OSPF. Alternatively, you can configure a routing policy for the device to increase the preference value of desired IS-IS routes (matching the routing policy). Such a configuration does not affect other IS-IS routes.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ] 
   ```
3. Configure a preference value for IS-IS.
   
   
   ```
   [preference](cmdqueryname=preference) { preference | route-policy route-policy-name }*
   ```
   
   By default, the preference value of IS-IS is 15. A lower preference value indicates a higher preference.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display this**](cmdqueryname=display+this) command in the IS-IS view to check the preference value of IS-IS.