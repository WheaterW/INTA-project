Configuring EVPN L3VPNv6 over SRv6 TE Policy
============================================

This section describes how to configure EVPN L3VPNv6 over SRv6 TE Policy so that EVPN L3VPNv6 services can be carried over SRv6 TE Policies.

#### Usage Scenario

EVPN L3VPNv6 over SRv6 TE Policy uses public SRv6 TE Policies to carry EVPN L3VPNv6 services. As shown in [Figure 1](#EN-US_TASK_0297800925__en-us_task_0179342421_fig_dc_vrp_evpn_cfg_015201), PE1 and PE2 communicate through an IPv6 public network. An SRv6 TE Policy is deployed on the network to carry EVPN L3VPNv6 services.

**Figure 1** EVPN L3VPNv6 over SRv6 TE Policy networking  
![](figure/en-us_image_0255966864.png)

#### Pre-configuration Tasks

Before configuring EVPN L3VPNv6 over SRv6 TE Policy, complete the following tasks:

* [Configure an SRv6 TE Policy manually](dc_vrp_srv6_cfg_all_0110.html) or [use a controller to dynamically deliver an SRv6 TE Policy](dc_vrp_srv6_cfg_all_0116.html).

#### Procedure

1. Configure an L3VPN instance.
   
   
   1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      A VPN instance is created, and the VPN instance view is displayed.
   2. Run [**ipv6-family**](cmdqueryname=ipv6-family)
      
      The VPN instance IPv6 address family is enabled, and the view of this address family is displayed.
   3. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      An RD is configured for the VPN instance IPv6 address family.
   4. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] **evpn**
      
      VPN targets are added to the VPN target list of the VPN instance IPv6 address family, so that routes of the VPN instance can be added to the routing table of the EVPN instance configured with a matching VPN target.
   5. (Optional) Run [**default-color**](cmdqueryname=default-color) *color-value* **evpn**
      
      The default color value is specified for the L3VPNv6 service to recurse to an SRv6 TE Policy.
      
      If a remote EVPN route without carrying the Color Extended Community is leaked to a local VPN instance, the default color value is used for the recursion.
   6. (Optional) Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name* **evpn**
      
      An import route-policy is applied to the VPN instance IPv6 address family to filter the routes to be imported from an EVPN instance to the address family. To precisely control the routes to be imported from the EVPN instance to the VPN instance IPv6 address family, perform this step and set attributes for eligible routes.
   7. (Optional) Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* **evpn**
      
      An export route-policy is applied to the VPN instance IPv6 address family to filter the routes to be advertised by the address family to an EVPN instance. To precisely control the routes to be advertised from the VPN instance IPv6 address family to the EVPN instance, perform this step and set attributes for eligible routes.
   8. Run [**quit**](cmdqueryname=quit)
      
      Exit the VPN instance IPv6 address family view.
   9. Run [**quit**](cmdqueryname=quit)
      
      Exit the VPN instance view.
   
   1. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Bind the L3VPN instance to an access-side interface.
   1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   2. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
      
      
      
      The L3VPN instance is bound to the interface.
   3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
      
      
      
      IPv6 is enabled on the interface.
   4. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* }
      
      
      
      An IPv6 address is configured for the interface.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the interface view.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
3. Configure BGP EVPN peers.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a BGP RR needs to be configured on the network, establish BGP EVPN peer relationships between all the PEs and the RR.
   
   
   
   1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
      
      
      
      BGP is enabled, and the BGP view is displayed.
   2. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } **as-number** { *as-number-plain* | *as-number-dot* }
      
      
      
      The remote PE is configured as a peer.
   3. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } **connect-interface** *interface-type* *interface-number*
      
      
      
      A source interface and a source address are specified to set up a TCP connection with the BGP peer.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If loopback interfaces are used to establish a BGP connection, you are advised to run the [**peer connect-interface**](cmdqueryname=peer+connect-interface) command on both ends to ensure the connectivity. If this command is run on one end only, the BGP connection may fail to be established.
   4. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv6 address family view is displayed.
   5. Run [**import-route**](cmdqueryname=import-route) { **direct** | **isis** *process-id* | **static** | **ospfv3** *process-id* | **ripng** *process-id* } [ **med** *med* | **route-policy** *route-policy-name* ] \*
      
      
      
      Routes of other protocols are imported to the BGP-VPN instance IPv6 address family. To advertise host IP routes, configure import of direct routes. To advertise routes on the network segment where the host resides, use a dynamic routing protocol (such as OSPFv3) to advertise routes on the network segment and then perform this step to import the routes of the dynamic routing protocol.
   6. Run [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn) [ **import-route-multipath** ]
      
      
      
      The device is enabled to advertise IP prefix routes. IP prefix routes are used to advertise host IP routes as well as routes on the network segment where the host resides.
      
      
      
      To implement SID-based load balancing, specify the **import-route-multipath** parameter for the device to advertise all IP prefix routes with the same destination address.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-VPN instance IPv6 address family view.
   8. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP EVPN address family view is displayed.
   9. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } **enable**
      
      
      
      The device is enabled to exchange EVPN routes with the specified peer or peer group.
   10. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } **advertise encap-type** **srv6** [ **advertise-srv6-locator** ]
       
       
       
       The device is enabled to send locator information and EVPN routes carrying SRv6-encapsulated attributes to the specified peer or peer group.
   11. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP EVPN address family view.
   12. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP view.
   13. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
