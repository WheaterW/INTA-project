Configuring External Route Exchanges Between Level 2 Carrier PEs
================================================================

The MP-BGP peer relationship is established between PEs of the Level 2 carrier to exchange IPv4 VPN routes.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** { *as-number-plain* | *as-number-dot* }
   
   
   
   The remote PE is configured as a BGP peer.
4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface loopback** *interface-number*
   
   
   
   The interface for setting up a TCP connection is specified.
5. (Optional) Run [**peer**](cmdqueryname=peer) *ipv4-address* **ebgp-max-hop** [ *hop-count* ]
   
   
   
   The maximum number of hops in the EBGP connection is specified.
   
   
   
   If the MP-EBGP peer relationship exists between the Level 2 carrier PEs, perform Step 5.
6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4**
   
   
   
   The BGP-VPNv4 address family view is displayed.
7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
   
   
   
   The exchange of the IPv4 VPN routes with the peer is enabled.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.