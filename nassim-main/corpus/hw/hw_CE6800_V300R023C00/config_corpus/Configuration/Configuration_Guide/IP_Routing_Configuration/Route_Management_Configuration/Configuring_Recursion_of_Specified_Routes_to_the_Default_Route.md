Configuring Recursion of Specified Routes to the Default Route
==============================================================

Configuring Recursion of Specified Routes to the Default Route

#### Context

The next hops of unicast and multicast static routes may not be directly reachable. In this case, recursion is required so that such routes can be used for traffic forwarding. You can configure whether to allow unicast and multicast static routes to recurse to the default route. By default, unicast static routes cannot recurse to the default route.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable unicast static routes to recurse to the default route.
   
   
   * Enable IPv4 unicast and multicast static routes to recurse to the default route.
     ```
     [ip route recursive-lookup default-route](cmdqueryname=ip+route+recursive-lookup+default-route) protocol { static | msr }
     ```
   * Enable recursion of IPv6 unicast static routes to the default route.
     ```
     [ipv6 route recursive-lookup default-route](cmdqueryname=ipv6+route+recursive-lookup+default-route) protocol { static | msr }
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The CE6885-LL in low latency mode does not support this command.
   
   
   
   By default, unicast static routes cannot recurse to the default route.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check the configuration.