Configuring the Working Modes for the E1 Channels of a CPOS Interface
=====================================================================

This section describes how to configure the working modes for the E1 channels of a channelized packet over SONET/SDH (CPOS) interface. Here, SONET stands for synchronous optical network, and SDH stands for synchronous digital hierarchy.

#### Context

The E1 channels of a CPOS interface can form serial interfaces with different transmission rates when they work in different modes:

* In clear channel mode, an E1 channel functions as a serial interface without timeslot division and with a transmission rate of 2.048 Mbit/s.
* In channelized mode, an E1 channel is divided into 32 timeslots numbered from 0 to 31. Timeslots 1 to 31 can be randomly bundled to form logical channels with transmission rates of N x 64 kbit/s.


#### Procedure

* Create a serial interface in clear channel mode.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
     
     The CPOS interface view is displayed.
  3. Run [**e1**](cmdqueryname=e1) *e1-number* **unframed**
     
     The specified E1 channel is configured to work in clear channel mode, and a serial interface with a transmission rate of 2.048 Mbit/s is created.
     
     After the serial interface is created, you can run the [**interface**](cmdqueryname=interface) **serial** *cpos-number*/*e1-number*:**0** command to enter the serial interface view.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Create a serial interface in channelized mode.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
     
     The CPOS interface view is displayed.
  3. Run [**e1**](cmdqueryname=e1) *e1-number* [**channel-set**](cmdqueryname=channel-set) *set-number* **timeslot-list** *slot-list*
     
     The specified timeslots of the specified E1 channel are bundled to form a serial interface with a transmission rate of N x 64 kbit/s. N indicates the number of bundled channels.
     
     After the serial interface is configured, you can run the [**interface**](cmdqueryname=interface) **serial** *cpos-number*/*e1-number*:*set-number* command to enter the serial interface view.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.