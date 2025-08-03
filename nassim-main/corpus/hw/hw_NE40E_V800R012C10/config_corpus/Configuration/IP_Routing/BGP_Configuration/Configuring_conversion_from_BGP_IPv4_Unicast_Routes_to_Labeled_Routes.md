Configuring conversion from BGP IPv4 Unicast Routes to Labeled Routes
=====================================================================

Configuring conversion from BGP IPv4 unicast routes to labeled routes can ensure that traffic is forwarded along a specified LSP.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0172366251__fig_dc_vrp_bgp_cfg_310301), an IBGP peer relationship and an MPLS LSP are established between the user device and DeviceA. It is required that traffic from DeviceB to the user device be forwarded along the MPLS LSP.

To implement this function, enable DeviceA and DeviceB to send or receive labeled routes, and run the [**unicast-route label advertise**](cmdqueryname=unicast-route+label+advertise) command on DeviceA. After DeviceA assigns MPLS labels to routes based on a route-policy, DeviceA converts the IPv4 public network unicast route (1.1.1.0/24) learned from the user device to a labeled route and sends the labeled route to DeviceB. After traffic from DeviceB reaches DeviceA, DeviceA performs the POPGO action. Specifically, DeviceA removes the BGP label, adds an LSP label, and forwards the traffic to the user device along the LSP.

**Figure 1** Networking for configuring conversion from BGP IPv4 unicast routes to labeled routes  
![](images/fig_dc_vrp_bgp_cfg_310301.png)  


#### Procedure

* Perform the following operations on the labeled route sender (DeviceA):
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**route-policy**](cmdqueryname=route-policy+node) *route-policy-name* *matchMode* **node** *node*
     
     
     
     A route-policy to be used to filter the routes to be advertised is created.
  3. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
     
     
     
     The device is enabled to assign labels to IPv4 routes.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     The system view is displayed.
  5. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  6. Run [**peer**](cmdqueryname=peer+label-route-capability+check-tunnel-reachable) { *group-name* | *ipv4-address* } **label-route-capability** [ **check-tunnel-reachable** ]
     
     
     
     The device is enabled to send labeled routes to a specified peer or peer group.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To prevent a traffic loop, it is recommended that **check-tunnel-reachable** be specified to allow the device to check tunnel reachability.
     
     [Figure 2](#EN-US_TASK_0172366251__fig_unicast-route_label_advertise_02) shows the networking diagram for a traffic loop. If **check-tunnel-reachable** is not specified, DeviceA converts the routes learned from the user side into labeled routes and advertises them to DeviceB, regardless of whether the tunnel is reachable. Traffic from DeviceB is forwarded based on the BGP label. When the traffic reaches DeviceA, the BGP label is removed. If the LSP is unreachable, the traffic recurses to a specific outbound interface and next hop. In this case, if a route that DeviceA learns from another device is more specific than that learned from the user side, traffic will be forwarded over an incorrect route or even be routed back to DeviceB, thereby causing a traffic loop.
     
     **Figure 2** Network diagram with a traffic loop  
     ![](figure/en-us_image_0206665529.png)
  7. Run [**peer**](cmdqueryname=peer+route-policy+export) { *group-name* | *ipv4-address* } **route-policy** *route-policy-name* **export**
     
     
     
     The route-policy is configured as an export policy based on which the device advertises routes to the peer.
  8. Run [**unicast-route label advertise**](cmdqueryname=unicast-route+label+advertise)
     
     
     
     The device is enabled to convert received IPv4 unicast routes to labeled routes and advertise the labeled routes to peers with the labeled route exchange capability.
  9. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Perform the following operations on the labeled route receiver (DeviceB):
  1. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  2. Run [**peer**](cmdqueryname=peer+label-route-capability+check-tunnel-reachable) { *group-name* | *ipv4-address* } **label-route-capability** [ **check-tunnel-reachable** ]
     
     
     
     The device is enabled to receive labeled routes.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display bgp routing-table label**](cmdqueryname=display+bgp+routing-table+label+statistics) [ **statistics** ] command to check information about labeled routes in the BGP routing table.