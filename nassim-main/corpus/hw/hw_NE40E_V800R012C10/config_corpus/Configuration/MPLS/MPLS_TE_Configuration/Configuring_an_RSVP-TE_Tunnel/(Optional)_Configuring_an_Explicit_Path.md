(Optional) Configuring an Explicit Path
=======================================

An explicit path is configured on the ingress of an MPLS TE tunnel. It defines the nodes through which the MPLS TE tunnel must pass or the nodes that are excluded from the MPLS TE tunnel.

#### Context

An explicit path consists of a series of nodes. These nodes are arranged in sequence and form a vector path. An interface IP address on every node is used to identify the node on an explicit path. The loopback IP address of the egress node is usually used as the destination address of an explicit path.

Two adjacent nodes on an explicit path are connected in either of the following modes:

* Strict: A hop is directly connected to its next hop.
* Loose: Other nodes may exist between a hop and its next hop.

The strict and loose modes are used either separately or simultaneously.

TE tunnels are classified as intra-area tunnels and inter-area tunnels. In this situation, areas indicate OSPF and IS-IS areas, but not an autonomous system (AS) running the Border Gateway Protocol (BGP). OSPF areas are differentiated by area IDs, whereas IS-IS areas are differentiated by levels.

* Intra-area tunnel: is a TE tunnel in a single OSPF or IS-IS area. An intra-area tunnel can be established over a strict or loose explicit path.
* Inter-area tunnel: is a TE tunnel traversing multiple OSPF or IS-IS areas. An explicit path must be used to establish an inter-area TE tunnel and an ABR or an Autonomous System Boundary Router (ASBR) must be included in the explicit path.

The explicit path in use can be updated.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**explicit-path**](cmdqueryname=explicit-path) *path-name*
   
   
   
   An explicit path is created, and the explicit path view is displayed.
3. Run [**next hop**](cmdqueryname=next+hop) *ip-address* [ **include** [ [ **strict** | **loose** ] | [ **incoming** | **outgoing** ] ] \* | **exclude** ]
   
   
   
   The next-hop address is specified for the explicit path.
   
   
   
   The **include** parameter indicates that the tunnel passes through a specified node; the **exclude** parameter indicates that the tunnel does not pass through a specified node.
4. (Optional) Run [**add hop**](cmdqueryname=add+hop) *ip-address1* [ **include** [ [ **strict** | **loose** ] | [ **incoming** | **outgoing** ] ] \* | **exclude** ] { **after** | **before** } *ip-address2*
   
   
   
   A node is added to the explicit path.
5. (Optional) Run [**modify hop**](cmdqueryname=modify+hop) *ip-address1* *ip-address2* [ **include** [ [ **strict** | **loose** ] | [ **incoming** | **outgoing** ] ] \* | **exclude** ]
   
   
   
   The node addresses of the explicit path are changed.
6. (Optional) Run [**delete hop**](cmdqueryname=delete+hop) *ip-address*
   
   
   
   A node is excluded from an explicit path.
7. (Optional) Run [**list hop**](cmdqueryname=list+hop) [ *ip-address* ]
   
   
   
   Information about nodes on the explicit path is displayed.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.