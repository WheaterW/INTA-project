(Optional) Configuring NG MVPN ORF
==================================

If NG MVPN outbound route filtering (ORF) is enabled in the BGP-MVPN address family, a BGP speaker filters the routes to be advertised to a peer by matching the local export route target (ERT) against the import route target (IRT) of the peer so that the peer receives only desired routes. In this way, NG MVPN ORF reduces network load.

#### Context

NG MVPN ORF allows PEs to receive only desired routes, which reduces network load.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **mvpn**
   
   
   
   The BGP-MVPN address family view is displayed.
4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **enable**
   
   
   
   BGP is enabled to exchange routing information with the specified BGP MVPN peer.
5. Run [**vpn-orf enable**](cmdqueryname=vpn-orf+enable)
   
   
   
   ORF is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**ipv4-family vpn-target**](cmdqueryname=ipv4-family+vpn-target) command must also be run. If the [**vpn-orf enable**](cmdqueryname=vpn-orf+enable) command is run, but the [**ipv4-family vpn-target**](cmdqueryname=ipv4-family+vpn-target) command is not, the BGP speaker does not advertise routes to the peer in the BGP-MVPN address family.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.