Configuring a Tunnel Interface on the Ingress
=============================================

A tunnel interface must be created before an MPLS TE tunnel is established on an ingress.

#### Context

Perform the following steps on the ingress of a TE tunnel to be established:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   A tunnel interface is created, and the tunnel interface view is displayed.
3. Run either of the following commands to assign an IP address to the tunnel interface:
   
   
   * To assign an IP address to the tunnel interface, run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ] command.
     
     The primary IP address must be configured prior to the secondary IP address for the tunnel interface.
   * To configure the tunnel interface to borrow the IP address of another interface, run the [**ip address unnumbered**](cmdqueryname=ip+address+unnumbered) **interface** *interface-type interface-number* command.
   
   To transmit IP traffic along an MPLS tunnel, you must configure an IP address for the tunnel interface. However, as an MPLS TE tunnel is unidirectional and does not involve a peer address, you do not need to configure a separate IP address for a tunnel interface. Instead, you can use the LSR ID of the tunnel egress as the tunnel address.
4. Run [**tunnel-protocol mpls te**](cmdqueryname=tunnel-protocol+mpls+te)
   
   
   
   MPLS TE is configured as the tunneling protocol.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Changing, deleting, or initially configuring the tunnel mode of a tunnel interface will delete all tunnel-related configurations on the interface, such as the MTU. Exercise caution when performing this operation.
5. Run [**destination**](cmdqueryname=destination) *ip-address*
   
   
   
   The tunnel destination address is specified. Generally, the LSR ID of the egress is used as the tunnel destination address.
   
   
   
   The required destination address varies according to the tunnel type. Therefore, if the tunneling protocol is changed to MPLS TE, the previous [**destination**](cmdqueryname=destination) configuration will be automatically deleted and you need to reconfigure a destination address.
6. Run [**mpls te tunnel-id**](cmdqueryname=mpls+te+tunnel-id) *tunnel-id*
   
   
   
   The tunnel ID is configured.
7. Run [**mpls te signal-protocol**](cmdqueryname=mpls+te+signal-protocol) **cr-static**
   
   
   
   Static CR-LSP signaling is configured.
8. Run [**mpls te bidirectional**](cmdqueryname=mpls+te+bidirectional)
   
   
   
   The bidirectional LSP attribute is configured.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.