Controlling the Processing of IP Packets Carrying Route Options
===============================================================

By disabling devices from processing IP packets carrying route options, you can effectively defend networks against attacks by sending these packets.

#### Context

IP packets can carry the following route options:

* Route alert option
* Record route option
* Source route option
* Timestamp option

These options are used to diagnose link faults and temporarily transmit special services. These options may also be utilized by network attackers to probe the network structure and launch attacks. Therefore, you need to run this command to enable the system to process or disable the system from processing IP packets with route options.

To defend networks against attacks by sending IP packets carrying route options, disable the system from processing these IP packets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run any of the following commands based on the route options:
   
   
   * Run [**undo ip option route-alert enable**](cmdqueryname=undo+ip+option+route-alert+enable)
     
     The system is disabled from processing IP packets carrying the route alert option.
   * Run [**undo ip option route-record enable**](cmdqueryname=undo+ip+option+route-record+enable)
     
     The system is disabled from processing IP packets carrying the record route option.
   * Run [**undo ip option source-route enable**](cmdqueryname=undo+ip+option+source-route+enable)
     
     The system is disabled from processing IP packets carrying the source route option.
   * Run [**undo ip option time-stamp enable**](cmdqueryname=undo+ip+option+time-stamp+enable)
     
     The system is disabled from processing IP packets carrying the timestamp option.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.