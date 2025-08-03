Adding Interfaces of an LMSP Group to a Trunk Interface
=======================================================

The working and protection interfaces in an LMSP group must be added to the same trunk interface.

#### Context

LMSP is used to protect traffic on attachment circuit (AC) links connecting Routers to add/drop multiplexers (ADMs) or radio network controllers (RNCs) on an SDH network. AC-side physical interfaces (CPOS or POS interfaces) need to be added to a trunk interface to carry services.

Perform the following steps on the working and protection interfaces in an LMSP group:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface cpos-trunk**](cmdqueryname=interface+cpos-trunk) *trunk-id*
   
   
   
   A CPOS-Trunk interface is created, and its view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   LMSP can be configured on CPOS and POS interfaces, which correspond to CPOS-Trunk and POS-Trunk interfaces, respectively. This example uses CPOS-Trunk interface configuration.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
   
   
   
   The CPOS interface view is displayed.
5. Run [**cpos-trunk**](cmdqueryname=cpos-trunk) *trunk-id*
   
   
   
   The CPOS interface is added to the trunk interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The working and protection interfaces in an LMSP group must be added to the same trunk interface with a unique trunk ID.