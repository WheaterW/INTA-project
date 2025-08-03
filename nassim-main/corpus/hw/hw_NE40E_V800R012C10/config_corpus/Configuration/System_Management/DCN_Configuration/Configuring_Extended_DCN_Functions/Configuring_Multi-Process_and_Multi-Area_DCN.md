Configuring Multi-Process and Multi-Area DCN
============================================

If a GNE belongs to multiple processes and areas, multi-process and multi-area DCN can be configured so that the GNE can manage all the NEs in different processes and areas.

#### Context

On large-scale DCNs, different NEs are usually deployed in multiple processes and areas. In this situation, allocate interfaces on the GNE to different processes and areas and enable the GNE to advertise its NEIP address to these processes and areas so that the GNE can learn information about the DCN core routing tables of all the NEs in these processes and areas and manage the NEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**dcn ospf enable**](cmdqueryname=dcn+ospf+enable) [ *process-id* ] [**area**](cmdqueryname=area) *area-id*
   
   
   
   A process and area is configured for the DCN serial interface or sub-interface 4094.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In most cases, the [**network (OSPF)**](cmdqueryname=network+%28OSPF%29) command adds an interface to the specified process and area. However, this command does not apply to DCN serial interfaces or sub-interface 4094 because they borrow the same IP address.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**dcn**](cmdqueryname=dcn)
   
   
   
   The DCN view is displayed.
6. Run [**advertise neip**](cmdqueryname=advertise+neip)
   
   
   
   The GNE is enabled to advertise its NEIP to multiple processes and areas.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.