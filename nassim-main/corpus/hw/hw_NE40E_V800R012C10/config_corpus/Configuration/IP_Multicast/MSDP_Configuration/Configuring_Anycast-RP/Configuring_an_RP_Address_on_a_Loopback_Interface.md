Configuring an RP Address on a Loopback Interface
=================================================

Before configuring Anycast-Rendezvous Point (RP) on Routers in a PIM-SM domain, specify a loopback interface on each Router and assign the same IP address to the loopback interfaces. In addition, configure the Routers to advertise the RP address through unicast routes to ensure that each Router has a reachable route to the RPs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The loopback interface view is displayed.
   
   
   
   In Anycast-RP, multiple RPs need to use the same IP address on a network. Therefore, configuring loopback interfaces as RPs is recommended.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
   
   
   
   The loopback interface address, that is, the RP address, is configured.
4. (Optional) Run [**pim sm**](cmdqueryname=pim+sm)
   
   
   
   PIM-SM is enabled on the RP interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Run this command before configuring Candidate-Rendezvous Points (C-RPs). If a static RP is used, this command is not required.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.