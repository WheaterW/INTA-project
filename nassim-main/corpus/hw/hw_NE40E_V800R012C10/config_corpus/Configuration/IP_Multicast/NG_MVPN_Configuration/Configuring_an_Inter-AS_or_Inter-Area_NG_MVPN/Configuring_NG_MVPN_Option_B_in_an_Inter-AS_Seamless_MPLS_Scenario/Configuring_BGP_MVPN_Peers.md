Configuring BGP MVPN Peers
==========================

Establish a BGP MVPN peer relationship between devices belonging to the same MVPN, so that the devices can use BGP to exchange BGP A-D and BGP C-multicast routes.

#### Context

To exchange BGP A-D and BGP C-multicast routes, different PEs on an MVPN must be able to discover other PEs on the MVPN. The discovery process is called MVPN membership auto discovery (AD). An NG MVPN uses BGP to implement this process. To support MVPN membership autodiscovery, BGP defines a new BGP-MVPN address family.

On an NG MVPN, a PE can be either a sender or receiver PE. To transmit multicast traffic from multicast sources to multicast receivers, sender PEs must establish BGP MVPN peer relationships with receiver PEs.

Perform the following steps on PEs, ABRs, and ASBRs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **mvpn**
   
   
   
   The BGP-MVPN address family view is displayed.
4. (On PEs) Run [**policy vpn-target**](cmdqueryname=policy+vpn-target)
   
   
   
   The VPN-Target filter function is enabled.
5. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **enable**
   
   
   
   The device is specified as a BGP MVPN peer.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.