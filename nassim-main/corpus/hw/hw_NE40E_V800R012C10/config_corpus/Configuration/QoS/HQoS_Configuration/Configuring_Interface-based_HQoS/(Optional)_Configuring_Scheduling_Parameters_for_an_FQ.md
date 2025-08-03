(Optional) Configuring Scheduling Parameters for an FQ
======================================================

(Optional) Configuring Scheduling Parameters for an FQ

#### Context

You can use a non-default FQ profile to configure scheduling parameters for FQs based on network requirements. Multiple flow WRED objects can be created for FQs to reference. You can set upper and lower drop thresholds and a drop probability for a created flow WRED profile. When the percentage of the actual length of a queue over the length of an FQ is less than the lower drop threshold, the system does not drop packets; when the percentage of the actual length of a queue over the length of an FQ is between the upper and lower drop thresholds, the system drops packets through the WRED mechanism (the longer the queue length, the higher the drop probability); when the percentage of the actual length of a queue over the length of an FQ is greater than the upper drop threshold, the system drops all subsequent packets.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The upper and lower drop thresholds for red packets can be set to the minimum; those for yellow packets can be greater; those for green packets can be set to the maximum.
* In the actual configuration, the lower drop threshold is recommended to begin with 50% and be adjusted based on different colors of packets. 100% is recommended for the drop probability.
* If no flow WRED object is set, the system adopts the default tail drop policy.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Configure a flow WRED object.
   1. Run [**flow-wred**](cmdqueryname=flow-wred) *wred-name*
      
      
      
      A flow WRED object is created and its view is displayed.
   2. Run [**color**](cmdqueryname=color) { **green** | **yellow** | **red** } **low-limit** *low-limit-percentage* **high-limit** *high-limit-percentage* **discard-percentage** *discard-percentage*
      
      
      
      Upper and lower drop thresholds as well as a drop probability are configured for packets of a color.
   3. Run [**queue-depth**](cmdqueryname=queue-depth) *queue-depth-value*
      
      
      
      A queue depth is set.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**quit**](cmdqueryname=quit) Return to the system view.
3. Configure scheduling parameters for an FQ.
   1. Run [**flow-queue**](cmdqueryname=flow-queue) *flow-queue-name*
      
      
      
      The FQ view is displayed.
   2. Run [**queue**](cmdqueryname=queue) *cos-value* **cir** { { *cir-value* [ **cbs** *cbs-value* ] **cir-schedule pq pir** *pir-value* } | { **cir-percentage** *cir-percentage-value* [ **cbs** *cbs-value* ] **cir-schedule pq pir pir-percentage** *pir-percentage-value* } } [ **pbs** *pbs-value* ] **pir-schedule** { **pq** | **wfq** **weight** *weight-value* | **lpq** } [ **flow-wred** *wred-name* ] \* or [**queue**](cmdqueryname=queue) *cos-value* { { **pq** | **wfq weight** *weight-value* | **lpq** } | { **shaping** { *shaping-value* | **shaping-percentage** *shaping-percentage-value* } [ **pbs** *pbs-value* ] | **car** { *car-value* | **car-percentage** *car-percentage-value* } [ **pbs** *pbs-value* ] } | { **flow-wred** *wred-name* } | **low-latency** | **low-jitter** } \*
      
      
      
      The scheduling parameters and policies of the FQ are modified.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
4. (Optional) Configure a mapping from an FQ to a PQ.
   1. Run **[**flow-mapping**](cmdqueryname=flow-mapping)** **mapping-name**
      
      
      
      A flow mapping object is created and its view is displayed.
   2. Run **[**map flow-queue**](cmdqueryname=map+flow-queue)** **cos-value** ****to**** ****port-queue**** **cos-value**
      
      
      
      A mapping from an FQ to a PQ is configured.
      
      
      
      By configuring a mapping from an FQ to a PQ, you can flexibly guide the service traffic of the FQ with a specified CoS into the PQ with a specified CoS for scheduling.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.