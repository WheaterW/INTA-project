Setting Priority Values for an MPLS TE Tunnel
=============================================

The priority values are set on the ingress of an MPLS TE tunnel. Preemption is performed based on the setup and holding priorities during the establishment of an MPLS TE tunnel.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The view of the MPLS TE tunnel interface is displayed.
3. Run [**mpls te priority**](cmdqueryname=mpls+te+priority) *setup-priority* [ *hold-priority* ]
   
   
   
   The priority values are set for the MPLS TE tunnel.
   
   Both the setup and holding priority values range from 0 to 7. The smaller the value, the higher the priority.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The setup priority value must be greater than or equal to the holding priority value. This means the setup priority is lower than or equal to the holding priority.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.