Configuring a Preference Value for IPv6 IS-IS
=============================================

Configuring a Preference Value for IPv6 IS-IS

#### Prerequisites

Before configuring a preference value for IPv6 IS-IS, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

If multiple routes to the same destination are discovered by different routing protocols running on the same device, the route discovered by the protocol with the highest preference is selected. For example, if both OSPFv3 and IPv6 IS-IS discover routes to the same network segment, the route discovered by OSPFv3 is selected because OSPFv3 has a higher preference than IPv6 IS-IS by default. To configure the device to select the route discovered by IPv6 IS-IS, you can increase the preference of IPv6 IS-IS to be higher than that of OSPFv3. Alternatively, you can configure a routing policy for the device to increase the preference value of desired IPv6 IS-IS routes (matching the routing policy). Such a configuration does not affect other IPv6 IS-IS routes.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ] 
   ```
3. Configure a preference value for IPv6 IS-IS.
   
   
   ```
   [ipv6 preference](cmdqueryname=ipv6+preference) { preference | route-policy route-policy-name }*
   ```
   
   By default, the preference value of IPv6 IS-IS is 15. A lower preference value indicates a higher preference.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display this**](cmdqueryname=display+this) command in the IS-IS view to check the preference value of IPv6 IS-IS.