Configuring PFC Deadlock Detection
==================================

Configuring PFC Deadlock Detection

#### Context

If a large number of PFC backpressure signals are present on the network, a network deadlock may occur, leading to system risks. After the PFC deadlock detection function is enabled, if the device continuously receives PFC frames throughout the deadlock detection period, the device does not respond to the frames, ensuring that a PFC deadlock does not occur.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the PFC profile view.
   
   
   ```
   [dcb pfc](cmdqueryname=dcb+pfc) [ profilename ]
   ```
3. Enable a device to automatically disable PFC on an interface after the specified number of deadlocks occur within a 20-second period.
   
   
   ```
   [priority](cmdqueryname=priority) priority turn-off threshold threshold-value
   ```
   
   By default, PFC is automatically disabled on an interface if 30 deadlocks occur within a 20-second period.
4. Enable a device to set the interface status to error-down after a specified number of deadlocks occur within a 20-second period.
   
   
   ```
   [priority](cmdqueryname=priority) priority error-down threshold threshold-value
   ```
   
   By default, an interface is set to the error-down state if deadlock occurs more than 30 times within a 20-second period.
5. (Optional) For the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855: Set the detection period for hardware-based deadlock detection.
   
   
   ```
   [priority](cmdqueryname=priority) priority deadlock-detect time time
   ```
   
   By default, the detection period for hardware-based deadlock detection is 100 ms.
6. (Optional) For the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855: Set the recovery period for hardware-based deadlock detection.
   
   
   ```
   [priority](cmdqueryname=priority) priority deadlock-recovery time time
   ```
   
   By default, the recovery period for hardware-based deadlock detection is 100 ms.
   
   If the recovery period (*time*) is set to 0, the device does not perform PFC deadlock recovery when a PFC deadlock occurs. Instead, the device performs a new round of deadlock detection.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   For the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855:
   
   The units of the detection period and recovery period for hardware-based deadlock detection are determined by the **dcb pfc deadlock-detect interval** *interval-value* command configuration. The detection period or recovery period that actually takes effect is the product of *interval-value* (the configured precision) and *time* (the configured detection period or recovery period).
7. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
8. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
9. Configure a device to set an interface to the error-down state or disable PFC on the interface when the number of PFC deadlocks on the interface exceeds the deadlock threshold within a 20-second period.
   
   
   ```
   [port pfc-deadlock trigger](cmdqueryname=port+pfc-deadlock+trigger) { error-down | turn-off }
   ```
   
   By default, if the number of PFC deadlocks on an interface exceeds the deadlock threshold within a 20-second period, PFC is automatically disabled.
10. Return to the system view.
    
    
    ```
    [quit](cmdqueryname=quit)
    ```
11. (Optional) For the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855: Set the precision of the detection period and recovery period for hardware-based PFC deadlock detection.
    
    
    ```
    [dcb pfc deadlock-detect interval](cmdqueryname=dcb+pfc+deadlock-detect+interval) interval-value
    ```
    
    By default, the precision of the detection period and recovery period for hardware-based PFC deadlock detection is 10 ms.
12. (Optional) For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM: Set the detection period for hardware-based deadlock detection.
    
    
    ```
    [dcb pfc deadlock-detect timer](cmdqueryname=dcb+pfc+deadlock-detect+timer) detect-time
    ```
    
    By default, the detection period for hardware-based deadlock detection is 100 ms.
13. (Optional) For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM: Set the recovery period for hardware-based deadlock detection.
    
    
    ```
    [dcb pfc deadlock-recovery timer](cmdqueryname=dcb+pfc+deadlock-recovery+timer) recovery-time
    ```
    
    By default, the recovery period for hardware-based deadlock detection is 100 ms.
14. (Optional) Configure the packet processing behavior of the device during the recovery period of hardware-based deadlock detection.
    
    
    ```
    [dcb pfc deadlock recovery-behavior](cmdqueryname=dcb+pfc+deadlock+recovery-behavior) { discard | forwarding } slot slot-id
    ```
    
    By default, during the recovery period of hardware-based deadlock detection, packets are discarded on the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, and are forwarded on the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.
    
    If any of the following exists on the PFC-enabled network, you need to set the forwarding behavior of all devices the network to discard during the recovery period of hardware-based deadlock detection: CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM
    
    ![](public_sys-resources/note_3.0-en-us.png) 
    
    The commands used to set the detection period and recovery period for hardware-based deadlock detection and the command used to configure the packet processing behavior of the device during the recovery period take effect for both PFC and antilocking PFC.
15. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```