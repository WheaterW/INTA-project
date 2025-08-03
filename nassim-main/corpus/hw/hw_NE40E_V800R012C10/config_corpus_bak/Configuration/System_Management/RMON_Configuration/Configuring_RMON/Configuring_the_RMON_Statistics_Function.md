Configuring the RMON Statistics Function
========================================

Configuring the RMON statistics function helps to collect and record statistics of an interface.

#### Context

RMON statistics can be divided into the Ethernet statistics function and historical sampling function.

* Ethernet statistics function (corresponding to the statistics group in RMON MIB): The system collects the statistics about basic traffic on monitored interfaces.
* Historical sampling function (corresponding to the history group in RMON MIB): The system samples the interface statuses on the network periodically and stores the information for later queries.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **interface-type** *interface-number*
   
   
   
   The interface on which traffic statistics are collected is specified and the view of the interface is displayed.
3. Run [**rmon-statistics enable**](cmdqueryname=rmon-statistics+enable)
   
   
   
   The RMON statistics function is enabled on the interface.
   
   If the RMON statistics function is not enabled, the Ethernet statistics and historical sampling functions cannot be enabled.
4. Run [**rmon statistics**](cmdqueryname=rmon+statistics) *entry-number* [ **owner** *owner-name* ]
   
   
   
   The Ethernet statistics function is configured.
5. Run [**rmon history**](cmdqueryname=rmon+history) *entry-number* **buckets** *number* **interval** *sampling-interval* [ **owner** *owner-name* ]
   
   
   
   The historical sampling function is configured.
   
   To reduce the impact of RMON on system performance, the sampling interval should be set to be longer than 10 seconds, and the historical sampling function should not be configured multiple times on an interface. RMON suggests that each monitored interface can be configured with more than two historical samples and the sampling interval should be 30 seconds.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.