Configuring a Link Layer Protocol for a Serial Interface
========================================================

This section describes how to configure a link-layer protocol for a serial interface. The link-layer protocol used by a serial interface determines the format of frames passing through this interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface serial**](cmdqueryname=interface+serial) *interface-number*
   
   
   
   The serial interface view is displayed:
   
   
   
   * To enter the view of a serial interface on a CE1 interface, you must specify *interface-number* in the format of "chassis number/slot number/card number/port number:serial interface number". For example, the name of serial interface 1 on CE1 0/2/0 is serial 0/2/0:1.
   * To enter the view of a serial interface on a CPOS interface, you must specify *interface-number* in the format of "chassis number/slot number/card number/port number/E1 channel number:serial interface number". For example, the name of serial interface 3 of E1 channel 2 on CPOS0/2/0 is serial 0/2/0/2:3.
3. Run [**link-protocol**](cmdqueryname=link-protocol) { **ppp** | **tdm** | **hdlc** | **atm** }
   
   
   
   A link-layer protocol type is set for the serial interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.