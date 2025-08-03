(Optional) Configuring BGP4+ Soft Reset
=======================================

(Optional) Configuring BGP4+ Soft Reset

#### Context

If a BGP4+ import routing policy changes, you can soft reset BGP4+ connections to allow the new policy to take effect immediately. Specifically, this configuration triggers re-acceptance of BGP4+ routes based on the new policy. BGP4+ route-refresh allows the system to update the BGP4+ routing table dynamically without tearing down any BGP4+ connection when a policy is changed.

* If a BGP4+ peer supports route-refresh, you can update the routing table by running the [**refresh bgp ipv6**](cmdqueryname=refresh+bgp+ipv6) command to perform a soft reset on the BGP4+ connection.
* If a BGP4+ peer does not support route-refresh, you can run the [**peer keep-all-routes**](cmdqueryname=peer+keep-all-routes) command to reserve all the original routes of the peer. In this manner, the routing table can be updated without resetting the BGP4+ connection.

#### Procedure

* If BGP4+ peers support route-refresh, perform the following steps:
  1. (Optional) Enable the route-refresh capability.
     
     
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
        [peer](cmdqueryname=peer) { ipv6-address | group-name } [capability-advertise](cmdqueryname=capability-advertise+route-refresh) route-refresh
        ```
        
        By default, the route-refresh capability is enabled.
        
        If route-refresh is enabled on all BGP4+ peers and the import routing policy of the local device is changed, the local device sends Route-refresh messages to its peers or peer groups. Upon receipt, the peers or peer groups re-send their routing information to the local device. This enables the local device to dynamically update its BGP4+ routing table and apply the new routing policy without terminating any BGP4+ connections.
  2. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
  3. Configure BGP4+ soft reset.
     
     
     1. Configure import BGP4+ soft reset in the user view.
        ```
        [refresh bgp](cmdqueryname=refresh+bgp+ipv6+all+group+external+internal+import) ipv6 { all | ipv6-address | group group-name | external | internal } import
        ```
     
     **external** soft resets an EBGP connection, and **internal** soft resets an IBGP connection.
* If the device's BGP4+ peers do not support route-refresh, perform the following steps:
  
  
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
  4. Configure the device to retain all the routing updates received from a specified peer or peer group.
     ```
     [peer](cmdqueryname=peer) { ipv6-address | group-name | ipv4-address } [keep-all-routes](cmdqueryname=keep-all-routes)
     ```
     
     By default, a device retains only the routing updates that are received from peers or peer groups and match a configured import policy.
     
     After this command is run, all routing updates sent by a specified peer or peer group are retained, regardless of whether an import policy is used. If the local routing policy changes, the retained information can be used to regenerate BGP4+ routes.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     This command needs to be run on both the local device and its peers. If the [**peer keep-all-routes**](cmdqueryname=peer+keep-all-routes) command is run on the device for the first time, the sessions between the device and its peers are re-established.
     
     The [**peer keep-all-routes**](cmdqueryname=peer+keep-all-routes) command does not need to be run on a device that supports route-refresh. If this command is run on such a device, the sessions between the device and its peers will not be re-established, but running the [**refresh bgp ipv6**](cmdqueryname=refresh+bgp+ipv6) command cannot update the routing table.
  5. Commit the configuration.
     ```
     [commit](cmdqueryname=commit)
     ```