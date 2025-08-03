Configuring RSVP-TE Srefresh
============================

Enabling Summary Refresh (Srefresh) on interfaces connecting two RSVP neighboring nodes reduces the network cost and improves network performance.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
   
   Srefresh enabled in the MPLS view takes effect on an entire device.
3. Run [**mpls rsvp-te srefresh**](cmdqueryname=mpls+rsvp-te+srefresh)
   
   
   
   Srefresh is enabled.
4. (Optional) Run [**mpls rsvp-te timer retransmission**](cmdqueryname=mpls+rsvp-te+timer+retransmission) { **increment-value** *incvalue* | **retransmit-value** *retvalue* } \*
   
   
   
   The retransmission parameters are set.
5. (Optional) Enable the summary refresh (Srefresh) forward compatibility.
   1. Run [**quit**](cmdqueryname=quit)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
      
      
      
      The view of the interface on which the MPLS TE tunnel is established is displayed.
   3. Run [**mpls rsvp-te srefresh compatible**](cmdqueryname=mpls+rsvp-te+srefresh+compatible)
      
      
      
      The Srefresh forward compatibility is enabled.
   
   
   
   When the primary and backup CR-LSPs share the same link, the node on both ends of the link may run different versions. If the upstream nodes run a version earlier than V8 and the downstream node runs V8, Srefresh incompatibility occurs. To address this problem, run the [**mpls rsvp-te srefresh compatible**](cmdqueryname=mpls+rsvp-te+srefresh+compatible) command on the interface that connects the downstream device to the upstream node to enable Srefresh compatibility.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command can only be run on a downstream node running V8 when its upstream node runs a version earlier than V8, which ensures that Srefresh can be properly negotiated between the two nodes.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.