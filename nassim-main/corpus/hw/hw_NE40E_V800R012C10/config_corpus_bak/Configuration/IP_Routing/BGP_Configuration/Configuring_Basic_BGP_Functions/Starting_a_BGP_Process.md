Starting a BGP Process
======================

Starting a BGP process is a prerequisite for configuring BGP functions. When starting a BGP process on a device, you need to specify the number of the AS to which the device belongs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**route loop-detect bgp enable**](cmdqueryname=route+loop-detect+bgp+enable)
   
   
   
   BGP routing loop detection is enabled.
   
   
   
   After this function is enabled, the device reports an alarm when detecting a BGP routing loop. Because the device cannot determine whether a routing loop is removed, the alarm will not be cleared automatically even if the routing loop is removed. To manually clear the BGP routing loop alarm, run the [**clear route loop-detect bgp alarm**](cmdqueryname=clear+route+loop-detect+bgp+alarm) command.
3. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   BGP is started (with the local AS number specified), and the BGP view is displayed.
4. (Optional) Run [**router-id**](cmdqueryname=router-id) *ipv4-address*
   
   
   
   A BGP router ID is configured.
   
   
   
   Configuring a new BGP router ID or changing the existing one will reset the BGP peer relationship between Routers.
   
   If two devices have different router IDs, an IBGP or EBGP connection can be established between them. If the router IDs are the same and the [**router-id allow-same enable**](cmdqueryname=router-id+allow-same+enable) command is run, an EBGP connection can be established.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   By default, BGP automatically selects a router ID configured in the system view as its router ID. If the selected router ID is the IP address of a physical interface, the change in the IP address will cause route flapping. To enhance network stability, configure the IP address of a loopback interface as the router ID. For rules in selecting router IDs from the system view, see the [**router-id**](cmdqueryname=router-id) command description.
   
   By default, Cluster\_List comparison takes precedence over router ID comparison during BGP route selection. To enable router ID comparison to take precedence over Cluster\_List comparison during BGP route selection, run the [**bestroute routerid-prior-clusterlist**](cmdqueryname=bestroute+routerid-prior-clusterlist) command.
5. (Optional) Run [**shutdown**](cmdqueryname=shutdown)
   
   
   
   All sessions between the device and its BGP peers are terminated.
   
   
   
   Frequent BGP route flapping may occur during system upgrade and maintenance. To prevent this from impacting the network, perform this step.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   After an upgrade or maintenance, run the [**undo shutdown**](cmdqueryname=undo+shutdown) command to restore the BGP sessions; otherwise, BGP functions will not work properly.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.