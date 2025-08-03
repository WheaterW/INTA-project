Configuring IS-IS to Generate IPv6 Default Routes
=================================================

This section describes how to configure IS-IS to generate IPv6 default routes to control the advertising of IS-IS routing information.

#### Context

The IPv6 default route is the route ::/0. If the destination address of a packet does not match any entry in the routing table of a device, the device sends the packet along the default route. If neither the default route nor the destination address of the packet exists in the routing table, the device discards the packet and informs the source end that the destination address or network is unreachable.

IS-IS can generate default routes using either of the following mode:

* [Command-triggered default route generation](#EN-US_TASK_0172366031__dc_vrp_isis_cfg_103401)
  
  After the device is configured to advertise the default route, the device adds the default route to an LSP before sending the LSP to a neighbor. In this way, the neighbor can learn this default route.
* [ATT bit setting-triggered default route generation](#EN-US_TASK_0172366031__dc_vrp_isis_cfg_103402)
  
  As defined in IS-IS, a Level-1-2 router sets the ATT bit in the Level-1 LSPs to be advertised if the Level-1-2 router can reach more Level-1 areas through the Level-2 area than through the Level-1 area. After a Level-1 router receives the LSP with the ATT bit set, it generates a default route destined for the Level-1-2 router that sent this LSP. Based on network requirements, you can configure whether the ATT bit is set and whether a Level-1 router generates a default route after it receives an LSP in which the ATT bit is set.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  This mode applies only to Level-1 routers.


#### Procedure

* Configure command-triggered default route generation mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**ipv6 default-route-advertise**](cmdqueryname=ipv6+default-route-advertise) [ **always** | **match** **default** | **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] [ [ **cost** *cost* ] | [ **tag** *tag* ] | [ **level-1** | **level-2** | **level-1-2** ] ] \* [ **avoid-learning** | **learning-avoid-loop** ]
     
     
     
     IS-IS is configured to generate default IPv6 routes.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure ATT bit setting-triggered default route generation mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Perform the following steps as required:
     
     
     + To set the ATT bit in the LSPs sent by the Level-1-2 router, run the [**attached-bit advertise**](cmdqueryname=attached-bit+advertise) { **always** | **never** } command.
       
       - If the **always** parameter is specified, the ATT bit is always set. After receiving the LSPs in which the ATT bit is set, the Level-1 router generates a default route.
       - If the **never** parameter is specified, the ATT bit is never set. After receiving the LSPs carrying the ATT bit that is not set, each Level-1 router does not generate a default route, which reduces the size of its routing table.
     + To disable the Level-1 router from generating default routes even though it receives the Level-1 LSPs in which the ATT bit is set, run the [**attached-bit avoid-learning**](cmdqueryname=attached-bit+avoid-learning) command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.