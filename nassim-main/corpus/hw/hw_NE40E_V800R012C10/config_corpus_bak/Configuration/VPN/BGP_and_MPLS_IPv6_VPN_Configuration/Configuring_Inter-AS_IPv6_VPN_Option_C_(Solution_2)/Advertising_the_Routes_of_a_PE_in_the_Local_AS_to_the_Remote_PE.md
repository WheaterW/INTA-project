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
     
     
     
     The function to advertise the loopback address of a PE in the local AS to the remote ASBR is enabled.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the peer ASBR to import BGP routes to an IGP.
  
  Perform the following steps on the peer ASBR:
  + If OSPF runs between the PE and ASBR:
    
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**ospf**](cmdqueryname=ospf) *process-id* command to enter the OSPF view.
    3. Run the [**import-route**](cmdqueryname=import-route) **bgp** [ **cost** *cost* ] [ **route-policy** *route-policy-name* ] command to import BGP routes to OSPF.
    4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
    5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  + If IS-IS runs between the PE and ASBR:
    
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**isis**](cmdqueryname=isis) *process-id* command to enter the IS-IS view.
    3. Run the [**import-route**](cmdqueryname=import-route) **bgp** [ **cost-type** { **external** | **internal** } | **cost** *cost* | **tag** *tag* | **route-policy** *route-policy-name* | [ **level-1** | **level-2** | **level-1-2** ] ] \* command to import BGP routes to IS-IS.
       
       If the IS-IS level is not specified in the command, BGP routes will be imported into the Level-2 IS-IS routing table.
    4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
    5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.