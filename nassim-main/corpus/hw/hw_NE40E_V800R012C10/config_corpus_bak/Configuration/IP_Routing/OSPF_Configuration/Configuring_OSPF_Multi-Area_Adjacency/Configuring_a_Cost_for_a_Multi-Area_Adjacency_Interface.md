Configuring a Cost for a Multi-Area Adjacency Interface
=======================================================

Configuring a cost for a multi-area adjacency interface can control route selection.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id*
   
   
   
   OSPF is enabled on the interface.
4. Run [**ospf enable multi-area**](cmdqueryname=ospf+enable+multi-area) *area-id*
   
   
   
   OSPF is enabled on the multi-area adjacency interface.
5. Run [**ospf cost**](cmdqueryname=ospf+cost) *cost* **multi-area** *area-id*
   
   
   
   A cost is configured for the multi-area adjacency interface.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.