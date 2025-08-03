Configuring the MPLS TE Tunnel Interface
========================================

This section describes how to configure the MPLS TE tunnel interface. You must create a tunnel interface before setting up an MPLS TE tunnel.

#### Context

Perform the following steps on the ingress of a TE tunnel to be established:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   The tunnel interface is created, and the tunnel interface view is displayed.
3. Run either of the following commands to assign an IP address to the tunnel interface:
   
   
   * To assign an IP address to the tunnel interface, run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ] command.
     
     The secondary IP address of the tunnel interface can be configured only after the primary IP address is configured.
   * To borrow an IP address from another interface, run the [**ip address unnumbered**](cmdqueryname=ip+address+unnumbered) **interface** *interface-type interface-number* command.
   
   A TE tunnel can be established on a tunnel interface without an IP address. However, an IP address must be configured for the tunnel interface before it can forward traffic over the TE tunnel. An MPLS TE tunnel is unidirectional; therefore, you do not need to consider the peer IP address when performing IP address configuration for the tunnel. You are advised to specify the ingress LSR ID as the IP address of the tunnel interface, instead of configuring a unique IP address for the interface.
4. Run [**tunnel-protocol mpls te**](cmdqueryname=tunnel-protocol+mpls+te)
   
   
   
   MPLS TE is configured as the tunneling protocol.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Changing, deleting, or initially configuring the tunnel mode of a tunnel interface will delete all tunnel-related configurations on the interface, such as the MTU. Exercise caution when performing this operation.
5. Run [**destination**](cmdqueryname=destination) *ip-address*
   
   
   
   The tunnel destination address is specified. Generally, the LSR ID of the egress is used as the tunnel destination address.
6. Run [**mpls te tunnel-id**](cmdqueryname=mpls+te+tunnel-id) *tunnel-id*
   
   
   
   A tunnel ID is configured.
7. Run [**mpls te signal-protocol**](cmdqueryname=mpls+te+signal-protocol) **cr-static**
   
   
   
   Static CR-LSP is configured as a signaling protocol of the tunnel.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.