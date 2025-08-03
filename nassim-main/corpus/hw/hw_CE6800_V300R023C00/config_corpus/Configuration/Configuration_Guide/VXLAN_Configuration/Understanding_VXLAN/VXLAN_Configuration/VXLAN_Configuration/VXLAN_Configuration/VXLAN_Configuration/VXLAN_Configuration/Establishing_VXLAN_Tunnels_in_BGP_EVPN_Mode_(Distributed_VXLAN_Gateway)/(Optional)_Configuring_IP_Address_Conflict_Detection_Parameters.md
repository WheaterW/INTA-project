(Optional) Configuring IP Address Conflict Detection Parameters
===============================================================

(Optional) Configuring IP Address Conflict Detection Parameters

#### Context

On a VXLAN, IP address conflict detection helps to eliminate IP address conflicts that prevent terminal users from going online.

![](../public_sys-resources/note_3.0-en-us.png) 

This configuration task is supported on IPv4 overlay networks only.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an interval at which terminal users' IP address conflicts are detected, as well as the IP address conflict threshold.
   
   
   ```
   [arp host ip-conflict-check](cmdqueryname=arp+host+ip-conflict-check) period period-value retry-times retry-times-value
   ```
   
   By default, terminal users' IP address conflicts are detected at an interval of 180s, and the IP address conflict threshold is 5. You can run the [**arp host ip-conflict-check**](cmdqueryname=arp+host+ip-conflict-check) **period** *period-value* **retry-times** *retry-times-value* command to change the detection interval and conflict threshold. If the number of detected IP address conflicts exceeds the threshold within the detection interval, the device generates an alarm.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```