Configuring Inter-AS BGP VPLS Option B
======================================

The advantage of the inter-AS Option B mode is that ASBRs exchange information through routes rather than dedicated links. The disadvantage of the inter-AS Option B mode is that label mappings need to be configured on ASBRs, and consequently, a great number of labels are consumed. In addition, an ASBR needs to set up an LSP with each PE, which results in the shortage of label resources on the ASBR and easily leads to a bottleneck.

#### Procedure

1. Configure BGP VPLS on each PE and ASBR in each AS. For configuration details, see [Configuring BGP VPLS](dc_vrp_vpls_cfg_6005.html).
2. Configure an MP-IBGP connection on each ASBR in each AS.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      The BGP view is displayed.
   3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
      
      An AS number is set for a specified peer.
   4. Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **connect-interface** { *interface-type**interface-number* | *ipv4-source-address* }
      
      A source interface from which BGP messages are sent or a source address used for initiating a connection is specified.
   5. Run [**l2vpn-ad-family**](cmdqueryname=l2vpn-ad-family)
      
      The BGP L2VPN AD address family view is displayed.
   6. Run[**policy vpn-target**](cmdqueryname=policy+vpn-target)
      
      The device is enabled to filter routes based on VPN targets.
   7. Run [**tunnel-selector**](cmdqueryname=tunnel-selector) *tunnel-selector-name*
      
      A tunnel selector is specified.
   8. Run [**signaling vpls**](cmdqueryname=signaling+vpls)
      
      The VPLS signaling capability is enabled.
   9. Run [**peer**](cmdqueryname=peer)*ipv4-address***enable**
      
      The capability to exchange routes with a specified BGP peer is configured.
   10. Run [**quit**](cmdqueryname=quit)
       
       Return to the system view.
   11. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.