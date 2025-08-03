Configuring a Client PE to Establish an MP-IBGP Peer Relationship with the RR
=============================================================================

You can configure a PE to establish an MP-IBGP peer relationship with an RR so that the PE can receive VPNv6 routes reflected by the RR.

#### Context

Perform the following steps on each client PE:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
   
   
   
   The RR is specified as a BGP peer.
4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface** *interface-type* *interface-number*
   
   
   
   The interface used to establish a TCP connection is specified.
5. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
   
   
   
   The BGP-VPN IPv6 address family view is displayed.
6. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
   
   
   
   The function to exchange VPNv6 routes with the RR is enabled on the PE.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.