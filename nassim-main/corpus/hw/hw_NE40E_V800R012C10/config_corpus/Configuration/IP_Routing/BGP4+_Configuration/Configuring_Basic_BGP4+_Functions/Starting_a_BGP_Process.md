Starting a BGP Process
======================

A BGP process must be started before configuring BGP functions. When starting a BGP process, specify the number of the AS to which the device belongs.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Changing BGP router IDs will cause the reestablishment of the BGP connection between Routers.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**route loop-detect bgp enable**](cmdqueryname=route+loop-detect+bgp+enable)
   
   
   
   BGP routing loop detection is enabled.
   
   
   
   After this function is enabled, the device reports an alarm when detecting a BGP4+ routing loop. Because the device cannot determine whether the routing loop is removed, the alarm will not be cleared automatically even if the routing loop is removed. To manually clear the BGP routing loop alarm, run the [**clear route loop-detect bgp alarm**](cmdqueryname=clear+route+loop-detect+bgp+alarm) command.
3. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   BGP is enabled (the local AS number is specified), and the BGP view is displayed.
4. (Optional) Run [**router-id**](cmdqueryname=router-id) *ipv4-address*
   
   
   
   A BGP router ID is configured.
   
   
   
   If two devices have different router IDs, an IBGP or EBGP connection can be established between them. If the router IDs are the same and the [**router-id allow-same enable**](cmdqueryname=router-id+allow-same+enable) command is run, an EBGP connection can be established.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the router ID of the Router is the IP address of a physical interface, a change in the IP address will cause route flapping on the network. To enhance network stability, configuring the IP address of a loopback interface as the router ID is recommended.
   
   If no interface on a device is configured with an IPv4 address, you need to configure a router ID for the device.
5. (Optional) Run [**shutdown**](cmdqueryname=shutdown)
   
   
   
   All sessions between the device and its BGP4+ peers are terminated.
   
   During the system upgrade or maintenance, you can run this command to terminate all sessions between a device and its BGP4+ peers to prevent possible BGP4+ route flapping from affecting the network.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   After the upgrade or maintenance, run the [**undo shutdown**](cmdqueryname=undo+shutdown) command to restore the BGP4+ peer sessions; otherwise, BGP4+ functions will be affected.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.