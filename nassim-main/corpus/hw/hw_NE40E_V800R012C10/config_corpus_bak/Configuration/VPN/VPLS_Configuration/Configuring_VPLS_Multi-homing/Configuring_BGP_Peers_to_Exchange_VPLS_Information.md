Configuring BGP Peers to Exchange VPLS Information
==================================================

BGP VPLS shares TCP connections with BGP and inherits most BGP configurations. A major difference between BGP and BGP VPLS is that BGP VPLS requires PEs to exchange VPLS information as BGP peers in the L2VPN AD address family view.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
   
   
   
   A BGP peer is configured, and an AS number is specified for the peer.
4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface** { *interface-name* | **ipv4-source-address** | *interface-type* *interface-number* | *interface-name* *ipv4-source-address* | *interface-type* *interface-number* *ipv4-source-address* }
   
   
   
   A source interface for sending BGP packets is configured.
5. Run [**l2vpn-ad-family**](cmdqueryname=l2vpn-ad-family)
   
   
   
   The L2VPN AD address family view is displayed.
6. (Optional) Run [**vpn-orf enable**](cmdqueryname=vpn-orf+enable)
   
   
   
   ORF is enabled.
7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
   
   
   
   The function to exchange route information with the specified peer is enabled.
8. Run [**signaling vpls**](cmdqueryname=signaling+vpls)
   
   
   
   BGP VPLS is enabled.
9. Run [**signaling multi-homing non-standard-compatible**](cmdqueryname=signaling+multi-homing+non-standard-compatible)
   
   
   
   BGP multi-homing is enabled.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.