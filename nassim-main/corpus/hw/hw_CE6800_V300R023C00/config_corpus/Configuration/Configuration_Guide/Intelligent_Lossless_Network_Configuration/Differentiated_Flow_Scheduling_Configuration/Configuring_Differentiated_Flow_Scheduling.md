Configuring Differentiated Flow Scheduling
==========================================

Configuring Differentiated Flow Scheduling

#### Context

In practice, differentiated flow scheduling must be enabled on both the inbound and outbound interfaces of a device based on the traffic forwarding path.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the system resource mode to **balance**. (This command is required only for the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.)
   
   
   ```
   [system resource](cmdqueryname=system+resource) balance
   ```
3. Enable the AI service and enter the AI service view.
   
   
   ```
   [ai-service](cmdqueryname=ai-service)
   ```
   
   By default, the AI service is disabled.
4. Enter the mice-elephant-flow view.
   
   
   ```
   [mice-elephant-flow](cmdqueryname=mice-elephant-flow)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:
   
   * You can run the [**mice-elephant-flow**](cmdqueryname=mice-elephant-flow) command to enter the mice-elephant-flow view only after you run the **[**system resource**](cmdqueryname=system+resource) balance** command to set the system resource mode to **balance** and restart the device to make the configuration take effect. You cannot enter the mice-elephant-flow view if you have configured any other system resource mode, even if the configured mode does not take effect.
   * If the system resource mode has been set to **balance** and differentiated flow scheduling has been configured, you need to delete the differentiated flow scheduling configuration in the AI service view before changing the system resource mode.
5. Specify the queue for which differentiated flow scheduling is to be enabled. The original queue for which differentiated flow scheduling is enabled is called an elephant-flow queue, and the high-priority queue to which a mice flow is scheduled is called a mice-flow queue.
   
   
   * For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM: Specify the elephant-flow queue for which differentiated flow scheduling is to be enabled.
     ```
     [assign queue](cmdqueryname=assign+queue){ start-queue-index [ to end-queue-index ] } &<1-6>
     ```
   * For the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855: Specify the elephant-flow queue for which differentiated flow scheduling is to be enabled.
     ```
     [assign queue](cmdqueryname=assign+queue){ start-queue-index [ to end-queue-index ] } &<1-2>
     ```
   * For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S: Specify the elephant-flow queue for which differentiated flow scheduling is to be enabled and the mice-flow queue to which a mice flow is to be scheduled.
     ```
     [assign queue](cmdqueryname=assign+queue){ start-queue-index [ to end-queue-index ] } &<1-7> adjust mice-flow to queue queue-id
     ```
   
   By default, differentiated flow scheduling is disabled for all queues.
6. Configure the number of packets in a mice flow. The first *N* (specified by *number*) packets in a flow are identified as a mice flow. (This command is available only on the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.)
   
   
   ```
   [mice-flow packet-number](cmdqueryname=mice-flow+packet-number) number
   ```
   By default, the first 128 packets in a flow are identified as a mice flow in differentiated flow scheduling.![](public_sys-resources/note_3.0-en-us.png) 
   
   If you configure the first *N* packets in a flow to be identified as a mice flow during traffic transmission, packets may become out of order. Therefore, you are advised to stop traffic transmission before configuring it.
7. (Optional) Configure the scheduling mode. (This command is available only on the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.)
   
   
   ```
   [scheduling-mode](cmdqueryname=scheduling-mode) hybrid
   ```
   
   The hybrid mode is used for performance optimization in hybrid scheduling scenarios. For example, it can effectively optimize performance in the scenario where TCP and UDP are used together in NVMe over TCP.
8. Exit the mice-elephant-flow view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
9. Exit the AI service view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
10. Enter the interface view.
    
    
    ```
    [interface](cmdqueryname=interface) interface-type interface-number
    ```
11. Enable differentiated flow scheduling on the interface.
    
    
    ```
    [mice-elephant-flow enable](cmdqueryname=mice-elephant-flow+enable)
    ```
    
    By default, differentiated flow scheduling is disabled on an interface.
    
    ![](public_sys-resources/note_3.0-en-us.png) 
    
    For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:
    
    * If the **assign queue adjust** command has been run to specify the queue for which differentiated flow scheduling is to be enabled and the **flex-buffer enable** command has been run to enable the TCP FlexBuffer function, differentiated flow scheduling can be enabled on an interface only when the dynamic threshold of the queue-level service buffer for elephant-flow queues on the interface is set to 9 using the **qos buffer queue** *queue-index* **shared-threshold dynamic** *dynamic-value* command. You can run the **display mice-elephant-flow configuration** command to view information about interfaces and queues for which differentiated flow scheduling is enabled.
    * If the **assign queue adjust** command has been run to specify the queue for which differentiated flow scheduling is to be enabled and the **flex-buffer enable** command has been run to enable the TCP FlexBuffer function, differentiated flow scheduling can be enabled on an interface only when no WRED profile is configured for elephant-flow queues on the interface.
12. Exit the interface view.
    
    
    ```
    [quit](cmdqueryname=quit)
    ```
13. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```