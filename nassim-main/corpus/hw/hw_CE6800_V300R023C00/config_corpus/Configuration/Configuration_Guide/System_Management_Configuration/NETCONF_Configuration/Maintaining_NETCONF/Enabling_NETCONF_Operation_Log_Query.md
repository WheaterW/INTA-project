Enabling NETCONF Operation Log Query
====================================

Enabling NETCONF Operation Log Query

#### Context

To query NETCONF operation logs, you need to enable NETCONF operation log query.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable NETCONF.
   
   
   ```
   [snetconf server enable](cmdqueryname=snetconf+server+enable)
   ```
3. Enter the NETCONF user interface view.
   
   
   ```
   [netconf](cmdqueryname=netconf)
   ```
4. Enable NETCONF operation log query.
   
   
   ```
   [rpc-message log protocol-operation get](cmdqueryname=rpc-message+log+protocol-operation+get)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```