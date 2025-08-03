Configuring the Loopback Function for an E1 Interface
=====================================================

This section describes how to configure the loopback function on a channelized E1 interface. The loopback function is used to check the interface or cable status. In normal situations, the loopback function is disabled.

#### Context

The loopback function has two types:

* Local loopback: is used to locate a system fault.
* Remote loopback: is used to locate a link fault or test the quality of a link.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* To enable local loopback on an E1 interface, ensure that the clock of the E1 interface works in master mode.
* To enable remote loopback on an E1 interface, ensure that the clock of the E1 interface works in slave mode.

This configuration process is supported only on the Admin-VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**controller e1**](cmdqueryname=controller+e1) *controller-number*
   
   
   
   The E1 interface view is displayed.
3. Run [**loopback**](cmdqueryname=loopback) { **local** | **remote** } [ **autoclear** **period** *hold-time* ]
   
   
   
   The loopback function is enabled on the E1 interface.
   
   To enable the E1 interface to delete the loopback configuration after a specified period, specify **autoclear** **period** *hold-time* in the command. This function takes effect when loopback is enabled. After the time specified by *hold-time* elapses, the loopback configuration is automatically deleted.
4. Restart the E1 interface.
   1. Run [**shutdown**](cmdqueryname=shutdown)
      
      
      
      The interface is disabled.
   2. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   3. Run [**undo shutdown**](cmdqueryname=undo+shutdown)
      
      
      
      The interface is enabled.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the configuration is complete, the configuration takes effect only after the interface is restarted.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.