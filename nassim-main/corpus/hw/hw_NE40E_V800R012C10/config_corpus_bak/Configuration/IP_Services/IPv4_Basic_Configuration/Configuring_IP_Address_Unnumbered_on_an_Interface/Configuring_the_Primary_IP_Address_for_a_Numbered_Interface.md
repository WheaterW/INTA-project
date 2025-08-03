Configuring the Primary IP Address for a Numbered Interface
===========================================================

Only the primary IP address of an interface can be borrowed.

#### Context

Configuring IP address unnumbered saves IP address resources. You can configure an interface that is occasionally used to borrow an IP address, instead of configuring a new IP address for the interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the numbered interface is displayed.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **tag** *tag-value* ]
   
   
   
   A primary IP address is configured for the numbered interface.
   
   The IP address of a numbered interface can be configured using the [**ip address**](cmdqueryname=ip+address) command or obtained through negotiation.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.