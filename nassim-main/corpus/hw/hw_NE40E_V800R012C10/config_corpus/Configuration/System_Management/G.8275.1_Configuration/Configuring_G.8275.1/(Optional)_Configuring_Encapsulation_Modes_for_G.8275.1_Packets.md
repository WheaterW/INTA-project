(Optional) Configuring Encapsulation Modes for G.8275.1 Packets
===============================================================

You can configure destination MAC addresses of packets according to the actual networking.

#### Prerequisites

G.8275.1 packets can be encapsulated only in Layer 2 multicast MAC encapsulation mode.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In G.8275.1 mode, the **ptp mac-egress** command does not support setting of VLAN parameters.



#### Context

Perform the following operations on the T-BC:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ptp mac-egress**](cmdqueryname=ptp+mac-egress) **destination-mac** *destination-mac*
   
   
   
   The G.8275.1 packets to be sent from the interface are encapsulated in multicast MAC encapsulation mode, and a destination multicast MAC address is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.