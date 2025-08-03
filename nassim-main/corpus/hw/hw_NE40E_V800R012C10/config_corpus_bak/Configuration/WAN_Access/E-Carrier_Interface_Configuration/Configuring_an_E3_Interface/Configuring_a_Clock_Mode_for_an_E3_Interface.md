Configuring a Clock Mode for an E3 Interface
============================================

An E3 interface works either in master clock mode or slave clock mode.

#### Context

An E3 interface has two clock modes:

* Master clock mode: The E3 interface uses internal clock signals.
* Slave clock mode: The E3 interface uses clock signals provided by an external device.

When two Routers are directly connected through E3 interfaces, configure one E3 interface as the master clock and the other E3 interface as the slave clock.

Perform the following steps on a router.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**controller**](cmdqueryname=controller) **e3** *controller-number*
   
   
   
   The specified E3 interface view is displayed.
3. Run [**clock**](cmdqueryname=clock) { **master** | **slave** }
   
   
   
   The clock mode of the E3 interface is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.