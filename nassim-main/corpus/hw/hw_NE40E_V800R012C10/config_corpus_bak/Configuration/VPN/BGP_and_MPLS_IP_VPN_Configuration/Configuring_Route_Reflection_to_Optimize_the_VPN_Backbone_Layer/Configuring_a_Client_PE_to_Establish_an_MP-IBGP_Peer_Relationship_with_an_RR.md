Configuring a Client PE to Establish an MP-IBGP Peer Relationship with an RR
============================================================================

You can configure a PE to establish an MP-IBGP peer relationship
with an RR so that the PE can receive VPNv4 routes reflected by the
RR.

#### Context

A PE or P can function as an RR on the backbone network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **as-number** *as-number*
   
   
   
   The RR is specified as a BGP peer.
4. Run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **connect-interface** **loopback** *interface-number*
   
   
   
   The interface used to establish a TCP connection is specified.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A client PE must use the loopback interface
   address with a 32-bit mask to establish an MP-IBGP peer relationship
   with the RR so that routes can recurse to a tunnel.
5. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4**
   
   
   
   The BGP-VPNv4 address family view is displayed.
6. Run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **enable**
   
   
   
   The function to exchange VPNv4 routes with the RR is enabled.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.