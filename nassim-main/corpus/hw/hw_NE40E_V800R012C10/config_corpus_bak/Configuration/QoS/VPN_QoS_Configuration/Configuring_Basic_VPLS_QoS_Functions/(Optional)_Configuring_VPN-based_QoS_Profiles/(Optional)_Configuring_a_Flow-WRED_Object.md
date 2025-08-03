(Optional) Configuring a Flow-WRED Object
=========================================

You can set upper and lower thresholds (in percentages) and drop probability for a flow-WRED object on a device. If the flow queue (FQ) length exceeds the upper threshold, the device randomly discards packets using the WRED mechanism.

#### Context

Perform the following configurations on the Router.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* If no flow-WRED object is set, the system adopts the default tail drop policy.
* The upper and lower drop thresholds for red packets can be set to the minimum; those for yellow packets can be greater; those for green packets can be set to the maximum.
* In the actual configuration, the lower threshold is recommended to begin with 50% and be adjusted based on the drop precedence. 100% is recommended for the drop probability.

By configuring a flow-WRED object, you can set upper and lower thresholds (in percentages) and drop probability for queues. By configuring a flow-WRED object, you can set upper and lower thresholds (in percentages) and drop probability for queues. Suppose that the percentage of the actual length of a queue to the length of an FQ is n, the lower threshold is x (in percentage), and the upper threshold is y (in percentage), packets are processed based on the following rules: If n is less than x, packets are not dropped. If n is greater than x and less than y, packets are dropped according to the WRED mechanism. The longer the queue length, the higher the drop probability. If n is greater than y, all the subsequent packets are dropped.

You can create multiple flow-WRED objects for FQs to reference as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**flow-wred**](cmdqueryname=flow-wred) *wred-name*
   
   
   
   A flow-WRED object is created, and its view is displayed.
3. Run [**color**](cmdqueryname=color) { **green** | **yellow** | **red** } **low-limit** *low-limit-percentage* **high-limit** *high-limit-percentage* **discard-percentage** *discard-percentage*
   
   
   
   Upper and lower thresholds (in percentages) and drop probability are set for packets of different colors.
4. (Optional) Run [**queue-depth**](cmdqueryname=queue-depth) *queue-depth-value*
   
   
   
   A queue depth is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.