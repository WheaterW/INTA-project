Configuring the TTL and EXP Processing Mode When the Explicit Null Label Is Used
================================================================================

This section describes how to configure the TTL and EXP processing mode when the explicit null label is used.

#### Context

If the explicit null label and the **uniform** mode are configured, an egress PE copies the TTL and EXP values to the IP or inner packets before forwarding them out of a public network. If the explicit null label and the **pipe** mode are configured, an egress PE does not copy the TTL or EXP values to the IP or inner packets.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration task is supported only by the admin VS.



#### Prerequisites

Complete the following tasks:

* Configure MPLS functions.
* Configure the egress PE to assign the explicit null label upstream.

#### Precautions

The configuration takes effect only on the egress PE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**label advertise explicit-null**](cmdqueryname=label+advertise+explicit-null)
   
   
   
   The egress PE is enabled to assign the explicit null label upstream.
4. Run [**explicit-null-label ttl-mode**](cmdqueryname=explicit-null-label+ttl-mode+uniform+pipe) { **uniform** | **pipe** }
   
   
   
   The mode used by the egress PE to process TTL values is configured.
   
   
   
   **uniform**: The egress PE copies the TTL value in an MPLS packet to the TTL field in the IP or inner packet.
   
   
   
   **pipe**: The egress PE does not copy the TTL value in an MPLS packet to the TTL field in the IP or inner packet.
5. Run [**explicit-null-label exp-mode**](cmdqueryname=explicit-null-label+exp-mode+uniform+pipe) { **uniform** | **pipe** }
   
   
   
   The mode used by the egress PE to process EXP values is configured.
   
   
   
   **uniform**: The egress PE copies the EXP value in an MPLS packet to the EXP field in the IP or inner packet.
   
   
   
   **pipe**: The egress PE does not copy the EXP value in an MPLS packet to the EXP field in the IP or inner packet.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.