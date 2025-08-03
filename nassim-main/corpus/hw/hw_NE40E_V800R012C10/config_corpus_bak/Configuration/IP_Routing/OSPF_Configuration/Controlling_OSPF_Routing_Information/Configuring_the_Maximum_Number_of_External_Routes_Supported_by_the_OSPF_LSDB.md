Configuring the Maximum Number of External Routes Supported by the OSPF LSDB
============================================================================

You can set the maximum number of external routes in the LDSB to keep a proper number of external routes.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**lsdb-overflow-limit**](cmdqueryname=lsdb-overflow-limit) *number*
   
   
   
   The maximum number of external routes in the LSDB is set.
   
   If the number of external routes imported by OSPF exceeds the maximum number allowed by the LSDB, the device deletes self-generated non-default external routes to ensure proper forwarding of the other external routes imported by OSPF.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.