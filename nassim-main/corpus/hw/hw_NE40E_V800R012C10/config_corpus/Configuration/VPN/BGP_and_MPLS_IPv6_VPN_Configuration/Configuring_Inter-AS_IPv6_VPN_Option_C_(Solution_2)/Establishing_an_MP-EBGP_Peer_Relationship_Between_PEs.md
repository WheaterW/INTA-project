Establishing an MP-EBGP Peer Relationship Between PEs
=====================================================

By importing extended community attributes into BGP, MP-IBGP can advertise VPNv6 routes between PEs. PEs of different ASs are generally not directly connected. To set up an EBGP connection between the PEs of different ASs, you must configure the permitted maximum number of hops between PEs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
   
   
   
   The remote PE is specified as the EBGP peer.
4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface** *interface-type* *interface-number* *ipv4-source-address*
   
   
   
   The source interface that sends BGP packets is specified.
5. Run [**peer**](cmdqueryname=peer) *ipv4-address* **ebgp-max-hop** [ *hop-count* ]
   
   
   
   The maximum number of hops permitted to establish the EBGP peer relationship is specified.
6. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
   
   
   
   The BGP-VPN IPv6 address family view is displayed.
7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
   
   
   
   The function to exchange VPNv6 routes with the remote PE is enabled.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.