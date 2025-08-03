Configuring the Working Mode for an E1 Interface
================================================

This section describes how to configure the working mode of a channelized E1 interface. E1 interfaces can work in either clear channel mode or channelized mode.

#### Context

An E1 interface can form serial interfaces with different transmission rates:

* If an E1 interface works in clear channel mode, the E1 interface forms a synchronous serial interface without timeslot division and with a transmission rate of 2.048 Mbit/s.
* If an E1 interface works in channelized mode, timeslots 1 to 31 of the E1 interface can be randomly bundled into channel-sets to form serial interfaces, each with a transmission rate of N x 64 kbit/s.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configuration of channelized mode is supported only on the Admin-VS.




#### Procedure

* Create a serial interface that works in clear channel mode.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**controller e1**](cmdqueryname=controller+e1) *controller-number*
     
     The E1 interface view is displayed.
  3. Run [**using**](cmdqueryname=using) **e1**
     
     The E1 interface is configured to work in clear channel mode, establishing a serial interface without timeslot division and with a transmission rate of 2.048 Mbit/s.
     
     You can run the [**interface**](cmdqueryname=interface) **serial** *controller-number*:**0** command to enter the serial interface view.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Create a serial interface that works in channelized mode.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**controller e1**](cmdqueryname=controller+e1) *controller-number*
     
     The E1 interface view is displayed.
  3. Run [**using**](cmdqueryname=using) **ce1**
     
     The interface is configured to work in channelized mode.
  4. Run [**channel-set**](cmdqueryname=channel-set) *set-number* **timeslot-list** *slot-list*
     
     A serial interface with a transmission rate of N x 64 kbit/s is created. N stands for the number of bundled timeslots.
     
     To change the working mode of an E1 interface:
     
     + Delete serial interfaces and their configurations and channelization configurations before you run the **using** **e1** command to switch an E1 interface from the channelized mode to the clear channel mode.
     + Delete clear channel configurations and serial interface configurations before you run the **using** **ce1** command to switch an E1 interface from the clear channel mode to the channelized mode.
     
     You can run the [**interface**](cmdqueryname=interface) **serial** *controller-number*:*set-number* command to enter the serial interface view.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.