(Optional) Configuring LDP MTU Signaling
========================================

LDP MTU signaling can be configured to allow sent Label Mapping messages to carry MTU TLVs.

#### Context

If the MTU value of a packet exceeds the maximum size supported by a receiver or transit device, the packet is fragmented during transmission, increasing the workload of the network. The packet may even be discarded during transmission, affecting services. If MTU values are correctly negotiated before packet transmission, packets can successfully reach the receiver without packet fragmentation and reassembly.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**mtu-signalling**](cmdqueryname=mtu-signalling+apply-tlv) [ **apply-tlv** ]
   
   
   
   The node is enabled to send Label Mapping message carrying MTU TLVs.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.