4. On each PE, configure EVPN L3VPNv6 services to recurse to an SRv6 TE Policy.
   1. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      SRv6 is enabled, and the SRv6 view is displayed.
   2. Configure a source address for SRv6 encapsulation. Note that you only need to perform one of the following operations. If both of the operations are performed, the latest configuration overrides the previous one.
      
      
      * Run the [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) *ipv6-address* [ **ip-ttl** *ttl-value* ] command to directly configure a source address for SRv6 encapsulation.
      * Run the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) { *intfname* | *interfaceType* *interfaceNum* } [ **ip-ttl** *ttl-value* ] command to specify the interface to which the source address used for SRv6 encapsulation belongs.
        
        If no IPv6 global address is configured for the interface specified using the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) command, the source address for SRv6 encapsulation is not configured.
   3. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ]
      
      
      
      An SRv6 locator is configured.
   4. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt6** **vpn-instance** *vpn-instance-name* **evpn** or [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt46** **vpn-instance** *vpn-instance-name*
      
      
      
      An opcode for static SIDs is configured.
      
      
      
      Alternatively, run the [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dx6** **vpn-instance** *vpn-instance-name* **evpn** **interface** *interface-type* *interface-number* **nexthop** *nexthop-address* command to configure an opcode for static SIDs.
      
      In EVPN scenarios, **end-dx6** is used to allocate SIDs based on the interfaces to which VPN instances are bound, and **end-dt6** is used to allocate SIDs based on VPN instances.
      
      A SID can be either dynamically allocated by BGP or manually configured. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable dynamic End.DT6 SID allocation through BGP or the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46) command to enable dynamic End.DT46 SID allocation through BGP in the future, skip this step.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 locator view.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 view.
   7. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
      
      
      
      The BGP view is displayed.
   8. Enable the device to add SIDs to VPN routes to be sent to EVPN. Note that you need to perform configurations only in one of the following two views. If you perform configurations in both views, the configurations in these views are mutually exclusive.
      
      
      * Configurations in the BGP-VPN instance IPv6 address family view
        + Run the [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv6 address family view.
        + Run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* **evpn** command to enable the device to add SIDs to VPN routes to be sent to EVPN.
      * Configurations in the BGP-VPN instance view
        + Run the **vpn-instance** *vpn-instance-name* command to create a BGP-VPN instance and enter the BGP-VPN instance view.
        + Run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* **end-dt46** command to enable the device to add SIDs to VPN routes to be sent to EVPN.
   9. Run [**segment-routing ipv6 traffic-engineer**](cmdqueryname=segment-routing+ipv6+traffic-engineer) [ **best-effort** ] **evpn**
      
      
      
      The function to recurse EVPN L3VPNv6 services to SRv6 TE Policies is enabled.
      
      If an SRv6 BE path exists on the network, you can set the **best-effort** parameter, allowing the SRv6 BE path to function as a best-effort path in the case of an SRv6 TE Policy fault.
   10. (Optional) Run [**segment-routing ipv6 color-only evpn**](cmdqueryname=segment-routing+ipv6+color-only+evpn)
       
       
       
       The device is enabled to recurse EVPN L3VPNv6 services to color-only SRv6 TE Policies.
       
       
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       This command applies only to color-only scenarios and supports only statically configured SRv6 TE Policies.
   11. (Optional) Configure the device to allocate SIDs to BGP VPN IPv6 routes based on next hops, thereby implementing SID-based load balancing.
       
       
       * To configure the device to allocate SIDs to BGP VPN IPv6 routes based on all next hops, run the [**segment-routing ipv6 apply-sid all-nexthop evpn**](cmdqueryname=segment-routing+ipv6+apply-sid+all-nexthop+evpn) command.
       * To configure the device to allocate a SID to a BGP VPN IPv6 route with a specified next hop, run the [**segment-routing ipv6 apply-sid specify-nexthop evpn**](cmdqueryname=segment-routing+ipv6+apply-sid+specify-nexthop+evpn) command. Then, run the [**nexthop**](cmdqueryname=nexthop) *nexthop-address* [**interface**](cmdqueryname=interface) { *interface-name* | *interfaceType* *interfaceNum* } command to specify a next hop and an outbound interface.
   12. Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
   13. Run [**quit**](cmdqueryname=quit) Return to the system view.
   14. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name* A tunnel policy is created, and the tunnel policy view is displayed.
   15. (Optional) Run [**description**](cmdqueryname=description) *description-text* A description is configured for the tunnel policy.
   16. Run [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) **ipv6 srv6-te-policy** **load-balance-number** *loadBalanceNumber* The tunnel selection sequence and the number of tunnels for load balancing are configured.
   17. Run [**quit**](cmdqueryname=quit) Exit the tunnel policy view.
   18. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* The VPN instance view is displayed.
   19. Run [**ipv6-family**](cmdqueryname=ipv6-family) The VPN instance IPv6 address family view is displayed.
   20. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn** A tunnel policy is applied to the EVPN L3VPN instance.
   21. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.

#### Verifying the Configuration

After configuring EVPN L3VPNv6 over SRv6 TE Policy, verify the configuration.

* Run the [**display bgp vpnv6**](cmdqueryname=display+bgp+vpnv6) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ *network* [ *prefix-length* ] ] command to check BGP VPNv6 route information. The command output shows that the value of **Relay Tunnel Out-Interface** is **SRv6 TE Policy**.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) **all** **routing-table** **prefix-route** *prefix* command to check EVPN IP prefix route information.
* Run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command to check information about IPv6 VPN routes received from the remote end.
* Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance)*vpn-instance-name* **tunnel-info nexthop** *nexthopIpv6Addr* command to check information about the tunnel to which the route with the specified next hop recurses in each address family of the current VPN instance.