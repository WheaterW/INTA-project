Configuring the Working Mode of a CPOS-Trunk Interface
======================================================

Configuring_the_Working_Mode_of_a_CPOS-Trunk_Interface

#### Context

A CPOS-Trunk interface can work in either clear channel mode or channelized mode. Trunk serial interfaces with different transmission rates can be generated in the two modes to meet different bandwidth requirements of services.![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configuration of channelized mode is supported only on the Admin-VS.




#### Procedure

* Configure a CPOS-Trunk interface to work in channelized mode.
  + Configure an E1 channel of a CPOS-Trunk interface to work in clear channel mode so that a trunk serial interface is generated.
    
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**interface cpos-trunk**](cmdqueryname=interface+cpos-trunk) *trunk-id*
       
       The CPOS-Trunk interface view is displayed.
    3. Run [**e1**](cmdqueryname=e1) *e1-number* **unframed**
       
       An E1 channel of the CPOS-Trunk interface is configured to work in clear channel mode, and a trunk serial interface is generated.
       
       After the trunk serial interface in clear channel mode is generated, you can run the [**interface**](cmdqueryname=interface) **trunk-serial** *cpos-trunk-id*/*e1-number*:**0** command to enter the trunk serial interface view.
    4. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
  + Configure an E1 channel of a CPOS-Trunk interface to work in channelized mode so that a trunk serial interface in channelized mode can be generated.
    
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**interface cpos-trunk**](cmdqueryname=interface+cpos-trunk) *trunk-id*
       
       The CPOS-Trunk interface view is displayed.
    3. Run [**e1**](cmdqueryname=e1) *e1-number* **channel-set** *set-number* **timeslot-list** *slot-list*
       
       Timeslots of an E1 channel of the CPOS-Trunk interface are bundled, and a trunk serial interface is generated.
       
       After the trunk serial interface in channelized mode is generated, you can run the [**interface**](cmdqueryname=interface) **trunk-serial** *cpos-trunk-id*/*e1-number*:*set-number* command to enter the trunk serial interface view.
    4. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
* Configure a CPOS-Trunk interface to work in clear channel mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface cpos-trunk**](cmdqueryname=interface+cpos-trunk) *trunk-id*
     
     The CPOS-Trunk interface view is displayed.
  3. Run [**using vc4**](cmdqueryname=using+vc4)
     
     The CPOS-Trunk interface is configured to work in clear channel mode, and a trunk serial interface is created on the CPOS-Trunk interface. The trunk serial interface transmits data at a high rate, without timeslot division.
     
     After the trunk serial interface is created, you can run the [**interface**](cmdqueryname=interface) **trunk-serial** *cpos-trunk-id*/*0*:*0* command to enter the trunk serial interface view.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.