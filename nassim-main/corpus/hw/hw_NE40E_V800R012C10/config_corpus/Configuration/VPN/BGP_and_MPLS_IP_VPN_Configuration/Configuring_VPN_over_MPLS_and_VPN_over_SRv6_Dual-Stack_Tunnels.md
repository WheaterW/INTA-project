Configuring VPN over MPLS/VPN over SRv6 Dual-Stack Tunnels
==========================================================

In IPv4/IPv6 dual-stack scenarios, you can configure VPN over MPLS/VPN over SRv6 dual-stack tunnels to prevent traffic interruption caused by direct switching from an IPv4 MPLS network to an SRv6 network.

#### Usage Scenario

As IPv4 addresses are gradually depleted, the deployment of IPv6 networks has become a trend. However, network evolution cannot be completed at once, and IPv4 and IPv6 dual-stack services will coexist for some time.

To prevent impact on existing services, L3VPN supports MPLS/SRv6 dual-stack tunnels. If the next hop address of a route is an IPv4 address, the route can recurse to an MPLS tunnel. If the next hop address of a route is an IPv6 address, the route can recurse to an SRv6 tunnel. Routes recurse to different tunnels based on their next hop address types, significantly improving the feasibility of transition from IPv4 MPLS networks to SRv6 networks.

On the network shown in [Figure 1](#EN-US_TASK_0176299498__fig9952391436), the transition process is essentially as follows:

1. Initially, IPv4 MPLS is configured on the public network, and only L3VPN over MPLS services exist.
2. During the transition, L3VPN over MPLS and L3VPN over SRv6 dual-stack tunnels coexist. Routes are selected based on the priorities of next hop addresses. PEs preferentially select SRv6 VPNv4 routes.
3. Finally, IPv4 MPLS is deleted from the public network, and only L3VPN over SRv6 services remain.

**Figure 1** Evolution from L3VPN over MPLS to L3VPN over SRv6  
![](figure/en-us_image_0000001751847525.png "Click to enlarge")

#### Pre-configuration Tasks

Before configuring VPN MPLS/VPN SRv6 dual-stack tunnels, complete the following tasks:

* Configure an IGP for the MPLS backbone network of each AS to ensure the IP connectivity of the backbone network in each AS.

* Configure basic MPLS capabilities and MPLS LDP in each AS on the MPLS backbone network.
* Establish an IBGP peer relationship between the PE and ASBR in each AS.
* [Configure a VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0155.html) on each PE that connects to a CE and [bind the PE interface that connects to the CE to the VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0156.html).
* Configure an IP address for each CE interface that connects to a PE.
* Configure inter-AS VPN. For example, configure [inter-AS VPN option C (solution 1)](dc_vrp_mpls-l3vpn-v4_cfg_0136.html).

#### Procedure

1. Configure priority-based route selection on each PE.
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp)*as-number* command to enter the BGP view.
   3. Run the [**ipv4-family vpnv4**](cmdqueryname=ipv4-family+vpnv4) command to enter the BGP-VPNv4 address family view.
   4. Run the [**peer**](cmdqueryname=peer+high-priority+%28BGP-VPNv4+address+family+view%29) *ipv4-address* **high-priority** or [**peer**](cmdqueryname=peer+high-priority+%28BGP-VPNv4+address+family+view%29) *peerGroupName* **high-priority** command to enable BGP VPNv4 routes learned from the IPv4 peer (group) to participate in route selection based on priorities. In a dual-stack scenario, if routes with the same prefix are learned from BGP VPNv4 IPv4 and IPv6 peers, you can run this command for the IPv4 peer to ensure that the routes learned from the specified peer are preferred.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Configure a VPN instance with the IPv4 address family enabled on each PE.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to create a VPN instance and enter its view.
   3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to configure the VPN instance IPv4 address family and enter its view.
   4. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command to configure an RD for the VPN instance IPv4 address family.
   5. Run the [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] command to configure VPN targets for the VPN instance IPv4 address family.
   6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   7. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance IPv4 address family view.
   8. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance view.
   9. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of the interface to be bound to the VPN instance.
   10. Run the [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name* command to bind the interface to the VPN instance. 
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) command deletes IPv4 and IPv6 Layer 3 features on the interface, such as the configured IP address and routing protocol. You have to reconfigure them if they are required.
   11. Run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } command to configure an IP address for the interface.
       
       
       
       Layer 3 features such as PE-CE route exchange can be configured only after an IP address is configured for the PE interface that connects to a CE.
   12. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   13. Run the [**quit**](cmdqueryname=quit) command to exit the interface view.
