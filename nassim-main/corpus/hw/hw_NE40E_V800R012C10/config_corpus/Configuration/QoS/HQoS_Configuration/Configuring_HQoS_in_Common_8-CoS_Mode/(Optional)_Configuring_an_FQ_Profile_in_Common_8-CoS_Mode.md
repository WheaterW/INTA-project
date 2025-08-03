(Optional) Configuring an FQ Profile in Common 8-CoS Mode
=========================================================

You can configure scheduling parameters and traffic shaping for FQs in common 8-CoS mode based on network requirements.

#### Context

You can use a non-default FQ profile to configure scheduling parameters for FQs based on network requirements. Multiple flow WRED objects can be created for FQs to reference. You can set upper and lower drop thresholds and a drop probability for a created flow WRED profile. When the percentage of the actual length of a queue over the length of an FQ is less than the lower drop threshold, the system does not drop packets; when the percentage of the actual length of a queue over the length of an FQ is between the upper and lower drop thresholds, the system drops packets through the WRED mechanism (the longer the queue length, the higher the drop probability); when the percentage of the actual length of a queue over the length of an FQ is greater than the upper drop threshold, the system drops all subsequent packets.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The upper and lower drop thresholds for red packets can be set to the minimum; those for yellow packets can be greater; those for green packets can be set to the maximum.
* In the actual configuration, the lower drop threshold is recommended to begin with 50% and be adjusted based on different colors of packets. 100% is recommended for the drop probability.
* If no flow WRED object is set, the system adopts the default tail drop policy.


#### Procedure

* Configure a flow WRED object.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**flow-wred**](cmdqueryname=flow-wred) *wred-name*
     
     
     
     A flow WRED object is created and its view is displayed.
  3. Run [**color**](cmdqueryname=color) { **green** | **yellow** | **red** } **low-limit** *low-limit-percentage* **high-limit** *high-limit-percentage* **discard-percentage** *discard-percentage*
     
     
     
     Upper and lower drop thresholds as well as a drop probability are configured.
  4. Run [**queue-depth**](cmdqueryname=queue-depth) *queue-depth-value*
     
     
     
     A queue depth is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
* Configure scheduling parameters for an FQ.
  1. Run [**flow-queue**](cmdqueryname=flow-queue) *flow-queue-name*
     
     
     
     The FQ view is displayed.
  2. Run [**queue**](cmdqueryname=queue) *cos-value* { { **pq** | **wfq** **weight** *weight-value* | **lpq** } | { **shaping** { *shaping-value* | **shaping-percentage** *shaping-percentage-value* } [ **pbs** *pbs-value* ] | **car** { *car-value* | **car-percentage** *car-percentage-value* } [ **pbs** *pbs-value* ] } | **flow-wred** *wred-name* | **low-latency** | **low-jitter** } \* or [**queue**](cmdqueryname=queue) *cos-value* **cir** { { *cir-value* [ **cbs** *cbs-value* ] **cir-schedule** **pq** **pir** *pir-value* } | { **cir-percentage** *cir-percentage-value* [ **cbs** *cbs-value* ] **cir-schedule** **pq** **pir** **pir-percentage** *pir-percentage-value* } } [ **pbs** *pbs-value* ] **pir-schedule** { **pq** | **wfq** **weight** *weight-value* | **lpq** } [ **flow-wred** *wred-name* ]
     
     
     
     The scheduling parameters and policy of the FQ are modified.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure share shaping.
  1. Run [**share-shaping**](cmdqueryname=share-shaping) [ *shap-id* ] { **af1** | **af2** | **af3** | **af4** | **be** | **cs6** | **cs7** | **ef** } \* [ **pq** | **wfq** **weight** *weight-value* | **lpq** ] *shaping-value* [ **pbs** *pbs-value* ]
     
     
     
     Share shaping is configured for multiple FQs.
     
     After share shaping is configured for queues, they are shaped before being scheduled together with other user queues.
  2. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
* Enable the low-latency function for FQs in PQ scheduling mode.
  1. Run [**qos flow-queue low-latency enable**](cmdqueryname=qos+flow-queue+low-latency+enable)
     
     
     
     The low-latency function is enabled for FQs in PQ scheduling mode to ensure the latency of PQ scheduling.
* Configure the PQ scheduling priority, the burst size, and the shared threshold for buffer resources.
  1. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  2. Run [**qos cos**](cmdqueryname=qos+cos) { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **burst-size** *buffer-size-value*
     
     
     
     The burst size of a module is configured.
  3. Run **[**qos cos all pack-size**](cmdqueryname=qos+cos+all+pack-size)** **pack-size-value**
     
     
     
     The maximum packet size is configured on the eTM subcard.
  4. Run [**qos pq-scheduler priority**](cmdqueryname=qos+pq-scheduler+priority) { **high** | **low** } { **inbound** | **outbound** }
     
     
     
     The PQ scheduling priority on the board is changed.
  5. Run [**qos pq-scheduler priority**](cmdqueryname=qos+pq-scheduler+priority) { **high** | **low** } **outbound** [ **card** *card\_id* ]
     
     
     
     The PQ scheduling priority on a subcard is changed.
  6. Run [**qos global-buffer**](cmdqueryname=qos+global-buffer) { **share-threshold** *share-value* | { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **share** } { **inbound** | **outbound** }
     
     
     
     A shared threshold is configured for buffer resources.
     
     
     
     To prevent buffer resources from being exhausted by some queues, control flow WRED scheduling. If the flow WRED value is set to a small value, packet loss occurs in traffic bursts. To resolve this problem, run the [**qos global-buffer**](cmdqueryname=qos+global-buffer) command to set a shared threshold for buffer resources. Before the shared buffer resources are exhausted, flow WRED configurations do not take effect, preventing packet loss.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  8. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
* Configure an FQ mapping.
  1. Run [**flow-mapping**](cmdqueryname=flow-mapping) *mapping-name*
     
     
     
     The flow mapping view is displayed.
     
     
     
     You can configure eight FQ-to-PQ mappings in an FQ mapping profile. You can also create multiple FQ mapping profiles for user queues to reference. A maximum of 15 FQ mapping profiles can be configured in the system.
  2. Run [**map flow-queue**](cmdqueryname=map+flow-queue) *cos-value* **to** **port-queue** *cos-value*
     
     
     
     The CoS of the FQ is mapped to the CoS of the PQ.
     
     
     
     If no FQ-to-PQ mapping is set, the system defaults the one-to-one mapping.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.