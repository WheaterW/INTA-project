Configuring MP-EBGP Between ASBRs in Different ASs
==================================================

After an MP-EBGP peer relationship is established between ASBRs, an ASBR can advertise the VPNv4 routes of its AS to the other ASBR.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *peer-address* **as-number** *as-number*
   
   
   
   The peer ASBR is specified as an EBGP peer.
4. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** [ **unicast** ]
   
   
   
   The BGP-VPNv4 address family view is displayed.
5. Run [**peer**](cmdqueryname=peer) *peer-address* **enable**
   
   
   
   The function to exchange VPNv4 routes with the peer ASBR is enabled.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.