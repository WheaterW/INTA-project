Importing BGP Routes to the IGP Routing Table
=============================================

To enable LDP to allocate labels to BGP routes, you need to import BGP routes into an IGP first.

#### Context

Import BGP routes into an IGP (IS-IS is used as an example here).

Perform the following steps on Level 1 carrier CEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. (Optional) Run [**import-rib public labeled-unicast**](cmdqueryname=import-rib+public+labeled-unicast)
   
   
   
   The device is configured to import labeled routes to the routing table of the public network unicast address family.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This step is mandatory when Level 1 carrier CEs access Level 1 carrier PEs using LDP label distribution and the labeled address family mode.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the upper-level view.
5. Run [**isis**](cmdqueryname=isis) [ *process-id* ] [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The IS-IS view is displayed.
6. Run [**import-route**](cmdqueryname=import-route) **bgp** [ **cost** *cost* ] [ **route-policy** *route-policy-name* ]
   
   
   
   BGP routes are imported into the IGP.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.