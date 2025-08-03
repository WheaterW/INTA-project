Configuring EVPN Functions
==========================

EVPN VPWS is established based on the EVPN service architecture. Before configuring EVPN VPWS over MPLS, you need to configure EVPN functions.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **vpws**
   
   
   
   An EVPN VPWS instance is created, and its view is displayed.
3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
   
   
   
   A description is configured for the EVPN instance.
   
   Similar to a hostname or an interface description, an EVPN instance description helps you memorize the EVPN instance.
4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
   
   
   
   An RD is configured for the EVPN instance.
   
   
   
   An EVPN instance takes effect only after an RD is configured for it. The RDs of different EVPN instances on a PE must be different.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If you need to create a large number of EVPN instances and plan a large number of RDs, you can run the **evpn route-distinguisher auto** *rd-ip* command in the system view to enable automatic RD allocation, thereby avoiding RD conflicts. The *rd-ip* parameter specifies an IPv4 address, enabling a device to allocate RDs in the format of *X.X.X.X*:*index* to all EVPN instances that are not allocated RDs. *X.X.X.X* indicates a user-defined RD-IP value, and *index* is a 2-byte value automatically allocated by the system in the range from 1 to 65535.
5. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
   
   
   
   VPN targets are configured for the EVPN instance.
   
   VPN targets are BGP extended community attributes used to control the acceptance and advertisement of EVPN routes. A maximum of eight VPN targets can be configured using the [**vpn-target**](cmdqueryname=vpn-target) command. To configure more VPN targets in the EVPN instance address family, run the [**vpn-target**](cmdqueryname=vpn-target) command several times.
6. (Optional) Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
   
   
   
   The EVPN instance is associated with a tunnel policy.
   
   This configuration enables PEs to use TE tunnels to transmit data packets.
7. (Optional) Run [**timer revert delay**](cmdqueryname=timer+revert+delay) *delay-value*
   
   
   
   A switchback delay is set.
   
   
   
   In dual-homing scenarios, if a fault on the access-side link of the active PE or the active PE is rectified, per-EVI A-D routes are generated on the active PE. Then, per-EVI A-D routes can be advertised to the remote PE based on the BGP EVPN peer relationship. After receiving the per-EVI A-D routes and generating forwarding entries, the remote PE switches traffic from the path destined for the standby PE to the path destined for the active PE. In this case, a few packets may be lost on the active PE because some forwarding entries are not generated. To prevent this problem, run the [**timer revert delay**](cmdqueryname=timer+revert+delay) *delay-value* command on the remote PE to configure a proper switchback delay. After receiving per-EVI A-D routes, the remote PE delays generating forwarding entries. Specifically, the remote PE generates forwarding entries only after the forwarding entries on the active PE become stable. After the delay timer expires, the remote PE generates new forwarding entries and sends traffic to the active PE, preventing packet loss.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
9. Run [**evpn source-address**](cmdqueryname=evpn+source-address) *ip-address*
   
   
   
   An EVPN source address is configured.
10. (Optional) Configure an ESI. In EVPN VPWS dual-homing networking, an ESI must be configured on the PE interface connecting to a CE.
    1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
    2. Run the [**esi**](cmdqueryname=esi) *esi* command to set an ESI.
    3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
11. Run [**bgp**](cmdqueryname=bgp) *as-number*
    
    
    
    The BGP view is displayed.
12. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** *as-number*
    
    
    
    A remote PE is configured as a peer.
13. Run [**peer**](cmdqueryname=peer+connect-interface) *ipv4-address* [**connect-interface**](cmdqueryname=connect-interface) **loopback** *interface-number*
    
    
    
    The interface on which a TCP connection to the specified BGP peer is established is specified.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    A PE must use a loopback interface address with a 32-bit mask to establish an MP-IBGP peer relationship with the peer PE so that routes can recurse to tunnels. The route to the local loopback interface is advertised to the peer PE using an IGP on the MPLS backbone network.
14. (Optional) Run [**group**](cmdqueryname=group)*group-name* [ **internal** | **external** ]
    
    
    
    A peer group is created.
15. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
    
    
    
    The BGP-EVPN address family view is displayed.
16. Run [**peer**](cmdqueryname=peer+enable) { *ipv4-address* | *group-name* } **enable**
    
    
    
    The device is enabled to exchange EVPN routes with a specified peer or peer group.
17. (Optional) Run [**peer**](cmdqueryname=peer+group) *ipv4-address* **group** *group-name*
    
    
    
    A BGP EVPN peer is added to the peer group.
    
    Adding BGP EVPN peers to peer groups simplifies BGP network configuration and management.
