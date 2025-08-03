Enabling an Interface
=====================

Physical interfaces on a device are initialized and started when the device is powered on.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration process is supported only by the admin VS.



#### Procedure

* By default, interfaces are started.
* If an interface is shut down, perform the following steps to start the interface:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**undo shutdown**](cmdqueryname=undo+shutdown)
     
     
     
     The interface is started.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.