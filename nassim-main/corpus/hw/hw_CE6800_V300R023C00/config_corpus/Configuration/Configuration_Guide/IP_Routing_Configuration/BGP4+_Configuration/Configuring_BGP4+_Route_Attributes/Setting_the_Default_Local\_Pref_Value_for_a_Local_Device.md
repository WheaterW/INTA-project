Setting the Default Local\_Pref Value for a Local Device
========================================================

Setting the Default Local\_Pref Value for a Local Device

#### Context

The Local\_Pref attribute is used to determine the optimal route when traffic leaves an AS. When a BGP4+ device receives multiple routes with the same destination address but different next hops from different IBGP peers, the device selects the route with the largest Local\_Pref value as the optimal route if all other attributes are the same.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
4. Set the default Local\_Pref value for the local device.
   
   
   ```
   [default local-preference](cmdqueryname=default+local-preference) local-preference
   ```
   
   
   
   By default, the Local\_Pref of BGP4+ is 100.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```