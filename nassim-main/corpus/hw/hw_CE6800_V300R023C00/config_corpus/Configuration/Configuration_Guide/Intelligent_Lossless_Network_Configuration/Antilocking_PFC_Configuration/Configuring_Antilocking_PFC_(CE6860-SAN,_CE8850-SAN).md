Configuring Antilocking PFC (CE6860-SAN, CE8850-SAN)
====================================================

Configuring Antilocking PFC (CE6860-SAN, CE8850-SAN)

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
3. Set the plane buffer optimization mode to enhanced long-distance mode.
   
   
   ```
   [buffer optimization mode](cmdqueryname=buffer+optimization+mode) enhanced-long-distance
   ```
   
   By default, the plane buffer optimization function is disabled. The configured plane buffer optimization mode takes effect after the device restarts.
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
6. Configure the long-distance mode for the interface and enable the distance-based headroom buffer check function.
   
   
   ```
   [long-distance mode](cmdqueryname=long-distance+mode) { level-1 | level-10 | level-25 | level-50 | level-100 }
   ```
   
   By default, the distance-based headroom buffer check function is disabled. After this function is enabled, the interface automatically sends a detection packet to measure the required headroom buffer space for lossless transmission on the current link.
7. Trigger the interface to send a detection packet for distance-based headroom buffer check. You need to trigger the interface to send a detection packet only when distance-based headroom buffer check fails.
   
   
   ```
   [start long-distance detect](cmdqueryname=start+long-distance+detect)
   ```
8. Configure antilocking PFC for interface queues.
   
   
   ```
   [dcb abs-pfc queue](cmdqueryname=dcb+abs-pfc+queue) first-queue-index [ second-queue-index ] enable [ threshold threshold-value ]
   ```
   
   By default, antilocking PFC is disabled for interface queues. The following table lists the interfaces that support antilocking PFC.
   
   **Table 1** Interfaces that support antilocking PFC
   | Product | Interface Supporting Antilocking PFC |
   | --- | --- |
   | CE6860-SAN | * 25GE interfaces 1 to 48 * 50GE interfaces 1 to 48 * 100GE interfaces 1 to 8 * 200GE interfaces 2, 4, 6, and 8 * Interfaces split from 100GE interfaces 2, 4, 6, and 8 |
   | CE8850-SAN | 100GE interfaces 1 to 8 and interfaces split from them |
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * Antilocking PFC takes effect only when the following conditions are met:
     + The **[**buffer optimization mode**](cmdqueryname=buffer+optimization+mode)** **enhanced-long-distance** command has been run to set the plane buffer optimization mode to enhanced long-distance mode, and the setting has taken effect upon a device restart.
     + The **long-distance mode** command has been run to enable the long-distance detection mode, and a detection success message has been returned.
   * Antilocking PFC can take effect only on antilocking PFC-capable interfaces specified by the **Interface that can be enabled with ABS PFC** field of the [**display buffer optimization configuration**](cmdqueryname=display+buffer+optimization+configuration) command output.
   * The [**dcb abs-pfc queue enable**](cmdqueryname=dcb+abs-pfc+queue+enable) and [**dcb pfc enable**](cmdqueryname=dcb+pfc+enable) commands are mutually exclusive on the same interface.
   * In scenarios such as device upgrade and restart, long-distance detection may fail. As a result, antilocking PFC becomes invalid. In this case, you can run the [**start long-distance detect**](cmdqueryname=start+long-distance+detect) command to manually send detection packets.
   * In a priority queue of an interface, antilocking PFC is mutually exclusive with differentiated flow scheduling.
   * On an interface, antilocking PFC for priority queue 1 is mutually exclusive with differentiated flow scheduling for any queue.
   * Antilocking PFC can be enabled for a maximum of 20 queues on the device.
9. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
10. (Optional) Set the detection period for hardware-based deadlock detection.
    
    
    ```
    [dcb pfc deadlock-detect timer](cmdqueryname=dcb+pfc+deadlock-detect+timer) detect-time
    ```
    
    By default, the detection period for hardware-based deadlock detection is 100 ms.
11. (Optional) Set the recovery period for hardware-based deadlock detection.
    
    
    ```
    [dcb pfc deadlock-recovery timer](cmdqueryname=dcb+pfc+deadlock-recovery+timer) recovery-time
    ```
    
    By default, the recovery period for hardware-based deadlock detection is 100 ms.
12. (Optional) Configure the packet processing behavior of the device during the recovery period of hardware-based deadlock detection.
    
    
    ```
    [dcb pfc deadlock recovery-behavior](cmdqueryname=dcb+pfc+deadlock+recovery-behavior) { discard | forwarding } slot slot-id
    ```
    
    By default, a device discards packets during the recovery period of hardware-based deadlock detection.
    
    ![](public_sys-resources/note_3.0-en-us.png) 
    
    The commands used to set the detection period and recovery period for hardware-based deadlock detection and the command used to configure the packet processing behavior of the device during the recovery period take effect for both traditional PFC and antilocking PFC.
13. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```