Configuring the Tunnel Interface on the Egress
==============================================

The reverse tunnel attribute is configured, and the tunnel interface is bound to a static bidirectional co-routed LSP on the egress.

#### Context

Perform the following steps on the egress of a static bidirectional co-routed LSP:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   A tunnel interface is created, and the tunnel interface view is displayed.
3. Run [**tunnel-protocol mpls te**](cmdqueryname=tunnel-protocol+mpls+te)
   
   
   
   MPLS TE is configured as the tunneling protocol to create an MPLS TE tunnel.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Changing, deleting, or initially configuring the tunnel mode of a tunnel interface will delete all tunnel-related configurations on the interface, such as the MTU. Exercise caution when performing this operation.
4. Run [**destination**](cmdqueryname=destination) *ip-address*
   
   
   
   The tunnel destination address is specified. Generally, the LSR ID of the ingress is used as the tunnel destination address.
   
   
   
   The required destination address varies according to the tunnel type. Therefore, if the tunneling protocol is changed to MPLS TE, the previous [**destination**](cmdqueryname=destination) configuration will be automatically deleted and you need to reconfigure a destination address.
5. Run [**mpls te tunnel-id**](cmdqueryname=mpls+te+tunnel-id) *tunnel-id*
   
   
   
   A tunnel ID is configured.
6. Run [**mpls te signal-protocol**](cmdqueryname=mpls+te+signal-protocol) **cr-static**
   
   
   
   A static CR-LSP is configured.
7. Run [**mpls te passive-tunnel**](cmdqueryname=mpls+te+passive-tunnel)
   
   
   
   The reverse tunnel attribute is configured.
8. Run [**mpls te binding**](cmdqueryname=mpls+te+binding) **bidirectional** **static-cr-lsp** **egress** *tunnel-name*
   
   
   
   The tunnel interface is bound to the specified static bidirectional co-routed LSP.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.