Configuring an Alarm Threshold for the Number of Routes in an IPv6 VPN Instance
===============================================================================

Configuring an Alarm Threshold for the Number of Routes in an IPv6 VPN Instance

#### Context

As the number of access hosts increases, the number of routes stored on the control plane also increases, consuming a significant amount of memory resources. To better monitor the memory usage in this case and ensure the device does not restart due to insufficient memory, configure an alarm threshold for the number of routes in a VPN instance. When the number of routes exceeds this threshold, a user log is generated. Conversely, when the number of routes falls below the recovery percentage, a recovery log is reported.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set an alarm threshold and a recovery percentage for the number of routes in an IPv6 VPN instance.
   
   
   ```
   [alarm-threshold route](cmdqueryname=alarm-threshold+route) route-number [ recovery-percentage percentage ] ipv6 vpn-instance vpn-instance-name
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```