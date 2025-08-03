Configuring an IP Address for an Interface
==========================================

This section describes how to configure an IP address for a device so that the device can communicate with other devices on the network.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* [ .*subinterface-number* ]
   
   
   
   The interface view is displayed.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ]
   
   
   
   An IP address is configured for the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.