Configuring BGP EVPN Peer Relationships
=======================================

After a BGP EVPN peer relationship is established between PEs, the PEs can exchange EVPN routes when MPLS or SR-MPLS tunnels are deployed on the backbone network.

#### Context

In EVPN networking, PEs have to establish BGP EVPN peer relationships before exchanging EVPN routes to implement communication between the PEs within an EVPN instance.

Perform the following steps on each PE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. (Optional) Run [**router-id**](cmdqueryname=router-id) *router-id-value*
   
   
   
   A BGP router ID is set.
   
   If this step is not performed, the device automatically selects the interface address as the BGP router ID. Perform this step if a router ID needs to be specified for the current BGP process.
4. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** *as-number*
   
   
   
   A remote PE is configured as a peer.
5. Run [**peer**](cmdqueryname=peer+connect-interface) *ipv4-address* [**connect-interface**](cmdqueryname=connect-interface) **loopback** *interface-number*
   
   
   
   The interface on which a TCP connection to the specified BGP peer is established is specified.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A PE must use a loopback interface address with a 32-bit mask to establish an MP-IBGP peer relationship with the peer PE so that routes can recurse to tunnels. The route to the local loopback interface is advertised to the peer PE using an IGP on the MPLS backbone network.
6. (Optional) Run [**group**](cmdqueryname=group)*group-name* [ **internal** | **external** ]
   
   
   
   A peer group is created.
7. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The BGP-EVPN address family view is displayed.
8. Run [**peer**](cmdqueryname=peer+enable) { *ipv4-address* | *group-name* } **enable**
   
   
   
   The device is enabled to exchange EVPN routes with a specified peer or peer group.
9. (Optional) Run [**peer**](cmdqueryname=peer+group) *ipv4-address* **group** *group-name*
   
   
   
   A BGP EVPN peer is added to the peer group.
   
   Adding BGP EVPN peers to peer groups simplifies BGP network configuration and management.
10. Run [**peer**](cmdqueryname=peer+advertise) { *ipv4-address* | *group-name* } **advertise** { **irb** | **arp** | **irbv6** | **nd** }
    
    
    
    IRB/IRBv6 or ARP/ND route advertisement is enabled.
11. (Optional) Run [**timer df-delay**](cmdqueryname=timer+df-delay) *delay-value*
    
    
    
    A DF election delay is configured.
    
    If a network is unstable, PE interfaces connecting to CEs will frequently alternate between up and down, resulting in repeated DF election and subsequent network performance deterioration. To prevent repeated DF election, run the [**timer df-delay**](cmdqueryname=timer+df-delay) command to set a longer DF election delay to improve network stability.
    
    In an EVPN dual-homing scenario where interface-based DF election is enabled, you need to run this command to set the DF election delay to 0s, preventing the long-time existence of dual standby devices during a switchback from causing traffic interruption.
12. (Optional) Run [**peer**](cmdqueryname=peer+mac-limit) { *group-name* | *ipv4-address* } [**mac-limit**](cmdqueryname=mac-limit) *number* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** *times* ]
    
    
    
    The maximum number of MAC advertisement routes that can be received from a peer or peer group is configured.
    
    If an EVPN instance imports many invalid MAC advertisement routes from peers and these routes account for a large proportion of the total MAC advertisement routes, run the command to configure the maximum number of MAC advertisement routes that can be received from each peer. If the number of received MAC advertisement routes exceeds the specified maximum number, the system displays an alarm, instructing users to check the validity of the MAC advertisement routes received in the EVPN instance.
13. (Optional) Run [**route-select delay**](cmdqueryname=route-select+delay) *delay-value* { [ **exclusive-eviad** ] | [ **inclusive-mac** ] } \*
    
    
    
    Delayed route selection is configured. An appropriate route selection delay ensures that traffic switches back to the newly recovered primary path after devices along the primary path complete refreshing forwarding entries. This helps prevent traffic loss caused by traffic switchback. To enable delayed route selection for routes other than Ethernet A-D per-EVI routes, configure the **exclusive-eviad** keyword. This keyword helps prevent EVPN VPWS from being affected after delayed route selection is enabled. To enable delayed route selection also for MAC routes, configure the **inclusive-mac** keyword. This keyword helps additionally enable delayed route selection for MAC routes in EVPN VPLS Option B scenarios.
