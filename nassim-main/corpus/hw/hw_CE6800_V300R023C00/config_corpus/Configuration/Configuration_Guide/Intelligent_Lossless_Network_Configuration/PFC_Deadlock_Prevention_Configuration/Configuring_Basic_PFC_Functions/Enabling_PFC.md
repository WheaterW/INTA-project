Enabling PFC
============

Enabling PFC

#### Context

When a link is congested by traffic of a certain type, you can configure PFC to control traffic of that type without interrupting traffic of other types.

![](public_sys-resources/note_3.0-en-us.png) 

* To set the PFC working mode to **auto**, [configure DCBX](galaxy_dcb_cfg_0018.html).
* If you configure both priority mapping and PFC, exercise caution when modifying the mappings between the priorities of PFC-enabled queues and priorities in the DiffServ domain. Otherwise, PFC may not work.
* By default, PFC deadlock detection is always enabled on the device. If the device continuously receives PFC frames throughout the deadlock detection interval, the device does not respond to the PFC frames and keeps forwarding received packets, ensuring that a PFC deadlock does not occur.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable PFC globally.
   
   
   ```
   [undo dcb pfc global disable](cmdqueryname=undo+dcb+pfc+global+disable)
   ```
   
   By default, PFC is enabled globally.
   
   You can enable PFC on a specified interface only after PFC has been enabled globally. If the [**dcb pfc global disable**](cmdqueryname=dcb+pfc+global+disable) command is run to disable PFC globally, PFC is also disabled on a PFC-enabled interface.
3. Configure the chip-level headroom buffer. (This step is mandatory for the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.)
   
   
   ```
   [qos buffer headroom-pool](cmdqueryname=qos+buffer+headroom-pool) size size { kbytes | mbytes } slot slot-id
   ```
   
   By default, the chip-level headroom buffer is not manually configured. The recommended chip-level headroom buffer is the sum of the headroom buffer thresholds configured for PFC queues in the inbound direction on PFC-enabled interfaces that are prone to congestion. Determine such interfaces based on the live network traffic model.
4. Create a PFC profile and enter the PFC profile view.
   
   
   ```
   [dcb pfc](cmdqueryname=dcb+pfc) [ profilename ]
   ```
   
   By default, the system provides the PFC profile **default**. This profile can be modified but not deleted. You can create a PFC profile or modify the default PFC profile according to service requirements.
5. Specify the priority queue for which PFC is enabled.
   
   
   * For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM:
     ```
     [priority](cmdqueryname=priority) { priority } &<1-3>
     ```
   * For the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855:
     ```
     [priority](cmdqueryname=priority) { priority } &<1-4>
     ```
   
   By default, PFC is enabled for priority 3.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If you run this command multiple times, all configurations take effect.
   
   For the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855: PFC can be enabled for a maximum of three queues in addition to priority queue 3.
   
   For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM:
   
   * PFC can be enabled for a maximum of three queues.
   * If PFC has been enabled for three queues and the system software is downgraded to a version where PFC can be enabled for only two queues, the configuration is lost. That is, PFC is not enabled for any queue.
   * If PFC has been enabled for no more than two queues and the system software is downgraded to a version where PFC can be enabled for only two queues, the configuration is retained. That is, PFC that has been enabled for queues still takes effect.
6. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Enter the view of the interface for which PFC is to be enabled.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
8. (Optional) Set the thresholds for triggering and stopping PFC frames in the inbound direction of a PFC queue.
   
   
   * For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM:
     ```
     [dcb pfc buffer](cmdqueryname=dcb+pfc+buffer) queue-index xon static xon-value { kbytes | mbytes } xoff static xoff-value { kbytes | mbytes }
     ```
     ```
     [dcb pfc buffer](cmdqueryname=dcb+pfc+buffer) queue-index xon dynamic alpha-value xoff dynamic alpha-value
     ```
   * For the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855:
     ```
     [dcb pfc buffer](cmdqueryname=dcb+pfc+buffer) queue-index xoff { static xoff-value [ kbytes | mbytes ] | dynamic alpha-value } [ xon offset offset-value [ kbytes | mbytes ] ]
     ```
   
   By default, the thresholds for triggering and stopping PFC frames for a PFC queue in the inbound direction are not configured.
9. (Optional) Configure the guaranteed and headroom buffer thresholds for a PFC queue in the inbound direction. (Supported only by the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.)
   
   
   ```
   [dcb pfc buffer](cmdqueryname=dcb+pfc+buffer) queue-index guaranteed guaranteed-value [ bytes | kbytes ]
   ```
   ```
   [dcb pfc buffer](cmdqueryname=dcb+pfc+buffer) queue-index hdrm hdrm-value [ kbytes ]
   ```
   
   By default, the guaranteed and headroom buffer thresholds are not configured for a PFC queue in the inbound direction.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * If you run the **undo dcb pfc buffer** command without specifying the *queue-index* parameter, the manually configured thresholds for triggering and stopping PFC frames, guaranteed buffer threshold, and headroom buffer threshold for all PFC queues in the inbound direction are deleted.
   * If you run the **undo dcb pfc buffer** *queue-index* command with only the **queue index** parameter specified, the manually configured thresholds for triggering and stopping PFC frames, guaranteed buffer threshold, and headroom buffer threshold for the specified PFC queue in the inbound direction are deleted.
10. Apply a PFC profile to the interface and specify the PFC working mode.
    
    
    * For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855:
      ```
      [dcb pfc enable](cmdqueryname=dcb+pfc+enable) [ pfcprofile ] [ mode { auto | manual } ]
      ```
    * For the CE6885-LL (low latency mode):
      ```
      [dcb pfc enable](cmdqueryname=dcb+pfc+enable) [ pfcprofile ] [ mode manual ]
      ```
    
    By default, no PFC profile is applied to an interface.
11. Configure the priority to be mapped for packets.
    
    
    ```
    [trust](cmdqueryname=trust) { 8021p { inner | outer } | dscp }
    ```
    
    By default, packets are processed based on the mapping of the outer 802.1p priority.
12. Return to the system view.
    
    
    ```
    [quit](cmdqueryname=quit)
    ```
13. (Optional) Enable a PFC-enabled device to implement backpressure based on the internal priority. (Supported only by the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.)
    
    
    ```
    [dcb pfc dscp-mapping enable](cmdqueryname=dcb+pfc+dscp-mapping+enable) slot slot-id
    ```
    
    By default, a PFC-enabled device implements backpressure based on the 802.1p priority of packets.
14. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```