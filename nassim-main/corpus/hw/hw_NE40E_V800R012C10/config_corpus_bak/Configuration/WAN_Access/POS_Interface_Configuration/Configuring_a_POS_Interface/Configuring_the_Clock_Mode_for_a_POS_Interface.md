Configuring the Clock Mode for a POS Interface
==============================================

A POS interface works in either master or slave clock mode. You can configure different clock modes for POS interfaces that function as a DTE or DCE.

#### Context

A POS interface supports the following clock modes:

* Master clock mode: uses internal clock signals.
* Slave clock mode: uses line clock signals.

The principles for configuring clock modes for POS interfaces in actual networking are as follows:

* Clocks modes on the POS interfaces of two directly connected Routers must be both set to **master**, or on one end set to **master** and the other end set to **slave**.
* If two Routers are connected over a WDM transmission device, clocks modes on the POS interfaces of the two interconnected devices must be both set to **master**.
* If two Routers are connected over an active SDH or SONET device, clock modes on the POS interfaces of the two interconnected devices can be set to **slave** to trace clock signals of the active SDH or SONET device.
* If the connection mode of two Routers is unknown, the clocks of the POS interfaces on the two Routers must work in master mode.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface pos**](cmdqueryname=interface+pos) *interface-number*
   
   
   
   The POS interface view is displayed.
3. Run [**clock**](cmdqueryname=clock) { **master** | **slave** }
   
   
   
   A clock mode is configured for the POS interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.