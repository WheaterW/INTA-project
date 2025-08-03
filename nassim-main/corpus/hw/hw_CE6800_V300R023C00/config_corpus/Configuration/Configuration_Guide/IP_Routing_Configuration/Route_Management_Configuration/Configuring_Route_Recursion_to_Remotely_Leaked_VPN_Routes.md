Configuring Route Recursion to Remotely Leaked VPN Routes
=========================================================

Configuring Route Recursion to Remotely Leaked VPN Routes

#### Context

The next hops of routes may not be directly reachable. In this case, recursion is required so that such routes can be used for traffic forwarding. You can enable route recursion to remotely leaked VPN routes. If routes are allowed to recurse to remotely leaked VPN routes, the routes correctly inherit the labels and tunnel IDs of the remotely leaked VPN routes, which ensures correct traffic forwarding.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable route recursion to remotely leaked VPN routes.
   
   
   * Enable recursion of all IPv4 routes to remotely leaked VPN routes.
     ```
     [ip route recursive-lookup inherit-label-route enable](cmdqueryname=ip+route+recursive-lookup+inherit-label-route+enable)
     ```
   * Enable recursion of all IPv6 routes to remotely leaked VPN routes.
     ```
     [ipv6 route recursive-lookup inherit-label-route enable](cmdqueryname=ipv6+route+recursive-lookup+inherit-label-route+enable)
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The CE6885-LL in low latency mode does not support this command.
   
   
   
   By default, route recursion to remotely leaked VPN routes is not enabled.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check the configuration.