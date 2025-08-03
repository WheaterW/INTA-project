Configuring BFD Session Flapping Suppression
============================================

Configuring BFD Session Flapping Suppression

#### Context

If link quality is poor, BFD detection results in frequent service switchovers. You can configure a link flapping suppression time to prevent frequent service switchovers. This helps protect link resources and reduce link resource consumption.


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable BFD globally and enter the global BFD view.
   ```
   [bfd](cmdqueryname=bfd)
   ```
3. Configure a flapping suppression time for BFD sessions.
   ```
   [dampening timer-interval](cmdqueryname=dampening+timer-interval) maximum maximum-milliseconds initial initial-milliseconds secondary secondary-milliseconds
   ```
   
   By default, the maximum BFD session flapping suppression time is 12000 ms, the initial BFD session suppression time is 2000 ms, and the secondary BFD session suppression time is 5000 ms.
   
   It is recommended that the maximum flapping suppression time be greater than the secondary suppression time and the secondary suppression time be greater than the initial suppression time.
4. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```