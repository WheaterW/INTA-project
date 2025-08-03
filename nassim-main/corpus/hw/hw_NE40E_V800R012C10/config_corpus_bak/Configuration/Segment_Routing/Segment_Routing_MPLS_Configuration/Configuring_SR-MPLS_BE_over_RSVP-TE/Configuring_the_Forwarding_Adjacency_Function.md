Configuring the Forwarding Adjacency Function
=============================================

Configure the forwarding adjacency function on the ingress of an RSVP-TE tunnel so that the ingress can advertise an LSP to neighbors for use.

#### Context

Routing protocols need to perform bidirectional checks on links. After the forwarding adjacency function is enabled for an RSVP-TE tunnel, you also need to configure a reverse RSVP-TE tunnel and enable this function for it.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The tunnel interface view of the specified MPLS TE tunnel is displayed.
3. Run [**mpls te igp advertise**](cmdqueryname=mpls+te+igp+advertise) [ **hold-time** *interval* | **include-ipv6-isis** ] \*
   
   
   
   The forwarding adjacency function is configured.
   
   
   
   If IPv6 IS-IS is used, you need to configure the **include-ipv6-isis** parameter.
4. Configure an IGP metric for the TE tunnel.
   * For IS-IS, run the [**mpls te igp metric**](cmdqueryname=mpls+te+igp+metric) **absolute** *value* command.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Configure suitable IGP metrics for RSVP-TE tunnels to ensure that LSPs are correctly advertised and used. The metric of an RSVP-TE tunnel should be smaller than that of an IGP route that is not expected to be used.
5. Enable the forwarding adjacency function.
   
   
   * For IS-IS, run the [**isis enable**](cmdqueryname=isis+enable) [ *process-id* ] command to enable the IS-IS process for the tunnel interface.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.