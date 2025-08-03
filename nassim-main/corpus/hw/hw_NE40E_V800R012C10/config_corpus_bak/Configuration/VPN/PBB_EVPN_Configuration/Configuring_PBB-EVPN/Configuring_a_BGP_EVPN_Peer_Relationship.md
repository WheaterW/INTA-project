Configuring a BGP EVPN Peer Relationship
========================================

After two provider edges (PEs) establish a Border Gateway Protocol (BGP) Ethernet VPN (EVPN) peer relationship, they can exchange EVPN routes.

#### Context

In provider backbone bridge (PBB)-EVPN networking, PEs need to have BGP EVPN peer relationships established before they can exchange EVPN routes and implement communication between EVPN instances.

Perform the following steps on each PE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** *as-number*
   
   
   
   A remote PE is configured as a peer.
4. Run [**peer**](cmdqueryname=peer+connect-interface) *ipv4-address* [**connect-interface**](cmdqueryname=connect-interface) **loopback** *interface-number*
   
   
   
   The interface used by BGP to set up a TCP connection is specified.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A PE must use a loopback interface address with a 32-bit mask to set up an MP-IBGP peer relationship with the peer PE, so that routes can recurse to tunnels. EVPN routes destined for a loopback interface address are advertised to the peer device using an Interior Gateway Protocol (IGP) on the Multiprotocol Label Switching (MPLS) backbone network.
5. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The BGP-EVPN address family view is displayed.
6. Run [**peer**](cmdqueryname=peer+enable) { *ipv4-address* | *group-name* } **enable**
   
   
   
   The capability to exchange EVPN routes with the specified peer or peer group is enabled.
7. (Optional) Run [**peer**](cmdqueryname=peer+group) *ipv4-address* **group** *group-name*
   
   
   
   The BGP EVPN peer is added to a peer group.
   
   Adding BGP EVPN peers to peer groups simplifies BGP network configuration and management.
8. (Optional) Run [**timer df-delay**](cmdqueryname=timer+df-delay) *delay-value*
   
   
   
   A designated forwarder (DF) election delay is configured.
   
   
   
   If a network is unstable, PE interfaces connecting to CEs will frequently alternate between up and down, resulting in frequent DF elections and subsequent network performance deterioration. To prevent frequent DF elections, run the [**timer df-delay**](cmdqueryname=timer+df-delay) command to set a longer DF election delay to improve network stability.
   
   In a PBB-EVPN dual-homing scenario where interface-based DF election is enabled, you need to run this command to set the DF election delay to 0s to prevent traffic interruption caused by the long-time existence of dual backup devices during switchback.
9. (Optional) Run [**peer**](cmdqueryname=peer+mac-limit) { *group-name* | *ipv4-address* } [**mac-limit**](cmdqueryname=mac-limit) *number* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** *times* ]
   
   
   
   The maximum number of MAC advertisement routes that can be received from each peer is configured.
   
   
   
   If an EVPN instance imports many invalid MAC advertisement routes from peers and these routes occupy a large proportion of the total MAC advertisement routes, run the [**mac-limit**](cmdqueryname=mac-limit) command to configure the maximum number of MAC advertisement routes that can be received from each peer. If the number of received MAC advertisement routes exceeds the specified maximum number, the system displays an alarm, instructing you to check the validity of the MAC advertisement routes received in the EVPN instance.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.