3. Configure IPv4 route exchange between the PE and CE in each AS. For configuration details, see [Configuring the PE and CE to Exchange Routes](dc_vrp_mpls-l3vpn-v4_cfg_0158.html).
4. Establish an MP-IBGP peer relationship between PEs that use IPv6 addresses.
   
   
   
   VPNv4 peers using IPv4 addresses are used for L3VPN over MPLS services. VPNv4 peers using IPv6 addresses are used for L3VPN over SRv6 services.
   
   The Add-Path function must be enabled for VPNv4 peers using IPv6 addresses to ensure that VPNv4 routes with the same destination address but different next hops can be preferentially selected and advertised to the peer PE.
   
   
   
   1. Run the [**bgp**](cmdqueryname=bgp)*as-number* command to enter the BGP view.
   2. Run the [**router-id**](cmdqueryname=router-id) *ipv4-address* command to configure a router ID.
   3. Run the [**peer**](cmdqueryname=peer+as-number+%28BGP+view%29) *ipv4-address* **as-number** *as-number* command to specify a remote PE as a peer.
   4. Run the [**peer**](cmdqueryname=peer+connect-interface+%28BGP+view%29) *ipv4-address* **connect-interface** **loopback** *interface-number* command to specify the interface for setting up a TCP connection for BGP.
   5. Run the [**peer**](cmdqueryname=peer+as-number+%28BGP+view%29+%28IPv6%29) *ipv6-address* **as-number** *as-number* command to specify a remote PE as a peer.
   6. Run the [**peer**](cmdqueryname=peer+connect-interface+%28BGP+view%29+%28IPv6%29) *ipv6-address* **connect-interface** **loopback** *interface-number* command to specify the interface for setting up a TCP connection for BGP.
   7. Run the [**ipv4-family vpnv4**](cmdqueryname=ipv4-family+vpnv4) command to enter the BGP-VPNv4 address family view.
   8. Run the [**bestroute add-path path-number**](cmdqueryname=bestroute+add-path+path-number) *path-number* command to enable the Add-Path function and set the number of preferred routes. The Add-Path function ensures that VPNv4 routes with IPv6 next hop addresses can also be advertised.
   9. Run the [**peer**](cmdqueryname=peer+enable+%28BGP-VPNv4+address+family+view%29) *ipv4-address* **enable** command to enable the capability to exchange VPN-IPv4 routes with peers that use IPv4 addresses.
   10. Run the [**peer**](cmdqueryname=peer+enable+%28BGP-VPNv4+address+family+view%29+%28IPv6%29) *ipv6-address* **enable** command to enable the capability to exchange VPN-IPv4 routes with peers that use IPv6 addresses.
   11. Run the [**peer**](cmdqueryname=peer+capability-advertise+add-path)*ipv6-address* **capability-advertise** **add-path** **both** command to enable the device to advertise and receive Add-Path routes.
       
       
       
       Configure the Add-Path capability for only peers that use IPv6 addresses. This capability does not need to be configured for peers that use IPv4 addresses. If you do so, a service interruption may occur when such peers restart.
   12. Run the [**peer**](cmdqueryname=peer) *ipv6-address* **advertise add-path path-number** *path-number* command to set the number of Add-Path preferred routes to be advertised to a specified peer.
   13. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   14. Run the [**quit**](cmdqueryname=quit) command to exit the BGP-VPNv4 address family view.
   15. Run the [**quit**](cmdqueryname=quit) command to exit the BGP view.
