Configuring External Route Exchanges Between Level 2 Carrier PEs
================================================================

This section describes how to configure the MP-BGP peer relationship between PEs to exchange VPNv6 routes.

#### Procedure

* Perform the following steps on the Level 2 carrier PE:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** { *as-number-plain* | *as-number-dot* }
     
     
     
     The remote PE is specified as the BGP peer.
  4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface loopback** *interface-number*
     
     
     
     The interface used to set up a TCP connection is specified.
  5. Run [**peer**](cmdqueryname=peer) *ipv4-address* **ebgp-max-hop** [ *hop-count* ]
     
     
     
     The number of maximum hops of the EBGP connection is set.
     
     If the MP-EBGP peer relationship exists between the Level 2 carrier PEs, you need to configure Step 5.
  6. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
     
     
     
     The BGP-VPN IPv6 address family is displayed.
  7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
     
     
     
     The function of exchanging VPN-IPv6 routes with the peer is enabled.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.