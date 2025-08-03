Enabling NETCONF Operation Log Query
====================================

To query NETCONF operation logs, you need to enable NETCONF operation log query.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**snetconf server enable**](cmdqueryname=snetconf+server+enable)
   
   
   
   NETCONF is enabled.
3. Run [**netconf**](cmdqueryname=netconf)
   
   
   
   The NETCONF user interface view is displayed.
4. Run [**rpc-message log protocol-operation get**](cmdqueryname=rpc-message+log+protocol-operation+get)
   
   
   
   NETCONF operation log query is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.