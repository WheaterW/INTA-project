Configuring EVPN L3VPN over OSPFv3 SRv6 BE
==========================================

This section describes how to configure EVPN L3VPN over SRv6 BE.

#### Usage Scenario

EVPN L3VPN over SRv6 BE uses SRv6 BE on a public network to carry EVPN L3VPN services. The key implementation of EVPN L3VPN over SRv6 BE involves deploying SRv6 BE, advertising EVPN routes, and forwarding data.

[Figure 1](#EN-US_TASK_0000001142686294__fig_dc_vrp_evpn_cfg_015201) shows an example where an IPv6 public network is established between PE1 and PE2. SRv6 BE is deployed on the IPv6 public network to carry EVPN L3VPN services.

**Figure 1** EVPN L3VPN over SRv6 BE networking  
![](figure/en-us_image_0000001188726077.png)

#### Pre-configuration Tasks

Before configuring EVPN L3VPN over SRv6 BE, complete the following tasks:

* Configure a link layer protocol.
* Configure network-layer addresses for interfaces to ensure that neighboring devices are reachable at the network layer.

#### Procedure

1. Configure OSPFv3 on each PE and P. For configuration details, see [Configuring Basic OSPFv3 Functions](dc_vrp_ospfv3_cfg_2003.html).
2. Configure an L3VPN instance.
   
   
   
   For IPv4 services, configure an IPv4 L3VPN instance.
   
   1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      A VPN instance is created, and its view is displayed.
   2. Run [**ipv4-family**](cmdqueryname=ipv4-family)
      
      The VPN instance IPv4 address family is enabled, and its view is displayed.
   3. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      An RD is configured for the VPN instance IPv4 address family.
   4. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] **evpn**
      
      VPN targets are added to the VPN target list of the VPN instance IPv4 address family, so that routes of the VPN instance can be added to the routing table of the EVPN instance configured with a matching VPN target.
   5. (Optional) Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn**
      
      The specified tunnel policy is associated with EVPN routes leaked to the VPN instance IPv4 address family.
   6. (Optional) Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name* **evpn**
      
      An import route-policy is applied to the VPN instance IPv4 address family to filter the routes to be imported from an EVPN instance to the address family. To precisely control the routes to be imported from the EVPN instance to the VPN instance IPv4 address family, perform this step and set attributes for eligible routes.
   7. (Optional) Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* **evpn**
      
      An export route-policy is applied to the VPN instance IPv4 address family to filter the routes to be advertised by the address family to an EVPN instance. To precisely control the routes to be advertised from the VPN instance IPv4 address family to the EVPN instance, perform this step and set attributes for eligible routes.
   8. Run [**quit**](cmdqueryname=quit)
      
      Exit the VPN instance IPv4 address family view.
   9. Run [**quit**](cmdqueryname=quit)
      
      Exit the VPN instance view.
   
   For IPv6 services, configure an IPv6 L3VPN instance.
   
   1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      A VPN instance is created, and its view is displayed.
   2. Run [**ipv6-family**](cmdqueryname=ipv6-family)
      
      The VPN instance IPv6 address family is enabled, and its view is displayed.
   3. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      An RD is configured for the VPN instance IPv6 address family.
   4. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] **evpn**
      
      VPN targets are added to the VPN target list of the VPN instance IPv6 address family, so that routes of the VPN instance can be added to the routing table of the EVPN instance configured with a matching VPN target.
   5. (Optional) Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn**
      
      The specified tunnel policy is associated with EVPN routes leaked to the VPN instance IPv6 address family.
   6. (Optional) Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name* **evpn**
      
      An import route-policy is applied to the VPN instance IPv6 address family to filter the routes to be imported from an EVPN instance to the address family. To precisely control the routes to be imported from the EVPN instance to the VPN instance IPv6 address family, perform this step and set attributes for eligible routes.
   7. (Optional) Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* **evpn**
      
      An export route-policy is applied to the VPN instance IPv6 address family to filter the routes to be advertised by the address family to an EVPN instance. To precisely control the routes to be advertised from the VPN instance IPv6 address family to the EVPN instance, perform this step and set attributes for eligible routes.
   8. Run [**quit**](cmdqueryname=quit)
      
      Exit the VPN instance IPv6 address family view.
   9. Run [**quit**](cmdqueryname=quit)
      
      Exit the VPN instance view.
3. Bind the L3VPN instance to an access-side interface.
   1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   2. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
      
      
      
      The interface is bound to the VPN instance.
   3. (Optional) Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
      
      
      
      IPv6 is enabled on the interface.
   4. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } or [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* }
      
      
      
      An IPv4/IPv6 address is configured for the interface.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the interface view.
