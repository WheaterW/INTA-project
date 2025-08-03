Establishing the MP-EBGP Peer Between PEs
=========================================

With extended community attributes added to BGP, MP-IBGP can advertise VPNv4 routes between PEs. PEs of different ASs are indirectly connected in most cases. Therefore, to set up the EBGP connections between them, you need to configure the permitted maximum hops between the PEs and ensure that the PEs are reachable.

#### Procedure

* Configure a PE to advertise its loopback interface IP addresses used for peer relationship establishment to the ASBRs of other ASs and peer PEs. You can also configure an ASBR to send the loopback interface IP addresses of a PE used for peer relationship establishment to the ASBRs of other ASs and peer PEs.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If you want to use inter-AS TE tunnels to transmit traffic in inter-AS Option C networking, perform the following steps on PEs, so that the loopback interface IP addresses of PEs used for peer relationship establishment can be advertised to peer PEs.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**network**](cmdqueryname=network) *ip-address* [ *mask* | *mask-length* ] [ **route-policy** *route-policy-name* ]
     
     
     
     The loopback address of the PE in the local AS is advertised to the remote ASBR.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Perform the following steps on the PE that is connected to a CE:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** { *as-number-plain* | *as-number-dot* }
     
     
     
     The peer PE is specified as the EBGP peer.
  4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface loopback** *interface-number*
     
     
     
     The source interface that sends BGP packets is specified.
  5. Run [**peer**](cmdqueryname=peer) *ipv4-address* **ebgp-max-hop** [ *hop-count* ]
     
     
     
     The maximum hop of the EBGP peer is set. PEs of different ASs are generally not directly connected. To set up the EBGP peer between PEs of different ASs, configure the maximum hop between PEs and ensure the PEs are reachable.
  6. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
     
     
     
     The BGP-VPN IPv6 address family view is displayed.
  7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
     
     
     
     The exchange of VPNv6 routes with the peer PE is enabled.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure a route reflector (RR).
  
  
  
  To improve scalability, specify an RR in each AS and establish MP-EBGP peer relationships between the RRs in ASs to save all VPNv6 routes on the RRs. Then configure PEs in each AS as the RR's clients to exchange VPNv6 routing information with the RR. Perform the following steps on a device that needs to be configured as an RR:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** { *as-number-plain* | *as-number-dot* }
     
     
     
     The RR in another AS is configured as its EBGP peer.
  4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface loopback** *interface-number*
     
     
     
     The source interface that sends BGP packets is specified.
  5. Run [**peer**](cmdqueryname=peer) *ipv4-address* **ebgp-max-hop** [ *hop-count* ]
     
     
     
     The maximum number of hops between RRs for which an EBGP peer relationship is to be configured is specified.
  6. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
     
     
     
     The BGP-VPN IPv6 address family view is displayed.
  7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
     
     
     
     The exchange of VPNv6 routes with the peer RR is enabled.
  8. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**reflect-client**](cmdqueryname=reflect-client)
     
     
     
     The device is configured as an RR, and PEs are specified as its clients.
  9. Run [**peer**](cmdqueryname=peer) *ipv4-address* **next-hop-invariable**
     
     
     
     The next hop is not changed when the route is advertised to the EBGP peer.
  10. Run [**peer**](cmdqueryname=peer) *ipv4-address* **next-hop-invariable**
      
      
      
      The next hop is not changed when the route is advertised to the IBGP peer.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.