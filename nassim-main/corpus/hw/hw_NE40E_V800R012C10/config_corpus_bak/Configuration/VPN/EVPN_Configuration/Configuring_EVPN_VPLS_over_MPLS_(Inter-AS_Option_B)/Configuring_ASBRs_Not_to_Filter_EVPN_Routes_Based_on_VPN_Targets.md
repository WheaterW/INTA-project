Configuring ASBRs Not to Filter EVPN Routes Based on VPN Targets
================================================================

In inter-AS EVPN Option B mode, ASBRs do not have EVPN instances. If you want ASBRs to keep received EVPN routes, configure ASBRs not to filter EVPN routes based on VPN targets.

#### Context

By default, an ASBR filters the VPN targets of only the received EVPN routes. The routes are imported into the routing table if they pass the filtration; otherwise, they are discarded. Therefore, if no VPN instance is configured on the ASBR or no VPN target is configured for the EVPN instance, the ASBR discards all the received EVPN routes.

In inter-AS EVPN Option B, the ASBR does not need to store EVPN instance information, but must store all the EVPN routing information and advertise the routing information to the peer ASBR. In this situation, the ASBR needs to import all the received EVPN routes without filtering them based on VPN targets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view of the ASBR is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The BGP-EVPN address family view is displayed.
4. Run [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target)
   
   
   
   The function to filter EVPN routes based on VPN targets is disabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.