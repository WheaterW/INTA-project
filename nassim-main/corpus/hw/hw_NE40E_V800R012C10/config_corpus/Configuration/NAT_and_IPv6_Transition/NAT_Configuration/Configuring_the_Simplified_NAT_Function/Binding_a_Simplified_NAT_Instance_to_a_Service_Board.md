Binding a Simplified NAT Instance to a Service Board
====================================================

After a simplified NAT instance is configured, a device automatically generates a service-instance group named **\_default\_** and binds it to the NAT instance. Then the simplified NAT instance is bound to a service board, so that the device automatically generates a service-location group and binds it to the service-instance-group named **\_default\_**. Consequently, the NAT configuration is simplified by eliminating manual configurations.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ] **simple-configuration**
   
   
   
   A simplified NAT instance is configured, and its view is displayed.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.