14. (Optional) Perform the following operations to enable the device to advertise the routes carrying the large-community attribute to BGP EVPN peers.
    
    
    
    The large-community attribute can completely represent a 2-byte or 4-byte AS number, and has two 4-byte LocalData IDs. This enables the administrator to apply policies more flexibly. Before enabling the function to advertise the routes carrying the large-community attribute to BGP EVPN peers, configure the [route-policy related to the large-community attribute](dc_vrp_bgp_cfg_4059.html) and use the route-policy to set the large-community attribute.
    
    
    
    1. Run the [**peer**](cmdqueryname=peer+route-policy) { *ipv4-address* | *group-name* } **route-policy** *route-policy-name* **export** command to configure an export route-policy to filter routes to be advertised to a specified BGP EVPN peer or peer group.
    2. Run the [**peer**](cmdqueryname=peer+advertise-large-community) { *ipv4-address* | *group-name* } **advertise-large-community** command to enable the device to advertise the routes carrying the large-community attribute to a specified BGP EVPN peer or peer group.
       
       
       
       If the routes carrying the large-community attribute do not need to be advertised to a specified BGP EVPN peer or a peer group, run the [**peer**](cmdqueryname=peer) *ipv4-address* **advertise-large-community** **disable** command.
15. (Optional) Run [**peer**](cmdqueryname=peer+graceful-restart) *ipv4-address* **graceful-restart static-timer** *restart-time*
    
    
    
    The maximum hold-off time is set for reestablishing BGP peer relationships, namely, the maximum duration from the time the peer finds that the local device restarts to the time the peer BGP reestablishes a BGP session.
    
    Graceful restart (GR) prevents traffic interruption caused by the reestablishment of BGP peer relationships. You can run the [**graceful-restart timer restart**](cmdqueryname=graceful-restart+timer+restart) *time* or [**peer graceful-restart static-timer**](cmdqueryname=peer+graceful-restart+static-timer) command to set the maximum waiting time for the local end to wait for the peer GR to recover.
    
    * To set the maximum hold-off time for reestablishing all BGP peer relationships, run the [**graceful-restart timer restart**](cmdqueryname=graceful-restart+timer+restart) command in the BGP view. The maximum hold-off time supported by this command is 3600s.
    * To set the maximum hold-off time for reestablishing a specified BGP-EVPN peer relationship, run the [**peer graceful-restart static-timer**](cmdqueryname=peer+graceful-restart+static-timer) command in the BGP-EVPN view. Run this command if you want to set a hold-off time longer than 3600s.
    
    If both the [**graceful-restart timer restart**](cmdqueryname=graceful-restart+timer+restart) *time* and [**peer graceful-restart static-timer**](cmdqueryname=peer+graceful-restart+static-timer) commands are run, the latter command takes precedence over the former one.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    This step can be performed only after GR is enabled using the [**graceful-restart**](cmdqueryname=graceful-restart) command in the BGP view.
16. (Optional) Run [**peer**](cmdqueryname=peer+path-attribute-treat) *peerIpv4Addr* **path-attribute-treat** **attribute-id** { *id* [ **to** *id2* ] } &<1-255> { **discard** | **withdraw** | **treat-as-unknown** }
    
    
    
    A special mode for processing BGP EVPN path attributes is configured.
    
    Alternatively, run the [**peer**](cmdqueryname=peer) { *peerIpv4Addr* | *peerIpv6Addr* } **treat-with-error** **attribute-id** *id* **accept-zero-value** command to configure a mode for processing malformed BGP EVPN path attributes.
    
    
    
    A BGP EVPN Update message contains various path attributes. If a local device receives Update messages containing malformed path attributes, the involved BGP EVPN sessions may flap. To enhance reliability, you can perform this step to perform special processing on specified path attributes or malformed path attributes in BGP EVPN Update messages.
    
    **path-attribute-treat** is used to specify the processing mode for path attributes. The processing mode can be:
    * Discarding the specified path attributes
    * Withdrawing routes with the specified path attributes
    * Processing the specified path attributes as unknown ones
    
    **treat-with-error** is used to specify the processing mode for malformed path attributes. The processing mode is as follows: Receiving path attributes with values being 0.
17. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.