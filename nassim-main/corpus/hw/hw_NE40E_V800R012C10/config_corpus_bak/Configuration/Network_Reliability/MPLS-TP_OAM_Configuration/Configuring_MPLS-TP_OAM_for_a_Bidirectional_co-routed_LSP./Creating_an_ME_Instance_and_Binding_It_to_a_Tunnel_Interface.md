Creating an ME Instance and Binding It to a Tunnel Interface
============================================================

This section describes how to create a ME instance and bind it to a tunnel interface. This is a prerequisite for configuring MPLS-TP OAM for LSP.

#### Context

RSVP tunnels for transmitting TE services are unidirectional, and TE services are transmitted only from the ingress to the egress of a tunnel. To transmit TE services from the egress to the ingress of an RSVP tunnel, you can only use a route to forward the services, but that may cause network congestion. Additionally, if a path from the egress to the ingress is also configured as an RSVP tunnel, two tunnels are established between the ingress and egress. When one tunnel fails, the other tunnel cannot be notified of the fault. As a result, services will be interrupted. To resolve the preceding issue, configure a bidirectional LSP.

Static bidirectional co-routed LSP: A static bidirectional co-routed LSP is similar to two LSPs in opposite directions. A static bidirectional co-routed LSP, however, is only one LSP. It is mapped to two forwarding entries for traffic in opposite directions and goes up only when both forwarding entries are available. If the conditions for forwarding traffic in one direction are not met, the LSP is in the down state. The two forwarding entries are associated with each other. When the IP forwarding capability is unavailable, any intermediate node can send back a response packet along the original path.

Static bidirectional co-routed LSP supported by MPLS-TP can be monitored using MPLS-TP OAM. A MEG corresponds to a static bidirectional LSP and includes only one ME. The ingress and egress of the LSP are configured as MEPs.

Two P2P LSPs in opposite directions are set up over a bidirectional co-routed transport path in an MEG. This means that there is a single LSP in both directions between an MEP and its RMEP. A single ME operates along this P2P LSP.

Perform the following steps on the local MEP and its RMEP:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**mpls-tp channel-type**](cmdqueryname=mpls-tp+channel-type) {**0x7ffa** | **0x8902** }
   
   
   
   An ACH label value is specified.
3. Run [**mpls-tp meg**](cmdqueryname=mpls-tp+meg) *meg-name*
   
   
   
   A MEG is created, and the MEG view is displayed.
4. Run [**me te interface**](cmdqueryname=me+te+interface) *interface-type* *interface-number* **mep-id** *mep-id* **remote-mep-id** *remote-mep-id*
   
   
   
   An ME instance is created and is bound to a bidirectional co-routed LSP.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.