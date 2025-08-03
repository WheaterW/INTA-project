Configuring MP-EBGP for PEs and ASBRs in Different ASs
======================================================

By introducing extended community attributes into BGP, MP-EBGP can advertise VPNv4 routes between PEs. After an MP-EBGP peer relationship is established between ASBRs in Different ASs, an ASBR can advertise the VPNv4 routes of its AS to the other ASBR.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
   
   
   
   The peer ASBR is specified as an EBGP peer.
4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface** **loopback** *interface-number*
   
   
   
   The loopback interface is specified as the outbound interface of BGP sessions.
5. Run [**peer**](cmdqueryname=peer) *ipv4-address* **ebgp-max-hop** [ *hop-count* ]
   
   
   
   The maximum number of hops between PEs for which an EBGP peer relationship is to be configured is specified. PEs of different ASs are generally not directly connected. To set up the EBGP peer relationship between PEs of different ASs, configure the maximum number of hops between PEs and ensure that PEs are reachable.
6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **unicast**
   
   
   
   The unicast IPv4 address family view is displayed.
7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
   
   
   
   The capability to exchange IPv4 routes is enabled.
8. (On PEs) Run [**quit**](cmdqueryname=quit)
   
   
   
   The BGP view is displayed.
9. (On PEs) Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** [ **unicast** ]
   
   
   
   The BGP-VPNv4 address family view is displayed.
10. (On PEs) Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
    
    
    
    The capability to exchange VPNv4 routes is enabled.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.