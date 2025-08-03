(Optional) Setting RSVP Authentication Lifetime
===============================================

The RSVP authentication lifetime is set to prevent RSVP authentication from being prolonged when CR-LSP flapping causes frequent reestablishment of RSVP neighbor relationships and repeatedly performed handshake.

#### Context

RSVP neighbors retain an RSVP neighbor relationship within a specified RSVP authentication lifetime even if there are no CR-LSPs between the RSVP neighbors. Configuring the RSVP authentication lifetime does not affect existing CR-LSPs.


#### Procedure

* Configure RSVP authentication lifetime in the interface view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The view of an RSVP-enabled interface is displayed.
  3. Run [**mpls rsvp-te authentication lifetime**](cmdqueryname=mpls+rsvp-te+authentication+lifetime) *lifetime*
     
     
     
     The RSVP authentication lifetime is set.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the RSVP authentication lifetime in the MPLS RSVP-TE peer view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls rsvp-te peer**](cmdqueryname=mpls+rsvp-te+peer) *peer-addr*
     
     
     
     The MPLS RSVP-TE peer view is displayed.
     
     If *peer-addr* is an interface IP address of the neighbor, not the neighbor LSR ID, key authentication will only take effect on that neighbor interface. Key authentication then provides high security and has the highest priority.
     
     If *peer-addr* is a neighbor LSR ID, key authentication will take effect on all interfaces on the neighbor. Authentication configured using this method has a lower priority than that configured based on the neighbor's interface IP address but has a higher priority than that configured in the interface view.
  4. Run [**mpls rsvp-te authentication lifetime**](cmdqueryname=mpls+rsvp-te+authentication+lifetime) *lifetime*
     
     
     
     The RSVP authentication lifetime is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.