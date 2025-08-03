(Optional) Configuring Inbound BGP Soft Reset
=============================================

The inbound BGP soft reset allows the system to apply new import policies immediately and refresh BGP routing table dynamically without tearing down any BGP connection.

#### Context

After an import BGP policy is changed, you can reset the BGP connection for the new policy to take effect immediately. This, however, interrupts the BGP connection temporarily. BGP route-refresh allows the system to refresh the BGP routing table dynamically without tearing down any BGP connection when a policy is changed.

* If a BGP peer supports route-refresh, you can run the [**refresh bgp**](cmdqueryname=refresh+bgp) command to softly reset the BGP connection to refresh the routing table.
* If a BGP peer does not support route-refresh, you can run the [**peer keep-all-routes**](cmdqueryname=peer+keep-all-routes) command to reserve all the original routes of the peer. In this manner, the routing table can be refreshed without resetting the BGP connection.

#### Procedure

* For BGP peers that support route-refresh:
  1. (Optional) Enable route-refresh.
     
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**peer**](cmdqueryname=peer+capability-advertise) { *ipv4-address* | *group-name* } [**capability-advertise**](cmdqueryname=peer+capability-advertise) **route-refresh**
        
        Route-refresh is enabled.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     
     If route-refresh is enabled on all BGP peers and the import routing policy of the local Router is changed, the local Router sends a Route-refresh message to its peers or peer groups. Upon receipt, the peers or peer groups re-send their routing information to the local Router. This enables the local Router to dynamically update its BGP routing table and apply the new policy without terminating any BGP connections.
  2. Configure BGP soft reset.
     
     
     1. Run the [**refresh bgp**](cmdqueryname=refresh+bgp+vpn-instance+ipv4-family+vpnv4+all+group+external) [ **vpn-instance** *vpn-instance-name* **ipv4-family** | **vpnv4** ] { **all** | *ipv4-address* | **group** *group-name* | **external** | **internal** } **import** command in the user view to trigger BGP soft reset immediately.
     
     **external** softly resets an EBGP connection, and **internal** softly resets an IBGP connection.
* For BGP peers that do not support route-refresh:
  + Configure the device to retain all the routing updates received from a specified peer or peer group.
    
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**bgp**](cmdqueryname=bgp) *as-number*
       
       The BGP view is displayed.
    3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
       
       The IPv4 unicast address family view is displayed.
    4. Run [**peer**](cmdqueryname=peer+keep-all-routes) { *ipv4-address* | *group-name* } [**keep-all-routes**](cmdqueryname=peer+keep-all-routes)
       
       The device is configured to retain all routing updates received from the specified peer or peer group.
       
       After this command is run, all routing updates received from the specified peer or peer group are retained, regardless of whether an import policy is used. If the local routing policy changes, the retained information can be used to regenerate BGP routes.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       This command needs to be run on both the local device and its peers. If the [**peer keep-all-routes**](cmdqueryname=peer+keep-all-routes) command is run on the device for the first time, the sessions between the device and its peers are re-established.
       
       The [**peer keep-all-routes**](cmdqueryname=peer+keep-all-routes) command does not need to be run on the Router that supports route-refresh. If this command is run, the sessions between the Router and its peers are not reestablished, but the [**refresh bgp**](cmdqueryname=refresh+bgp) command does not take effect on the Router.
    5. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.