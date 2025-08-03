Configuring BGP4+ Soft Reset
============================

BGP4+ soft reset allows the system to refresh a BGP4+ routing table dynamically without tearing down any BGP4+ connection if routing policies are changed.

#### Context

After a BGP4+ routing policy is changed, you can reset the BGP4+ connection for the new policy to take effect immediately. This, however, interrupts the BGP4+ connection temporarily. BGP4+ route-refresh allows the system to refresh the BGP4+ routing table dynamically without tearing down any BGP4+ connection when a policy is changed.

* If a BGP4+ peer supports route-refresh, you can refresh the routing table by running the [**refresh bgp**](cmdqueryname=refresh+bgp) command to perform a soft reset on the BGP4+ connection.
* If a BGP4+ peer does not support route-refresh, you can run the [**peer keep-all-routes**](cmdqueryname=peer+keep-all-routes) command to reserve all the original routes of the peer. In this manner, the routing table can be updated without resetting the BGP4+ connection.

#### Procedure

* Manually perform a soft reset on a BGP4+ connection with a BGP4+ peer that supports route-refresh.
  
  
  
  Perform the following steps on a BGP4+ device:
  
  
  
  1. (Optional) Enable route-refresh.
     
     
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
     3. Run the [**peer**](cmdqueryname=peer+capability-advertise+route-refresh) { *ipv4-address* | *ipv6-address* | *group-name* } **capability-advertise** **route-refresh** command to enable route-refresh.
     4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  2. Manually perform a soft reset on a BGP4+ connection.
     
     
     
     Run the [**refresh bgp**](cmdqueryname=refresh+bgp+ipv6+all+group+external+internal+export+import) **ipv6** { **all** | *ipv4-address* | *ipv6-address* | **group** *group-name* | **external** | **internal** } { **export** | **import** } command to perform a soft reset on a BGP4+ connection.
     
     To perform a soft reset on a BGP4+ connection, run the preceding command in the user view.
     
     The **external** and **internal** parameters indicate soft resets of EBGP and IBGP connections, respectively.
* Retain all routing updates of a BGP4+ peer that does not support route-refresh.
  
  
  
  Perform the following steps on a BGP4+ device:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+keep-all-routes) { *ipv4-address* | *ipv6-address* | *group-name* } **keep-all-routes**
     
     
     
     The device is configured to store all routing updates received from its peers.
     
     After this command is used, all routing updates sent by a specified peer are stored, regardless of whether a filtering policy is used. When the local routing policy is changed, the routing updates can be used to regenerate BGP4+ routes.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.