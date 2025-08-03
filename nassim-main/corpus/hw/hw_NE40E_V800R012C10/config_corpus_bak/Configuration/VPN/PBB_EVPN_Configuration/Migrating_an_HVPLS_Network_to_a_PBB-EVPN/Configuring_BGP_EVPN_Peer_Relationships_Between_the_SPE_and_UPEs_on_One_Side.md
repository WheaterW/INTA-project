Configuring BGP EVPN Peer Relationships Between the SPE and UPEs on One Side
============================================================================

After a superstratum provider edge (SPE) and a user-end provider edge (UPE) establishes a Border Gateway Protocol (BGP) Ethernet VPN (EVPN) peer relationship, they can exchange EVPN routes.

#### Context

In provider backbone bridge EVPN (PBB-EVPN) networking, establishing BGP EVPN peer relationships with UPEs is the prerequisite for an SPE to exchange EVPN routes with UPEs and communicate with them.

Perform the following steps on each SPE and UPE:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
   
   
   
   A BGP EVPN peer IP address is specified.
4. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**connect-interface**](cmdqueryname=connect-interface) **loopback** *interface-number*
   
   
   
   The interface on which a TCP connection to the specified peer is to be established is specified.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   An SPE and a UPE must use loopback interface addresses with 32-bit subnet masks to establish a Multiprotocol Interior Border Gateway Protocol (MP-IBGP) peer relationship, so that EVPN routes can recurse to tunnels. EVPN routes destined for a loopback interface address are advertised to the peer device using an IGP on the MPLS backbone network.
5. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The BGP-EVPN address family view is displayed.
6. Run [**peer**](cmdqueryname=peer+enable) { *ipv4-address* | *group-name* } **enable**
   
   
   
   The capability to exchange EVPN routes with the specified peer or peer group is enabled.
7. (Optional) Run [**peer**](cmdqueryname=peer+group) *ipv4-address* **group** *group-name*
   
   
   
   The BGP EVPN peer is added to a peer group.
   
   Adding BGP EVPN peers to peer groups simplifies BGP network configuration and management.
8. (Optional) Run [**timer df-delay**](cmdqueryname=timer+df-delay) *delay-value*
   
   
   
   A designated forwarder (DF) election delay is configured.
   
   
   
   If a network is unstable, UPE interfaces connecting to CEs will frequently alternate between Up and Down, resulting in frequent DF elections and subsequent network performance deterioration. To prevent frequent DF elections, run the [**timer df-delay**](cmdqueryname=timer+df-delay) command to set a longer DF election delay to improve network stability.
9. (Optional) Run [**peer**](cmdqueryname=peer+mac-limit) { *group-name* | *ipv4-address* } [**mac-limit**](cmdqueryname=mac-limit) *number* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** *times* ]
   
   
   
   The maximum number of MAC advertisement routes that can be received from each peer is configured.
   
   
   
   If an EVPN instance imports many invalid MAC advertisement routes from peers and these routes occupy a large proportion of the total MAC advertisement routes, run the [**mac-limit**](cmdqueryname=mac-limit) command to configure the maximum number of MAC advertisement routes that can be received from each peer. If the number of received MAC advertisement routes exceeds the specified maximum number, the system displays an alarm, instructing you to check the validity of the MAC advertisement routes received in the EVPN instance.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.