Configuring the Loopback Function for the E1 Channels of a CPOS Interface
=========================================================================

You can enable the loopback function on an interface to
check whether the interface or the link works properly.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view
   is displayed.
2. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
   
   
   
   The CPOS interface
   view is displayed.
3. Run [**e1**](cmdqueryname=e1) *e1-number* **set** **loopback** { **local** | **remote** } [ **autoclear period** *hold-time* ]
   
   
   
   A loopback
   mode is configured for the E1 channel.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * To enable local loopback for an E1 channel, the channel must work
     in master clock mode.
   * To enable remote loopback for an E1 channel, the channel must
     work in slave clock mode.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.