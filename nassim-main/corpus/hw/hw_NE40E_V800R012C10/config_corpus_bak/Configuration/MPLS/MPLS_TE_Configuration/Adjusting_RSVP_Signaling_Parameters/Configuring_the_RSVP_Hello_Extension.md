Configuring the RSVP Hello Extension
====================================

The RSVP Hello extension rapidly monitors the connectivity of RSVP neighbors.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls rsvp-te hello**](cmdqueryname=mpls+rsvp-te+hello)
   
   
   
   The RSVP Hello extension is enabled on the local node.
4. Run [**mpls rsvp-te hello-lost**](cmdqueryname=mpls+rsvp-te+hello-lost) *times*
   
   
   
   The maximum number of Hello messages that can be discarded is set.
5. Run [**mpls rsvp-te timer hello**](cmdqueryname=mpls+rsvp-te+timer+hello) *interval*
   
   
   
   The interval at which Hello messages are refreshed is set.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the refresh interval is changed, the modification takes effect after the existing refresh timer expires.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   The system view is displayed.
7. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of an RSVP-enabled interface is displayed.
8. Run [**mpls rsvp-te hello**](cmdqueryname=mpls+rsvp-te+hello)
   
   
   
   The RSVP Hello extension is enabled on an interface.
   
   The RSVP Hello extension rapidly detects the reachability of RSVP neighbors. For details, see relevant standards.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.