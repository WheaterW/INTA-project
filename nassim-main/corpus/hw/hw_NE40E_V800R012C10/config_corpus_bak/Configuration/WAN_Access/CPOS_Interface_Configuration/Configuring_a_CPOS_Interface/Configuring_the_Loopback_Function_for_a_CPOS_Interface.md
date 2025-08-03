Configuring the Loopback Function for a CPOS Interface
======================================================

This section describes how to configure the loopback function on a channelized packet over SONET/SDH (CPOS) interface. Here, SONET stands for synchronous optical network, and SDH stands for synchronous digital hierarchy. The loopback function is used to check interface or cable status when devices are malfunctioning and must be disabled when devices are working properly.

#### Context

The loopback function has two types:

* Local loopback: is used to locate a system fault.
* Remote loopback: is used to locate a link fault or test the quality of a link.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* To enable local loopback on a CPOS interface, ensure that the clock of the CPOS interface works in master mode.

This configuration process is supported only on the Admin-VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
   
   
   
   The CPOS interface view is displayed.
3. Run [**loopback**](cmdqueryname=loopback) { **local** | **remote** } [ **autoclear** **period** *hold-time* ]
   
   
   
   The loopback function is enabled on the CPOS interface.
   
   To enable the CPOS interface to delete the loopback configuration after a specified period, specify **autoclear** **period** *hold-time* in the command. This function takes effect when loopback is enabled. After the time specified by *hold-time* elapses, the loopback configuration is automatically deleted.
   
   
   
   By default, the loopback function is disabled on a CPOS interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.