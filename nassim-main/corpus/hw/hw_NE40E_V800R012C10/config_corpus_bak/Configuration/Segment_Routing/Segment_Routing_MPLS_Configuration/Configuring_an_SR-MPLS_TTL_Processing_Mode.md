Configuring an SR-MPLS TTL Processing Mode
==========================================

SR-MPLS supports both uniform and pipe modes for TTL processing.

#### Context

When IP packets pass through an MPLS network, the TTL fields in an MPLS packet transmitted over an SR-MPLS public network tunnel are processed in either of the following modes:

* Uniform mode: The ingress decrements the IP TTL by 1 and maps it to the MPLS TTL field. Then, the packet is processed in standard TTL processing mode on the MPLS network. After receiving the packet, the egress decrements the MPLS TTL by 1, compares it with the IP TTL, and then maps the smaller of these two values to the IP TTL field.
* Pipe mode: The ingress decrements the IP TTL by 1 and sets the MPLS TTL to a fixed value. Then, the packet is processed in standard TTL processing mode on the MPLS network. After receiving the packet, the egress decrements the IP TTL by 1. To summarize, the IP TTL in a packet passing through an MPLS network is decremented by 1 only on the ingress and egress, regardless of how many hops exist between the ingress and egress.

This configuration applies to SR-MPLS BE and SR-MPLS TE tunnels as well as SR-MPLS TE Policies.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**mpls**](cmdqueryname=mpls) command to enter the MPLS view.
3. Run the [**mpls sr ttl-mode**](cmdqueryname=mpls+sr+ttl-mode) { **pipe** | **uniform** } command to configure a TTL processing mode for SR-MPLS tunnels established based on node labels.
4. Run the [**mpls sr adjacency ttl-mode**](cmdqueryname=mpls+sr+adjacency+ttl-mode) { **pipe** | **uniform** } command to configure a TTL processing mode for SR-MPLS tunnels established based on adjacency labels.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.