Directing Multicast Traffic into a P2MP TE Tunnel
=================================================

Multicast data traffic can be correctly forwarded over a point-to-multipoint (P2MP) traffic engineering (TE) tunnel only after being directed into the P2MP TE tunnel.

#### Context

When a P2MP TE tunnel is used to carry multicast services, you do not need to deploy the Protocol Independent Multicast (PIM) on the transit nodes of the tunnel. As a result, you must direct multicast traffic on a P2MP tunnel interface of the ingress on the P2MP TE tunnel into the P2MP TE tunnel.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The tunnel interface view is displayed.
3. Run [**igmp static-group**](cmdqueryname=igmp+static-group) *group-address* [ **inc-step-mask** { *group-mask* | *group-mask-length* } **number** *group-number* ] [ **source** *source-address* ]
   
   
   
   The interface is configured to statically join an IGMP group.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.