Configuring an FQ Profile in Priority-based 8-CoS Mode
======================================================

You can configure priorities, scheduling parameters, and traffic shaping parameters for FQs based on network requirements.

#### Context

In HQoS in priority-based 8-CoS mode, eight queues are assigned different priorities in a priority-based FQ profile. The priorities are 0, 1, 2, and 3 in descending order. You can configure traffic shaping parameters and scheduling weights for the queues based on the priorities.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

By default, the default priority values of queues are used.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**flow-wred**](cmdqueryname=flow-wred) *wred-name*
   
   
   
   A flow WRED object is created and its view is displayed.
3. (Optional) Run [**color**](cmdqueryname=color) { **green** | **yellow** | **red** } **low-limit** *low-limit-percentage* **high-limit** *high-limit-percentage* **discard-percentage** *discard-percentage*
   
   
   
   Upper and lower drop thresholds as well as a drop probability are configured.
4. (Optional) Run [**queue-depth**](cmdqueryname=queue-depth) *queue-depth-value*
   
   
   
   A queue depth is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run[**flow-queue**](cmdqueryname=flow-queue) *flow-queue-name* **priority-mode**
   
   
   
   The priority-based FQ view is displayed.
8. Run [**priority**](cmdqueryname=priority) *priority-value* { **pq** | **wfq** }
   
   
   
   The scheduling mode of priority-based FQs on the same scheduler is set to PQ or WFQ.
9. Run [**queue**](cmdqueryname=queue) *cos-value* { **priority** *priority-value* [ **weight** *weight-value* ] | { **shaping** { *shaping-value* | **shaping-percentage** *shaping-percentage-value* } } | **flow-wred** *wred-name* } \*
   
   
   
   The priority, weight, and shaping value of the FQ are changed, and a flow WRED profile is bound.
10. Run [**share-shaping**](cmdqueryname=share-shaping) [ *shap-id* ] { **af1** | **af2** | **af3** | **af4** | **be** | **cs6** | **cs7** | **ef** } \* [ **pq** | **wfq** **weight** *weight-value* | **lpq** ] *shaping-value* [ **pbs** *pbs-value* ]
    
    
    
    Share shaping is configured for multiple FQs.
    
    
    
    After share shaping is configured for queues, they are shaped before being scheduled together with other user queues. In the priority-based FQ view, if no scheduling mode is specified for share shaping, share shaping uses the same scheduling mode as sub-schedulers.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    *shap-id* is not supported on the NE40E-M2E.