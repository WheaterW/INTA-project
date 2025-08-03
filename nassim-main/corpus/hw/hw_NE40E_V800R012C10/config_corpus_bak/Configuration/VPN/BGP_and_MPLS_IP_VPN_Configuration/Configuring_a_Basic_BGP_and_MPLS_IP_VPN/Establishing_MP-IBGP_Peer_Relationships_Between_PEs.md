Establishing MP-IBGP Peer Relationships Between PEs
===================================================

By introducing extended community attributes into BGP, MP-IBGP can advertise VPNv4 routes between PEs.

#### Context

If VPN sites in a basic BGP/MPLS IP VPN need to communicate, PEs must use MP-IBGP to advertise VPNv4 routes with the RD information to each other. Since all the PEs reside in the same AS, MP-IBGP peer relationships can be set up between them.

Perform the following steps on each PE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
   
   
   
   The remote PE is configured as a peer.
4. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**connect-interface**](cmdqueryname=connect-interface) **loopback** *interface-number*
   
   
   
   An interface is specified for setting up a TCP connection with the BGP peer.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A PE must use a loopback interface address with a 32-bit mask to set up an MP-IBGP peer relationship with the peer PE so that VPN routes can recurse to tunnels. The route to the local loopback interface is advertised to the peer PE using IGP on the MPLS backbone network.
5. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4**
   
   
   
   The BGP-VPNv4 address family view is displayed.
6. (Optional) Run [**activate-route-tag compatible**](cmdqueryname=activate-route-tag+compatible)
   
   
   
   The function to match VPNv4 routes (with a non-zero tag value) against the rule configured using the [**if-match tag**](cmdqueryname=if-match+tag) command is enabled.
   
   
   
   The default tag value of VPNv4 routes is 0, and the VPNv4 routes that carry tag 0 are matched against the rule configured using the [**if-match tag**](cmdqueryname=if-match+tag) command by default. If the tag value of a VPNv4 route is not 0, you need to run the [**activate-route-tag compatible**](cmdqueryname=activate-route-tag+compatible) command to enable the [**if-match tag**](cmdqueryname=if-match+tag) command, so that the VPNv4 route can be matched against the rule configured using the [**if-match tag**](cmdqueryname=if-match+tag) command.
7. (Optional) Run [**vpn-orf disable**](cmdqueryname=vpn-orf+disable)
   
   
   
   VPN ORF is disabled.
   
   
   
   By default, VPN ORF is enabled for VPNv4 and VPNv6 routes. After the [**vpn-orf disable**](cmdqueryname=vpn-orf+disable) command is run, the device that has established a BGP-VPNv4/BGP-VPNv6 peer relationship does not filter VPN routes based on the import VPN target (IRT) of the remote peer when advertising VPN routes.
8. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
   
   
   
   The function to exchange VPN-IPv4 routing information with the specified peer is enabled.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.