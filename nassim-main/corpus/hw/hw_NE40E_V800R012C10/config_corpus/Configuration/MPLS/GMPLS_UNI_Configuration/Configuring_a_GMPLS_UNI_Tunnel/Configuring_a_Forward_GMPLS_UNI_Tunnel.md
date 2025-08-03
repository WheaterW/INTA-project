Configuring a Forward GMPLS UNI Tunnel
======================================

A GMPLS UNI tunnel is unidirectional. A forward GMPLS UNI tunnel and a reverse GMPLS UNI tunnel must be established to implement bidirectional traffic transmission. The ingress EN initiates tunnel establishment requests containing tunnel attributes. Therefore, basic tunnel attributes and functions must be configured on the ingress EN.

#### Context

Forward and reverse UNI-LSPs are established for bidirectional GMPLS UNI tunnels and have the same requirements on traffic engineering. A GMPLS UNI tunnel is established using extended RSVP-TE. The ingress EN initiates tunnel establishment requests containing tunnel attributes by sending Path messages. Therefore, tunnel attributes and functions need to be configured on the ingress EN and do not need to be configured on the egress EN for a reverse GMPLS UNI tunnel.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**gmpls-tunnel**](cmdqueryname=gmpls-tunnel) *gmpls-tunnel-name*
   
   
   
   A GMPLS UNI tunnel is established, and the tunnel view is displayed.
3. Run [**tunnel-id**](cmdqueryname=tunnel-id) *tunnel-id*
   
   
   
   The tunnel ID is configured.
4. Run [**destination**](cmdqueryname=destination) *ip-address*
   
   
   
   A destination IP address is set for the GMPLS UNI tunnel. Generally, the LSR ID of the sink C node is set as the destination IP address.
5. Run [**bandwidth**](cmdqueryname=bandwidth) *bw-value*
   
   
   
   The bandwidth is configured for the GMPLS UNI tunnel.
6. Run [**explicit-path**](cmdqueryname=explicit-path) *path-name*
   
   
   
   Explicit path constraints are configured.
7. Run [**switch-type**](cmdqueryname=switch-type+dcsc+evpl) { **dcsc** | **evpl** }
   
   
   
   A data switching type is set for a GMPLS UNI tunnel.
8. Run [**bind interface**](cmdqueryname=bind+interface) *interface-type* *interface-number*
   
   
   
   A GMPLS UNI tunnel interface is bound to a service interface.
   
   Only a local GMPLS UNI can function as a service interface.
9. (Optional) Run [**link protection-type**](cmdqueryname=link+protection-type+unprotected) **unprotected**
   
   
   
   The link protection function is configured for the GMPLS UNI tunnel.
   
   If PCE path calculation is configured, this command does not need to be run. This is because the device forcibly sets the protection type to rerouting for PCE path calculation.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.