Disabling OSPF IP FRR on an OSPF Multi-Area Adjacency Interface
===============================================================

If an interface runs key services, ensure that the backup path does not pass through this interface so that services will not be affected after FRR calculation.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id*
   
   
   
   OSPF is enabled on the interface.
4. Run [**ospf enable multi-area**](cmdqueryname=ospf+enable+multi-area) *area-id*
   
   
   
   OSPF is enabled on the multi-area adjacency interface.
5. Run [**ospf frr block**](cmdqueryname=ospf+frr+block) **multi-area** *area-id*
   
   
   
   OSPF IP FRR is disabled on the OSPF multi-area adjacency interface.
6. (Optional) Run [**ospf remote-lfa disable**](cmdqueryname=ospf+remote-lfa+disable) **multi-area** *area-id*
   
   
   
   The multi-area adjacency interface is prevented from participating in remote LFA next hop calculation.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.