Configuring the LAN or OTN Transmission Mode for a 10GE or 100GE Interface
==========================================================================

If the transmission modes of the interfaces at both ends of a link are different, the link goes down. To ensure reliable communication, set the same transmission mode (either LAN or OTN) for the interfaces at both ends of a link. If the VS mode is used, this configuration task is supported only by the admin VS.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration does not apply to the NE40E-M2E.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **gigabitethernet** *interface-number*
   
   
   
   The 10GE/100GE LAN interface view is displayed.
3. Run [**shutdown**](cmdqueryname=shutdown)
   
   
   
   The interface is shut down.
4. Run [**set transfer-mode**](cmdqueryname=set+transfer-mode) { **lan** | **otn** }
   
   
   
   The LAN transmission mode is configured for the 10GE/100GE LAN interface.
5. Run [**undo shutdown**](cmdqueryname=undo+shutdown)
   
   
   
   The interface is started again.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before configuring a 10GE/100GE interface to work in LAN mode, delete all configurations on the interface (excluding the IP address) and shut down the interface.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.