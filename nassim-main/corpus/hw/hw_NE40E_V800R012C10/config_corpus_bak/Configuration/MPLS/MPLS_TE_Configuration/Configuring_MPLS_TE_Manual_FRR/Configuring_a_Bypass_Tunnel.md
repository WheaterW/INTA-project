Configuring a Bypass Tunnel
===========================

A path and attributes must be configured for a bypass tunnel after TE manual FRR is enabled on a PLR.

#### Context

Bypass tunnels are established on selected links or nodes that are not on the protected primary tunnel. If a link or node on the protected primary tunnel is used for a bypass tunnel and fails, the bypass tunnel also fails to protect the primary tunnel.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* TE FRR does not take effect if multiple nodes or links fail simultaneously. After FRR switching is performed to switch data from the primary tunnel to a bypass tunnel, the bypass tunnel must remain Up when forwarding data. If the bypass tunnel goes Down, the protected traffic is interrupted, and FRR fails. Even though the bypass tunnel goes Up again, traffic is unable to flow through the bypass tunnel but travels through the primary tunnel after the primary tunnel recovers or is reestablished.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The view of the bypass tunnel interface is displayed.
3. Run [**tunnel-protocol mpls te**](cmdqueryname=tunnel-protocol+mpls+te)
   
   
   
   MPLS TE is configured.
4. Run [**destination**](cmdqueryname=destination) *ip-address*
   
   
   
   The LSR ID of an MP is configured as the destination address of the bypass tunnel.
5. Run [**mpls te tunnel-id**](cmdqueryname=mpls+te+tunnel-id) *tunnel-id*
   
   
   
   The bypass tunnel ID is configured.
6. Run [**mpls te bypass-tunnel**](cmdqueryname=mpls+te+bypass-tunnel)
   
   
   
   A bypass tunnel is configured.
7. Run [**mpls te protected-interface**](cmdqueryname=mpls+te+protected-interface) *interface-type* *interface-number*
   
   
   
   The interface to be protected by the bypass tunnel is specified.
8. (Optional) Run [**mpls te path explicit-path**](cmdqueryname=mpls+te+path+explicit-path) *path-name* [ **secondary** ]
   
   
   
   An explicit path is configured for the bypass tunnel.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Physical links of a bypass tunnel cannot overlap protected physical links of the primary tunnel.
9. (Optional) Run [**mpls te bandwidth**](cmdqueryname=mpls+te+bandwidth) **ct0** *bandwidth*
   
   
   
   Bandwidth is configured for the bypass tunnel.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Follow-up Procedure

Routes and labels are automatically recorded after a bypass tunnel is configured.

When a tunnel is specified to protect a physical interface, the corresponding LSP becomes the bypass LSP. A bypass tunnel is established over a configured explicit path on the PLR.

If a primary tunnel fails, traffic switches to a bypass tunnel. If the bypass tunnel goes Down, the protected traffic is interrupted, and FRR fails. Even though the bypass tunnel goes Up, traffic cannot be forwarded. Traffic will be forwarded only after the primary tunnel has been restored or re-established.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The [**mpls te fast-reroute**](cmdqueryname=mpls+te+fast-reroute) command and the [**mpls te bypass-tunnel**](cmdqueryname=mpls+te+bypass-tunnel) command cannot be configured on the same tunnel interface.
* After FRR switches traffic from a primary tunnel to a bypass tunnel, the bypass tunnel must be kept Up, and its path must remain unchanged when transmitting traffic. If the bypass tunnel goes Down, the protected traffic is interrupted, and FRR fails.