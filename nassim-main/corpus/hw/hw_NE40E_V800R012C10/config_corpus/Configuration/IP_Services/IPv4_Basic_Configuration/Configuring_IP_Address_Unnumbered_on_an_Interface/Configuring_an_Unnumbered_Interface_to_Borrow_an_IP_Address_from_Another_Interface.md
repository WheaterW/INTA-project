Configuring an Unnumbered Interface to Borrow an IP Address from Another Interface
==================================================================================

An Ethernet interface can borrow the IP address of another interface.

#### Context

Configuring IP address unnumbered saves IP address resources. You can configure an interface that is occasionally used to borrow an IP address, instead of configuring a new IP address for the interface.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configuration procedure described in this section involves only configuring an interface to borrow an IP address. An unnumbered interface cannot run dynamic routing protocols because it does not have an IP address itself. As such, the interface must have a default route or a dynamically learned route. If the interface does not have such a route, to enable the interface to communicate with a remote device, you must manually configure a static route to the network segment of the remote device.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the unnumbered interface is displayed.
3. Run [**ip address unnumbered**](cmdqueryname=ip+address+unnumbered+interface) **interface** *interface-type* *interface-number*
   
   
   
   The unnumbered interface is configured to borrow an IP address from a specified interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.