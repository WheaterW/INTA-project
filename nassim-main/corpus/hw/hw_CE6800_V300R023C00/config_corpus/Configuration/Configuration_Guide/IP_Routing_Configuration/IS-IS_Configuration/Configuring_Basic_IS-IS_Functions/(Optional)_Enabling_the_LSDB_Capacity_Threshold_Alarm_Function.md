(Optional) Enabling the LSDB Capacity Threshold Alarm Function
==============================================================

(Optional) Enabling the LSDB Capacity Threshold Alarm Function

#### Context

On an IS-IS network, incorrect configurations may cause a large number of external routes to be imported. Similarly, an IS-IS device may advertise a large number of LSPs when attack packets are received. Both instances would lead to a network fault. To prevent this problem, you can configure the LSDB capacity threshold alarm function, which generates an alarm if the number of LSPs reaches the configured threshold, facilitating troubleshooting by the administrator.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an IS-IS process and enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ] [ vpn-instance vpn-instance-name ]
   ```
3. Enable the LSDB capacity threshold alarm function.
   
   
   ```
   [lsdb limit](cmdqueryname=lsdb+limit) limit-number threshold-alarm upper-limit upper-limit-value lower-limit lower-limit-value
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```