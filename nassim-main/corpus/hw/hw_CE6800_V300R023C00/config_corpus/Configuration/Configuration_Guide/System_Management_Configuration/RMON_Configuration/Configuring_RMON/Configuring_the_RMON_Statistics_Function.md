Configuring the RMON Statistics Function
========================================

Configuring the RMON Statistics Function

#### Context

Configuring the RMON statistics function helps to collect and record statistics of an interface.

RMON statistics can be divided into the Ethernet statistics function and historical sampling function.

* Ethernet statistics function (corresponding to the statistics group in the RMON MIB): The system collects the statistics about basic traffic on monitored interfaces.
* Historical sampling function (corresponding to the history group in the RMON MIB): The system samples the interface statuses on the network periodically and stores the information for later queries.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Determine the interface on which statistics are collected and enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Enable RMON statistics on the interface.
   
   
   ```
   [rmon-statistics enable](cmdqueryname=rmon-statistics+enable)
   ```
   
   
   
   By default, the RMON statistics function is disabled on an interface.
   
   If the RMON statistics function is not enabled, the Ethernet statistics and historical sampling functions do not take effect.
4. Configure the Ethernet statistics function.
   
   
   ```
   [rmon statistics](cmdqueryname=rmon+statistics) entry-number [ owner owner-name ]
   ```
5. Configure the historical sampling function.
   
   
   ```
   [rmon history](cmdqueryname=rmon+history) entry-number buckets number interval sampling-interval [ owner owner-name ]
   ```
   
   
   
   To reduce the impact of RMON on system performance, set a sampling interval longer than 10 seconds and do not configure excessive historical sampling on an interface. RMON specifications suggest a sampling interval of 30 seconds and more than two historical samplings per interface.
6. Exit the interface view.
   
   
   ```
   quit
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```