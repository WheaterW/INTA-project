Applying WRED
=============

You can apply the configured WRED profile based on the service type.

#### Context

Do as follows on the Router that is configured with a WRED profile.


#### Procedure

* Apply WRED in the interface view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**port-queue**](cmdqueryname=port-queue) *cos-value* **port-wred** *wred-name* **outbound**
     
     
     
     A WRED profile is applied to a specified port queue in the outbound direction of the interface.
  4. (Optional) Run [**qos buffer-monitor default-queue enable**](cmdqueryname=qos+buffer-monitor+default-queue+enable)
     
     
     
     Buffer monitoring is enabled for the default SQ.
     
     
     
     After buffer monitoring is enabled for the default SQ on an interface, the device collects the buffer value of the default SQ on the interface. You can use the NMS or run the [**display port-queue statistics interface outbound default**](cmdqueryname=display+port-queue+statistics+interface+outbound+default) command to view the buffer value's change trend, determining whether traffic congestion occurs.
  5. (Optional) Run [**port-queue-alarm**](cmdqueryname=port-queue-alarm) *cos-value* **buffer** **percentage** *percentage-value*
     
     
     
     An alarm threshold is set for the usage of QoS queues in the outbound direction of the interface.
  6. (Optional) Run [**port-queue-alarm**](cmdqueryname=port-queue-alarm) *cos-value* { **discard-packet** *discard-packet-number* | **discard-byte** *discard-byte-number* | **discard-packet-ratio** *discard-packet-coefficient* *discard-packet-exponent* } **interval** *interval-time*
     
     
     
     The packet loss alarm function is enabled for port queues.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  8. Run **quit**
     
     
     
     Return to the system view.
* Apply WRED to the MTunnel interface configured in the slot view.
  1. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  2. Run [**port-queue**](cmdqueryname=port-queue) *cos-value* { { **pq** | **wfq** **weight** *weight-value* | **lpq** } | **shaping** { *shaping-value* | **shaping-percentage** *shaping-percentage-value* } | **port-wred** *wred-name* } \* **outbound** **bind** **mtunnel**
     
     
     
     Scheduling policies are configured for multicast queues of different classes on the MTunnel interface that is bound to distributed multicast VPN, and the configured WRED profile is applied to these scheduling policies.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.