4. Configure BGP EVPN peer relationships.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a BGP RR needs to be deployed on the network, establish BGP EVPN peer relationships between all the PEs and the RR.
   
   
   
   1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
      
      
      
      BGP is enabled, and the BGP view is displayed.
   2. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } **as-number** { *as-number-plain* | *as-number-dot* }
      
      
      
      The remote PE is configured as a peer.
   3. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } **connect-interface** *interface-type* *interface-number*
      
      
      
      A source interface and a source address are specified to set up a TCP connection with the BGP peer.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If loopback interfaces are used to establish a BGP connection, you are advised to run the [**peer connect-interface**](cmdqueryname=peer+connect-interface) command on both ends to ensure connectivity. If this command is run on one end only, the BGP connection may fail to be established.
   4. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* or [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv4/IPv6 address family view is displayed.
   5. Run [**import-route**](cmdqueryname=import-route) { **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** | **ospfv3** *process-id* | **ripng** *process-id* } [ **med** *med* | **route-policy** *route-policy-name* ] \*
      
      
      
      Other protocol routes are imported to the BGP-VPN instance IPv4/IPv6 address family. To advertise host IP routes, you only need to configure import of direct routes. To advertise the subnet route of the host, use a dynamic routing protocol (such as OSPF) to advertise the route and then perform this step to import the routes of the dynamic routing protocol.
   6. Run [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn) [ **import-route-multipath** ]
      
      
      
      The device is enabled to advertise IP prefix routes. This type of route can be used to advertise host IP routes as well as the routes on the subnet where the device resides.
      
      
      
      To implement SID-based load balancing, specify the **import-route-multipath** parameter for the device to advertise all IP prefix routes with the same destination address.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-VPN instance IPv4/IPv6 address family view.
   8. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP EVPN address family view is displayed.
   9. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } **enable**
      
      
      
      The device is enabled to exchange EVPN routes with a specified peer or peer group.
   10. (Optional) Run [**nexthop recursive-lookup default-route**](cmdqueryname=nexthop+recursive-lookup+default-route)
       
       
       
       The device is enabled to send packets over a default route when the recursive next-hop address is unavailable.
       
       
       
       In an EVPN over SRv6 BE scenario, problems such as configuration errors or faults may cause the PE at one end to fail to recurse services to SRv6 BE due to route unreachability, resulting in a service forwarding failure. To prevent this, run the [**nexthop recursive-lookup default-route**](cmdqueryname=nexthop+recursive-lookup+default-route) command on the local PE and configure the remote PE to send a default route to the local PE. In this way, if the next hop of a specific route on the local PE is unreachable, services can be steered to an SRv6 BE path through recursion to the default route, ensuring service continuity.
   11. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP EVPN address family view.
   12. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP view.
   13. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
5. Configure basic SRv6 functions.
   1. (Optional) Run [**evpn srv6 next-header-field**](cmdqueryname=evpn+srv6+next-header-field) { **59** | **143** }
      
      
      
      A value is set for the Next Header field in an SRv6 extension header.
   2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      SRv6 is enabled, and the SRv6 view is displayed.
   3. Configure a source address for SRv6 encapsulation. Note that you only need to perform one of the following operations. If both of the operations are performed, the latest configuration overrides the previous one.
      
      
      * Run the [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) *ipv6-address* [ **ip-ttl** *ttl-value* ] command to directly configure a source address for SRv6 encapsulation.
      * Run the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) { *intfname* | *interfaceType* *interfaceNum* } [ **ip-ttl** *ttl-value* ] command to specify the interface to which the source address used for SRv6 encapsulation belongs.
        
        If no IPv6 global address is configured for the interface specified using the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) command, the source address for SRv6 encapsulation is not configured.
   4. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ]
      
      
      
      An SRv6 locator is configured.
   5. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* { **end-dt4** | **end-dt6** } **vpn-instance** *vpn-instance-name* **evpn**
      
      
      
      An opcode for static SIDs is configured. If the device carries IPv4 services, specify the **end-dt4** parameter. If the device carries IPv6 services, specify the **end-dt6** parameter.
      
      
      
      Alternatively, run the [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt46** **vpn-instance** *vpn-instance-name* command to configure an opcode for static SIDs. This command applies to both IPv4 and IPv6 services.
      
      In EVPN scenarios, **end-dx4** and **end-dx6** are used to allocate SIDs based on the interfaces to which VPN instances are bound, and **end-dt4** and **end-dt6** are used to allocate SIDs based on VPN instances.
      
      A SID can be either dynamically allocated by BGP or manually configured. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable dynamic SID allocation through BGP or the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46) command to enable dynamic End.DT46 SID allocation through BGP in the future, skip this step.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 locator view.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 view.
