Configuring ECN
===============

Configuring ECN

#### Context

With fast ECN enabled, the device tags an outgoing packet with the ECN field when the packet leaves the queue. The destination server then can receive the tagged packet with the least delay possible.

For best effect, WRED and ECN can be combined, as follows:

1. When detecting congestion on an outbound interface, the device adds an ECN field to packets to notify the destination server of the congestion.
2. After receiving a packet carrying the ECN field, the destination server sends a CNP to instruct the source server to reduce the traffic rate.
3. After receiving the CNP, the source server reduces the traffic rate, alleviating or avoiding congestion.

You can configure ECN to reduce the rate of traffic sent from the upstream device and therefore mitigate network congestion.

![](public_sys-resources/note_3.0-en-us.png) 

After ECN is enabled for a queue, if congestion occurs in that queue, the device does not randomly discard packets. Instead, it randomly marks packets based on the configured WRED drop profile. When the queue length reaches the upper threshold in the WRED drop profile, the device starts to mark all packets.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a WRED drop profile and enter the WRED drop profile view.
   
   
   ```
   [drop-profile](cmdqueryname=drop-profile) drop-profile-name
   ```
   
   By default, a WRED drop profile named **default** exists on the device.
   
   A maximum of 16 WRED drop profiles, including the default drop profile, can be configured on the device for the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM. The default drop profile cannot be deleted, and only parameters in the profile can be modified.
   
   A maximum of 63 WRED drop profiles, including the default drop profile, can be configured on the device for the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ. The default drop profile cannot be deleted, and only parameters in the profile can be modified.
3. Set ECN parameters, including the absolute values of upper and lower drop thresholds, upper and lower drop thresholds in percentage, and maximum drop probability.
   
   
   ```
   [ecn](cmdqueryname=ecn) { buffer-size low-limit low-buffer-size high-limit high-buffer-size | buffer-size cell low-limit low-buffer-cell-size high-limit high-buffer-cell-size | low-limit low-limit-percentage high-limit high-limit-percentage } discard-percentage discard-percentage-value
   ```
   
   By default, the upper and lower drop thresholds in percentage, absolute values of upper and lower drop thresholds, and maximum drop probability are not set.
4. Exit the WRED drop profile view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
6. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-type interface-number | interface-name }
   ```
7. Apply the WRED drop profile to queues on an interface.
   
   
   ```
   [qos queue](cmdqueryname=qos+queue) queue-index wred drop-profile-name
   ```
8. Enable ECN for a specified queue.
   
   
   ```
   [qos queue](cmdqueryname=qos+queue) queue-index ecn
   ```
9. Enable ECN globally for the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM.
   
   
   ```
   [quit](cmdqueryname=quit)
   [qos ecn enable](cmdqueryname=qos+ecn+enable)
   ```
   
   If ECN needs to be enabled for multiple queues, you can enable this function in the system view.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```