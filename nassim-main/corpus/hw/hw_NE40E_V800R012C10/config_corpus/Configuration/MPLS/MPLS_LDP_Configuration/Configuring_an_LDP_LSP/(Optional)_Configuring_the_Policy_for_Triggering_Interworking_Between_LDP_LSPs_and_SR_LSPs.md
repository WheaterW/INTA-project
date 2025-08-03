(Optional) Configuring the Policy for Triggering Interworking Between LDP LSPs and SR LSPs
==========================================================================================

Configure the policy for triggering interworking between LDP LSPs and SR LSPs, allowing SR LSPs to interwork with proxy egress LSPs and transit LSPs that are established over non-local host routes with a 32-bit mask.

#### Context

When an LDP network is connected with an SR network, it is required that LDP LSPs interwork with SR LSPs, so that traffic on LDP LSPs can be further forwarded on SR LSPs when the traffic enters the SR network. To meet this requirement, configure the policy for triggering interworking between LDP LSPs and SR LSPs, allowing SR LSPs to interwork with proxy egress LSPs and transit LSPs that are established over non-local host routes with a 32-bit mask. If they interwork successfully, traffic on such LDP LSPs can be further forwarded on SR LSPs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**lsp-trigger segment-routing-interworking best-effort host**](cmdqueryname=lsp-trigger+segment-routing-interworking+best-effort+host)
   
   
   
   The policy that triggers interworking between SR LSPs and proxy egress LSPs and transit LSPs that are established over non-local host routes with a 32-bit mask is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.