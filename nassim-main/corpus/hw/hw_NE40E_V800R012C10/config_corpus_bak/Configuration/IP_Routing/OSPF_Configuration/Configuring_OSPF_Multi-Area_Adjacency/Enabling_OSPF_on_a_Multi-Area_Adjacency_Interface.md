Enabling OSPF on a Multi-Area Adjacency Interface
=================================================

Enabling OSPF on a multi-area adjacency interface is the prerequisite for configuring basic multi-area adjacency functions.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* | **router-id** *router-id* ] \*
   
   
   
   An OSPF process is started, and the OSPF view is displayed.
3. Run [**area**](cmdqueryname=area) *area-id*
   
   
   
   The OSPF area view is displayed.
4. Enable OSPF on an interface.
   1. Run twice [**quit**](cmdqueryname=quit)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   3. Run [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id*
      
      
      
      OSPF is enabled on the interface.
5. Run [**ospf enable multi-area**](cmdqueryname=ospf+enable+multi-area) *area-id*
   
   
   
   OSPF is enabled on the multi-area adjacency interface.
6. Run [**ospf mtu-enable multi-area**](cmdqueryname=ospf+mtu-enable+multi-area) *area-id*
   
   
   
   The multi-area adjacency interface is configured to fill in DD packets with the MTU value when sending the packets and check whether the MTU in each DD packet received from a neighbor exceeds the MTU of the local interface.
   
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   Enabling an interface to fill in DD Packets with its MTU will cause the involved neighbor relationship to be re-established.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.