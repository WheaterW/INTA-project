Configuring Antilocking PFC (CE6885-SAN)
========================================

Configuring Antilocking PFC (CE6885-SAN)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Configure the long-distance mode for the interface and enable the distance-based headroom buffer check function.
   
   
   ```
   [long-distance mode](cmdqueryname=long-distance+mode) { level-1 | level-10 | level-25 | level-50 | level-100 }
   ```
   
   By default, the distance-based headroom buffer check function is disabled. After this function is enabled, the interface automatically sends a detection packet to measure the required headroom buffer space for lossless transmission on the current link.
4. Trigger the interface to send a detection packet for distance-based headroom buffer check. You need to trigger the interface to send a detection packet only when distance-based headroom buffer check fails.
   
   
   ```
   [start long-distance detect](cmdqueryname=start+long-distance+detect)
   ```
5. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Create an antilocking PFC profile and enter its view.
   
   
   ```
   [abs-pfc profile](cmdqueryname=abs-pfc+profile) profile-name
   ```
   
   By default, no antilocking PFC profile is configured.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * A maximum of two antilocking PFC profiles can be configured globally.
   * If an antilocking PFC profile has been applied to an interface, you need to delete the application of the profile in the interface view before deleting the profile.
7. Specify the priority queue for which antilocking PFC is to be enabled.
   
   
   ```
   [priority](cmdqueryname=priority) priority &<1-4>
   ```
   
   By default, antilocking PFC is not enabled for any priority queue.
8. (Optional) Configure the buffer threshold for antilocking PFC to take effect based on priority queues.
   
   
   ```
   [priority](cmdqueryname=priority) priority threshold threshold-value
   ```
   
   By default, the buffer threshold for antilocking PFC to take effect is 0.
9. (Optional) Set the detection period for hardware-based deadlock detection.
   
   
   ```
   [priority](cmdqueryname=priority) priority deadlock-detect time time
   ```
   
   By default, the detection period for hardware-based deadlock detection is 100 ms.
10. (Optional) Set the recovery period for hardware-based deadlock detection.
    
    
    ```
    [priority](cmdqueryname=priority) priority deadlock-recovery time time
    ```
    
    By default, the recovery period for hardware-based deadlock detection is 100 ms.
    
    ![](public_sys-resources/note_3.0-en-us.png) 
    
    The units of the detection period and recovery period for hardware-based deadlock detection are determined by the **[**dcb pfc deadlock-detect interval**](cmdqueryname=dcb+pfc+deadlock-detect+interval)** **interval-value** command configuration. The detection period or recovery period that actually takes effect is the product of *interval-value* (the configured precision) and *time* (the configured detection period or recovery period).
11. Return to the system view.
    
    
    ```
    [quit](cmdqueryname=quit)
    ```
12. Enter the view of the interface for which antilocking PFC needs to be enabled.
    
    
    ```
    [interface](cmdqueryname=interface) interface-type interface-number
    ```
13. Apply the antilocking PFC profile to the interface to enable antilocking PFC.
    
    
    ```
    [abs-pfc enable](cmdqueryname=abs-pfc+enable) profile-name
    ```
    
    By default, no antilocking PFC profile is applied to an interface.
    
    ![](public_sys-resources/note_3.0-en-us.png) 
    * Antilocking PFC takes effect only after the **[**long-distance mode**](cmdqueryname=long-distance+mode)** command is run to enable the long-distance detection mode and a detection success message is returned.
    * The **[**abs-pfc enable**](cmdqueryname=abs-pfc+enable)** and **[**dcb pfc enable**](cmdqueryname=dcb+pfc+enable)** commands are mutually exclusive on the same interface.
    * In scenarios such as device upgrade and restart, long-distance detection may fail. As a result, antilocking PFC becomes invalid. In this case, you can run the **[**start long-distance detect**](cmdqueryname=start+long-distance+detect)** command to manually send detection packets.
    * An antilocking PFC profile can be bound only when it has priority queue configuration.
    * Antilocking PFC can be enabled for a maximum of 20 queues on the device.
14. Return to the system view.
    
    
    ```
    [quit](cmdqueryname=quit)
    ```
15. (Optional) Set the precision of the detection period and recovery period for hardware-based deadlock detection.
    
    
    ```
    [dcb pfc deadlock-detect interval](cmdqueryname=dcb+pfc+deadlock-detect+interval) interval-value
    ```
    
    By default, the precision of the detection period and recovery period for hardware-based deadlock detection is 10 ms.
16. (Optional) Configure the packet processing behavior of the device during the recovery period of hardware-based deadlock detection.
    
    
    ```
    [dcb pfc deadlock recovery-behavior](cmdqueryname=dcb+pfc+deadlock+recovery-behavior) { discard | forwarding } slot slot-id
    ```
    
    By default, a device forwards packets during the recovery period of hardware-based deadlock detection.
    
    ![](public_sys-resources/note_3.0-en-us.png) 
    
    The command used to set the precision of the detection period and recovery period for hardware-based deadlock detection and the command used to configure the packet processing behavior of the device during the recovery period take effect for both traditional PFC and antilocking PFC.
17. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```