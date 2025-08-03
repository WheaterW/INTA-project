Configuring IS-IS to Generate IPv4 Default Routes
=================================================

This section describes how to configure IS-IS to generate default routes to control the advertising of IS-IS routing information.

#### Context

The destination address and mask of a default route are all 0s. If the destination address of a packet does not match any entry in the routing table of a device, the device sends the packet along the default route. If neither the default route nor the destination address of the packet exists in the routing table, the device discards the packet and informs the source end that the destination address or network is unreachable.

IS-IS can generate default routes using either of the following mode:

* [Command-triggered default route generation mode](#EN-US_TASK_0172365985__dc_vrp_isis_cfg_101101)
  
  You can run the [**default-route-advertise**](cmdqueryname=default-route-advertise) command on a device so that the device adds a default route to the LSP before sending the LSP to a neighbor. Therefore, the neighbor can learn this default route.
* [ATT bit 1-triggered default route generation mode](#EN-US_TASK_0172365985__dc_vrp_isis_cfg_101102)
  
  According to IS-IS, a Level-1-2 router sets the ATT bit to 1 in the LSP to be advertised to a Level-1 area if the Level-1-2 router can reach more Level-1 areas through the Level-2 area than through the Level-1 area. After a Level-1 router in the Level-1 area receives the LSP, it generates a default route destined for the Level-1-2 router. Based on the network requirements, you can configure whether the Level-1-2 router sets the ATT bit carried in the LSP and whether a Level-1 router generates a default route after it receives the LSP carrying ATT bit 1.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  This mode applies only to Level-1 routers.


#### Procedure

* Configure command-triggered default route generation mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**default-route-advertise**](cmdqueryname=default-route-advertise) [ **always** | **match** **default** | **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] [ [ **cost** *cost* ] | [ **tag** *tag* ] | [ **level-1** | **level-2** | **level-1-2** ] ] \* [ **avoid-learning** ]
     
     
     
     IS-IS is configured to generate default routes.
     
     
     
     The IS-IS level of a router determines the IS-IS level of the generated default routes. The default routes generated using this command are advertised only to routers of the same level. You can configure a routing policy so that IS-IS generates default routes only when there are matched routes in the routing table.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure ATT bit 1-triggered default route generation mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run the following command as required:
     
     
     + To set the ATT bit in the LSPs sent by the Level-1-2 router, run the [**attached-bit advertise**](cmdqueryname=attached-bit+advertise) { **always** | **never** } command.
       
       - If the **always** parameter is specified, the ATT bit is set to 1. After receiving the LSPs carrying the ATT bit 1, the Level-1 router generates a default route.
       - If the **never** parameter is specified, the ATT bit is set to 0. After receiving the LSPs carrying the ATT bit 0, the Level-1 router does not generate a default route, which reduces the size of a routing table.
     + To disable the Level-1 router from generating default routes even though it receives the LSPs carrying ATT bit 1, run the [**attached-bit avoid-learning**](cmdqueryname=attached-bit+avoid-learning) command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.