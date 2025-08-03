Configuring the Frame Format for the E1 Channels of a CPOS Interface
====================================================================

E1 channels support the frame format with a 4-bit CRC code.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view
   is displayed.
2. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
   
   
   
   The CPOS interface
   view is displayed.
3. Run [**e1**](cmdqueryname=e1) *e1-number* **set** **frame-format** { **crc4** | **no-crc4** }
   
   
   
   A frame format
   is configured for the E1 channel.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   The frame format of the E1 channel must be the same on the local
   and remote devices.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.