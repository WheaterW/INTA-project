Configuring the Processing Mode for Non-NAT Service Packets
===========================================================

Non-NAT service packets distributed to a service board can be either discarded or transparently transmitted.

#### Context

By default, service boards transparently transmit received non-NAT service packets, such as the packets containing only IP headers. Considering network security, however, you may hope not to forward such non-NAT service packets. Then you can configure the device to discard non-NAT service packets.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.


![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only [dedicated boards](dc_ne_nat_feature_0008.html#EN-US_CONCEPT_0172359138__li1033371595) support this configuration.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat pure-ip-packet drop**](cmdqueryname=nat+pure-ip-packet+drop)
   
   
   
   The device is configured to discard the IP packets that are not NATed after being distributed to the service board.
   
   
   
   After this command is run, some IP packets that are distributed to the service board without the need for matching the NAT policy are discarded based on the packet type.
3. Run [**nat session-miss mode drop**](cmdqueryname=nat+session-miss+mode+drop)
   
   
   
   The device is configured to discard non-NAT service packets.
   
   
   
   After this command is run, some IP packets that are distributed to the service board without the need for matching the NAT policy are discarded based on the packet type.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.