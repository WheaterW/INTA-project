Advertising the Routes of a PE in the Local AS to the Remote PE
===============================================================

After the routes of the loopback interface on a PE in an AS are advertised to the remote PE in another AS, the MP-EBGP peer relationship is established between PEs.

#### Procedure

* Configure an ASBR to advertise the loopback address of a PE in the local AS to the remote ASBR.
  
  Perform the following steps on each ASBR:
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**network**](cmdqueryname=network) *ip-address* [ *mask* | *mask-length* ]
     
     
     
     The function to advertise the loopback
     address of a PE in the local AS to the remote ASBR is enabled.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the peer ASBR to import BGP routes to an IGP.
  
  Perform the following steps on the peer ASBR:
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospf**](cmdqueryname=ospf) *process-id*
     
     
     
     The OSPF view is displayed.
  3. Run [**import-route**](cmdqueryname=import-route) **bgp** [ **cost** *cost* ] [ **route-policy** *route-policy-name* ]
     
     
     
     The BGP routes are imported to the IGP.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.