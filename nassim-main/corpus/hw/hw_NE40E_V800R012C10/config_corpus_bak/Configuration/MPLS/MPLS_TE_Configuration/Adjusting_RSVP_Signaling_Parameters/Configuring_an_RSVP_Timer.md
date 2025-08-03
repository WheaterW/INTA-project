Configuring an RSVP Timer
=========================

An RSVP timer is configured to define the interval at which Path and Resv messages are refreshed, and the timeout multiplier associated with the RSVP blocked state is also configured.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls rsvp-te timer refresh**](cmdqueryname=mpls+rsvp-te+timer+refresh) *interval*
   
   
   
   The interval at which Path and Resv messages are refreshed is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the refresh interval is modified, the modification takes effect after the existing refresh timer expires. You are advised not to set a long refresh interval or frequently modify a refresh interval.
4. Run [**mpls rsvp-te keep-multiplier**](cmdqueryname=mpls+rsvp-te+keep-multiplier) *number*
   
   
   
   The PSB and RSB timeout multiplier is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.