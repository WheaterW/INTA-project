Configuring IGP Shortcut
========================

After IGP shortcut is configured on the ingress of a CR-LSP, the CR-LSP is not advertised to or used by neighbors.

#### Context

During path calculation in a scenario where IGP shortcut is configured, the device calculates an SPF tree based on the paths in the IGP physical topology, and then finds the SPF nodes on which shortcut tunnels are configured. If the metric of a TE tunnel is smaller than that of an SPF node, the device replaces the outbound interfaces of the routes to this SPF node and those of the other routes passing through the SPF node with the TE tunnel interface.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

IGP shortcut and forwarding adjacency cannot be both configured.

Before configuring IGP shortcut in an LDP over TE scenario, you need to set up a remote LDP session. If no remote LDP session is established, traffic is steered to a TE tunnel, and traffic forwarding is interrupted.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The view of the MPLS TE tunnel interface is displayed.
3. Run [**mpls te igp shortcut**](cmdqueryname=mpls+te+igp+shortcut) [ **isis** | **ospf** ] or [**mpls te igp shortcut**](cmdqueryname=mpls+te+igp+shortcut) **isis** **hold-time** *interval*
   
   
   
   IGP shortcut is configured.
   
   **hold-time** *interval* specifies the period after which IS-IS responds to the Down status of the TE tunnel.
   
   If a TE tunnel goes Down and this parameter is not specified, IS-IS recalculates routes. If this parameter is specified, IS-IS responds to the Down status of the TE tunnel after only the specified interval elapses. It either recalculates routes or not depending on the TE tunnel status:
   * If the TE tunnel goes Up, IS-IS does not recalculate routes.
   * If the TE tunnel goes Down, IS-IS still recalculates routes.
4. Run [**mpls te igp metric**](cmdqueryname=mpls+te+igp+metric) { **absolute** | **relative** } *value*
   
   
   
   The IGP metric of the TE tunnel is configured.
   
   
   
   You can set either of the following parameters when configuring the metric to be used by a TE tunnel during IGP shortcut path calculation:
   
   * If **absolute** is configured, the TE tunnel metric is equal to the configured value.
   * If **relative** is configured, the TE tunnel metric is equal to the sum of the IGP route metric and relative TE tunnel metric.
5. For IS-IS, run [**isis enable**](cmdqueryname=isis+enable) [ *process-id* ]
   
   
   
   IS-IS is enabled on the tunnel interface.
6. For OSPF, run the following commands in sequence.
   
   
   * Run the [**ospf enable**](cmdqueryname=ospf+enable) *process-id* **area** *area-id* command to enable OSPF on the tunnel interface.
     
     You can also run the [**network**](cmdqueryname=network) *address* *wildcard-mask* command in the OSPF view to enable network segment routing on the tunnel interface.
   * Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   * Run the [**ospf**](cmdqueryname=ospf) [ *process-id* ] command to enter the OSPF view.
   * Run the [**enable traffic-adjustment**](cmdqueryname=enable+traffic-adjustment) command to enable IGP shortcut.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

If a network fault occurs, IGP convergence is triggered. In this case, a transient forwarding status inconsistency may occur among nodes because of their different convergence rates, which poses the risk of microloops. To prevent microloops, perform the following steps:![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before you enable the OSPF TE tunnel anti-microloop function, [configure CR-LSP backup parameters](dc_vrp_te-p2p_cfg_0058.html).

* For IS-IS, run the following commands in sequence.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     An IS-IS process is created, and the IS-IS process view is displayed.
  3. Run [**avoid-microloop te-tunnel**](cmdqueryname=avoid-microloop+te-tunnel)
     
     The IS-IS TE tunnel anti-microloop function is enabled.
  4. (Optional) Run [**avoid-microloop te-tunnel rib-update-delay**](cmdqueryname=avoid-microloop+te-tunnel+rib-update-delay) *rib-update-delay*
     
     The delay in delivering the IS-IS routes whose outbound interface is a TE tunnel interface is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* For OSPF, run the following commands in sequence.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
     
     The OSPF view is displayed.
  3. Run [**avoid-microloop te-tunnel**](cmdqueryname=avoid-microloop+te-tunnel)
     
     The OSPF TE tunnel anti-microloop function is enabled.
  4. (Optional) Run [**avoid-microloop te-tunnel rib-update-delay**](cmdqueryname=avoid-microloop+te-tunnel+rib-update-delay) *rib-update-delay*
     
     The delay in delivering the OSPF routes whose outbound interface is a TE tunnel interface is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.