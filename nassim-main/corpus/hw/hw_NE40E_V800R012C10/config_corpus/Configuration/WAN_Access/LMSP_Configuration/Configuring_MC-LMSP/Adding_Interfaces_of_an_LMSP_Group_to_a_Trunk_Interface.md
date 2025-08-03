Adding Interfaces of an LMSP Group to a Trunk Interface
=======================================================

A working interface and a protection interface in an LMSP group must be added to a single trunk interface.

#### Context

LMSP is used to protect traffic on attachment circuit (AC) links connecting Routers to Add/Drop Multiplex (ADM) devices or Radio Network Controllers (RNCs) on a Synchronous Digital Hierarchy (SDH) network. AC-side physical channelized Packet Over SDH/SONET (CPOS) interfaces on the Routers are added to a trunk interface to carry services.

Perform the following steps on the working and protection interfaces of an LMSP group:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface cpos-trunk**](cmdqueryname=interface+cpos-trunk) *interface-number*
   
   
   
   A CPOS-Trunk interface is created, and the view of the CPOS-Trunk interface is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   LMSP can be configured on the CPOS interfaces. The corresponding trunk interfaces are CPOS-Trunk.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   The system view is displayed.
4. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
   
   
   
   The interface view is displayed.
5. Run [**cpos-trunk**](cmdqueryname=cpos-trunk) *trunk-id*
   
   
   
   The interface is added to a trunk interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The working and protection interfaces of an LMSP group must be added to the trunk interface with the same trunk ID.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.