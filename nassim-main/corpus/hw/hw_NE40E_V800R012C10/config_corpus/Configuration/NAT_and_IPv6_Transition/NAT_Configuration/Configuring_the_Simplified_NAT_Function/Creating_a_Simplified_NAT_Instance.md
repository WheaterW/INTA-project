Creating a Simplified NAT Instance
==================================

After a simplified NAT instance is configured, a device automatically generates a service-instance group named **\_default\_** and binds it to a service-location group and the NAT instance. This process does not requires manual intervention and therefore simplifies the NAT configuration.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ] **simple-configuration**
   
   
   
   A simplified NAT instance is configured, and its NAT instance view is displayed.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.