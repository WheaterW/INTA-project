Configuring MPLS GR Helper on the Backbone Network
==================================================

In the process of master/slave control board switchover or the system upgrade, you can configure MPLS GR Helper to ensure normal MPLS traffic forwarding. If LDP LSPs are configured on the backbone network, you can configure MPLS LDP GR Helper; if RSVP-TE tunnels are configured on the backbone network, you can configure MPLS RSVP GR Helper; if other types of tunnels are configured on the backbone network, you do not need to perform the operation.

#### Context

You can configure different MPLS GR Helper functions on a backbone network for different tunnel types.

* If LDP LSPs are used, configure the MPLS LDP GR Helper function on the backbone network.
* If RSVP-TE tunnels are used, configure the MPLS RSVP GR Helper function on the backbone network.


#### Procedure

* Configure MPLS LDP GR.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     LDP is enabled on the local LSR and the MPLS LDP view is displayed.
  3. Run [**graceful-restart**](cmdqueryname=graceful-restart)
     
     
     
     LDP GR is enabled.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + Enabling or disabling LDP GR can lead to reestablishment of an LDP session.
     + During the LDP GR, the [**undo mpls ldp**](cmdqueryname=undo+mpls+ldp) command and the [**reset mpls ldp**](cmdqueryname=reset+mpls+ldp) command cannot be run.
  4. (Optional) Run [**graceful-restart timer reconnect**](cmdqueryname=graceful-restart+timer+reconnect) *time*
     
     
     
     The value of a Reconnect timer is set.
     
     
     
     After a GR Restarter performs an active/standby switchover, a GR helper detects that an LDP session established between the GR Helper and Restarter fails and then starts a Reconnect timer and waits for the reestablishment of the LDP session.
     + If the Reconnect timer expires before the LDP session between the GR Helper and Restarter is established, the GR Helper immediately deletes MPLS forwarding entries associated with the GR Restarter and exits from the GR Helper process.
     + If the LDP session between the GR Helper and Restarter is established before the Reconnect timer expires, the GR Helper deletes the timer and starts a Recovery timer.
     
     When the GR Restarter and Helper negotiate the time to reestablish the LDP session, the value of the Reconnect timer that takes effect on the local end is the smaller value between the Neighbor-liveness timer value on the GR Helper and the Reconnect timer value on the GR Restarter.
  5. (Optional) Run [**graceful-restart timer recovery**](cmdqueryname=graceful-restart+timer+recovery) *time*
     
     
     
     The value of a Recovery timer is set.
     
     
     
     A GR Helper starts a Recovery timer after an LDP session is reestablished and waits for LSP recovery.
     + If the Recovery timer expires before LSPs are reestablished, the GR Helper considers that the GR process is completed on the GR Restarter and deletes the unrecovered LSPs.
     + If all LSPs recover before the Recovery timer expires, the GR Helper considers that the GR process is completed on the GR Restarter only after the Recovery timer expires.
     
     On a network with a large number of routes is faulty, run the [**graceful-restart timer recovery**](cmdqueryname=graceful-restart+timer+recovery) command to increase the value of the Recovery timer to ensure that all LSPs recover before the timer expires.
     
     LDP GR devices negotiate the LSP Recovery timer values. The value that takes effect on the local end is the smaller one between the locally configured value and the value sent by the peer.
  6. (Optional) Run [**graceful-restart timer neighbor-liveness**](cmdqueryname=graceful-restart+timer+neighbor-liveness) *time*
     
     
     
     The value of a Neighbor-liveness timer is set.
     
     
     
     LDP GR-enabled devices negotiate the LDP reconnection time and uses the smaller value between the Neighbor-liveness time configured on a Helper and the Reconnect time configured on the Restarter. On a network with a few LSPs, the [**graceful-restart timer neighbor-liveness**](cmdqueryname=graceful-restart+timer+neighbor-liveness) command can be run to set a small value for the Neighbor-liveness timer to shorten the GR period.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configurations are committed.
* Configure RSVP GR.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls rsvp-te**](cmdqueryname=mpls+rsvp-te)
     
     
     
     RSVP-TE is enabled.
  4. Run [**mpls rsvp-te hello**](cmdqueryname=mpls+rsvp-te+hello)
     
     
     
     The RSVP Hello extension is enabled globally.
  5. Run [**mpls rsvp-te hello support-peer-gr**](cmdqueryname=mpls+rsvp-te+hello+support-peer-gr)
     
     
     
     The RSVP GR support function is enabled.
  6. (Optional) Run [**mpls rsvp-te hello nodeid-session**](cmdqueryname=mpls+rsvp-te+hello+nodeid-session) *ip-address*
     
     
     
     A Hello session is set up between two RSVP neighboring nodes.
     
     *ip-address* specifies the LSR ID of an RSVP neighboring node.
     
     On a TE FRR network, to ensure the protection of the primary tunnel when FRR and RSVP-TE GR simultaneously occur, run the **mpls rsvp-te hello nodeid-session** command to establish a Hello session between a Point of Local Repair (PLR) node and a Merge Point (MP).
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  8. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The view of an MPLS TE interface is displayed.
  9. Run [**mpls rsvp-te hello**](cmdqueryname=mpls+rsvp-te+hello)
     
     
     
     The RSVP Hello extension is enabled on an interface. This function needs to be configured on each involved interface after being enabled globally.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.