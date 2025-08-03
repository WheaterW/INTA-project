Configuring TCP Flow Aging
==========================

Configuring TCP Flow Aging

#### Context

When configuring intelligent traffic analysis for TCP flows, you need to configure the TCP flow aging function. Once enabled, the device sends the TCP flow table to the TDA when a TCP flow table meets aging conditions.


#### Procedure

* Configure active flow aging.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure the active flow aging time for TCP flows.
     
     
     ```
     [traffic-analysis tcp timeout active](cmdqueryname=traffic-analysis+tcp+timeout+active) active-interval
     ```
     
     
     
     By default, the active flow aging time of TCP flows is 10 seconds.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure inactive flow aging.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure the inactive flow aging time for TCP flows.
     
     
     ```
     [traffic-analysis tcp timeout inactive](cmdqueryname=traffic-analysis+tcp+timeout+inactive) inactive-interval
     ```
     
     
     
     By default, the inactive flow aging time of TCP flows is 30 seconds.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure FIN- and RST-based aging.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure the function of aging TCP flows based on the FIN or RST flag in the TCP packet header.
     
     
     ```
     [traffic-analysis tcp timeout tcp-session](cmdqueryname=traffic-analysis+tcp+timeout+tcp-session)
     ```
     
     
     
     By default, this function is disabled.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```