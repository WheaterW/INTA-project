Establishing BGP MVPN Peer Relationships
========================================

Establish BGP multicast virtual private network (MVPN) peer relationships, allowing provider edges (PEs) on the same MVPN to exchange Auto-Discovery (A-D) and C-multicast routes through BGP.

#### Context

To enable PEs on the same MVPN to exchange A-D and C-multicast routes, enable each PE to discover the other PEs on the same MVPN. Peer discovery is implemented automatically through BGP, and therefore the process is called automatic discovery. To implement automatic discovery, BGP defined the BGP-MVPN address family.

In intra-AS segmented next generation MVPN (NG MVPN), to transmit multicast data traffic from multicast sources to multicast receivers, all PEs must establish BGP MVPN peer relationships with ABRs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **mvpn**
   
   
   
   The BGP-MVPN address family view is displayed.
4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
   
   
   
   The BGP MVPN peer relationship is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.