Configuring Manual FRR for a Manually Configured P2MP TE Tunnel
===============================================================

Manual FRR can be configured on the tunnel interface of a manually configured P2MP TE tunnel.

#### Context

The process of configuring P2MP TE FRR is identical to that for configuring P2P TE FRR, which includes the following two procedures:

* [Enable the P2MP TE FRR function on the tunnel interface of the primary tunnel.](#EN-US_TASK_0172368213__steps-unordered_0368E8DC)
* [Configure a bypass tunnel on the point of local repair (PLR) node and bind the bypass tunnel to the primary tunnel.](#EN-US_TASK_0172368213__steps-unordered_0368FC64)

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Manual P2MP TE FRR only applies to manual P2MP TE tunnels.




#### Procedure

* Enable the P2MP TE FRR function on the tunnel interface of the primary tunnel (P2MP TE tunnel).
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
     
     
     
     The MPLS TE tunnel interface view is displayed.
  3. Run [**mpls te fast-reroute**](cmdqueryname=mpls+te+fast-reroute) [ **bandwidth** ]
     
     
     
     TE FRR is enabled.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     You can run the [**mpls te bypass-attributes**](cmdqueryname=mpls+te+bypass-attributes) command to configure bypass tunnel attributes only after running the [**mpls te fast-reroute**](cmdqueryname=mpls+te+fast-reroute) **bandwidth** command.
  4. (Optional) Run [**mpls te bypass-attributes**](cmdqueryname=mpls+te+bypass-attributes)
     
     
     
     Bypass tunnel attributes are configured.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a bypass tunnel on the PLR node and bind the bypass tunnel to the primary tunnel.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
     
     
     
     The tunnel interface view of a bypass tunnel is displayed.
  3. Run [**tunnel-protocol mpls te**](cmdqueryname=tunnel-protocol+mpls+te)
     
     
     
     MPLS TE is configured as the tunnel protocol.
  4. Run [**destination**](cmdqueryname=destination) *ip-address*
     
     
     
     The LSR ID of a merge point (MP) is specified as the destination address of the bypass tunnel.
  5. Run [**mpls te tunnel-id**](cmdqueryname=mpls+te+tunnel-id) *tunnel-id*
     
     
     
     The bypass tunnel ID is specified.
  6. (Optional) Run [**mpls te path explicit-path**](cmdqueryname=mpls+te+path+explicit-path) *path-name*
     
     
     
     An explicit path is specified for the bypass tunnel.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The explicit path planned for the bypass tunnel and the primary tunnel path to be protected must use different physical links.
  7. (Optional) Run [**mpls te bandwidth**](cmdqueryname=mpls+te+bandwidth) **ct0** *bandwidth*
     
     
     
     The bypass tunnel bandwidth is configured.
  8. Run [**mpls te bypass-tunnel**](cmdqueryname=mpls+te+bypass-tunnel)
     
     
     
     A bypass tunnel is configured.
  9. Run [**mpls te protected-interface**](cmdqueryname=mpls+te+protected-interface) *interface-type* *interface-number*
     
     
     
     A link interface to be protected by a bypass tunnel is specified.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.