Configuring FRR for Automatic P2MP TE Tunnels
=============================================

Auto P2MP TE FRR is configured in a P2MP TE template for automatic P2MP TE tunnels.

#### Context

The process of configuring FRR for automatic P2MP TE tunnels is as follows:

* [Configure the ingress.](#EN-US_TASK_0172368214__step_01)
* [Configure a bypass tunnel on the PLR and bind it to the primary tunnel.](#EN-US_TASK_0172368214__step_02)


#### Procedure

* Configure the ingress.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls te p2mp-template**](cmdqueryname=mpls+te+p2mp-template) *template-name*
     
     
     
     A P2MP tunnel template is created, and the MPLS TE P2MP template view is displayed.
  3. Run [**fast-reroute**](cmdqueryname=fast-reroute) [ **bandwidth** ]
     
     
     
     P2MP TE FRR is enabled.
     
     
     
     The **bandwidth** parameter enables bandwidth protection for the primary tunnel. A bypass tunnel is selected to provide bandwidth protection for the primary tunnel.
  4. (Optional) Run [**bypass-attributes**](cmdqueryname=bypass-attributes) { **bandwidth** *bandwidth* | **priority** *setup-priority* [ *hold-priority* ] } \*
     
     
     
     Attributes for the FRR bypass tunnel are set.
     
     The **bandwidth** parameter sets the bandwidth for the bypass tunnel. The **priority** parameter sets the holding and setup priority values for the bypass tunnel.
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