6. Enable OSPFv3 SRv6 on the PEs.
   1. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
      
      
      
      The OSPFv3 process view is displayed.
   2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name* [ **auto-sid-disable** ]
      
      
      
      OSPFv3 SRv6 is enabled.
   3. (Optional) Run [**segment-routing ipv6 compatible locator-fixed-length**](cmdqueryname=segment-routing+ipv6+compatible+locator-fixed-length)
      
      
      
      A fixed length is configured for the Locator field in the SRv6 Locator TLV carried in an SRv6 Locator LSA.
      
      
      
      As defined in *draft-ietf-lsr-ospfv3-srv6-extensions-12* and later versions, the length of the Locator field in the SRv6 Locator TLV carried in an SRv6 Locator LSA is variable. To facilitate the interworking between protocols defining different lengths for the Locator field, you can run this command to configure the Locator field to be fixed at 128 bits.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the OSPFv3 process view.
7. Configure EVPN routes on the PEs to carry SIDs and recurse to SRv6 BE paths based on the SIDs.
   1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
      
      
      
      The BGP view is displayed.
   2. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP EVPN address family view is displayed.
   3. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } **advertise encap-type** **srv6** [ **advertise-srv6-locator** ]
      
      
      
      The device is enabled to send EVPN routes carrying SRv6-encapsulated attributes to the specified peer or peer group.
      
      
      
      In a scenario where BFD is used to check locator reachability, if locator routes are summarized by a P device between local and remote PEs, the remote PE can learn only the summary locator route, not the locator on the local PE. This leads to a BFD failure. To address this issue, specify the **advertise-srv6-locator** parameter in the command to allow the local PE to carry locator length information in the EVPN route to be advertised to the remote PE. In this way, after receiving the EVPN route, the remote PE can calculate the locator on the local PE, enabling BFD to take effect.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP EVPN address family view.
   5. Enable the device to add SIDs to VPN routes to be sent to EVPN. Note that you need to perform configurations only in one of the following two views. If you perform configurations in both views, the configurations in these views are mutually exclusive.
      
      
      * Configurations in the BGP-VPN instance IPv4/IPv6 address family view
        + Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* or [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv4/IPv6 address family view.
        + Run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* **evpn** command to enable the device to add SIDs to VPN routes to be sent to EVPN.
        + Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
      * Configurations in the BGP-VPN instance view
        + Run the [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* command to create a BGP-VPN instance and enter its view.
        + Run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* **end-dt46** command to enable the device to add SIDs to VPN routes to be sent to EVPN.
        + Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
   6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* or [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv4/IPv6 address family view is displayed.
   7. Run [**segment-routing ipv6 best-effort evpn**](cmdqueryname=segment-routing+ipv6+best-effort+evpn)
      
      
      
      The device is enabled to perform route recursion based on the SIDs carried by EVPN routes.
   8. (Optional) Configure the device to allocate SIDs to BGP VPN routes based on next hops, thereby implementing SID-based load balancing.
      
      
      
      To configure the device to allocate SIDs to BGP VPN routes based on all next hops:
      
      
      
      * For EVPN L3VPNv4 services, run the [**segment-routing ipv6 apply-sid all-nexthop evpn**](cmdqueryname=segment-routing+ipv6+apply-sid+all-nexthop+evpn) command in the BGP-VPN instance IPv4 address family view.
      * For EVPN L3VPNv6 services, run the [**segment-routing ipv6 apply-sid all-nexthop evpn**](cmdqueryname=segment-routing+ipv6+apply-sid+all-nexthop+evpn) command in the BGP-VPN instance IPv6 address family view.
      
      To configure the device to allocate a SID to a BGP VPN route with a specified next hop:
      
      * For EVPN L3VPNv4 services, run the [**segment-routing ipv6 apply-sid specify-nexthop evpn**](cmdqueryname=segment-routing+ipv6+apply-sid+specify-nexthop+evpn) command in the BGP-VPN instance IPv4 address family view, and then run the [**nexthop**](cmdqueryname=nexthop) *nexthop-address* [**interface**](cmdqueryname=interface) { *interface-name* | *interfaceType* *interfaceNum* } command to specify a next hop and an outbound interface.
      * For EVPN L3VPNv6 services, run the [**segment-routing ipv6 apply-sid specify-nexthop evpn**](cmdqueryname=segment-routing+ipv6+apply-sid+specify-nexthop+evpn) command in the BGP-VPN instance IPv6 address family view, and then run the [**nexthop**](cmdqueryname=nexthop) *nexthop-address* [**interface**](cmdqueryname=interface) { *interface-name* | *interfaceType* *interfaceNum* } command to specify a next hop and an outbound interface.
   9. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After configuring EVPN L3VPN over SRv6 BE, verify the configuration.

* Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ *network* [ *prefix-length* ] ] command to check BGP VPN route information.
* Run the [**display bgp vpnv6**](cmdqueryname=display+bgp+vpnv6) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ *network* [ *prefix-length* ] ] command to check BGP VPNv6 route information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) **all** **routing-table** **prefix-route** *prefix* command to check EVPN IP prefix route information.
* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* or [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command to check information about the VPN routes received from the remote device.