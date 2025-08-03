(Optional) Configuring BGP Soft Reset
=====================================

(Optional) Configuring BGP Soft Reset

#### Context

If a BGP import routing policy changes, you can soft-reset BGP connections to allow the new policy to take effect immediately. Specifically, this configuration triggers re-acceptance of BGP routes based on the new policy. BGP route-refresh allows the system to update the BGP routing table dynamically without tearing down any BGP connection when a policy is changed.

* If a BGP peer supports route-refresh, you can run the [**refresh bgp**](cmdqueryname=refresh+bgp) command to update the routing table through a soft reset on BGP connections.
* If a BGP peer does not support route-refresh, you can run the [**peer keep-all-routes**](cmdqueryname=peer+keep-all-routes) command to retain all the original routes of the peer. In this manner, the routing table can be updated without resetting the BGP connection.

#### Procedure

* For BGP peers that support route-refresh:
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
        [peer](cmdqueryname=peer) { ipv4-address | group-name | ipv6-address } [capability-advertise](cmdqueryname=capability-advertise+route-refresh) route-refresh
        ```
        
        By default, the route-refresh capability is enabled.
        
        If route-refresh is enabled on all BGP peers and the import routing policy of the local device is changed, the local device sends a Route-refresh message to its peers or peer groups. Upon receipt, the peers or peer groups re-send their routing information to the local device. This enables the local device to dynamically update its BGP routing table and apply the new routing policy without terminating any BGP connections.
     4. Commit the configuration.
        ```
        [commit](cmdqueryname=commit)
        ```
  2. Configure BGP soft reset.
     
     
     1. Configure inbound BGP soft reset in the user view.
        ```
        [refresh bgp](cmdqueryname=refresh+bgp+all+group+external+internal+import) { all | ipv4-address | group group-name | external | internal } import
        ```
     
     **external** softly resets an EBGP connection, and **internal** softly resets an IBGP connection.
* If the device's peers do not support route-refresh, perform the following operations:
  
  
  1. Enter the system view.
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Enter the IPv4 unicast address family view.
     ```
     [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
     ```
  4. Configure the device to retain all the routing updates received from a specified peer or peer group.
     ```
     [peer](cmdqueryname=peer) { ipv4-address | group-name | peerIpv6Addr } [keep-all-routes](cmdqueryname=keep-all-routes)
     ```
     
     By default, a device retains only the routing updates that are received from peers or peer groups and match a configured import policy.
     
     After this command is run, all routing updates sent by a specified peer or peer group are retained, regardless of whether an import policy is used. If the local routing policy changes, the retained information can be used to regenerate BGP routes.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     This command needs to be run on both the local device and its peers. If the [**peer keep-all-routes**](cmdqueryname=peer+keep-all-routes) command is run on the device for the first time, the sessions between the device and its peers are re-established.
     
     The [**peer keep-all-routes**](cmdqueryname=peer+keep-all-routes) command does not need to be run on a device that supports route-refresh. If this command is run on such a device, the sessions between the device and its peers will not be re-established, but running the [**refresh bgp**](cmdqueryname=refresh+bgp) command cannot update the routing table.
  5. Commit the configuration.
     ```
     [commit](cmdqueryname=commit)
     ```