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
3. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** { *as-number-plain* | *as-number-dot* }
   
   
   
   The remote PE is configured as a BGP peer.
4. Run [**peer**](cmdqueryname=peer+connect-interface) *ipv4-address* **connect-interface loopback** *interface-number*
   
   
   
   The interface for setting up a TCP connection is specified.
5. (Optional) Run [**peer**](cmdqueryname=peer+ebgp-max-hop) *ipv4-address* **ebgp-max-hop** [ *hop-count* ]
   
   
   
   The maximum number of hops allowed for an EBGP connection is specified.
   
   
   
   If an MP-EBGP peer relationship exists between Level 2 carrier PEs, you need to perform Step 5.
6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** [ **unicast** ]
   
   
   
   The BGP VPNv4 address family view is displayed.
7. Run [**peer**](cmdqueryname=peer+enable) *ipv4-address* **enable**
   
   
   
   The function to exchange IPv4 VPN routes with the peer is enabled.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.