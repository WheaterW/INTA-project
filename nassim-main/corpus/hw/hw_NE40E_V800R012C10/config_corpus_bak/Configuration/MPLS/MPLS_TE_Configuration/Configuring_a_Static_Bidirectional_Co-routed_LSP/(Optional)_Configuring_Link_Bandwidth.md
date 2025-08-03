(Optional) Configuring Link Bandwidth
=====================================

By configuring the link bandwidth, you can constrain the bandwidth of a CR-LSP. This section describes how to configure link bandwidth so that nodes can reserve the configured link bandwidth for an LSP to be established.

#### Context

Plan link bandwidth before you perform this procedure. The reserved bandwidth must be higher than or equal to the bandwidth required by MPLS TE traffic. Perform the following steps on each node along the tunnel to be established:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of an MPLS TE-enabled interface is displayed.
3. Run [**mpls te bandwidth max-reservable-bandwidth**](cmdqueryname=mpls+te+bandwidth+max-reservable-bandwidth) *max-bw-value*
   
   
   
   The maximum reservable link bandwidth is set.
4. Run [**mpls te bandwidth**](cmdqueryname=mpls+te+bandwidth) **bc0** *bc0-bw-value*
   
   
   
   The BC bandwidth is set for the link.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The maximum reservable bandwidth of a link cannot be higher than the actual bandwidth of the link. A maximum of 80% of the actual bandwidth of the link is recommended for the maximum reservable bandwidth of the link.
   * The BC0 bandwidth cannot be higher than the maximum reservable bandwidth of the link.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.