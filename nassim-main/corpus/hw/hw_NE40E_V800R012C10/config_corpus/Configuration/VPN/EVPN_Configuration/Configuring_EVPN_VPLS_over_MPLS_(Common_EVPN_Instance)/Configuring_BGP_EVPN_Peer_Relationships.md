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
   
   
   
   A BGP router ID is configured.
   
   
   
   If this step is not performed, the device automatically selects an interface address as the BGP router ID. This step is mandatory if you need to specify a router ID for the current BGP process.
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
10. (Optional) Run [**timer df-delay**](cmdqueryname=timer+df-delay) *delay-value*
    
    
    
    A designated forwarder (DF) election delay is configured.
    
    If a network is unstable, PE interfaces connecting to CEs will frequently alternate between up and down, resulting in repeated DF election and subsequent network performance deterioration. To prevent repeated DF election, run the [**timer df-delay**](cmdqueryname=timer+df-delay) command to set a longer DF election delay to improve network stability.
    
    In an EVPN dual-homing scenario where interface-based DF election is enabled, you need to run this command to set the DF election delay to 0s, preventing the long-time existence of dual standby devices during a switchback from causing traffic interruption.
11. (Optional) Run [**peer**](cmdqueryname=peer+mac-limit) { *group-name* | *ipv4-address* } [**mac-limit**](cmdqueryname=mac-limit) *number* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** *times* ]
    
    
    
    The maximum number of MAC advertisement routes that can be received from a peer or peer group is configured.
    
    If an EVPN instance imports many inapplicable MAC routes from a peer or peer group and they account for a large proportion of the total number of MAC routes, you are advised to run this command to limit the maximum number of MAC advertisement routes that can be imported. If the number of imported MAC advertisement routes exceeds the specified maximum number, the device displays an alarm, prompting you to check the validity of the MAC advertisement routes imported into the EVPN instance.
12. (Optional) Perform the following operations to enable the device to advertise the routes carrying the large-community attribute to BGP EVPN peers.
    
    
    
    The large-community attribute can represent a whole 2-byte or 4-byte AS number, and contain two 4-byte LocalData IDs, facilitating the flexible application of route-policies. Before enabling the function to advertise the routes carrying the large-community attribute to BGP EVPN peers, [configure the route-policy related to the large-community attribute](dc_vrp_bgp_cfg_4059.html) and use the route-policy to set the large-community attribute.
    
    
    
    1. Run the [**peer**](cmdqueryname=peer+route-policy) { *ipv4-address* | *group-name* } **route-policy** *route-policy-name* **export** command to configure an export route-policy for the BGP EVPN peer or group.
    2. Run the [**peer**](cmdqueryname=peer+advertise-large-community) { *ipv4-address* | *group-name* } **advertise-large-community** command to enable the device to advertise the routes carrying the large-community attribute to the specified BGP EVPN peer or peer group.
       
       
       
       If the routes carrying the large-community attribute do not need to be advertised to a specified BGP EVPN peer in a peer group, run the [**peer**](cmdqueryname=peer) *ipv4-address* **advertise-large-community** **disable** command.
13. (Optional) Run [**peer**](cmdqueryname=peer+path-attribute-treat) *peerIpv4Addr* **path-attribute-treat** **attribute-id** { *id* [ **to** *id2* ] } &<1-255> { **discard** | **withdraw** | **treat-as-unknown** }
    
    
    
    A special mode for processing BGP EVPN path attributes is configured.
    
    Alternatively, run the [**peer**](cmdqueryname=peer) { *peerIpv4Addr* | *peerIpv6Addr* } **treat-with-error** **attribute-id** *id* **accept-zero-value** command to configure a mode for processing malformed BGP EVPN path attributes.
    
    
    
    A BGP EVPN Update message contains various path attributes. If a local device receives Update messages containing malformed path attributes, the involved BGP EVPN sessions may flap. To enhance reliability, you can perform this step to perform special processing on specified path attributes or malformed path attributes in BGP EVPN Update messages.
    
    **path-attribute-treat** is used to specify the processing mode for path attributes. The processing mode can be:
    * Discarding the specified path attributes
    * Withdrawing routes with the specified path attributes
    * Processing the specified path attributes as unknown ones
    
    **treat-with-error** is used to specify the processing mode for malformed path attributes. The processing mode is as follows: Receiving path attributes with values being 0.
14. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.