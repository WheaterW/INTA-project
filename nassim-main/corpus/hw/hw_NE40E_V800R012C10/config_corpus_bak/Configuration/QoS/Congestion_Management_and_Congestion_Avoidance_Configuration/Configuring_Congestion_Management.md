Configuring Congestion Management
=================================

This section describes how to configure queue scheduling parameters to implement congestion management.

#### Context

Congestion management manages and controls traffic by placing packets sent from one interface into multiple queues with different priorities. These packets are then sent based on the priorities. Different queue scheduling mechanisms are designed for different situations and lead to varying results.

Queue scheduling parameters can be configured using a port-queue profile or directly on interfaces.

* If queue scheduling parameters are required on multiple interfaces, you can configure the queue scheduling parameters in a port-queue profile to reduce configuration workload.
* If queue scheduling parameters are required only on a few interfaces and vastly vary between interfaces, you can configure the queue scheduling parameters directly on interfaces.

#### Procedure

* Configure queue scheduling parameters directly on an interface.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
  3. Run the [**port-queue**](cmdqueryname=port-queue) cos-value { { **pq** | **wfq weight** weight-value | **lpq** } | **shaping** { shaping-value | **shaping-percentage** shaping-percentage-value } [ **pbs** pbs-value ] | **port-wred** wred-name | **low-latency** } \* **outbound** or [**port-queue**](cmdqueryname=port-queue) *cos-value* **cir** { { *cir-value* [ **cbs** *cbs-value* ] **cir-schedule pq pir** *pir-value* } | { **cir-percentage** *cir-percentage-value* [ **cbs** *cbs-value* ] **cir-schedule pq pir pir-percentage** *pir-percentage-value* } } [ **pbs** *pbs-value* ] **pir-schedule** { **pq** | **wfq weight** *weight-value* | **lpq** } [ **port-wred** *wred-name* ] **outbound** command to configure queue scheduling parameters in the interface view.
  4. (Optional) Run the **[**port-queue-alarm**](cmdqueryname=port-queue-alarm)** **cos-value** ****buffer**** ****percentage**** **percentage-value** command to configure an alarm threshold for the port queue usage.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the alarm threshold for the port queue usage needs to be configured on multiple interfaces, run the **[**port-queue-alarm**](cmdqueryname=port-queue-alarm)** **cos-value** ****buffer**** ****percentage**** **percentage-value** command in the slot view. The configuration in the slot view takes effect on all the interfaces in the slot. If the configuration is performed in both the slot and interface views, the configuration in the interface view takes effect preferentially.
  5. (Optional) Run the [**port-queue-alarm**](cmdqueryname=port-queue-alarm) *cos-value* { **discard-packet** *discard-packet-number* | **discard-byte** *discard-byte-number* | **discard-packet-ratio** *discard-packet-coefficient* *discard-packet-exponent* } [ **interval** *interval-time* ] command to configure alarm thresholds for discarded packets in a port queue.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure queue scheduling parameters in a port-queue profile.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**port-queue-template**](cmdqueryname=port-queue-template) *port-queue-name* command to create a port-queue profile and enter its view.
  3. Run the [**queue**](cmdqueryname=queue) *cos-value* { { **pq** | **wfq weight** *weight-value* | **lpq** } | **shaping** { *shaping-value* | **shaping-percentage** *shaping-percentage-value* } [ **pbs** *pbs-value* ] | **port-wred** *wred-name* | **low-latency** } \* or [**queue**](cmdqueryname=queue) *cos-value* **cir** { { *cir-value* [ **cbs** *cbs-value* ] **cir-schedule pq pir** *pir-value* } | { **cir-percentage** *cir-percentage-value* [ **cbs** *cbs-value* ] **cir-schedule pq pir pir-percentage** *pir-percentage-value* } } [ **pbs** *pbs-value* ] **pir-schedule** { **pq** | **wfq weight** *weight-value* | **lpq** } [ **port-wred** *wred-name* ] command to configure scheduling parameters for queues in the port-queue profile.
  4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  5. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
  6. Run the [**port-queue-template**](cmdqueryname=port-queue-template) *port-queue-name* **outbound** command to apply the port-queue profile to the interface.
  7. (Optional) Run the **[**port-queue-alarm**](cmdqueryname=port-queue-alarm)** **cos-value** ****buffer**** ****percentage**** **percentage-value** command to configure an alarm threshold for the port queue usage.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the alarm threshold for the port queue usage needs to be configured on multiple interfaces, run the **[**port-queue-alarm**](cmdqueryname=port-queue-alarm)** **cos-value** ****buffer**** ****percentage**** **percentage-value** command in the slot view. The configuration in the slot view takes effect on all the interfaces in the slot. If the configuration is performed in both the slot and interface views, the configuration in the interface view takes effect preferentially.
  8. (Optional) Run the [**port-queue-alarm**](cmdqueryname=port-queue-alarm) *cos-value* { **discard-packet** *discard-packet-number* | **discard-byte** *discard-byte-number* | **discard-packet-ratio** *discard-packet-coefficient* *discard-packet-exponent* } [ **interval** *interval-time* ] command to configure alarm thresholds for discarded packets in a port queue.
  9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.