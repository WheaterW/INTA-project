Configuring External Route Exchange Between Level 2 Carrier PEs
===============================================================

An MP-BGP peer relationship is established between Level 2 carrier PEs to exchange IPv4 VPN routes.

#### Context

Perform the following steps on each Level 2 carrier PE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** { *as-number-plain* | *as-number-dot* }
   
   
   
   The remote PE is configured as a peer.
4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface loopback** *interface-number*
   
   
   
   The interface for setting up a TCP connection is specified.
5. (Optional) Run [**peer**](cmdqueryname=peer) *ipv4-address* **ebgp-max-hop** [ *hop-count* ]
   
   
   
   The maximum number of hops supported in an EBGP connection is specified.
   
   
   
   If the MP-EBGP peer relationship exists between the Level 2 carrier PEs, perform Step 5.
6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** [ **unicast** ]
   
   
   
   The BGP VPNv4 address family is displayed.
7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
   
   
   
   The exchange of the IPv4 VPN routes with the peer is enabled.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.