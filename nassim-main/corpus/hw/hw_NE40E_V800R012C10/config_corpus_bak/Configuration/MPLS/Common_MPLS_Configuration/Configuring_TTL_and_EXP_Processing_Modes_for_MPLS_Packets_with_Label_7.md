Configuring TTL and EXP Processing Modes for MPLS Packets with Label 7
======================================================================

This section describes how to configure the mode of handling the TTL and EXP fields carried in MPLS packets with label 7 on the egress PE.

#### Prerequisites

When MPLS packets with label 7 are sent out of a public network, the mode of handling TTL and EXP fields can be set to **uniform** or **pipe**.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration task is supported only by the admin VS.

Complete the following task:

* Configure MPLS functions.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**entropy-label ttl-mode**](cmdqueryname=entropy-label+ttl-mode+uniform+pipe) { **uniform** | **pipe** }
   
   
   
   A mode of handling the TTL field in MPLS packets with label 7 is set.
   
   
   
   * **uniform**: The egress reduces the MPLS TTL by one, compares it with the IP TTL, and propagates the smaller value to the IP TTL field before forwarding the packet.
   * **pipe**: The egress reduces the IP TTL by one, without propagating the MPLS TTL to the IP TTL.
4. Run [**entropy-label exp-mode**](cmdqueryname=entropy-label+exp-mode+uniform+pipe) { **uniform** | **pipe** }
   
   
   
   A mode of handling the EXP field in MPLS packets with label 7 is set.
   
   
   
   * **uniform**: The egress PE copies the EXP value in an MPLS packet to the EXP field in the IP or inner packet.
   * **pipe**: The egress PE does not copy the EXP value in an MPLS packet to the EXP field in the IP or inner packet.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.