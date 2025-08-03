Creating a Synchronous Serial Interface on an E3 Interface
==========================================================

Before using an E3 interface to transmit data, you must create a synchronous serial interface on the E3 interface.

#### Context

Depending on the E3 interface working modes, you can create the following two types of synchronous serial interfaces on an E3 interface:

* If the E3 interface works in clear channel mode, an unframed synchronous serial interface with a bandwidth of 34.368 Mbit/s is created.
* If the E3 interface works in unchannelized mode, a synchronous serial interface with a bandwidth of 33.831 Mbit/s is created after you manually create a framed E3 channel.

This configuration process is supported only on the Admin-VS.


#### Procedure

* Create a synchronous serial interface on an E3 interface working in clear channel mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**controller**](cmdqueryname=controller) **e3** *controller-number*
     
     
     
     The specified E3 interface view is displayed.
  3. Run [**using**](cmdqueryname=using) **e3**
     
     
     
     The E3 interface is configured to work in clear channel mode, and an unframed synchronous serial interface with a bandwidth of 34.368 Mbit/s is created.
     
     
     
     After the synchronous serial interface is created, you can run the [**interface serial**](cmdqueryname=interface+serial) *controller-number* command to display the view of the synchronous serial interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Create a synchronous serial interface on an E3 interface working in unchannelized mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**controller**](cmdqueryname=controller) **e3** *controller-number*
     
     
     
     The specified E3 interface view is displayed.
  3. Run [**using**](cmdqueryname=using) **ce3**
     
     
     
     The E3 interface is configured to work in unchannelized mode.
  4. Run [**e3 framed**](cmdqueryname=e3+framed)
     
     
     
     A framed E3 channel is created, and an unframed synchronous serial interface with a bandwidth of 33.831 Mbit/s is created.
     
     
     
     After the synchronous serial interface is created, you can run the [**interface serial**](cmdqueryname=interface+serial) *controller-number* command to display the view of the synchronous serial interface.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.