18. (Optional) Run [**peer**](cmdqueryname=peer+reflect-client) { *ipv4-address* | *group-name* } [**reflect-client**](cmdqueryname=reflect-client)
    
    
    
    An RR and its client are configured.
    
    If all PEs are in the same AS, you can configure an RR to reduce IBGP connections. The device with the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command functions as an RR and treats the specified peer or peer group as a client.
19. (Optional) Run [**timer df-delay**](cmdqueryname=timer+df-delay) *seconds*
    
    
    
    A DF election delay is configured.
    
    If a network is unstable, PE interfaces connecting to CEs will frequently alternate between up and down, resulting in repeated DF election and subsequent network performance deterioration. To prevent repeated DF election, run the [**timer df-delay**](cmdqueryname=timer+df-delay) command to set a longer DF election delay to improve network stability.
    
    In an EVPN dual-homing scenario where interface-based DF election is enabled, you need to run this command to set the DF election delay to 0s, preventing the long-time existence of dual standby devices during a switchback from causing traffic interruption.
20. (Optional) Run [**peer**](cmdqueryname=peer+mac-limit) { *group-name* | *ipv4-address* } [**mac-limit**](cmdqueryname=mac-limit) *number* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** *times* ]
    
    
    
    The maximum number of MAC advertisement routes that can be received from a peer is configured.
    
    If an EVPN instance imports many invalid MAC advertisement routes from peers and these routes occupy a large proportion of the total MAC advertisement routes, run the command to configure the maximum number of MAC advertisement routes that can be received from each peer. If the number of received MAC advertisement routes exceeds the specified maximum number, the system displays an alarm, instructing users to check the validity of the MAC advertisement routes received in the EVPN instance.
21. (Optional) Perform the following operations to enable the device to advertise the routes carrying the large-community attribute to BGP EVPN peers.
    
    
    
    The large-community attribute can represent a whole 2-byte or 4-byte AS number, and contain two 4-byte LocalData IDs, facilitating the flexible application of route-policies. Before enabling the function to advertise the routes carrying the large-community attribute to BGP EVPN peers, configure the [route-policy related to the large-community attribute](dc_vrp_bgp_cfg_4059.html) and use the route-policy to set the large-community attribute.
    
    
    
    1. Run the [**peer**](cmdqueryname=peer+route-policy) { *ipv4-address* | *group-name* } **route-policy** *route-policy-name* **export** command to apply an export route-policy to filter routes to be advertised to a specified BGP EVPN peer or peer group.
    2. Run the [**peer**](cmdqueryname=peer+advertise-large-community) { *ipv4-address* | *group-name* } **advertise-large-community** command to enable the device to advertise the routes carrying the large-community attribute to the specified BGP EVPN peer or peer group.
       
       
       
       If the routes carrying the large-community attribute do not need to be advertised to a specified BGP EVPN peer in a peer group, run the [**peer**](cmdqueryname=peer) *ipv4-address* **advertise-large-community** **disable** command.
22. (Optional) Run [**peer**](cmdqueryname=peer+path-attribute-treat) *peerIpv4Addr* **path-attribute-treat** **attribute-id** { *id* [ **to** *id2* ] } &<1-255> { **discard** | **withdraw** | **treat-as-unknown** }
    
    
    
    A special mode for processing BGP EVPN path attributes is configured.
    
    Alternatively, run the [**peer**](cmdqueryname=peer) { *peerIpv4Addr* | *peerIpv6Addr* } **treat-with-error** **attribute-id** *id* **accept-zero-value** command to configure a mode for processing malformed BGP EVPN path attributes.
    
    
    
    A BGP EVPN Update message contains various path attributes. If a local device receives Update messages containing malformed path attributes, the involved BGP EVPN sessions may flap. To enhance reliability, you can perform this step to perform special processing on specified path attributes or malformed path attributes in BGP EVPN Update messages.
    
    **path-attribute-treat** is used to specify the processing mode for path attributes. The processing mode can be:
    * Discarding the specified path attributes
    * Withdrawing routes with the specified path attributes
    * Processing the specified path attributes as unknown ones
    
    **treat-with-error** is used to specify the processing mode for malformed path attributes. The processing mode is as follows: Receiving path attributes with values being 0.
23. Run [**quit**](cmdqueryname=quit)
    
    
    
    Return to the BGP view.
24. Run [**quit**](cmdqueryname=quit)
    
    
    
    Return to the system view.
25. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.