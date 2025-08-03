Configuring Tunnel Re-optimization
==================================

Tunnel re-optimization is configured to allow a device to dynamically adjust paths for tunnels.

#### Usage Scenario

Topology and link attributes of an IP/MPLS network are changeable. As a result, a path over which an MPLS TE tunnel has been established may not be optimal. Tunnel re-optimization can be configured to allow the MPLS TE tunnel to be reestablished over an optimal path.

Re-optimization is implemented in either of the following modes:

* Automatic re-optimization: The system automatically re-optimizes TE tunnels when the re-optimization interval is reached or when changes occur in the network topology (such as link addition, link removal, or IGP link cost adjustment). This implementation does not involve manual intervention and reduces labor cost.
* Manual re-optimization: Manual re-optimization can be configured for the TE tunnels if you want to immediately re-optimize the TE tunnels.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Tunnel re-optimization is performed based on tunnel path constraints. During path re-optimization, path constraints, such as explicit path constraints and bandwidth constraints, are also considered.
* Tunnel re-optimization cannot be used on tunnels for which a system selects paths in most-fill tie-breaking mode.
* Tunnel re-optimization takes effect on the primary and hot-standby paths, but not on ordinary backup and best-effort paths.
* Tunnel re-optimization cannot be configured if a bypass tunnel is configured, path locking is enabled, or the fixed filter (FF) resource reservation style is used.


#### Pre-configuration Tasks

Before configuring tunnel re-optimization, [configure an RSVP-TE tunnel](dc_vrp_te-p2p_cfg_0003.html).


#### Procedure

* (Optional) Enable IGP metric-based re-optimization for an MPLS TE tunnel.
  
  
  
  Perform this step if you want to re-optimize an MPLS TE tunnel based only on the IGP metric. The following constraints are ignored during re-optimization:
  
  + Bandwidth usage: A link is selected based on the percentage of the used reservable bandwidth to the maximum reservable bandwidth.
  + Hop-counts: A link is selected based on the number of hops on the path.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run either of the following commands:
     
     
     
     The global MPLS configuration takes effect on all MPLS TE tunnels and is used for batch configuration. A single tunnel configuration takes precedence over the global MPLS configuration.
     
     + Configure global MPLS.
       1. Run [**mpls**](cmdqueryname=mpls)
          
          The MPLS view is displayed.
       2. Run [**mpls te**](cmdqueryname=mpls+te)
          
          MPLS TE is enabled globally.
       3. Run [**mpls te reoptimization-aggressive enable**](cmdqueryname=mpls+te+reoptimization-aggressive+enable) (MPLS view)
          
          Re-optimization based only on IGP metric is enabled globally for MPLS TE tunnels.
          
          This command takes effect on all MPLS TE tunnels. To delete the configuration for some tunnels, enter the interface views of the MPLS TE tunnels, and then run the [**mpls te reoptimization-aggressive block**](cmdqueryname=mpls+te+reoptimization-aggressive+block) command.
       4. Run [**quit**](cmdqueryname=quit)
          
          Return to the system view.
     + Configure based on a single tunnel.
       1. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
          
          The tunnel interface view of the MPLS TE tunnel to be established is displayed.
       2. Run [**tunnel-protocol**](cmdqueryname=tunnel-protocol) **mpls** **te**
          
          MPLS TE is configured as the tunneling protocol.
       3. Run [**mpls te reoptimization-aggressive enable**](cmdqueryname=mpls+te+reoptimization-aggressive+enable) (tunnel interface view)
          
          Re-optimization based only on IGP metric is enabled globally for MPLS TE tunnels.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure automatic tunnel re-optimization.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
     
     
     
     The tunnel interface view of the MPLS TE tunnel to be established is displayed.
  3. Run [**mpls te reoptimization**](cmdqueryname=mpls+te+reoptimization) [ **frequency** *interval* ]
     
     
     
     Automatic tunnel re-optimization is enabled.
  4. (Optional) Run [**mpls te inter-area reoptimization**](cmdqueryname=mpls+te+inter-area+reoptimization)
     
     
     
     Inter-IGP-area tunnel re-optimization is enabled.
     
     
     
     In an inter-IGP-area scenario, when a better path exists in the downstream area and tunnel re-optimization is triggered on the ingress, the tunnel can only detect whether a better path exists in the area where the ingress resides, not in the downstream area. As a result, if a better path exists only in the downstream area, it is impossible to establish an RSVP-TE P2P LSP over that path through re-optimization. To address the issue, you can perform this step to enable inter-IGP-area tunnel re-optimization so that the RSVP-TE P2P LSP of the tunnel can be established over a better path in the downstream area.
  5. (Optional) Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. (Optional) Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  7. (Optional) Run [**mpls te reoptimization link-up disable**](cmdqueryname=mpls+te+reoptimization+link-up+disable)
     
     
     
     Link change-triggered RSVP-TE tunnel re-optimization is disabled.
     
     
     
     If route flapping occurs on a network, tunnel re-optimization is repeatedly triggered, wasting network resources. To prevent the problem, run this command to disable link change-triggered RSVP-TE tunnel re-optimization so that tunnel re-optimization will not be performed.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     This command takes effect only for link change-triggered tunnel re-optimization. It does not take effect if the [**mpls te reoptimization (tunnel interface view)**](cmdqueryname=mpls+te+reoptimization+%28tunnel+interface+view%29) command is run with the **frequency** *interval* parameter specified.
     
     This command disables the re-optimization function configured for all tunnels.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure manual tunnel re-optimization.
  
  
  
  In the user view, run [**mpls te reoptimization**](cmdqueryname=mpls+te+reoptimization) [ **auto-tunnel name** *tunnel-interface* | **tunnel** *tunnel-number* ]
  
  Manual re-optimization is configured.
  
  Manual re-optimization can be enabled on a specific or all tunnels on a node.

#### Verifying the Configuration

After completing the configuration, run the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) command on the ingress of the tunnel to view the following information:

* Whether automatic re-optimization is enabled
* Interval between automatic re-optimization processes