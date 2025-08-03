Configuring MBGP Soft Resetting
===============================

MBGP soft resetting allows the system to refresh an MBGP routing table dynamically without tearing down any MBGP connection if routing policies are changed.

#### Procedure

* Enable the route-refresh capability.
  
  
  
  Perform the following steps on an MBGP Router:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } **capability-advertise** **route-refresh**
     
     
     
     The route-refresh capability is enabled.
     
     
     
     If all MBGP Routers are enabled with the route-refresh capability and an MBGP routing policy changes, the local Router sends Route-refresh messages to its peers. After receiving the messages, the peers resend their routing information to the local MBGP Router. This enables the local device to dynamically update its MBGP routing table and apply the new routing policy without terminating MBGP connections.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an MBGP device to store all routing updates received from its peers.
  
  
  
  Perform the following steps on an MBGP Router:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
  4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } **keep-all-routes**
     
     
     
     The device is configured to retain all route updates received from the specified peer.
     
     
     
     After this command is run, all routing updates received from the specified peer are retained, regardless of whether a routing policy is used. If the local routing policy changes, the retained information can be used to regenerate MBGP routes.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Softly reset an MBGP connection.
  
  
  
  Perform the following steps on an MBGP Router:
  
  
  
  1. Run [**refresh bgp**](cmdqueryname=refresh+bgp) { **all** | *ipv4-address* |  [**ipv6**](cmdqueryname=ipv6) i*pv6-address* | **group** *group-name* | **external** | **internal** } { **export** | **import** }
     
     
     
     A soft reset is performed on MBGP connections.
     
     
     
     To perform a soft reset on MBGP connections, run this command in the user view.