Configuring the MTU of an Interface
===================================

Configuring a proper MTU for an ATM interface effectively improves efficiency of assembly and fragmentation of IP packets on the interface.

#### Context

The MTU of the ATM interface is used for the assembly and fragmentation of IP packets.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

After running the [**mtu**](cmdqueryname=mtu) command on an interface, restart the interface to validate the MTU configuration by running the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands.

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface atm**](cmdqueryname=interface+atm) *interface-number*
   
   
   
   The ATM interface view is displayed.
3. Run [**mtu**](cmdqueryname=mtu) *mtu*
   
   
   
   The MTU of the ATM interface is configured.
   
   The default MTU is 1500 bytes.
4. Run [**shutdown**](cmdqueryname=shutdown)
   
   
   
   The ATM interface is shut down.
5. Run [**undo shutdown**](cmdqueryname=undo+shutdown)
   
   
   
   The ATM interface is started.
   
   After changing the MTU by using the [**mtu**](cmdqueryname=mtu) command on a specified interface, restart the interface to validate the newly configured MTU value.