Configuring the Working Mode of a CPOS Interface
================================================

A CPOS interface can work in either clear channel mode or channelized mode. Synchronous serial interfaces with different transmission rates can be generated in the two modes to meet different bandwidth requirements of services.

#### Context

If a CPOS interface works in clear channel mode, synchronous serial interfaces with higher transmission rates can be generated, so that the CPOS interface can provide sufficient bandwidth for service bearer.

If a CPOS interface works in channelized mode, the E1 channels of the CPOS interface can generate synchronous serial interfaces with different transmission rates when they work in different modes:

* In clear channel mode, an E1 channel functions as a synchronous serial interface without timeslot division and with a transmission rate of 2.048 Mbit/s.
* In channelized mode, an E1 channel is divided into 32 timeslots numbered from 0 to 31. Timeslots 1 to 31 can be randomly bundled to generate logical channels with transmission rates of N x 64 kbit/s.


#### Procedure

* Configure a CPOS interface to work in channelized mode.
  + Configure an E1 channel of the CPOS interface to work in clear channel mode so that a trunk serial interface is generated.
    
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
       
       The CPOS interface view is displayed.
    3. Run [**e1**](cmdqueryname=e1) *e1-number* **unframed**
       
       The specified E1 channel is configured to work in clear channel mode, and a serial interface with a transmission rate of 2.048 Mbit/s is created.
       
       By default, an E1 channel works in channelized mode.
       
       In VS mode, this command is supported only by the admin VS.
       
       After the serial interface is created, you can run the [**interface**](cmdqueryname=interface) **serial** *cpos-number*/*e1-number*:**0** command to enter the serial interface view.
    4. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
  + Configure an E1 channel of a CPOS interface to work in channelized mode so that a trunk serial interface in channelized mode can be generated.
    
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
       
       The CPOS interface view is displayed.
    3. Run [**e1**](cmdqueryname=e1) *e1-number* [**channel-set**](cmdqueryname=channel-set) *set-number* **timeslot-list** *slot-list*
       
       The specified timeslots of the specified E1 channel are bundled to generate a serial interface with a transmission rate of N x 64 kbit/s. N indicates the number of bundled timeslots.
       
       In VS mode, this command is supported only by the admin VS.
       
       After the serial interface is configured, you can run the [**interface**](cmdqueryname=interface) **serial** *cpos-number*/*e1-number*:*set-number* command to enter the serial interface view.
    4. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
* Configure a CPOS interface to work in clear channel mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
     
     The CPOS interface view is displayed.
  3. Run [**using vc4**](cmdqueryname=using+vc4)
     
     The CPOS interface is configured to work in clear channel mode, and a synchronous serial interface is created on the CPOS interface. The synchronous serial interface transmits data at 150.336 Mbit/s, without timeslot division.
     
     After the synchronous serial interface is created, you can run the [**interface**](cmdqueryname=interface) **serial** *cpos-number*/*0*:*0* command to enter the serial interface view.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.