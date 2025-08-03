Configuring L3VPNv4 over SRv6 TE Policy
=======================================

This section describes how to configure L3VPNv4 over SRv6 TE Policy.

#### Usage Scenario

L3VPNv4 over SRv6 TE Policy uses public SRv6 TE Policies to carry L3VPNv4 data. The implementation of L3VPNv4 over SRv6 TE Policy involves establishing SRv6 TE Policies, advertising VPN routes, and forwarding data.

As shown in [Figure 1](#EN-US_TASK_0184364555__fig_dc_vrp_srv6_cfg_all_001201), PE1 and PE2 communicate through an IPv6 public network. The VPN is a traditional IPv4 network. SRv6 TE Policies can be deployed on the IPv6 public network to carry L3VPNv4 services on the VPN.

**Figure 1** L3VPNv4 over SRv6 TE Policy networking  
![](figure/en-us_image_0184386857.png)

#### Pre-configuration Tasks

Before configuring L3VPNv4 over SRv6 TE Policy, complete the following tasks:

* Configure a link layer protocol.
* Configure network-layer addresses for interfaces to ensure that neighboring devices are reachable at the network layer.

#### Procedure

1. Configure IPv6 IS-IS on each PE and P. For details, see [Configuring Basic IS-IS Functions (IPv6)](dc_vrp_isis_cfg_1023.html).
2. Configure a VPN instance on each PE and enable the IPv4 address family for the instance.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      
      
      A VPN instance is created, and the VPN instance view is displayed.
   3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
      
      
      
      The VPN instance IPv4 address family is enabled, and the view of this address family is displayed.
   4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      
      
      An RD is configured for the VPN instance IPv4 address family.
   5. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
      
      
      
      VPN targets are configured for the VPN instance IPv4 address family.
   6. (Optional) Run [**default-color**](cmdqueryname=default-color) *color-value*
      
      
      
      The default color value is specified for the L3VPNv4 service to recurse to an SRv6 TE Policy.
      
      If a remote VPN route without carrying the Color Extended Community is leaked to a local VPN instance, the default color value is used for the recursion.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the VPN instance IPv4 address family view.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the VPN instance view.
   10. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
       
       
       
       The view of the interface to which the VPN instance needs to be bound is displayed.
   11. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
       
       
       
       The interface is bound to the VPN instance.
       
       
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) command deletes IPv4 and IPv6 Layer 3 configurations on the interface, such as the configured IP addresses and routing protocols. You have to reconfigure them if they are required.
   12. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
       
       
       
       An IP address is configured for the interface.
       
       
       
       Some Layer 3 functions such as route exchange between the PE and CE can be configured only after an IP address is configured for the VPN interface on the PE.
   13. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
   14. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the interface view.
3. Configure PE-CE IPv4 route exchange. For configuration details, see [Configuring Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v4_cfg_0158.html).
4. Establish an MP-IBGP peer relationship between the PEs.
   1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
      
      
      
      The BGP view is displayed.
   2. Run [**router-id**](cmdqueryname=router-id) *ipv4-address*
      
      
      
      A router ID is configured.
   3. Run [**peer**](cmdqueryname=peer) *ipv6-address* **as-number** { *as-number-plain* | *as-number-dot* }
      
      
      
      The remote PE is configured as a peer.
   4. Run [**peer**](cmdqueryname=peer) *ipv6-address* [**connect-interface**](cmdqueryname=connect-interface) **loopback** *interface-number*
      
      
      
      The interface on which a TCP connection to the specified BGP peer is established is specified.
   5. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4**
      
      
      
      The BGP VPNv4 address family view is displayed.
   6. Run [**peer**](cmdqueryname=peer) *peerIpv6Addr* **enable**
      
      
      
      The device is enabled to exchange VPN-IPv4 routes with the specified peer.
   7. Run [**peer**](cmdqueryname=peer) *ipv6-address* **prefix-sid** [ **sid-type5** [ **advertise-srv6-locator** ] ]
      
      
      
      The device is enabled to exchange IPv4 prefix SID and locator information with the specified IPv6 peer.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP VPNv4 address family view.
   10. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP view.
