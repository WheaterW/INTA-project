Configuring an IP Addresses for an Interface
============================================

The IP address assigned to an interface needs to be in the same network segment with the IP addresses of the users of all the VLANs associated to this interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* [ .*subinterface-number* ]
   
   
   
   The view of the interface on which proxy ARP between VLANs needs to be configured is displayed.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ]
   
   
   
   An IP address is configured for the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.