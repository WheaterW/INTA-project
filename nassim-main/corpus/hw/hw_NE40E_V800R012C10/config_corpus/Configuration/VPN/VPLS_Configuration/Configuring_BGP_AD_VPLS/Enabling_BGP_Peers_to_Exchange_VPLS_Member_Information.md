Enabling BGP Peers to Exchange VPLS Member Information
======================================================

BGP peers need to be enabled to exchange VPLS member information in the L2VPN-AD address family view.

#### Context

BGP AD VPLS shares TCP connections with BGP and inherits most BGP configurations. Unlike BGP, BGP AD VPLS requires the exchange of route information between BGP peers. BGP peers need to be enabled to exchange route information in the L2VPN-AD address family view.

Perform the following steps on the endpoint PEs of a PW.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
   
   
   
   A BGP peer is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   *ipv4-address* is the same as the remote LSR ID.
4. Run [**l2vpn-ad-family**](cmdqueryname=l2vpn-ad-family)
   
   
   
   The L2VPN-AD address family view is displayed.
5. (Optional) Run [**vpn-orf enable**](cmdqueryname=vpn-orf+enable)
   
   
   
   ORF is enabled.
6. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
   
   
   
   The function to exchange VPLS member information with the specified BGP peer is enabled.
   
   
   
   The BGP AD signaling capability is enabled in the L2VPN AD address family view by default.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   *ipv4-address* in this command must be the same as that specified in the [**peer**](cmdqueryname=peer) command run in the BGP view and same as the LSR ID of the peer device.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.