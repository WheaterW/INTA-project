(Optional) Configuring GR Helper Timers
=======================================

Configuring GR Helper timers includes configuring the LDP session Reconnect timer and LSP Recovery timer.

#### Context

Timers associated with LDP GR are as follows:

* Reconnect timer: After the GR restarter performs an active/standby switchover, the GR Helper detects that the LDP session with the GR Restarter fails, starts the Reconnect timer, and waits for the reestablishment of the LDP session.
  + If the Reconnect timer expires before the LDP session between the GR Helper and Restarter is established, the GR Helper immediately deletes MPLS forwarding entries associated with the GR Restarter and exits from the GR Helper process.
  + If the LDP session between the GR Helper and the GR Restarter is established before the Reconnect timer times out, the GR Helper deletes the timer and starts the Recovery timer.
* Recovery timer: After an LDP session is reestablished, the GR Helper starts the Recovery timer and waits for the LSP to recover.
  + If the Recovery timer expires, the GR Helper considers that the GR process on the neighbor is complete and deletes non-restored LSPs.
  + If all LSPs are restored before the Recovery timer expires, the GR Helper considers that the GR process is complete on the neighbor after the Recovery timer expires.
* Neighbor-liveness timer: indicates the LDP GR time.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Changing the value of an LDP GR timer also causes an LDP session to be reestablished.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**graceful-restart timer reconnect**](cmdqueryname=graceful-restart+timer+reconnect) *time*
   
   
   
   The Reconnect timer value is set.
   
   
   
   The Reconnect timer value that takes effect is the smaller value between the Neighbor-liveness timer value configured on the GR Helper and the Reconnect timer value configured on the GR Restarter.
4. Run [**graceful-restart timer recovery**](cmdqueryname=graceful-restart+timer+recovery) *time*
   
   
   
   The Recovery timer value is set.
   
   
   
   The Recovery timer value that takes effect is the smaller value between the Recovery timer value configured on the GR Helper and the Recovery timer value configured on the GR Restarter.
5. Run [**graceful-restart timer neighbor-liveness**](cmdqueryname=graceful-restart+timer+neighbor-liveness) *time*
   
   
   
   The Neighbor-liveness timer value is set.
   
   
   
   When negotiating the reconnection time of an LDP session during LDP GR, the device uses the smaller value between the Neighbor-liveness timer value configured on the GR helper and the Reconnect timer value configured on the GR restarter.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.