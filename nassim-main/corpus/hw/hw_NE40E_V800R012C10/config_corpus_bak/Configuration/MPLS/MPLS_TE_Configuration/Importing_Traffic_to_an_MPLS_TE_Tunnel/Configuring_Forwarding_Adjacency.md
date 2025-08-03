Configuring Forwarding Adjacency
================================

The forwarding adjacency is configured on the ingress of a CR-LSP. The forwarding adjacency allows a route of a CR-LSP to be advertised to neighbors so that these neighbors can use this CR-LSP to transmit traffic.

#### Context

A routing protocol performs bidirectional detection on a link. The forwarding adjacency needs to be enabled on both ends of a tunnel. The forwarding adjacency allows a node to advertise a CR-LSP route to other nodes. Another tunnel for transferring data packets in the reverse direction must be configured.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Forwarding adjacency and IGP shortcut cannot be used together.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The view of an MPLS TE tunnel interface is displayed.
3. Run [**mpls te igp advertise**](cmdqueryname=mpls+te+igp+advertise) [ **hold-time** *interval* | **include-ipv6-isis** ] \*
   
   
   
   The forwarding adjacency is configured.
   
   
   
   If IPv6 IS-IS is used, the **include-ipv6-isis** parameter must be configured.
4. Configure an IGP metric for a TE tunnel.
   * For IS-IS, run the [**mpls te igp metric**](cmdqueryname=mpls+te+igp+metric) **absolute** *value* command.
   * For OSPF, run the [**mpls te igp metric**](cmdqueryname=mpls+te+igp+metric) { **absolute** | **relative** } *value* command.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Set proper IGP metrics for TE tunnels to ensure that LSP routes are correctly advertised and used. The metric of a TE tunnel should be smaller than that of an IGP route that is not expected for use.
5. You can select either of the following modes to enable the forwarding adjacency.
   
   
   * For IS-IS, run the [**isis enable**](cmdqueryname=isis+enable) [ *process-id* ] command to enable the IS-IS process of the tunnel interface.
   * For OSPF, run the following commands in sequence.
     1. Run the [**ospf enable**](cmdqueryname=ospf+enable)[ *process-id* ] **area** { *area-id* | *areaidipv4* } command to enable OSPF on the tunnel interface.
     2. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     3. Run the [**ospf**](cmdqueryname=ospf) [ *process-id* ] command to enter the OSPF view.
     4. Run the [**enable traffic-adjustment**](cmdqueryname=enable+traffic-adjustment) **advertise** command to enable the forwarding adjacency.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.