Configuring a Neighbor Reachability Detection Interval
======================================================

Configuring a Neighbor Reachability Detection Interval

#### Context

A device can send NS messages to detect whether its neighbors are reachable. To control the neighbor reachability detection frequency, you can configure an NS message transmission interval. Do not set a short interval, because although frequent NS message transmissions help rapidly determine whether neighbors are reachable, this negatively impacts system performance.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Enable the pre-detection of ND entries.
   
   
   ```
   [ipv6 nd pre-detect](cmdqueryname=ipv6+nd+pre-detect)
   ```
   
   To enable a device to send an NS message to detect the validity of ND entries before the ND entries change from the Reachable state to the Stale state, you can enable the pre-detection of ND entries.
3. (Optional) Enable the auto-detection of ND entries.
   
   
   ```
   [undo ipv6 nd auto-detect disable](cmdqueryname=undo+ipv6+nd+auto-detect+disable)
   ```
   
   The system sends NS messages to detect whether its neighbors are reachable before aging ND entries.
4. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
5. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
6. Enable IPv6.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
7. Configure an interval for sending NS messages.
   
   
   ```
   [ipv6 nd ns retrans-timer](cmdqueryname=ipv6+nd+ns+retrans-timer) interval
   ```
   
   You can configure an interval for sending NS messages to control the intervals at which a routing device detects neighbor reachability and performs DAD. In addition, the configured interval functions as a parameter in an RA message to instruct hosts to specify this interval as their own interval for sending NS messages.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```