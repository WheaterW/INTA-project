Configuring an E2E SR-MPLS TE Tunnel Interface
==============================================

A tunnel interface must be configured on an ingress so that the interface is used to establish and manage an E2E SR-MPLS TE tunnel.

#### Context

An SR-MPLS TE tunnel is unidirectional. To configure a reverse tunnel, perform the configuration on the ingress of the reverse tunnel.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   An inter-AS E2E tunnel interface is created, and the tunnel interface view is displayed.
3. Run either of the following commands to assign an IP address to the tunnel interface:
   
   
   * To configure an IP address for the tunnel interface, run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ] command.
     
     The secondary IP address of the tunnel interface can be configured only after the primary IP address is configured.
   * To configure the tunnel interface to borrow the IP address of another interface, run the [**ip address unnumbered**](cmdqueryname=ip+address+unnumbered) **interface** *interface-type* *interface-number* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SR-MPLS TE tunnel is unidirectional and does not need a peer IP address. A separate IP address for the tunnel interface is not recommended. Use the LSR ID of the ingress as the tunnel interface's IP address.
4. Run [**tunnel-protocol**](cmdqueryname=tunnel-protocol) **mpls** **te**
   
   
   
   MPLS TE is configured as a tunneling protocol.
5. Run [**destination**](cmdqueryname=destination) *ip-address*
   
   
   
   A tunnel destination address, which is usually the LSR ID of the egress, is configured.
   
   Various types of tunnels require specific destination addresses. If a tunnel protocol is changed from another protocol to MPLS TE, a configured destination address is deleted automatically and a new destination address needs to be configured.
6. Run [**mpls te tunnel-id**](cmdqueryname=mpls+te+tunnel-id) *tunnel-id*
   
   
   
   A tunnel ID is set.
7. Run [**mpls te signal-protocol**](cmdqueryname=mpls+te+signal-protocol) **segment-routing**
   
   
   
   Segment Routing is configured as the signaling protocol of the TE tunnel.
8. Run [**mpls te pce delegate**](cmdqueryname=mpls+te+pce+delegate)
   
   
   
   PCE server delegation is enabled so that the controller can compute paths.
9. (Optional) Run the [**match dscp**](cmdqueryname=match+dscp) { **ipv4** | **ipv6** } { **default** | { *dscp-value* [ **to** *dscp-value* ] } &<1-32> } command to configure DSCP values for IPv4/IPv6 packets to enter the SR-MPLS TE tunnel.
   
   
   
   The DSCP configuration and [**mpls te service-class**](cmdqueryname=mpls+te+service-class) command configuration of an SR-MPLS TE tunnel are mutually exclusive.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.