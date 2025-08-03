(Optional) Configuring ORF for the BGP IPv6 SR-Policy Address Family
====================================================================

When a device advertises BGP IPv6 SR-Policy address family routes to peers, you can configure the outbound route filtering (ORF) function to enable the device to advertise only routes carrying the BGP router IDs of peers. This function helps reduce the network load.

#### Usage Scenario

If ORF is configured for two devices between which a BGP-VPN-Target peer relationship has been established, the devices can advertise ORF routes carrying local BGP router IDs to each other in order to notify each other of their required routes. For example, in a scenario with one controller, one route reflector (RR), and multiple forwarders deployed, you can configure ORF on the RR and forwarders. This way, each of the forwarders can notify the RR of the required BGP SR-Policy routes. When the controller advertises the BGP SR-Policy routes required by all the forwarders to the RR, the RR can apply the ORF function to advertise only the target routes to the peer forwarder. This means that the peer forwarder receives only the required routes, reducing the route receiving pressure and network load.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* } **as-number** { *as-number-plain* | *as-number-dot* }
   
   
   
   A BGP peer is configured.
4. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-target**
   
   
   
   The BGP-VPN-Target address family view is displayed.
5. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* } **enable**
   
   
   
   The BGP peer relationship is enabled for the local address family.
6. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* } **reflect-client**
   
   
   
   The device is enabled to function as an RR, and the specified peer is configured as an RR client.
   
   
   
   On a network where an RR is deployed, you also need to perform this step in the BGP-VPN-Target address family view of the RR to enable its reflector function.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the BGP-VPN-Target address family view.
8. Run [**ipv6-family sr-policy**](cmdqueryname=ipv6-family+sr-policy)
   
   
   
   The BGP IPv6 SR-Policy address family view is displayed.
9. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* } **enable**
   
   
   
   The BGP peer relationship is enabled for the local address family.
10. Run [**route-target-orf enable**](cmdqueryname=route-target-orf+enable)
    
    
    
    ORF is enabled globally.
    
    
    
    This step enables ORF for all BGP IPv6 SR-Policy peers. If some of the peers do not need ORF, run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* } **route-target-orf disable** command to disable this function for them.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.