5. Establish an SRv6 BE tunnel between PEs.
   1. Run the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) command to enable SR on the IPv6 forwarding plane and enter the SRv6 view.
   2. Run the [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) *ipv6-address* [ **ip-ttl** *ttl-value* ] command to specify a source address for SRv6 VPN encapsulation.
   3. Run the [**locator**](cmdqueryname=locator) *locator-name*[ **ipv6-prefix** *ipv6-address prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ] command to configure a SID node route locator and enter the SRv6 locator view.
   4. Run the [**opcode**](cmdqueryname=opcode+end-dt4) *func-opcode* **end-dt4** **vpn-instance** *vpn-instance-name* command to configure the opcode of a static SID.
   5. Run the [**quit**](cmdqueryname=quit) command to exit the SRv6 locator view.
   6. Run the [**quit**](cmdqueryname=quit) command to exit the SRv6 view.
   7. Run the [**bgp**](cmdqueryname=bgp)*as-number* command to enter the BGP view.
   8. Run the [**ipv4-family vpnv4**](cmdqueryname=ipv4-family+vpnv4) command to enter the BGP-VPNv4 address family view.
   9. Run the [**peer**](cmdqueryname=peer+prefix-sid+%28BGP-VPNv4+address+family+view%29+%28IPv6%29) *ipv6-address* **prefix-sid** command to enable the device to exchange IPv4 prefix SID information with a specified IPv6 peer.
   10. Run the [**quit**](cmdqueryname=quit) command to exit the BGP-VPNv4 address family view.
   11. Configure the device to add SIDs to VPN routes. Note that you need to perform configurations only in one of the following two views. If you perform configurations in both views, the configurations in these views are mutually exclusive.
       
       
       * Configurations in the BGP-VPN instance IPv4 address family view
         1. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv4 address family view.
         2. Run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [ **auto-sid-disable** ] command to enable the device to add SIDs to VPN routes.
            
            If **auto-sid-disable** is not specified, the device supports dynamic SID allocation. If there are static SIDs in the range of the locator specified using *locator-name*, the static SIDs are used. Otherwise, dynamically allocated SIDs are used.
            
            If **auto-sid-disable** is specified, BGP does not dynamically allocate SIDs.
       * Configurations in the BGP-VPN instance view
         1. Run the [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* command to create a BGP-VPN instance and enter its view.
         2. Run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* **end-dt46** command to enable the device to add SIDs to VPN routes.
         3. Run the [**quit**](cmdqueryname=quit) command to exit the BGP-VPN instance view.
         4. Run the [**ipv4-family vpn-instance**](cmdqueryname=ipv4-family+vpn-instance) *vpn-instance-name* command to enter the BGP-VPN instance IPv4 address family view.
   12. (Optional) Run the [**bestroute nexthop-priority**](cmdqueryname=bestroute+nexthop-priority) { **ipv4** | **ipv6** } [ **high-level** ] command to configure the device to prefer routes with IPv4 or IPv6 next hop addresses. In a dual-stack scenario, if routes with the same prefix are learned from both IPv4 and IPv6 peers, the route whose next hop is of the specified IP address type is preferred.
   13. Run the [**segment-routing ipv6 best-effort**](cmdqueryname=segment-routing+ipv6+best-effort) command to enable the device to recurse VPN routes based on the SIDs carried in the routes.
   14. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
6. On the PE, disable BGP VPNv4 routes learned from IPv4 peers from participating in route selection based on the high priority and enable BGP VPNv4 routes learned from IPv6 peers to do so, so that user traffic is switched to the SRv6 tunnel.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp)*as-number* command to enter the BGP view.
   3. Run the [**ipv4-family vpnv4**](cmdqueryname=ipv4-family+vpnv4) command to enter the BGP-VPNv4 address family view.
   4. Run the [**undo peer**](cmdqueryname=peer+high-priority+%28BGP-VPNv4+address+family+view%29) *ipv4-address***high-priority** command to disable BGP VPNv4 routes learned from the IPv4 peer from participating in route selection based on the high priority.
   5. Run the [**peer**](cmdqueryname=peer+high-priority+%28BGP-VPNv4+address+family+view%29) *ipv6-address* **high-priority** or [**peer**](cmdqueryname=peer+high-priority+%28BGP-VPNv4+address+family+view%29) *peerGroupName* **high-priority** command to enable BGP VPNv4 routes learned from the IPv6 peer (group) to participate in route selection based on priorities.
   6. Run the [**quit**](cmdqueryname=quit) command to exit the BGP-VPNv4 address family view.
   7. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv4 address family view.
   8. (Optional) Run the [**bestroute nexthop-priority**](cmdqueryname=bestroute+nexthop-priority) **ipv6** [ **high-level** ] command to configure the device to prefer routes with IPv6 next hop addresses. In a dual-stack scenario, if routes with the same prefix are learned from both IPv4 and IPv6 peers, the route whose next hop is of the specified IPv6 address type is preferred.
   9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After the configuration is complete:

* Run the [**display bgp vpnv4 all routing-table**](cmdqueryname=display+bgp+vpnv4+all+routing-table) command in the system view to check BGP VPNv4 routes and BGP VPN routes.
* Run the [**display bgp vpnv4 all peer**](cmdqueryname=display+bgp+vpnv4+all+peer) command in the system view to check BGP peers.