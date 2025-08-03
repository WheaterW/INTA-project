Enabling RSVP-TE Reservation Confirmation
=========================================

RSVP-TE reservation confirmation configured on the egress of a tunnel verifies that resources are successfully reserved.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls rsvp-te resvconfirm**](cmdqueryname=mpls+rsvp-te+resvconfirm)
   
   
   
   RSVP-TE reservation confirmation is enabled.
   
   
   
   After a node receives a Path message, it initiates reservation confirmation by sending a Resv message carrying an object that requests reservation confirmation.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Receiving ResvConf messages does not mean that resource reservation is successful. It merely indicates that resources have been successfully reserved at the furthest upstream node that receives this Resv message. These resources could be later preempted by other applications.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.