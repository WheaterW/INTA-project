Configuring the Clock Mode for a CE1 Interface
==============================================

A CE1 interface works in either master clock mode or slave clock mode. When two CE1 interfaces are directly connected, you must configure one to work in master clock mode and the other in slave clock mode. When a CE1 interface is connected to a transmission device, the CE1 interface must work in slave clock mode.

#### Context

A CE1 interface works in either of the following clock modes:

* Master clock mode: In master clock mode, a CE1 interface uses internal clock signals.
* Slave clock mode: In slave clock mode, a CE1 interface uses line clock signals.

When CE1 interfaces of two NE40Es are directly connected, you must configure one interface to work in master clock mode and the other interface in slave clock mode. When the CE1 interface of the NE40E is connected to a transmission device, you must configure this interface to work in slave clock mode and use the clock signals provided by the transmission device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**controller e1**](cmdqueryname=controller+e1) *controller-number*
   
   
   
   The CE1 interface view is displayed.
3. Run [**clock**](cmdqueryname=clock) { **master** | **slave** }
   
   
   
   A clock mode is configured for the CE1 interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.