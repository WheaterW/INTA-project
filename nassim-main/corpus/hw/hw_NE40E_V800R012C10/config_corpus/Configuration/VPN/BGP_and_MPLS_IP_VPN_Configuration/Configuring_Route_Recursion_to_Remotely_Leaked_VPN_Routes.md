Configuring Route Recursion to Remotely Leaked VPN Routes
=========================================================

After route recursion to remotely leaked VPN routes is enabled, a route can inherit the label and tunnel ID of a route leaked from the remote end. Then, the device can forward data through the tunnel to which the route recurses.

#### Usage Scenario

A static route needs recursion if its next hop is indirect. To enable static routes to recurse to remotely leaked VPN routes, run the [**ip route recursive-lookup bgp-vpnv4-route enable**](cmdqueryname=ip+route+recursive-lookup+bgp-vpnv4-route+enable) command. After recursing to remotely leaked VPN routes, static routes may inherit the labels and tunnel IDs of these leaked routes. In this case, the device can forward data through tunnels to which the static routes recurse.

In some upgrade scenarios, however, you need to prevent static routes from recursing to remotely leaked VPN routes to ensure that the path along which traffic is forwarded remains unchanged after the upgrade. On the network shown in [Figure 1](#EN-US_TASK_0172369388__fig_dc_vrp_cli_ip_route_recursive-lookup_bgp-vpnv4-route), BGP VPNv4 peer relationships are established between AGGs and between AGGs and the RSG. L3VE interfaces are configured on AGGs and bound to VPN instances, so that the CSG can access the L3VPN. To guide traffic forwarding, BGP is configured to import direct routes on both AGGs, and static routes to the eNodeB are also configured on both AGGs. The static routes use 1.1.1.1/32 as their destination address and share the same next hop, which is the address of the interface used by the CSG to connect to AGGs.

Before the upgrade, the static routers configured on AGGs cannot recurse to remotely leaked VPN routes. Therefore, the downstream traffic path is Link A. After the upgrade, however, the static routes configured on AGGs can recurse to remotely leaked VPN routes by default. The static route configured on AGG2 will recurse to route 11.11.11.0/24 on AGG1 and inherits its label and tunnel ID. After the recursion, the static route on AGG2 will also be advertised to the RSG based on the BGP VPNv4 peer relationship. As a result, the RSG receives two routes with the same prefix from AGG1 and AGG2. If the RSG selects the route from AGG2 as the optimal route, the traffic forwarding path will switch to Link B, which is different from Link A before the upgrade. To prevent the preceding problem, run the [**ip route recursive-lookup bgp-vpnv4-route disable**](cmdqueryname=ip+route+recursive-lookup+bgp-vpnv4-route+disable) command on AGGs to prevent the static routes from recursing to remotely leaked VPN routes.

**Figure 1** L2VPN accessing L3VPN networking  
![](figure/en-us_image_0185535031.png)

On the network shown in [Figure 2](#EN-US_TASK_0172369388__fig_ip_route_recursive-lookup_inherit-label-route_enable), PE1 and PE2 are IBGP peers, and CE1 and PE1 are IGP neighbors. PE2 has learned the IP address of CE1's loopback interface, and an EBGP peer relationship is established between CE1 and PE2 using loopback interface addresses. By default, the BGP routes that PE2 learns from CE1 through the EBGP peer connection cannot recurse to remotely leaked VPN routes. As a result, traffic fails to be forwarded. To address this problem, run the [**ip route recursive-lookup inherit-label-route enable**](cmdqueryname=ip+route+recursive-lookup+inherit-label-route+enable) command to allow the BGP routes to recurse to remotely leaked VPN routes. After the BGP routes inherit the labels and tunnel IDs of the remotely leaked VPN routes, traffic can be correctly forwarded.

**Figure 2** Basic BGP/MPLS IP VPN networking  
![](figure/en-us_image_0231806285.png)

#### Pre-configuration Tasks

Before configuring route recursion to remotely leaked VPN routes, [configure basic BGP/MPLS IP VPN](dc_vrp_mpls-l3vpn-v4_cfg_0154.html).


#### Procedure

* Configure recursion of static routes to remotely leaked VPN routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip route recursive-lookup bgp-vpnv4-route**](cmdqueryname=ip+route+recursive-lookup+bgp-vpnv4-route) { **enable** | **disable** }
     
     
     
     To prevent traffic forwarding path inconsistency in some upgrade scenarios, recursion of static routes to remotely leaked VPN routes needs to be disabled using the [**ip route recursive-lookup bgp-vpnv4-route**](cmdqueryname=ip+route+recursive-lookup+bgp-vpnv4-route) **disable** command.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure recursion of all routes to remotely leaked VPN routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip route recursive-lookup inherit-label-route enable**](cmdqueryname=ip+route+recursive-lookup+inherit-label-route+enable)
     
     
     
     Route recursion to remotely leaked VPN routes is enabled.
  
  
  
  This command mainly applies to BGP/MPLS IP VPN scenarios.

#### Verifying the Configuration

After the configuration is complete, run the [**display current-configuration**](cmdqueryname=display+current-configuration) command in the system view to check whether route recursion to remotely leaked VPN routes is enabled.