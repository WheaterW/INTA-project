Configuring the Working Rate for an Ethernet Electrical Interface
=================================================================

The volume of traffic that can be transmitted on an Ethernet electrical interface is determined by the working rate of the interface. To ensure communication between devices, set a proper working rate for Ethernet electrical interfaces.

#### Context

On a large-scale Ethernet network, it takes a great deal of time to manually set the interface rate and duplex mode, verify device configurations, and check statistics on Ethernet interfaces. Manually setting the interface rate and duplex mode is recommended only when auto-negotiation of an Ethernet link fails. When there is an auto-negotiation problem, upgrade software or hardware to support the auto-negotiation mechanism defined in IEEE 802.3u/z.

You need to set the working rate only for Ethernet electrical interfaces, not Ethernet optical interfaces.

Perform the following steps on target Routers:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **gigabitethernet** *interface-number*
   
   
   
   The specified Ethernet interface view is displayed.
3. Run [**speed**](cmdqueryname=speed) { **10** | **100** | **1000** | **auto** }
   
   
   
   A working rate is set for the Ethernet electrical interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.