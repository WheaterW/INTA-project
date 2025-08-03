Configuring BGP MVPN Peer Relationships
=======================================

You need to configure BGP MVPN peer relationships between PEs in the same MVPN so that the PEs can use BGP to exchange BGP A-D and BGP C-multicast routes.

#### Context

To exchange BGP A-D and BGP C-multicast routes, different PEs on an MVPN must be able to discover other PEs on the MVPN. The discovery process is called MVPN membership auto discovery (AD). NG MVPN over BIER uses BGP to implement this process. To support MVPN membership auto discovery, BGP defines a new BGP-MVPN address family.

PEs are classified as sender PEs or receiver PEs in NG MVPN over BIER. To transmit multicast traffic from multicast sources to multicast receivers, sender PEs must establish BGP MVPN peer relationships with receiver PEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family mvpn**](cmdqueryname=ipv4-family+mvpn)
   
   
   
   The BGP-MVPN address family view is displayed.
4. Run [**peer**](cmdqueryname=peer+enable+%28BGP-MVPN+address+family+view%29) *ipv4-address* **enable**
   
   
   
   The BGP MVPN peer relationship is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.