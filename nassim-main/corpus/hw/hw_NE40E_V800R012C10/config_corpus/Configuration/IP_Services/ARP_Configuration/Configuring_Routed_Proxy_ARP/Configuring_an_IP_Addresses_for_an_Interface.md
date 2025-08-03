Configuring an IP Addresses for an Interface
============================================

The IP address assigned to a routed proxy ARP-enabled interface must be on the same network segment with the IP address of the host on the LAN to which this interface connects.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* [ .*subinterface-number* ] *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ]
   
   
   
   An IP address is configured for the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.