Configuring WRED
================

Configuring WRED

#### Context

WRED randomly discards packets based on WRED parameter settings, preventing global TCP synchronization and ensuring packets with higher priorities are less likely to be discarded. According to a packet's color (drop priority), a WRED drop profile defines absolute values of upper and lower drop thresholds, upper and lower drop thresholds in percentage and the maximum drop probability.

Colors are used to determine whether packets are discarded during congestion avoidance implementation and are independent of the mapping between internal priorities and queues.


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
3. Set WRED parameters.
   
   
   ```
   [color](cmdqueryname=color) { green | red | yellow } { buffer-size low-limit low-buffer-size high-limit high-buffer-size | buffer-size cell low-limit low-buffer-size-cell high-limit high-buffer-size-cell | low-limit low-limit-percentage high-limit high-limit-percentage } discard-percentage discard-percentage
   ```
   
   By default, the upper drop threshold in percentage, lower drop threshold in percentage, and maximum drop probability in a WRED drop profile are all 100, and absolute values of upper and lower drop thresholds are not configured.
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
7. Apply the WRED drop profile to a port queue.
   
   
   ```
   [qos queue](cmdqueryname=qos+queue) queue-index wred drop-profile-name
   ```
8. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```