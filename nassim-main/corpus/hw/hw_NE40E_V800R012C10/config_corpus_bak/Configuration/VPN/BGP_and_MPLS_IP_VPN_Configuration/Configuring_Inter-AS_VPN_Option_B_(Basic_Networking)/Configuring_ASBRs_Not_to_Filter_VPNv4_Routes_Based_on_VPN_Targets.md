Configuring ASBRs Not to Filter VPNv4 Routes Based on VPN Targets
=================================================================

In inter-AS VPN Option B mode, ASBRs do not have VPN instances.
If you want ASBRs to keep received VPNv4 routes, configure ASBRs not
to filter VPNv4 routes based on VPN targets.

#### Context

By default, an ASBR filters the VPN targets of only the
received VPNv4 routes. The routes are imported into the routing table
if they pass the filtration; otherwise, they are discarded. Therefore,
if no VPN instance is configured on the ASBR or no VPN target is configured
for the VPN instance, the ASBR discards all the received VPNv4 routes.

In inter-AS VPN Option B mode, the ASBR does not need to store
VPN instance information, but must store information about all the
VPNv4 routing information and advertise the routing information to
the peer ASBR. In this situation, the ASBR needs to import all the
received VPNv4 routes without filtering them based on VPN targets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view of the ASBR is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** [ **unicast** ]
   
   
   
   The BGP-VPNv4 address family view is displayed.
4. Run [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target)
   
   
   
   The function to filter VPNv4 routes based on VPN
   targets is disabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.