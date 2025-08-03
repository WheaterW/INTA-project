Configuring Secure Synchronization
==================================

Secure synchronization prevents traffic loss after a device is restarted.

#### Context

When the Routers in an area just finish synchronizing the LSDBs, the LSDBs of these Routers are different from each other. As a result, route flapping occurs. You can configure secure synchronization to solve this problem. This, however, may delay the establishment of the OSPF neighbor relationship.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [*process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**safe-sync enable**](cmdqueryname=safe-sync+enable)
   
   
   
   Secure synchronization is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.