Disabling an OSPF Multi-Area Adjacency Interface from Creating BFD Sessions
===========================================================================

After BFD for OSPF is configured, all interfaces on which neighbor relationships are in Full state in the OSPF process create BFD sessions. You can disable an interface from creating BFD sessions as required.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id*
   
   
   
   OSPF is enabled on the interface.
4. Run [**ospf enable multi-area**](cmdqueryname=ospf+enable+multi-area) *area-id*
   
   
   
   OSPF is enabled on the multi-area adjacency interface.
5. Run [**ospf bfd block**](cmdqueryname=ospf+bfd+block) **multi-area** *area-id*
   
   
   
   The OSPF multi-area adjacency interface is disabled from creating BFD sessions.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.