Configuring VLANIF Interfaces for Inter-VLAN Communication
==========================================================

Configuring VLANIF interfaces for inter-VLAN communication saves expenditure and helps implement fast forwarding.

#### Context

VLANIF interfaces are Layer 3 logical interfaces. After being assigned IP addresses, VLANIF interfaces are able to communicate at the network layer. Layer 3 switches and routers can be configured with VLANIF interfaces.

By using VLANIF interfaces to implement inter-VLAN communication, you need to configure a VLANIF interface for each VLAN and assign an IP address to each VLANIF interface. The communication process by using VLANIF interfaces is similar to that by using sub-interfaces.

**Figure 1** Configuring VLANIF interfaces for inter-VLAN communication  
![](figure/en-us_image_0000001671870705.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

The default gateway address of each PC in a VLAN must be the IP address of the corresponding VLANIF interface. Otherwise, inter-VLAN communication will fail.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **vlanif** *vlan-id*
   
   
   
   A VLANIF interface is created, and its view is displayed.
   
   
   
   The VLAN ID specified in this command must be the ID of an existing VLAN.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A VLANIF interface is up only when at least one physical port added to the corresponding VLAN is up.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ]
   
   
   
   An IP address is assigned to the VLANIF interface.
   
   
   
   VLANIF interfaces must belong to different network segments.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.