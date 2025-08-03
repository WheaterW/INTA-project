Configuring the Frame Format for a CE1 Interface
================================================

You can configure a CE1 interface to use a 4-bit CRC code to check physical frames.

#### Context

You can configure the frame format for a CE1 interface only when it works in channelized mode.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**controller e1**](cmdqueryname=controller+e1) *controller-number*
   
   
   
   The CE1 interface view is displayed.
3. Run [**frame-format**](cmdqueryname=frame-format) { **crc4** | **no-crc4** }
   
   
   
   A frame format is configured for the CE1 interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When setting the frame format of a CE1 interface, ensure that the local and remote ends are configured with the same frame format.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.