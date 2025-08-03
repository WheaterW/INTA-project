Establishing an MP-EBGP Peer Relationship Between PEs
=====================================================

By introducing extended community attributes into BGP, MP-EBGP can advertise VPNv4 routes between PEs. PEs of different ASs are generally not directly connected. Therefore, to set up the EBGP connection between the PEs of different ASs, you need to configure the permitted maximum hops between PEs.

#### Procedure

* Configure an ASBR to send the loopback interface IP addresses of a PE used for peer relationship establishment to the ASBRs of other ASs and peer PEs. You can also configure a PE to advertise its loopback interface IP addresses used for peer relationship establishment to the peer PEs.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If you want to use inter-AS traffic engineering (TE) tunnels to transmit traffic in inter-AS Option C networking, perform the following steps on PEs so that the loopback interface addresses of the PEs used for BGP session establishment can be advertised to peer PEs.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**network**](cmdqueryname=network) *ip-address* [ *mask* | *mask-length* ] [ **route-policy** *route-policy-name* ]
     
     
     
     The loopback address of the PE in the local AS is advertised to the remote ASBR.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Disable an ASBR from advertising BGP supernet labeled routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**supernet label-route advertise**](cmdqueryname=supernet+label-route+advertise) **disable**
     
     
     
     The ASBR is disabled from advertising BGP supernet labeled routes.
     
     
     
     After disabling the ASBR from advertising BGP supernet labeled routes, if you want the loopback addresses of PEs in the local AS to be advertised to PEs in another AS, you need to run the [**network**](cmdqueryname=network) command for the ASBR to advertise BGP routes carrying the loopback addresses of PEs in the local AS.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Perform the following steps on the PE that is connected to a CE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** { *as-number-plain* | *as-number-dot* }
     
     
     
     The peer PE is specified as the EBGP peer.
  4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface loopback** *interface-number*
     
     
     
     The source interface that sends BGP packets is specified.
  5. Run [**peer**](cmdqueryname=peer) *ipv4-address* **ebgp-max-hop** [ *hop-count* ]
     
     
     
     The maximum number of hops between PEs for which an EBGP peer relationship is to be configured is specified.
     
     
     
     PEs of different ASs are generally not directly connected. To set up the EBGP peer relationship between PEs of different ASs, configure the maximum number of hops between PEs and ensure that PEs are reachable.
  6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** [ **unicast** ]
     
     
     
     The BGP VPNv4 address family is displayed.
  7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
     
     
     
     The function to exchange VPNv4 routes with the peer PE is enabled.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure an RR.
  
  
  
  To improve scalability, specify an RR in each AS and establish MP-EBGP peer relationships between the RRs in ASs to save all VPNv4 routes on the RRs. Then configure PEs in each AS as the RR's clients to exchange VPNv4 routing information with the RR. Perform the following steps on a device that needs to be configured as an RR:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address1* **as-number** { *as-number-plain* | *as-number-dot* }
     
     
     
     The RR in another AS is configured as its EBGP peer.
  4. Run [**peer**](cmdqueryname=peer) *ipv4-address1* **connect-interface loopback** *interface-number*
     
     
     
     The source interface that sends BGP packets is specified.
  5. Run [**peer**](cmdqueryname=peer) *ipv4-address1* **ebgp-max-hop** [ *hop-count* ]
     
     
     
     The maximum number of hops between RRs for which an EBGP peer relationship is to be configured is specified.
  6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** [ **unicast** ]
     
     
     
     The BGP VPNv4 address family view is displayed.
  7. Run [**peer**](cmdqueryname=peer) *ipv4-address1* **enable**
     
     
     
     The function to exchange VPNv4 routes with the peer RR is enabled.
  8. Run [**peer**](cmdqueryname=peer) *ipv4-address2* [**reflect-client**](cmdqueryname=reflect-client)
     
     
     
     The device is configured as an RR, and PEs are specified as its clients.
  9. Run [**peer**](cmdqueryname=peer) *ipv4-address1* **next-hop-invariable**
     
     
     
     The next hop is not changed when the route is advertised to the EBGP peer.
  10. Run [**peer**](cmdqueryname=peer) *ipv4-address2* **next-hop-invariable**
      
      
      
      The next hop is not changed when the route is advertised to the IBGP peer.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.