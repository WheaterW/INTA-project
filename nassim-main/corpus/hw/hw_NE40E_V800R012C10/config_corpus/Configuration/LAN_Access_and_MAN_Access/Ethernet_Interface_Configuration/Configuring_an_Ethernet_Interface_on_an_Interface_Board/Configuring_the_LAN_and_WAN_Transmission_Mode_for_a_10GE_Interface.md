Configuring the LAN/WAN Transmission Mode for a 10GE Interface
==============================================================

A 10G XFP multi-mode optical transceiver works in either LAN or WAN mode. You can configure a proper mode as required.

#### Context

Perform the following steps on the Router:

If the VS mode is used, this configuration task is supported only by the admin VS.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration is not supported by the following: NE40E-M2K-B.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **gigabitethernet** *interface-number*
   
   
   
   The 10GE LAN/WAN interface view is displayed.
3. Run [**shutdown**](cmdqueryname=shutdown)
   
   
   
   The interface is shut down.
4. Run [**set transfer-mode**](cmdqueryname=set+transfer-mode) { **lan** | **wan** }
   
   
   
   The LAN or WAN transmission mode is configured for the 10GE interface.
5. Run [**undo shutdown**](cmdqueryname=undo+shutdown)
   
   
   
   The interface is started again.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before configuring a 10GE LAN or 100GE LAN interface to work in LAN transmission mode, delete the clock, PTP, and loopback configurations from the interface and shut down the interface.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.