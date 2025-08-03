Configuring OSPFv3 to Import External Routes
============================================

Importing the routes discovered by other routing protocols can enrich OSPFv3 routing information.

#### Context

Because OSPFv3 is a link-state routing protocol and cannot filter LSAs to be advertised directly, it can only filter routes when importing them. As such, only the routes that match the filtering conditions can be converted into LSAs and advertised.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

OSPFv3 and other dynamic routing protocols such as IS-IS and BGP often import routes from each other. If no routing policy is configured or a routing policy is incorrectly configured on a device where IS-IS, OSPFv3, and BGP import routes from each other, a Layer 3 routing loop may occur due to a route selection result change. As a result, services are compromised.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
3. Run [**default**](cmdqueryname=default) { **cost** *cost**value* | **tag** *tagvalue* | **type** *typevalue* } \*
   
   
   
   The default cost is set for imported routes.
4. Run [**import-route**](cmdqueryname=import-route) { **bgp** [ **permit-ibgp** ] | **direct** | **static** | **unr** } [ { **cost** *cost* | **inherit-cost** } | **tag** *tag* | **type** *type* | { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* } ] \*
   
   
   
   The device is configured to import external routes.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**import-route**](cmdqueryname=import-route) command cannot be used to import the default route from another AS.
5. (Optional) Run [**import-route limit**](cmdqueryname=import-route+limit) *limit-number* [ **threshold-alarm** { **upper-limit** *upper-limit-value* | **lower-limit** *lower-limit-value* } \* ]
   
   
   
   A limit is configured on the number of imported external routes to be advertised by OSPFv3.
   
   
   
   If OSPFv3 imports a large number of external routes and advertises them to a device with a small routing table capacity, the device may restart unexpectedly. To prevent this problem, configure a limit on the number of imported external routes to be advertised by OSPFv3.
   
   Ensure that *upper-limit-value* is greater than or equal to *lower-limit-value*.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.