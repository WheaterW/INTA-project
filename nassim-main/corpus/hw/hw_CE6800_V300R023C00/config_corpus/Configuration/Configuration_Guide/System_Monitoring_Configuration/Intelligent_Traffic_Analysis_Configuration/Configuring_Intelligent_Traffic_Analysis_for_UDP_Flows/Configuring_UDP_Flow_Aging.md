Configuring UDP Flow Aging
==========================

Configuring UDP Flow Aging

#### Context

When a UDP flow is continuously received, analysis results of the UDP flow are periodically sent to the TDA on a per-block basis. When the inactive time (the time from when the last UDP packet is received to the current time) of the UDP flow exceeds the configured inactive flow aging time, the device considers that the UDP flow is inactive (the flow is interrupted). In this case, the device forcibly sends the current flow table to the TDA and deletes it. This process is called inactive flow aging.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the inactive flow aging time for UDP flows.
   
   
   ```
   [traffic-analysis udp timeout inactive](cmdqueryname=traffic-analysis+udp+timeout+inactive) inactive-interval
   ```
   
   By default, the inactive flow aging time of UDP flows is 30 seconds.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```