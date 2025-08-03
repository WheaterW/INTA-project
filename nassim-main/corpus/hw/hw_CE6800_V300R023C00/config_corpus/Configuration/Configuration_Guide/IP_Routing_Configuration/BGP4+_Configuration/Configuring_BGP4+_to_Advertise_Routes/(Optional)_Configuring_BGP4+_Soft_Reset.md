(Optional) Configuring BGP4+ Soft Reset
=======================================

(Optional) Configuring BGP4+ Soft Reset

#### Context

If a BGP4+ export routing policy changes, you can configure BGP4+ soft reset to allow the new policy to immediately take effect. This configuration allows the BGP4+ routing table to be updated dynamically without terminating any BGP4+ connection.

BGP4+ soft reset requires peers to support the route-refresh capability.


#### Procedure

* (Optional) Enable the route-refresh capability.
  
  
  
  Perform the following steps on a BGP4+ device:
  
  
  
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Enable the route-refresh capability.
     
     
     ```
     [peer](cmdqueryname=peer+capability-advertise+route-refresh) { ipv6-address | group-name } capability-advertise route-refresh
     ```
     
     If the route-refresh capability is enabled on all BGP4+ devices and a BGP4+ routing policy changes, the local device sends Route-refresh messages to its peers. Upon receipt of these messages, the peers advertise their routing information to the local device again. This enables the local device to dynamically update its BGP4+ routing table and apply the new routing policy without terminating any BGP4+ connections.
     
     By default, the route-refresh capability is enabled.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Manually soft reset BGP4+ connections.
  
  
  
  Perform the following steps on a BGP4+ device:
  
  
  
  1. Configure export BGP4+ soft reset in the user view.
     
     
     ```
     [refresh bgp](cmdqueryname=refresh+bgp+ipv6+all+group+external+internal+export) ipv6 { all | ipv6-address | group group-name | external | internal } export
     ```
     
     **external** soft resets an EBGP connection, and **internal** soft resets an IBGP connection.