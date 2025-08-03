Configuring Route Exchange Between a Hub-PE and a Spoke-PE
==========================================================

By introducing extended community attributes into BGP, MP-IBGP can advertise VPNv4 routes between PEs.

#### Context

An MP-IBGP peer relationship needs to be established between the Hub-PE and each Spoke-PE. Spoke-PEs do not need to exchange routes directly and therefore they do not need to establish MP-IBGP peer relationships.

Perform the following steps on the Hub-PE and all the Spoke-PEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *peer-address* **as-number** *as-number*
   
   
   
   The remote PE is configured as a BGP peer.
4. Run [**peer**](cmdqueryname=peer) *peer-address* **connect-interface** **loopback** *interface-number*
   
   
   
   The interface used to establish a TCP connection is specified.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   PEs must use the loopback interface addresses with 32-bit masks to establish an MP-IBGP peer relationship so that routes can recurse to a tunnel. The route to the loopback interface is advertised to the peer PE through IGP on the MPLS backbone network.
5. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** [ **unicast** ]
   
   
   
   The BGP-VPNv4 address family view is displayed.
6. Run [**peer**](cmdqueryname=peer) *peer-address* **enable**
   
   
   
   The capability of exchanging BGP VPNv4 routing information with the peer is enabled.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.