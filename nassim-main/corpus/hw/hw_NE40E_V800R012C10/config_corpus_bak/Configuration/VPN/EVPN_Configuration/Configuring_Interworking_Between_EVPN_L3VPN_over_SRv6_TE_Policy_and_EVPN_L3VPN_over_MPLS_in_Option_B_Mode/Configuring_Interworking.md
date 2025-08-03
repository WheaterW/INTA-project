Configuring Interworking
========================

After enabling interworking between EVPN L3VPN over SRv6 and EVPN L3VPN over MPLS in Option B mode in the EVPN address family, configure SID application on a per-route or per-next-hop basis so that different types of tunnels can communicate with each other.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view of the ASBR is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. (Optional) Run [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46)
   
   
   
   The device is enabled to add the SID attribute to EVPN routes to be sent.
4. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The EVPN address family is enabled, and its view is displayed.
5. Run [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target)
   
   
   
   VPN target-based VPN route filtering is canceled. Then all VPN routes can be received.
6. Run [**interworking srv6-mpls evpn ip-prefix**](cmdqueryname=interworking+srv6-mpls+evpn+ip-prefix)
   
   
   
   Interworking between EVPN L3VPN over SRv6 and EVPN L3VPN over MPLS in Option B mode is configured.
7. Run [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name*
   
   
   
   The device is enabled to add the SID attribute to EVPN routes to be sent.
8. (Optional) Run [**apply-label per-nexthop**](cmdqueryname=apply-label+per-nexthop)
   
   
   
   The device is configured to allocate labels on a per-next-hop basis to routes received from SRv6 peers in the EVPN address family.
9. Run [**segment-routing ipv6 apply-sid**](cmdqueryname=segment-routing+ipv6+apply-sid) **{ per-route | per-nexthop }** **evpn** **mpls** **ip-prefix**
   
   
   
   The device is configured to apply for SIDs in one-SID-per-route or one-SID-per-next-hop mode for routes received from MPLS peers in the EVPN address family.
10. (Optional) Run [**peer**](cmdqueryname=peer+next-hop-local) *ipv4-address* **next-hop-local**
    
    
    
    The device is configured to set its IP address as the next hop of routes to be advertised to the specified IBGP peer. If IBGP peers are configured on the network, you need to run this command.
11. (Optional) Run [**peer**](cmdqueryname=peer+reflect-client) *ipv4-address* **reflect-client**
    
    
    
    The device is configured as an RR, and its peer as an RR client. If IBGP peers are configured on the network, you need to run this command.
12. (Optional) Run [**peer**](cmdqueryname=peer+next-hop-local) *ipv6-address* **next-hop-local**
    
    
    
    The device is configured to set its IP address as the next hop of routes to be advertised to the specified IBGP peer. If IBGP peers are configured on the network, you need to run this command.
13. (Optional) Run [**peer**](cmdqueryname=peer+reflect-client) *ipv6-address* **reflect-client**
    
    
    
    The device is configured as an RR, and its peer as an RR client. If IBGP peers are configured on the network, you need to run this command.
14. Run [**quit**](cmdqueryname=quit)
    
    
    
    Exit the BGP-EVPN address family view.
15. Run [**quit**](cmdqueryname=quit)
    
    
    
    Exit the BGP address family view.
16. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.