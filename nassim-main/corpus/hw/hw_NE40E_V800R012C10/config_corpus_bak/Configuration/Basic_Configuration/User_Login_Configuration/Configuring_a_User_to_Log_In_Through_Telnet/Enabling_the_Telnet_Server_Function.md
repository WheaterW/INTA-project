Enabling the Telnet Server Function
===================================

Before a user terminal establishes a Telnet connection with a device, log in to the device through the console port to enable the Telnet server function on the device. You can then use Telnet to remotely log in to the device.

#### Context

Perform the following steps on the device to be used as a Telnet server as required:


#### Procedure

* Enable the Telnet IPv4 server function.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**telnet server enable**](cmdqueryname=telnet+server+enable)
     
     The Telnet IPv4 server function is enabled.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Enable the Telnet IPv6 server function.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**telnet**](cmdqueryname=telnet) **ipv6 server enable**
     
     The Telnet IPv6 server function is enabled.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If you disable the Telnet server function on a device, the established Telnet connections are not interrupted but new Telnet connections are denied. In this situation, you can log in to the device only by using SSH or through the console port.