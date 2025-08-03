Importing BGP routes to the IGP Routing Table
=============================================

To enable LDP to allocate labels for BGP, you need first import BGP routes into the IGP routing table.

#### Context

Import BGP routes to the IGP routing table. IS-IS is used as an example.

Perform the following steps on the Level 1 carrier CE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ] [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The IS-IS view is displayed.
3. Run [**import-route**](cmdqueryname=import-route) **bgp** [ **cost** *cost* ] [ **route-policy** *route-policy-name* ]
   
   
   
   BGP routes are imported into the IGP routing table.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.