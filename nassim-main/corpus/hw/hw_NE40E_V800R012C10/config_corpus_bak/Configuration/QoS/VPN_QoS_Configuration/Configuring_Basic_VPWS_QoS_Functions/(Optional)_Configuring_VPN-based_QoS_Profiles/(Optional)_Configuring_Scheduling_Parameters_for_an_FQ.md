(Optional) Configuring Scheduling Parameters for an FQ
======================================================

You can use a non-default FQ profile to configure WFQ scheduling weights, traffic shaping, shaping rates, and drop modes for FQs based on network requirements.

#### Context

Perform the following configurations on the Router.

You can configure scheduling parameters for eight FQs of a user in an FQ profile.

If you do not configure an FQ, the system uses the default FQ profile.

* By default, the system performs PQ scheduling on the FQs with the priorities of EF, CS6, and CS7.
* By default, the system performs WFQ scheduling on the FQs with the priorities of BE, AF1, AF2, AF3, and AF4. The scheduling weight proportion is 10:10:10:15:15.
* By default, the system does not perform traffic shaping.
* The tail drop policy is used by default.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**flow-queue**](cmdqueryname=flow-queue) *flow-queue-name* [ **priority-mode** ]
   
   
   
   The FQ view is displayed.
   
   
   
   If **priority-mode** is specified in the command, the priority-based FQ view is displayed.
3. (Optional) Run [**priority**](cmdqueryname=priority) *priority-value* { **pq** | **wfq** }
   
   
   
   The scheduling mode of priority-based FQs on the same scheduler is set to PQ or WFQ.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command must be run in the priority-based FQ view, which is displayed using the [**flow-queue**](cmdqueryname=flow-queue) *flow-queue-name* **priority-mode** command.
4. (Optional) Run [**share-shaping**](cmdqueryname=share-shaping) [ *shap-id* ] { **af1** | **af2** | **af3** | **af4** | **be** | **cs6** | **cs7** | **ef** } \* [ **pq** | **wfq** **weight** *weight-value* | **lpq** ] *shaping-value* [ **pbs** *pbs-value* ]
   
   
   
   Share shaping is configured for multiple FQs.
   
   
   
   After FQs configured with share shaping are shaped, the FQs are scheduled together with other user queues. In the priority-based FQ view, if no scheduling mode is specified for share shaping, share shaping uses the same scheduling mode as sub-schedulers.
5. Run **queue** *cos-value* { { **pq** | **wfq****weight** *weight-value* | **lpq** } | { **shaping** { *shaping-value* | **shaping-percentage** *shaping-percentage-value* } [ **pbs** *pbs-value* ] | **car** { *car-value* | **car-percentage** *car-percentage-value* } [ **pbs** *pbs-value*] } | **flow-wred** *wred-name* | **low-latency** | **low-jitter** } \* or **[**queue**](cmdqueryname=queue)** *cos-value* ****cir**** { { *cir-value* [ ****cbs**** *cbs-value* ] **[**cir-schedule**](cmdqueryname=cir-schedule)** **pq** ****pir**** *pir-value* } | { ****cir-percentage**** *cir-percentage-value* [ ****cbs**** *cbs-value* ] ****cir-schedule**** **pq** **pir** ****pir-percentage**** *pir-percentage-value* } } [ ****pbs**** *pbs-value* ] ****pir-schedule**** { ****pq**** | ****wfq**** **weight** *weight-value* | ****lpq**** } [ ****flow-wred**** *wred-name* ]
   
   
   
   The scheduling parameters and policy of the FQ are modified.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. (Optional) Run [**qos flow-queue low-latency enable**](cmdqueryname=qos+flow-queue+low-latency+enable)
   
   
   
   The low-latency function is enabled for FQs in PQ scheduling mode.
8. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
9. (Optional) Run [**qos user-queue burst-size bytes**](cmdqueryname=qos+user-queue+burst-size+bytes) *min-bytes* **time** *burst-time*
   
   
   
   The minimum default burst size and burst time are configured for user queues.
10. (Optional) Run [**qos cos**](cmdqueryname=qos+cos) { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **burst-size** *burst-size-value*
    
    
    
    The burst size of the eTM module is set.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.