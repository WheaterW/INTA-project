Enabling BFD for RSVP
=====================

You can enable BFD for RSVP either globally or on a specified interface.

#### Context

Perform either of the following operations:

* [Enable BFD for RSVP globally](#EN-US_TASK_0172368277__step_dc_vrp_cfg_00381601) if most RSVP interfaces on a node need BFD for RSVP.
* [Enable BFD for RSVP on an RSVP interface](#EN-US_TASK_0172368277__step_dc_vrp_cfg_00381602) if some RSVP interfaces on a node need BFD for RSVP.

#### Procedure

* Enable BFD for RSVP globally.
  
  
  
  Perform the following steps on the two RSVP neighboring nodes between which a Layer 2 device resides:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls rsvp-te bfd all-interfaces enable**](cmdqueryname=mpls+rsvp-te+bfd+all-interfaces+enable)
     
     
     
     BFD for RSVP is enabled globally.
     
     After this command is run in the MPLS view, BFD for RSVP is enabled on all RSVP interfaces except the interfaces with BFD for RSVP that are blocked.
  4. (Optional) Block BFD for RSVP on the RSVP interfaces that do not need BFD for RSVP.
     
     
     + Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     + Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the RSVP interface view.
     + Run the [**mpls rsvp-te bfd block**](cmdqueryname=mpls+rsvp-te+bfd+block) command to block BFD for RSVP on the interface.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable BFD for RSVP on the RSVP interface.
  
  
  
  Perform the following steps on the two RSVP neighboring nodes between which a Layer 2 device resides:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of an RSVP-enabled interface is displayed.
  3. Run [**mpls rsvp-te bfd enable**](cmdqueryname=mpls+rsvp-te+bfd+enable)
     
     
     
     BFD for RSVP is enabled on the RSVP interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.