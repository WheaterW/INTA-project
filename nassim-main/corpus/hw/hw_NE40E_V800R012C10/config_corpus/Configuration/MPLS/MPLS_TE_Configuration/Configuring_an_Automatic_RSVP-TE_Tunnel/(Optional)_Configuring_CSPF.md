(Optional) Configuring CSPF
===========================

CSPF is configured to calculate the shortest path destined for a specified node.

#### Context

After CSPF is configured, it can be used to calculate paths if a connection between the forwarder and controller is disconnected. If CSPF is not configured and a connection between the forwarder and controller is disconnected, no path can be created because only the controller can calculate paths.

CSPF calculates only the shortest path to the specified tunnel destination. During path computation, if there are multiple paths with the same weight, the optimal path is selected using the tie-breaking function.

Tie-breaking is based on the percentage of the available bandwidth to the maximum reservable bandwidth. The maximum reservable bandwidth is configured using the [**mpls te bandwidth max-reservable-bandwidth**](cmdqueryname=mpls+te+bandwidth+max-reservable-bandwidth) command, not the BC bandwidth configured using the [**mpls te bandwidth bc0**](cmdqueryname=mpls+te+bandwidth+bc0) command on an interface. The following tie-breaking policies are available:

* Most-fill: The path with a larger percentage of the available bandwidth to the maximum reservable bandwidth is preferred. That is, the path with lower bandwidth usage is preferred.
* Least-fill: The path with a smaller percentage of the available bandwidth to the maximum reservable bandwidth is preferred. That is, the path with higher bandwidth usage is preferred.
* Random: The device selects a path at random. This mode allows LSPs to be evenly distributed among links, regardless of their bandwidth.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The Most-fill and Least-fill modes are only effective when the difference in bandwidth usage between the two links exceeds 10%, such as 50% of link A bandwidth utilization and 45% of link B bandwidth utilization. The value is 5%. At this time, the Most-fill and Least-fill modes do not take effect, and the Random mode is still used.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te cspf**](cmdqueryname=mpls+te+cspf)
   
   
   
   CSPF is enabled on the local node.
4. (Optional) Run [**mpls te cspf preferred-igp**](cmdqueryname=mpls+te+cspf+preferred-igp) { **isis** [ *process-id* [ **level-1** | **level-2** ] ] | **ospf** [ *process-id* [ **area** *area-id* ] ] }
   
   
   
   A preferred IGP is configured. Its process and area or level can also be configured.
5. (Optional) Run [**mpls te cspf multi-instance shortest-path**](cmdqueryname=mpls+te+cspf+multi-instance+shortest-path) [ **preferred-igp** { **isis** | **ospf** } [ *process-id* ] ]
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   This command is mutually exclusive with the [**mpls te cspf preferred-igp**](cmdqueryname=mpls+te+cspf+preferred-igp) command, which is executed in [Step 4](#EN-US_TASK_0172368110__step_preferred-igp). If both commands are run, the latest command configuration overrides the previous one.
6. (Optional) Run [**mpls te cspf optimize-mode disable**](cmdqueryname=mpls+te+cspf+optimize-mode+disable)
   
   
   
   The optimization mode is disabled when CSPF calculates the path.
   
   CSPF provides a method for selecting a path in the MPLS domain. By default, the optimization mode is used for path calculation, and the path calculation is performed from Egress to Ingress. Compared with the common calculation method, the optimization mode has higher efficiency.
   
   The [**mpls te cspf optimize-mode disable**](cmdqueryname=mpls+te+cspf+optimize-mode+disable) command is used to disable the CSPF optimization mode. After the configuration, the path is calculated from Ingress to Egress.
7. (Optional) Configure a CR-LSP tie-breaking mode on the local node.
   
   
   
   A CR-LSP tie-breaking mode can be configured globally or for a specific tunnel. The tunnel-specific tie-breaking configuration takes preference over the global configuration, and the global configuration is used by a tunnel only if no CR-LSP tie-breaking mode is configured for this tunnel.
   
   
   
   * Global configuration in the MPLS view
     
     Run the [**mpls te tie-breaking**](cmdqueryname=mpls+te+tie-breaking) { **least-fill** | **most-fill** | **random** } command to configure a CR-LSP tie-breaking mode on the local node.
   * Tunnel-specific configuration in the tunnel interface view
     1. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     2. Run the [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number* command to enter the tunnel interface view of a specific MPLS TE tunnel.
     3. Run the [**mpls te tie-breaking**](cmdqueryname=mpls+te+tie-breaking) { **least-fill** | **most-fill** | **random** } command to configure a CR-LSP tie-breaking mode for the tunnel.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.