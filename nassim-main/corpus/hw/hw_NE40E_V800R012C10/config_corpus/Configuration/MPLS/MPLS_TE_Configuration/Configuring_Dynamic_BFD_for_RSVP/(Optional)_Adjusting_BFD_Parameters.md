(Optional) Adjusting BFD Parameters
===================================

BFD parameters can be adjusted either globally or on a specific RSVP interface after BFD for RSVP is configured.

#### Context

Perform either of the following operations:

* [Adjust global BFD parameters](#EN-US_TASK_0172368278__step_dc_vrp_cfg_00381701) if most RSVP interfaces on a node use the same BFD parameters.
* [Adjust BFD parameters on an RSVP interface](#EN-US_TASK_0172368278__step_dc_vrp_cfg_00381702) if some RSVP interfaces require BFD parameters different from global BFD parameters.

#### Procedure

* Adjust global BFD parameters globally.
  
  
  
  Perform the following steps on the two RSVP neighboring nodes between which a Layer 2 device resides:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls rsvp-te bfd all-interfaces**](cmdqueryname=mpls+rsvp-te+bfd+all-interfaces) { **min-tx-interval** *tx-interval* | **min-rx-interval** *rx-interval* | **detect-multiplier** *multiplier* } \*
     
     
     
     BFD parameters are set globally.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) BFD detection parameters that take effect on the local node may be different from the configured parameters:
     + Effective local interval at which BFD packets are sent = MAX { min-tx-interval configured for local device, min-rx-interval configured for remote device }
     + Effective local interval at which BFD packets are received = MAX { min-tx-interval configured for remote device, min-rx-interval configured for local device }
     + Effective local detection interval = MAX { min-tx-interval configured for remote device, min-rx-interval configured for local device } x Configured remote detection multiplier
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Adjust BFD parameters on an RSVP interface.
  
  
  
  Perform the following steps on the two RSVP neighboring nodes between which a Layer 2 device resides:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the RSVP-enabled interface is displayed.
  3. Run [**mpls rsvp-te bfd**](cmdqueryname=mpls+rsvp-te+bfd) { **min-tx-interval** *tx-interval* | **min-rx-interval** *rx-interval* | **detect-multiplier** *multiplier* } \*
     
     
     
     BFD parameters on the RSVP interface are adjusted.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.