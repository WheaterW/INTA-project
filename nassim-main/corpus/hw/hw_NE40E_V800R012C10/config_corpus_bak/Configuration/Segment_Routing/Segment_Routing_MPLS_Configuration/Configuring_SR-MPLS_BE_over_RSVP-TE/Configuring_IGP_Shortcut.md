Configuring IGP Shortcut
========================

After IGP shortcut is configured on the ingress of an RSVP-TE tunnel, the associated LSP is not advertised to or used by neighbors.

#### Context

During path calculation in a scenario where IGP shortcut is configured, the device calculates an SPF tree based on the paths in the IGP physical topology, and then finds the SPF nodes on which shortcut tunnels are configured. If the metric of an RSVP-TE tunnel is smaller than that of an SPF node, the device replaces the outbound interfaces of the routes to this SPF node and those of the other routes passing through the SPF node with the RSVP-TE tunnel interface.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

IGP shortcut and forwarding adjacency cannot be both configured.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The tunnel interface view of the specified MPLS TE tunnel is displayed.
3. Run [**mpls te igp shortcut**](cmdqueryname=mpls+te+igp+shortcut) **isis** [ **hold-time** *interval* ]
   
   
   
   IGP shortcut is configured.
   
   
   
   **hold-time** *interval* specifies the period after which IGP responds to the Down status of a TE tunnel. If a TE tunnel goes Down but this parameter is not specified, routes are recalculated. If this parameter is specified, IGP responds to the Down status of the TE tunnel only when the delay period expires. Given that no other conditions trigger route recalculation during this delay, one of the following situations occurs:
   * If the TE tunnel goes Up after the delay, routes are not recalculated.
   * If the TE tunnel remains Down after the delay, routes are recalculated.
4. Run [**mpls te igp metric**](cmdqueryname=mpls+te+igp+metric) { **absolute** | **relative** } *value*
   
   
   
   An IGP metric is configured for the TE tunnel.
   
   
   
   When specifying a metric for the TE tunnel in path calculation through IGP shortcut, pay attention to the following points:
   
   * If the **absolute** parameter is configured, the metric of the TE tunnel is equal to the configured metric.
   * If the **relative** parameter is configured, the metric of the TE tunnel is the sum of the metric of the corresponding IGP path and the relative metric.
5. For IS-IS, run [**isis enable**](cmdqueryname=isis+enable) [ *process-id* ]
   
   
   
   The IS-IS process is enabled for the tunnel interface.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

If a network fault occurs, IGP re-convergence is performed. In this case, a transient forwarding status inconsistency may occur among nodes because of their different convergence rates, posing the risk of microloops. To avoid microloops, perform the following steps:![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before configuring microloop avoidance, [configure CR-LSP backup parameters](dc_vrp_te-p2p_cfg_0058.html).

* For IS-IS:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**isis**](cmdqueryname=isis) [ *process-id* ] command to create an IS-IS process and enter its view.
  3. Run the [**avoid-microloop te-tunnel**](cmdqueryname=avoid-microloop+te-tunnel) command to enable microloop avoidance for the IS-IS TE tunnel.
  4. (Optional) Run the [**avoid-microloop te-tunnel rib-update-delay**](cmdqueryname=avoid-microloop+te-tunnel+rib-update-delay) *rib-update-delay* command to configure a delay in delivering IS-IS routes whose outbound interface is a TE tunnel interface.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.