(Optional) Configuring a Flow Queue
===================================

You can configure scheduling parameters, traffic shaping, queue buffer resources, and more for a flow queue based on network requirements.

#### Context

A flow queue (FQ) is used to buffer data flows of one priority for a user. Different users cannot share FQs. A traffic shaping value can be configured for each FQ to restrict the maximum bandwidth.

An FQ has the following attributes:

* Queue priority and weight
* Queue shaping rate (PIR)
* Drop policy: tail drop or WRED

You can configure scheduling parameters, traffic shaping, queue buffer resources, and more for a flow queue based on network requirements.


#### Procedure

* Configure a flow WRED object.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**flow-wred**](cmdqueryname=flow-wred) *wred-name*
     
     
     
     A flow WRED object is created and its view is displayed.
  3. Run [**color**](cmdqueryname=color) { **green** | **yellow** | **red** } **low-limit** *low-limit-percentage* **high-limit** *high-limit-percentage* **discard-percentage** *discard-percentage*
     
     
     
     Upper and lower drop thresholds as well as a drop probability are configured for packets of different colors.
  4. Run [**queue-depth**](cmdqueryname=queue-depth) *queue-depth-value*
     
     
     
     A queue depth is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
* Create an FQ and set scheduling parameters.
  1. Run [**flow-queue**](cmdqueryname=flow-queue) *flow-queue-name* [ ****4cos-mode**** ] An FQ is created and its view is displayed.
     
     
     
     Home users support FQs in common 8-CoS mode and 4-CoS mode.
     
     If an FQ in 4-CoS mode is created, the system provides the default mappings between the priorities of the FQs in 8-CoS mode and those of the FQs in 4-CoS mode. The following table lists the default mappings. You can also customize the mappings between the priorities of the two types of queues.
     
     | FQ | Mapping | Scheduling Mode | Weight | Traffic Shaping Percentage | Drop Mode |
     | --- | --- | --- | --- | --- | --- |
     | cos0 | BE and AF1 | WFQ | 10 | - | Tail drop |
     | cos1 | AF2, AF3, and AF4 | WFQ | 15 | - | Tail drop |
     | cos2 | EF | PQ | - | - | Tail drop |
     | cos3 | CS6 and CS7 | PQ | - | - | Tail drop |
     
     To customize the mappings between the priorities of the two types of queues, perform the following operations:
     
     1. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     2. Run [**queue-4cos-mapping**](cmdqueryname=queue-4cos-mapping) *mapping-name*
        
        A 4-CoS mapping profile is created and its view is displayed.
     3. Run [**queue**](cmdqueryname=queue) *serviceclass* **mapping** { **cos0** | **cos1** | **cos2** | **cos3** }
        
        The mappings between 8-CoS and 4-CoS priorities are configured.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
  2. Run [**queue**](cmdqueryname=queue) *cos-value* { { **pq** | **wfq** **weight** *weight-value* | **lpq** } | { **shaping** { *shaping-value* | **shaping-percentage** *shaping-percentage-value* } [ **pbs** *pbs-value* ] | **car** { *car-value* | **car-percentage** *car-percentage-value* } [ **pbs** *pbs-value* ] } | **flow-wred** *wred-name* | **low-latency** | **low-jitter** } \* or [**queue**](cmdqueryname=queue) *cos-value* **cir** { { *cir-value* [ **cbs** *cbs-value* ] **cir-schedule** **pq** **pir** *pir-value* } | { **cir-percentage** *cir-percentage-value* [ **cbs** *cbs-value* ] **cir-schedule** **pq** **pir** **pir-percentage** *pir-percentage-value* } } [ **pbs** *pbs-value* ] **pir-schedule** { **pq** | **wfq** **weight** *weight-value* | **lpq** } [ **flow-wred** *wred-name* ]
     
     
     
     Scheduling parameters are set for the FQ.
* Configure share shaping.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  FQs in 4-CoS mode do not support share shaping.
  
  
  
  1. Run [**share-shaping**](cmdqueryname=share-shaping) [ *shap-id* ] { **af1** | **af2** | **af3** | **af4** | **be** | **cs6** | **cs7** | **ef** } \* [ **pq** | **wfq** **weight** *weight-value* | **lpq** ] *shaping-value* [ **pbs** *pbs-value* ]
     
     
     
     Share shaping is configured for multiple FQs.
     
     
     
     After share shaping is configured for queues, traffic shaping is first performed on the queues, which are then scheduled together with other user queues.
  2. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
* Enable the low-latency function for FQs in PQ scheduling mode.
  1. Run [**qos flow-queue low-latency enable**](cmdqueryname=qos+flow-queue+low-latency+enable)
     
     
     
     The low-latency function is enabled for FQs in PQ scheduling mode.
* Configure a PQ scheduling priority mapping, global buffer, and burst size.
  1. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  2. Run [**qos pq-scheduler priority**](cmdqueryname=qos+pq-scheduler+priority) { **high** | **low** } **outbound** [ **card** *card\_id* ]
     
     
     
     The PQ scheduling priority mapping of a subcard is modified to change the original default priority mapping.
  3. Run [**qos cos**](cmdqueryname=qos+cos) { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **burst-size** *buffer-size-value*
     
     
     
     A burst size is configured for a queue.
  4. Run **[**qos cos all pack-size**](cmdqueryname=qos+cos+all+pack-size)** **pack-size-value**
     
     
     
     The maximum packet size is configured for the eTM subcard.
  5. Run [**qos global-buffer**](cmdqueryname=qos+global-buffer) { **share-threshold** *share-value* | { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **share** } { **inbound** | **outbound** }
     
     
     
     Queue buffer resources on the board are controlled.
     
     
     
     To prevent some queues from occupying a large amount of queue buffer resources, you need to limit the maximum queue buffer resources that can be used by a queue. If flow-wred is used for limiting and the configured flow-wred value is too small, packet loss may occur due to a traffic burst. To prevent this issue, you can run the [**qos global-buffer**](cmdqueryname=qos+global-buffer) command to set the global queue buffer. This ensures that the flow-wred configuration does not take effect before the shared queue buffer resources are exhausted.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
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