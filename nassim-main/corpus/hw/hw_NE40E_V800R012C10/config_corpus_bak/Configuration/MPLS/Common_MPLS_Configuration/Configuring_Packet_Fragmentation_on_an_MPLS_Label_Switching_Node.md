Configuring Packet Fragmentation on an MPLS Label Switching Node
================================================================

This section describes how to configure packet fragmentation on an MPLS P node.

#### Context

As the network scale expands and network complexity increases, devices of different specifications are deployed on the same network. In a scenario where the MTU set on the ingress PE is greater than the MRU set on the egress PE and the egress PE is configured to discard received packets whose length exceeds the MRU, if the MPLS label switching node is not configured with the fragmentation function, packets from the ingress PE are transparently transmitted to the egress PE and are discarded.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration task is supported only by the admin VS.



#### Prerequisites

Complete the following task:

* Configure MPLS functions.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**mpls fragment enable**](cmdqueryname=mpls+fragment+enable)
   
   
   
   MPLS fragmentation is enabled for the MPLS label switching node.
   
   
   
   The configuration takes effect only on MPLS packets that have no more than five labels and all inner labels are in the IPv4 format.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.