Enabling BFD Globally
=====================

To configure dynamic BFD for RSVP, you must enable BFD on both ends of RSVP neighbors.

#### Context

Perform the following steps on the two RSVP neighboring nodes between which a Layer 2 device resides:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled globally.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.