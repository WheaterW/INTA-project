Configuring EVPN VPWS over MPLS/EVPN VPWS over SRv6 Dual-Stack Tunnels
======================================================================

In IPv4/IPv6 dual-stack scenarios, you can configure EVPN VPWS over MPLS/EVPN VPWS over SRv6 dual-stack tunnels to prevent traffic interruption caused by direct switching from an IPv4 MPLS network to an SRv6 network.

#### Usage Scenario

As IPv4 addresses are gradually depleted, the deployment of IPv6 networks has become a trend. However, network evolution cannot be completed at once, and IPv4 and IPv6 services will coexist for some time.

EVPN over SRv6 is today's mainstream transport solution for 5G services. To prevent live network services from being affected, a new transport solution must be deployed based on these services. In a scenario where a large number of EVPN VPWS over MPLS services exist on the live network, to prevent traffic interruption caused by direct switching from the IPv4 MPLS network to an SRv6 network (IPv4 and IPv6 networks coexist), configure IPv4/IPv6 dual-stack. This facilitates evolution from EVPN VPWS over MPLS to EVPN VPWS over SRv6.

On the network shown in [Figure 1](#EN-US_TASK_0000001150003980__fig79406277579), the transition process is essentially as follows:

1. Initially, IPv4 MPLS is configured on the public network, and only EVPN VPWS over MPLS services exist.
2. During the transition, EVPN VPWS over MPLS and EVPN VPWS over SRv6 dual-stack tunnels coexist. Routes are selected based on the priorities of next hop addresses. PEs preferentially select SRv6 EVPN routes.
3. Finally, IPv4 MPLS is deleted from the public network, and only EVPN VPWS over SRv6 services remain.

**Figure 1** EVPN VPWS over MPLS/EVPN VPWS over SRv6 dual-stack tunnels  
![](figure/en-us_image_0000001232368545.png)

#### Pre-configuration Tasks

Before configuring EVPN VPWS over MPLS/EVPN VPWS over SRv6 dual-stack tunnels, complete the following tasks:

* Configure Layer 3 route reachability on the IPv4 network.
* Configure IPv6 IS-IS on the PEs and P. For detailed configurations, see [Configuring Basic IS-IS Functions (IPv6)](dc_vrp_isis_cfg_1023.html).

#### Procedure

1. Configure EVPN VPWS over MPLS between PEs. For detailed configurations, see [Configuring EVPN VPWS over MPLS](dc_vrp_evpn_cfg_0020.html).
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) If an RR exists on the network, perform the following configurations on the RR and PEs:
   > 1. To enable PEs to receive all routes from IPv4 and IPv6 peers, configure the Add-Path function:
   
   > a. Run the [**bestroute add-path**](cmdqueryname=bestroute+add-path) **path-number** *path-number*, [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } **capability-advertise** **add-path** **send**, and [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } **advertise add-path path-number** *number* commands in the EVPN address family view of the RR.
   
   > b. Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } **capability-advertise** **add-path** **receive** command in the EVPN address family view of each PE to enable the function to receive Add-Path routes from a specified peer.
   
   > 2. In an Option B scenario, to ensure service continuity, run the [**peer**](cmdqueryname=peer) *peerIpv4Addr* **high-priority** command in the EVPN address family view of the RR to control route priorities.
2. Configure priority-based route selection on PEs.
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **vpws** command to enter the view of an existing VPWS EVPN instance.
   3. Run the [**bestroute nexthop-priority**](cmdqueryname=bestroute+nexthop-priority) **ipv6** **high-level** command to configure the device to prefer the routes with IPv6 next hop addresses after the routes learned from IPv4 or IPv6 peers are leaked into the EVPN instance.
   4. Run the [**srv6-local-route advertise-to-mpls**](cmdqueryname=srv6-local-route+advertise-to-mpls) **enable** command to enable the function to advertise locally generated SRv6 routes to both BGP EVPN IPv4 and BGP EVPN IPv6 peers.
   5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * In a scenario where IPv4 services smoothly evolve to IPv6 services, to ensure service continuity, run the [**srv6-local-route advertise-to-mpls**](cmdqueryname=srv6-local-route+advertise-to-mpls) **enable** command to enable the device to advertise BGP EVPN routes carrying SIDs to both BGP EVPN IPv4 and BGP EVPN IPv6 peers, and then configure EVPN VPWS over SRv6.
      * If a large number of EVPN VPWS services on a device need evolution, perform the following operations in the EVPN global view to simplify the configuration.
        
        Run the [**srv6-local-route advertise-to-mpls**](cmdqueryname=srv6-local-route+advertise-to-mpls) **evpn-vpws** command to enable all VPWS EVPN instances on the device to advertise BGP EVPN routes carrying SIDs to both BGP EVPN IPv4 and BGP EVPN IPv6 peers.
        
        Run the [**bestroute nexthop-priority**](cmdqueryname=bestroute+nexthop-priority) **ipv6** **high-level** command to enable the device to prefer routes with IPv6 next hop addresses when routes learned by all VPWS EVPN instances are leaked locally.
3. Configure EVPN VPWS over SRv6 between PEs. For detailed configurations, see [Configuring EVPN VPWS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0021_copy.html) or [Configuring EVPN VPWS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpws_over_srv6-te_policy_copy.html).

#### Verifying the Configuration

* Run the [**display bgp evpn evpl**](cmdqueryname=display+bgp+evpn+evpl) command to check information about all EVPL instances.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* ] command to check BGP EVPN route information.
* Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end-dx2** **evpl-instance** *evpl-id* **forwarding** command to check SRv6 BE local SID table information.
* Run the [**display evpn vpn-instance**](cmdqueryname=display+evpn+vpn-instance) [ **name** *vpn-instance-name* ] **tunnel-info** command to check information about the tunnel associated with an EVPN instance.
* Run the [**display evpn vpn-instance name**](cmdqueryname=display+evpn+vpn-instance+name)*vpn-instance-name* **tunnel-info** **nexthop** **nexthopIpv6Addr** command to check information about the tunnel that is associated with a specified EVPN instance and matches a specified next hop.