Changing the PSB and RSB Timeout Multiplier
===========================================

The PSB and RSB timeout multiplier defines the maximum number of signaling packets that can be discarded in a weak signaling environment.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls rsvp-te keep-multiplier**](cmdqueryname=mpls+rsvp-te+keep-multiplier) *number*
   
   
   
   The PSB and RSB timeout multiplier is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Set the PSB and RSB timeout multiplier greater than or equal to 5. This setting prevents the PSB and RSB from aging or being deleted if the PSB and RSB fail to refresh when a great number of services are transmitted.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.