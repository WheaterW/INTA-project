Enabling MPLS
=============

After MPLS is enabled, related MPLS configurations can be performed.

#### Context

Perform the following steps on each LSR in an MPLS domain:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id*
   
   An LSR ID is set for a local node.
3. Run [**mpls**](cmdqueryname=mpls)
   
   MPLS is enabled globally, and the MPLS view is displayed.
4. Run [**quit**](cmdqueryname=quit)
   
   Return to the system view.
5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   An interface is configured to forward MPLS packets.
6. Run [**mpls**](cmdqueryname=mpls)
   
   MPLS is enabled on the interface.
7. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.