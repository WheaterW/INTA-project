(Optional) Configuring Packet Loss Monitoring for User-Level Rate Limiting
==========================================================================

(Optional) Configuring Packet Loss Monitoring for User-Level Rate Limiting

#### Context

After user-level rate limiting is enabled, the switch discards the excess packets if the rate of packets from the same source MAC address exceeds the rate limit within a specified period of time. You can configure packet loss monitoring for user-level rate limiting to check which packets are discarded.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable monitoring for packets discarded due to user-level rate limiting.
   
   
   ```
   [undo cpu-defend host-car drop-packet monitor disable](cmdqueryname=undo+cpu-defend+host-car+drop-packet+monitor+disable)
   ```
   
   By default, packet loss monitoring for user-level rate limiting is enabled.
3. The rate limit for packets discarded due to user-level rate limiting is set.
   
   
   ```
   [cpu-defend host-car drop-packet pps](cmdqueryname=cpu-defend+host-car+drop-packet+pps) pps-value
   ```
   
   By default, the packet loss monitoring threshold for user-level rate limiting is 64 pps.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```