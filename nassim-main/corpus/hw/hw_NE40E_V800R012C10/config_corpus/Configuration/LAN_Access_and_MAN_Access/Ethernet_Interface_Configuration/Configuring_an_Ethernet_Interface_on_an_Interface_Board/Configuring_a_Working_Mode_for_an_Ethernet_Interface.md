Configuring a Working Mode for an Ethernet Interface
====================================================

An Ethernet interface works in either half-duplex or full-duplex mode at the physical layer of an Ethernet network. To ensure communication between devices, configure a proper duplex mode for an Ethernet interface.

#### Context

On a large-scale Ethernet network, manually setting the interface rate and duplex mode, verifying device configurations, and checking Ethernet interface statistics are time-consuming. Manually setting the interface rate and duplex mode is recommended only when auto-sensing of an Ethernet link fails. When there is an auto-sensing problem, you are advised to upgrade device software or hardware for the device to support the auto-sensing mechanism defined in IEEE 802.3u/z.

Perform the following steps on target Routers:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **gigabitethernet** *interface-number*
   
   
   
   The specified Ethernet interface view is displayed.
3. Run either of the following commands as needed:
   
   
   * To configure a working mode for the Ethernet interface, run the [**duplex**](cmdqueryname=duplex+full+half+auto) { **full** | **half** | **auto** } command.
   * To configure the Ethernet interface to work in auto-negotiation mode, run the [**negotiation auto**](cmdqueryname=negotiation+auto) command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Ethernet optical interfaces work only in full-duplex mode.
   * When connecting to a hub, an Ethernet electrical interface on the Router must work in half-duplex mode because the hub can work only in this mode. When connecting to a LAN switch, an Ethernet electrical interface on the Router can work in either full-duplex or half-duplex mode. Ethernet electrical interfaces on the Router and peer device must work in the same mode.
   * If the working rate of a GE electrical interface is 1000 Mbit/s, you cannot configure the GE electrical interface to work in half-duplex mode.
   * If the working rate of a GE electrical interface is 1000 Mbit/s and auto-negotiation is enabled, you cannot configure the GE electrical interface to work in half-duplex or full-duplex mode. In addition, you cannot disable auto-negotiation on the interface.
   * If the working rate of a GE electrical interface is 10 Mbit/s or 100 Mbit/s, you can configure the interface to work in half-duplex or auto-sensing mode.
   * The rate of a 50GE|100GE interface can be adjusted using the [**switch-mode**](cmdqueryname=switch-mode) command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.