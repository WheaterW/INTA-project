Establishing MP-IBGP Peer Relationships Between PEs
===================================================

MP-IBGP uses extended community attributes to advertise VPNv6 routes between PEs.

#### Context

If VPN sites in a basic BGP/MPLS IPv6 VPN need to communicate, PEs must use MP-IBGP to advertise VPNv6 routes with the RD information to each other. Since all the PEs reside in the same AS, MP-IBGP peer relationships can be set up between them. In the current implementation, IPv4 BGP peer relationships are set up between PEs.

Perform the following steps on each PE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
   
   
   
   A peer PE is configured as a BGP peer.
4. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**connect-interface**](cmdqueryname=connect-interface) [**loopback**](cmdqueryname=loopback) *interface-number*
   
   
   
   An interface used to establish a TCP connection is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A PE must use a loopback interface address with a 32-bit mask to set up an MP-IBGP peer relationship with the peer PE so that VPN routes can recurse to tunnels. The route to the local loopback interface is advertised to the peer PE using an IGP on the MPLS backbone network.
5. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
   
   
   
   The BGP-VPN IPv6 address family view is displayed.
6. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
   
   
   
   The function to exchange VPN-IPv6 routes with the BGP peer is enabled.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.