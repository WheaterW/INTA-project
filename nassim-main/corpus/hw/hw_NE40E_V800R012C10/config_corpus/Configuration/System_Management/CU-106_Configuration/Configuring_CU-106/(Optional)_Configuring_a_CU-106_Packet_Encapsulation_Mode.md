(Optional) Configuring a CU-106 Packet Encapsulation Mode
=========================================================

You can configure destination MAC addresses of packets according to the actual networking.

#### Prerequisites

CU-106 packets can be encapsulated only in Layer 2 multicast MAC encapsulation mode.


#### Context

Perform the following steps on each T-BC:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ptp mac-egress**](cmdqueryname=ptp+mac-egress) **destination-mac** *destination-mac*
   
   
   
   The multicast MAC encapsulation mode is configured for packets to be sent from the interface, and a destination MAC address is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.