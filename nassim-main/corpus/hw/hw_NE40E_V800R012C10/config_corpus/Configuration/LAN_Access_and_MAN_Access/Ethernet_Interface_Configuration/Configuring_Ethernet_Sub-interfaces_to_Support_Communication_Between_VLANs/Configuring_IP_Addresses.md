Configuring IP Addresses
========================

To implement communication between VLANs, establish IP routes.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=ip+address+sub) *interface-type interface-number.subinterface-number*
   
   
   
   The view of the Ethernet sub-interface that needs to be configured with an IP address is displayed.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ]
   
   
   
   An IP address is configured for the Ethernet sub-interface.
   
   If two or more IP addresses are configured for an Ethernet sub-interface, the keyword **sub** can be used to indicate the IP addresses configured after the first one.
   
   For the detailed configuration of an IP address, see *NE40E-M2 Configuration Guide - IP Service*.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the scenario where an interface has a large number of sub-interfaces, if you run the [**shutdown**](cmdqueryname=shutdown) command in the sub-interface view to shut down the sub-interfaces one after another, the work load is huge. In this case, you can shut down the sub-interfaces in batches by running the [**shutdown interface**](cmdqueryname=shutdown+interface) command in the system view.