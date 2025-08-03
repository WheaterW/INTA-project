Enabling PIM BFD
================

Enable PIM BFD on the devices that set up PIM neighbor relationships.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

PIM BFD applies to non-broadcast multiple access (NBMA) interfaces and broadcast interfaces, not MTunnel interfaces.

Perform the following steps on PIM Routers that set up neighbor relationships:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**pim bfd enable**](cmdqueryname=pim+bfd+enable)
   
   
   
   PIM BFD is enabled.