5. Configure the device to carry SIDs in VPN routes.
   1. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      SRv6 is enabled, and the SRv6 view is displayed.
   2. Configure a source address for SRv6 encapsulation. Note that you only need to perform one of the following operations. If both of the operations are performed, the latest configuration overrides the previous one.
      
      
      * Run the [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) *ipv6-address* [ **ip-ttl** *ttl-value* ] command to directly configure a source address for SRv6 encapsulation.
      * Run the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) { *intfname* | *interfaceType* *interfaceNum* } [ **ip-ttl** *ttl-value* ] command to specify the interface to which the source address used for SRv6 encapsulation belongs.
        
        If no IPv6 global address is configured for the interface specified using the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) command, the source address for SRv6 encapsulation is not configured.
   3. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *mask-length* [ **static** *static-length* | **args** *args-length* ] \* ]
      
      
      
      An SRv6 locator is configured.
   4. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt4** **vpn-instance** *vpn-instance-name* or [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt46** **vpn-instance** *vpn-instance-name*
      
      
      
      An opcode for static SIDs is configured.
      
      
      
      A SID can be either dynamically allocated by BGP or manually configured. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable dynamic End.DT4 SID allocation through BGP or the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46) command to enable dynamic End.DT46 SID allocation through BGP in the future, skip this step.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 locator view.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 view.
   7. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
      
      
      
      The BGP view is displayed.
   8. Configure the device to add SIDs to VPN routes. Note that you need to perform configurations only in one of the following two views. If you perform configurations in both views, the configurations in these views are mutually exclusive.
      
      
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
   9. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **traffic-engineer** [ **best-effort** ]
      
      
      
      The device is enabled to perform VPN route recursion based on the SIDs carried in the routes.
      
      If an SRv6 BE path exists on the network, you can set the **best-effort** parameter, allowing the SRv6 BE path to function as a best-effort path in the case of an SRv6 TE Policy fault.
   10. (Optional) Run [**segment-routing ipv6 color-only**](cmdqueryname=segment-routing+ipv6+color-only)
       
       
       
       The device is enabled to recurse VPN routes to color-only SRv6 TE Policies.
       
       
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       This command applies only to color-only scenarios and supports only statically configured SRv6 TE Policies.
   11. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
   12. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP-VPN instance IPv4 address family view.
   13. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP view.
6. Configure an SRv6 TE Policy. For details, see [Configuring an SRv6 TE Policy (Manual Configuration + IS-IS as an IGP)](dc_vrp_srv6_cfg_all_0110.html) or [Configuring an SRv6 TE Policy (Dynamic Delivery by a Controller + IS-IS as an IGP)](dc_vrp_srv6_cfg_all_0116.html).
7. Configure VPNv4 routes to recurse to the SRv6 TE Policy.
   1. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **deny** | **permit** } **node** *node*
      
      
      
      A route-policy node is created, and the route-policy view is displayed.
   2. (Optional) Configure an if-match clause as a route-policy filter criterion. You can add or modify the Color Extended Community only for a route-policy that meets the filter criterion.
      
      
      
      For details about the configuration, see [(Optional) Configuring an if-match Clause](dc_vrp_route-policy_cfg_0009.html).
   3. Run [**apply extcommunity**](cmdqueryname=apply+extcommunity) **color** *color*
      
      
      
      The BGP Color Extended Community is configured.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the route-policy view.
   5. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4**
      
      
      
      The BGP VPNv4 address family view is displayed.
   7. Run [**peer**](cmdqueryname=peer) *ipv6-address* [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **import** | **export** }
      
      
      
      A BGP import or export route-policy is configured.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP VPNv4 address family view.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
   10. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
       
       
       
       A tunnel policy is created, and the tunnel policy view is displayed.
   11. (Optional) Run [**description**](cmdqueryname=description) *description-text*
       
       
       
       A description is configured for the tunnel policy.
   12. Run [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) **ipv6 srv6-te-policy** **load-balance-number** *loadBalanceNumber*
       
       
       
       The tunnel selection sequence and the number of tunnels for load balancing are configured.
   13. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the tunnel policy view.
   14. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
       
       
       
       The VPN instance view is displayed.
   15. Run [**ipv4-family**](cmdqueryname=ipv4-family)
       
       
       
       The VPN instance IPv4 address family view is displayed.
   16. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
       
       
       
       A tunnel policy is applied to the VPN instance IPv4 address family.
   17. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.

#### Verifying the Configuration

After configuring L3VPNv4 over SRv6 TE Policy, verify the configuration.

* Run the [**display segment-routing ipv6 locator**](cmdqueryname=display+segment-routing+ipv6+locator) [ *locator-name* ] **verbose** command to check SRv6 locator information.
* Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) { **end** | **end-x** | **end-dt4** | **end-dt46** } [ *sid* ] **forwarding** command to check information about the SRv6 local SID table.
* Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance)*vpn-instance-name* **tunnel-info nexthop** *nexthopIpv6Addr* command to check information about the tunnel to which the route with the specified next hop recurses in each address family of the current VPN instance.
* Run the [**ping srv6-te policy**](cmdqueryname=ping+srv6-te+policy) { **policy-name** *policyname* | **endpoint-ip** *endpointipv6* **color** *colorid* | **binding-sid** *bsid* } [ **end-op** *endop* ] [ **-a** *sourceaddr6* | **-c** *count* | **-m** *interval* | **-s** *packetsize* | **-t** *timeout* | **-tc** *tc* | **-h** *hoplimit* ] \* command with the **policy-name** *policyname*, **endpoint-ip** *endpointipv6* **color** *colorid*, or **binding-sid** *bsid* parameter to initiate a ping operation on the specified SRv6 TE Policy for connectivity check.
* Run the [**ping**](cmdqueryname=ping) command to check the connectivity between CEs.