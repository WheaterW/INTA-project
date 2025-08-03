Configuring AI ECN for Lossless Queues
======================================

Configuring AI ECN for Lossless Queues

#### Prerequisites

Before configuring AI ECN for lossless queues, you have completed the following task:

* Configure the PFC function. A queue enabled with the PFC function is a lossless queue. For details, see "Configuring PFC" in Configuration Guide > DCN and Network Management Configuration > DCB Configuration.

#### Context

After the AI ECN function is enabled for lossless queues, the device collects traffic characteristics on the live network and sends them to the AI ECN component. The AI ECN component intelligently sets the optimal ECN thresholds for lossless queues based on intelligent algorithms to ensure low delay and high throughput of lossless queues. In this way, the optimal performance of lossless services can be achieved in different traffic scenarios.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the AI service and enter the AI service view.
   
   
   ```
   [ai-service](cmdqueryname=ai-service)
   ```
   
   By default, the AI service is disabled.
3. Enter the AI ECN view.
   
   
   ```
   [ai-ecn](cmdqueryname=ai-ecn)
   ```
4. Specify a lossless queue for which the AI ECN function is enabled.
   
   
   ```
   [assign queue](cmdqueryname=assign+queue) queue-id [ model { ai_ecn_centralizedstorage | ai_ecn_hpc | ai_ecn_distributedfilestorage } ]
   ```
   
   By default, no lossless queue is specified for enabling the AI ECN function.
   
   * If you run the [**assign queue**](cmdqueryname=assign+queue) *queue-id* command without specifying a model, the distributed storage model **ai\_ecn\_distributedstorage** is loaded by default.
   * If you run the [**assign queue**](cmdqueryname=assign+queue) *queue-id* **model** **ai\_ecn\_centralizedstorage** command, the centralized storage model **ai\_ecn\_centralizedstorage** is loaded.
   * If you run the [**assign queue**](cmdqueryname=assign+queue) *queue-id* **model** **ai\_ecn\_hpc** command, the high-performance computing model **ai\_ecn\_hpc** is loaded.
   * If you run the [**assign queue**](cmdqueryname=assign+queue) *queue-id* **model** **ai\_ecn\_distributedfilestorage** command, the distributed file storage model **ai\_ecn\_distributedfilestorage** is loaded.![](public_sys-resources/note_3.0-en-us.png) 
   
   For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM:
   
   * The AI ECN function can be enabled for a maximum of two queues.
   * When the AI ECN function is enabled for two queues on an interface, the performance can be improved only when the distributed storage model and high-performance computing model are loaded for the two queues respectively.
   * If the AI ECN function has been enabled for two queues and the device is downgraded to a version that supports AI ECN enabled for only one queue, some of the configuration is lost and only one queue with AI ECN enabled is retained.
   * If the AI ECN function has been enabled for one queue and the device is downgraded to a version that supports AI ECN enabled for only one queue, the configuration is retained. That is, the queue for which AI ECN has been enabled still takes effect.
   
   For the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855:
   
   * AI ECN and static ECN can be enabled for a combined total of four queues. To enable static ECN for a specified queue, run the **qos queue ecn** command.
   * When the AI ECN function is enabled for two or more queues on an interface, the performance can be improved only when both the distributed storage model and high-performance computing model are loaded.
5. Enable the AI ECN function for the lossless queue.
   
   
   ```
   [ai-ecn enable](cmdqueryname=ai-ecn+enable)
   ```
   By default, the AI ECN function is disabled for lossless queues.![](public_sys-resources/note_3.0-en-us.png) 
   * The AI ECN function identifies lossless queues based on the PFC priority configured on an interface. This function is not affected after the [**dcb pfc global disable**](cmdqueryname=dcb+pfc+global+disable) command is run in the system view to disable PFC globally.
   * AI ECN takes effect only on interfaces in up state.
6. Exit the AI ECN view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the **[**display ai-ecn calculated state**](cmdqueryname=display+ai-ecn+calculated+state)** [ **interface** { *interface-name* | *interface-type interface-number* } ] command to check whether the AI ECN function is enabled for lossless queues and the calculated ECN threshold.