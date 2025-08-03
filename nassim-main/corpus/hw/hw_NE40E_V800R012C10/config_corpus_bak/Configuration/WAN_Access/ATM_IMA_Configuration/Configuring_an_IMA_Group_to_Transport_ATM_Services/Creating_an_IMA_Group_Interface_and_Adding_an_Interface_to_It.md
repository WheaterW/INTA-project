Creating an IMA Group Interface and Adding an Interface to It
=============================================================

To increase bandwidth, create an IMA group and bundle several
links in the IMA group.

#### Context

Interfaces can only be added to an IMA group interface
that has been created. After an IMA group interface is created, add
a serial interface to the IMA group interface.


#### Procedure

* Create an IMA group interface.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface ima-group**](cmdqueryname=interface+ima-group) *interface-number*
     
     An IMA group
     interface is created.
  3. Run [**quit**](cmdqueryname=quit)
     
     Exit from the IMA group interface view.
* Add a serial interface to the created IMA group interface.
  
  
  1. Run [**interface serial**](cmdqueryname=interface+serial) *interface-number*
     
     The serial interface view is displayed.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The IMA group interface and the serial interface to be added to
     the IMA group interface must reside on the same subcard of the same
     board.
  2. Run [**link-protocol atm**](cmdqueryname=link-protocol+atm)
     
     ATM is configured as the link layer protocol of
     the serial interface.
  3. Run [**ima ima-group**](cmdqueryname=ima+ima-group) *interface-number*
     
     The serial interface is added
     to the created IMA group interface.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) After a serial interface is added to a created IMA group interface,
     the ATM interface type configured for the IMA group interface before
     the serial interface is added becomes invalid. You must run the [**atm interface-type**](cmdqueryname=atm+interface-type) { **uni** | **nni** } command in the IMA group interface view to reconfigure the ATM
     interface type for the IMA group interface.
     + If a device is connected to a user device through an IMA group
       interface, set the ATM interface type of the IMA group interface to
       UNI.
     + If a device is connected to a network device through
       an IMA group interface, set the ATM interface type of the IMA group
       interface to NNI.
  4. Run [**quit**](cmdqueryname=quit)
     
     Exit from the serial interface view.