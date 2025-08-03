Configuring L3VPNv6 over SRv6 TE Policy
=======================================

This section describes how to configure L3VPNv6 over SRv6 TE Policy.

#### Context

L3VPNv6 over SRv6 TE Policy uses public network SRv6 TE Policies to carry L3VPNv6 data. The key implementation of L3VPNv6 over SRv6 TE Policy involves establishing SRv6 TE Policies, advertising VPN routes, and forwarding data.

[Figure 1](#EN-US_TASK_0290562100__fig_dc_vrp_srv6_cfg_all_001201) shows an example where an IPv6 public network is established between PE1 and PE2 and the involved VPNs are also IPv6 networks. SRv6 TE Policies can be deployed on the IPv6 public network to carry L3VPNv6 services.

**Figure 1** L3VPNv6 over SRv6 TE Policy networking  
![](figure/en-us_image_0290562119.png)

#### Pre-configuration Tasks

Before configuring L3VPNv6 over SRv6 TE Policy, complete the following tasks:

* Configure a link-layer protocol.
* Configure network-layer addresses for interfaces to ensure that neighboring devices are reachable at the network layer.

#### Procedure

1. Configure IPv6 IS-IS on the PEs and P. For configuration details, see [Configuring Basic IS-IS Functions (IPv6)](dc_vrp_isis_cfg_1023.html).
2. Configure a VPN instance on each PE and enable the IPv6 address family.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to create a VPN instance and enter the VPN instance view.
   3. Run the [**ipv6-family**](cmdqueryname=ipv6-family) command to enable the VPN instance IPv6 address family and enter the VPN instance IPv6 address family view.
   4. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command to set an RD for the VPN instance IPv6 address family.
   5. Run the [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] command to configure VPN targets for the VPN instance IPv6 address family.
   6. (Optional) Run the [**default-color**](cmdqueryname=default-color) *color-value* command to specify the default color value for the L3VPNv6 service to be recursed to an SRv6 TE Policy.
      
      
      
      If a remote VPN route without carrying the color extended community is leaked to a local VPN instance, the default color value is used for the recursion to an SRv6 TE Policy.
   7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   8. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance IPv6 address family view.
   9. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance view.
   10. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of the interface to be bound to the VPN instance.
   11. Run the [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name* command to bind the interface to the VPN instance.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) command deletes IPv4 and IPv6 Layer 3 configurations on the interface, such as the configured IP addresses and routing protocols. You have to reconfigure them if they are required.
   12. Run the [**ipv6 enable**](cmdqueryname=ipv6+enable) command to enable IPv6 on the interface.
   13. Run the [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } command to configure an IPv6 address for the interface.
       
       
       
       Layer 3 features such as PE-CE route exchange can be configured for PE-CE communication only after an IPv6 address is configured for the involved VPN interface.
   14. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   15. Run the [**quit**](cmdqueryname=quit) command to exit the interface view.
3. Configure PE-CE IPv6 route exchange. For configuration details, see [Configuring Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v6_cfg_2061.html).
4. Establish an MP-IBGP peer relationship between the PEs.
   1. Run the [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* } command to enter the BGP view.
   2. Run the [**router-id**](cmdqueryname=router-id) *ipv4-address* command to configure a router ID.
   3. Run the [**peer**](cmdqueryname=peer) *ipv6-address* **as-number** { *as-number-plain* | *as-number-dot* } command to configure the remote PE as a peer.
   4. Run the [**peer**](cmdqueryname=peer) *ipv6-address* [**connect-interface**](cmdqueryname=connect-interface) **loopback** *interface-number* command to specify the interface used to establish a TCP connection with the specified BGP peer.
   5. Run the [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6** command to enter the BGP-VPNv6 address family view.
   6. Run the [**peer**](cmdqueryname=peer) *ipv6-address* **enable** command to enable the device to exchange VPN-IPv6 routing information with the specified peer.
   7. Run the [**peer**](cmdqueryname=peer) *ipv6-address* **prefix-sid** [ **advertise-srv6-locator** ] command to enable the device to exchange IPv6 prefix SID and locator information with the specified IPv6 peer.
   8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   9. Run the [**quit**](cmdqueryname=quit) command to exit the BGP-VPNv6 address family view.
   10. Run the [**quit**](cmdqueryname=quit) command to exit the BGP view.
5. Configure the device to carry SIDs in VPN routes.
   1. Run the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) command to enable SRv6 and enter its view.
   2. Configure a source address for SRv6 encapsulation. Note that you only need to perform one of the following operations. If both of the operations are performed, the latest configuration overrides the previous one.
      
      
      * Run the [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) *ipv6-address* [ **ip-ttl** *ttl-value* ] command to directly configure a source address for SRv6 encapsulation.
      * Run the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) { *intfname* | *interfaceType* *interfaceNum* } [ **ip-ttl** *ttl-value* ] command to specify the interface to which the source address used for SRv6 encapsulation belongs.
        
        If no IPv6 global address is configured for the interface specified using the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) command, the source address for SRv6 encapsulation is not configured.
   3. Run the [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ] command to configure an SRv6 locator.
   4. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt6** **vpn-instance** *vpn-instance-name* or [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt46** **vpn-instance** *vpn-instance-name*
      
      
      
      An opcode for static SIDs is configured.
      
      
      
      A SID can be either dynamically allocated by BGP or manually configured. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable dynamic End.DT6 SID allocation through BGP or the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46) command to enable dynamic End.DT46 SID allocation through BGP in the future, skip this step.
   5. Run the [**quit**](cmdqueryname=quit) command to exit the SRv6 locator view.
   6. Run the [**quit**](cmdqueryname=quit) command to exit the SRv6 view.
   7. Run the [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* } command to enter the BGP view.
   8. Configure the device to add SIDs to VPN routes. Note that you need to perform configurations only in one of the following two views. If you perform configurations in both views, the configurations in these views are mutually exclusive.
      
      
      * Configurations in the BGP-VPN instance IPv6 address family view
        1. Run the [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv6 address family view.
        2. Run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable the device to add SIDs to VPN routes.
      * Configurations in the BGP-VPN instance view
        1. Run the [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* command to create a BGP-VPN instance and enter its view.
        2. Run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* **end-dt46** command to enable the device to add SIDs to VPN routes.
        3. Run the [**quit**](cmdqueryname=quit) command to exit the BGP-VPN instance view.
        4. Run the [**ipv4-family vpn-instance**](cmdqueryname=ipv4-family+vpn-instance) *vpn-instance-name* command to enter the BGP-VPN instance IPv6 address family view.
   9. Run the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **traffic-engineer** [ **best-effort** ] command to enable the device to recurse VPN routes based on the SIDs carried in the routes.
      
      
      
      If an SRv6 BE path exists on the network, you can set the **best-effort** parameter, allowing the SRv6 BE path to function as a best-effort path in the case of an SRv6 TE Policy fault.
   10. (Optional) Run [**segment-routing ipv6 color-only**](cmdqueryname=segment-routing+ipv6+color-only)
       
       
       
       The device is enabled to recurse VPN routes to color-only SRv6 TE Policies.
       
       
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       This command applies only to color-only scenarios and supports only statically configured SRv6 TE Policies.
   11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   12. Run the [**quit**](cmdqueryname=quit) command to exit the BGP-VPN instance IPv6 address family view.
   13. Run the [**quit**](cmdqueryname=quit) command to exit the BGP view.
6. Configure an SRv6 TE Policy. For configuration details, see [Configuring an SRv6 TE Policy (Manual Configuration + IS-IS as an IGP)](dc_vrp_srv6_cfg_all_0110.html) or [Configuring an SRv6 TE Policy (Dynamic Delivery by a Controller + IS-IS as an IGP)](dc_vrp_srv6_cfg_all_0116.html).
7. Configure VPNv6 routes to recurse to the SRv6 TE Policy.
   1. Run the [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **deny** | **permit** } **node** *node* command to create a route-policy with a specified node and enter the route-policy view.
   2. (Optional) Configure an if-match clause for the route-policy. The community attributes of routes can be added or modified only if the routes match specified if-match clauses.
      
      
      
      For configuration details, see [(Optional) Configuring an if-match Clause](dc_vrp_route-policy_cfg_0009.html).
   3. Run the [**apply extcommunity**](cmdqueryname=apply+extcommunity) **color** *color* command to configure the BGP color extended community.
   4. Run the [**quit**](cmdqueryname=quit) command to exit the route-policy view.
   5. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   6. Run the [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6** command to enter the BGP-VPNv6 address family view.
   7. Run the [**peer**](cmdqueryname=peer) *ipv6-address* [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **import** | **export** } command to configure a BGP import or export route-policy.
   8. Run the [**quit**](cmdqueryname=quit) command to exit the BGP-VPNv6 address family view.
   9. Run the [**quit**](cmdqueryname=quit) command to exit the BGP view.
   10. Run the [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name* command to create a tunnel policy and enter the tunnel policy view.
   11. (Optional) Run the [**description**](cmdqueryname=description) *description-text* command to configure a description for the tunnel policy.
   12. Run the [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) **ipv6 srv6-te-policy** **load-balance-number** *loadBalanceNumber* command to configure the tunnel selection sequence and the number of tunnels for load balancing.
   13. Run the [**quit**](cmdqueryname=quit) command to exit the tunnel policy view.
   14. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to enter the VPN instance view.
   15. Run the [**ipv6-family**](cmdqueryname=ipv6-family) command to enter the VPN instance IPv6 address family view.
   16. Run the [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* command to apply the specified tunnel policy to the VPN instance IPv6 address family.
   17. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After configuring L3VPNv6 over SRv6 TE Policy, verify the configuration.

* Run the [**display segment-routing ipv6 locator**](cmdqueryname=display+segment-routing+ipv6+locator) [ *locator-name* ] **verbose** command to check SRv6 locator information.
* Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) { **end** | **end-x** | **end-dt6** | **end-dt46** } [ *sid* ] **forwarding** command to check information about the SRv6 local SID table.
* Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance)*vpn-instance-name* **tunnel-info nexthop** *nexthopIpv6Addr* command to check information about the tunnel to which the route with the specified next hop recurses in each address family of the current VPN instance.
* Run the [**ping srv6-te policy**](cmdqueryname=ping+srv6-te+policy) { **policy-name** *policyname* | **endpoint-ip** *endpointipv6* **color** *colorid* | **binding-sid** *bsid* } [ **end-op** *endop* ] [ **-a** *sourceaddr6* | **-c** *count* | **-m** *interval* | **-s** *packetsize* | **-t** *timeout* | **-tc** *tc* | **-h** *hoplimit* ] command with the **policy-name** *policyname*, **endpoint-ip** *endpointipv6* **color** *colorid*, or **binding-sid** *bsid* parameter to initiate a ping operation on the specified SRv6 TE Policy for connectivity check.
* Run the [**ping ipv6**](cmdqueryname=ping+ipv6) command to check the connectivity between CEs.