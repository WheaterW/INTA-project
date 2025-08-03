Configuring EVPN L3VPN over SRv6 Flex-Algo
==========================================

This section describes how to configure EVPN L3VPN over SRv6 Flex-Algo.

#### Context

When SRv6 uses an IGP to calculate paths, it can associate locators with Flex-Algos to ensure that calculated SRv6 BE paths meet specific requirements.

EVPN L3VPN over SRv6 Flex-Algo uses forwarding paths calculated based on Flex-Algos to carry L3VPNv4/L3VPNv6 services on the public network.

On the network shown in [Figure 1](#EN-US_TASK_0279862419__fig_dc_vrp_srv6_cfg_all_001201), multiple links exist between PEs. You can configure the PEs to forward L3VPNv4/L3VPNv6 services over a path calculated using a specified Flex-Algo.

**Figure 1** EVPN L3VPN over SRv6 Flex-Algo networking  
![](figure/en-us_image_0279951879.png)

#### Pre-configuration Tasks

Before performing the configuration, complete the following tasks:

* Configure IS-IS to enable devices to communicate at the network layer.
* [Enable the advertisement of IPv6 delay information](dc_vrp_isis_cfg_0094.html) if the Flex-Algo metric type is **delay**.

#### Procedure

1. Configure Flex-Algo link attributes.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**te attribute enable**](cmdqueryname=te+attribute+enable)
      
      
      
      TE is enabled.
   3. Run [**path-constraint affinity-mapping**](cmdqueryname=path-constraint+affinity-mapping)
      
      
      
      An affinity name template is configured, and the affinity mapping view is displayed.
      
      
      
      This template must be configured on each node that is involved in path computation, and the same mappings between affinity bit values and names must be configured on each node.
   4. Run [**attribute**](cmdqueryname=attribute) *bit-name* **bit-sequence** *bit-number* Mappings between affinity bit values and names are configured.
      
      
      
      This step configures only one bit of an affinity attribute, which has a total of 128 bits. Repeat this step as needed to configure some or all of the bits.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   6. Use either of the following methods to configure Flex-Algo link attributes.
      
      
      * Inherit interface TE attributes.
        1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
           
           The interface view is displayed.
        2. Run [**te link administrative group name**](cmdqueryname=te+link+administrative+group+name) *bit-name* &<1-32>
           
           The link administrative group attribute is configured. The *bit-name* value must be in the range specified in the affinity name template.
        3. Run [**te metric**](cmdqueryname=te+metric)*metric-value*
           
           The TE metric of the link is configured.
        4. Run [**te link-attribute-application flex-algo**](cmdqueryname=te+link-attribute-application+flex-algo)
           
           The Flex-Algo link attribute application view is created and displayed.
        5. Run [**te inherit**](cmdqueryname=te+inherit)
           
           The interface TE attributes are inherited.
           
           After the [**te inherit**](cmdqueryname=te+inherit) command is run, the Flex-Algo link inherits the [**te metric**](cmdqueryname=te+metric) and [**te link administrative group name**](cmdqueryname=te+link+administrative+group+name) command configurations on the interface.
           
           In the Flex-Algo link attribute application view, the [**te inherit**](cmdqueryname=te+inherit) command is mutually exclusive from the [**metric**](cmdqueryname=metric) and [**link administrative group name**](cmdqueryname=link+administrative+group+name) commands.
      * Configure Flex-Algo link attributes separately.
        1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
           
           The interface view is displayed.
        2. Run [**te link-attribute-application flex-algo**](cmdqueryname=te+link-attribute-application+flex-algo)
           
           The Flex-Algo link attribute application view is created and displayed.
        3. Run [**link administrative group name**](cmdqueryname=link+administrative+group+name) *name-string* &<1-128>
           
           The link administrative group attribute of the Flex-Algo link is configured. The *name-string* value must be in the range specified in the affinity name template.
        4. (Optional) Run [**delay**](cmdqueryname=delay)*delay-value*
           
           The Flex-Algo link delay is configured.
        5. (Optional) Run [**metric**](cmdqueryname=metric)*metric-value*
           
           The Flex-Algo link metric is configured.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the interface view.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Configure a FAD.
   1. Run [**flex-algo identifier**](cmdqueryname=flex-algo+identifier)*flexAlgoId*
      
      
      
      A Flex-Algo is created, and the Flex-Algo view is displayed.
   2. Run [**priority**](cmdqueryname=priority)*priority-value*
      
      
      
      The priority of the Flex-Algo is configured.
      
      
      
      A larger value indicates a higher priority.
   3. Run [**metric-type**](cmdqueryname=metric-type) { **igp** | **delay** | **te** }
      
      
      
      The Metric-Type of the Flex-Algo is configured.
      
      
      
      After this command is run, links must have the corresponding metric type. Otherwise, these links will be pruned and cannot participate in IGP path calculation.
   4. Run [**affinity**](cmdqueryname=affinity) { **include-all** | **include-any** | **exclude** } { *name-string* } &<1-32>
      
      
      
      The affinity attribute of the Flex-Algo is configured.
      
      A FAD can constrain a path to include or exclude a link with a specific affinity attribute. The following three types of affinity attributes are defined for FADs:
      
      * Include-All Admin Group (**include-all**): A link is included in path calculation only if each link administrative group bit has the same name as each affinity bit.
      * Include-Any Admin Group (**include-any**): A link is included in path calculation if at least one link administrative group bit has the same name as an affinity bit.
      * Exclude Admin Group (**exclude**): A link is excluded from path calculation if any link administrative group bit has the same name as an affinity bit.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the Flex-Algo view.
3. Configure IPv6 IS-IS on each PE and P. For configuration details, see [Configuring Basic IS-IS Functions (IPv6)](dc_vrp_isis_cfg_1023.html).
4. Configure an L3VPN instance.
   
   
   
   For IPv4 services, configure an IPv4 L3VPN instance.
   
   1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      A VPN instance is created, and the VPN instance view is displayed.
   2. Run [**ipv4-family**](cmdqueryname=ipv4-family)
      
      The VPN instance IPv4 address family is enabled, and the view of this address family is displayed.
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
      
      A VPN instance is created, and the VPN instance view is displayed.
   2. Run [**ipv6-family**](cmdqueryname=ipv6-family)
      
      The VPN instance IPv6 address family is enabled, and the view of this address family is displayed.
   3. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      An RD is configured for the VPN instance IPv6 address family.
   4. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] **evpn**
      
      VPN targets are added to the VPN target list of the VPN instance IPv6 address family, so that routes of the VPN instance can be added to the routing table of the EVPN instance configured with a matching VPN target.
   5. (Optional) Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn**
      
      The EVPN routes imported to the VPN instance IPv6 address family are enabled to be associated with a tunnel policy.
   6. (Optional) Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name* **evpn**
      
      An import route-policy is applied to the VPN instance IPv6 address family to filter the routes to be imported from an EVPN instance to the address family. To precisely control the routes to be imported from the EVPN instance to the VPN instance IPv6 address family, perform this step and set attributes for eligible routes.
   7. (Optional) Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* **evpn**
      
      An export route-policy is applied to the VPN instance IPv6 address family to filter the routes to be advertised by the address family to an EVPN instance. To precisely control the routes to be advertised from the VPN instance IPv6 address family to the EVPN instance, perform this step and set attributes for eligible routes.
   8. Run [**quit**](cmdqueryname=quit)
      
      Exit the VPN instance IPv6 address family view.
   9. Run [**quit**](cmdqueryname=quit)
      
      Exit the VPN instance view.
5. Bind the L3VPN instance to an access-side interface.
   1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   2. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
      
      
      
      The L3VPN instance is bound to the interface.
   3. (Optional) Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
      
      
      
      IPv6 is enabled on the interface.
   4. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } or [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* }
      
      
      
      An IPv4/IPv6 address is configured for the interface.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the interface view.
6. Configure BGP EVPN peer relationships.
   
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
7. Configure basic SRv6 functions.
   1. (Optional) Run [**evpn srv6 next-header-field**](cmdqueryname=evpn+srv6+next-header-field) { **59** | **143** }
      
      
      
      A value is set for the Next Header field in an SRv6 extension header.
   2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      SRv6 is enabled, and the SRv6 view is displayed.
   3. Configure a source address for SRv6 encapsulation. Note that you only need to perform one of the following operations. If both of the operations are performed, the latest configuration overrides the previous one.
      
      
      * Run the [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) *ipv6-address* [ **ip-ttl** *ttl-value* ] command to directly configure a source address for SRv6 encapsulation.
      * Run the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) { *intfname* | *interfaceType* *interfaceNum* } [ **ip-ttl** *ttl-value* ] command to specify the interface to which the source address used for SRv6 encapsulation belongs.
        
        If no IPv6 global address is configured for the interface specified using the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) command, the source address for SRv6 encapsulation is not configured.
   4. Run [**locator**](cmdqueryname=locator) *locator-name* **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* | **flex-algo** *flexAlgoId* ] \*
      
      
      
      An SRv6 locator is configured.
      
      
      
      If **flex-algo** *flexAlgoId* is specified, the IGP uses the specified Flex-Algo to calculate locator routes.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      In SRv6 Flex-Algo scenarios, locators must be configured on both PEs and Ps, and IS-IS SRv6 must be enabled using the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name* command in the IS-IS view. Otherwise, SRv6 locator routes cannot be advertised, and PEs at both ends cannot learn locator routes from each other.
   5. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* { **end-dt4** | **end-dt6** } **vpn-instance** *vpn-instance-name* **evpn**
      
      
      
      An opcode for static SIDs is configured. If the device carries IPv4 services, specify the **end-dt4** parameter. If the device carries IPv6 services, specify the **end-dt6** parameter.
      
      
      
      Alternatively, run the [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt46** **vpn-instance** *vpn-instance-name* command to configure an opcode for static SIDs. This command applies to both IPv4 and IPv6 services.
      
      In EVPN scenarios, **end-dx4** and **end-dx6** are used to allocate SIDs based on the interfaces to which VPN instances are bound, and **end-dt4** and **end-dt6** are used to allocate SIDs based on VPN instances.
      
      A SID can be either dynamically allocated by BGP or manually configured. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable dynamic SID allocation through BGP or the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46) command to enable dynamic End.DT46 SID allocation through BGP in the future, skip this step.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 locator view.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 view.
8. Enable IS-IS SRv6 on the PEs and Ps, and configure IS-IS Flex-Algo.
   1. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
      
      
      
      The IS-IS view is displayed.
   2. Run [**cost-style**](cmdqueryname=cost-style) { **wide** | **compatible** | **wide-compatible** }
      
      
      
      The IS-IS wide cost type is configured.
   3. Run [**flex-algo**](cmdqueryname=flex-algo)*flexAlgoIdentifier* [ **level-1** | **level-2** | **level-1-2** ]
      
      
      
      IS-IS is enabled to advertise Flex-Algos.
   4. (Optional) Run [**flex-algo prefix-sid incr-prefix-cost**](cmdqueryname=flex-algo+prefix-sid+incr-prefix-cost) The device is enabled to count in the IS-IS cost of the loopback interface when calculating the cost of an IS-IS Flex-Algo SRv6 prefix SID route.
      
      
      
      By default, the device does not count in the IS-IS cost of the loopback interface when calculating the cost of an IS-IS Flex-Algo SRv6 prefix SID route in the same IS-IS level. After you run the [**flex-algo prefix-sid incr-prefix-cost**](cmdqueryname=flex-algo+prefix-sid+incr-prefix-cost) command, the cost of the prefix SID route covers the IS-IS cost of the loopback interface, regardless of the metric type used in Flex-Algo calculation.
      
      When a Huawei device interworks with a non-Huawei device, you can run this command to prevent loops caused by the difference in default route calculation behaviors.
   5. Run [**ipv6 enable topology ipv6**](cmdqueryname=ipv6+enable+topology+ipv6)
      
      
      
      IPv6 is enabled for the IS-IS process in the IPv6 topology.
   6. Run [**ipv6 traffic-eng**](cmdqueryname=ipv6+traffic-eng) [ **level-1** | **level-2** | **level-1-2** ]
      
      
      
      IS-IS TE is enabled.
   7. Run [**ipv6 advertise link attributes**](cmdqueryname=ipv6+advertise+link+attributes)
      
      
      
      The IS-IS process is enabled to advertise link attribute-related TLVs through LSPs. Link attributes include the IPv6 address and interface index.
   8. (Optional) Run [**ipv6 metric-delay advertisement enable**](cmdqueryname=ipv6+metric-delay+advertisement+enable) { **level-1** | **level-2** | **level-1-2** }
      
      
      
      The advertisement of IPv6 delay information is enabled.
      
      In a scenario where IS-IS Flex-Algos calculate paths based on delay information, you need to run this command to enable link delay advertisement through IS-IS.
   9. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6+%28IS-IS+view%29) **locator** *locator-name* [ **auto-sid-disable** ]
      
      
      
      IS-IS SRv6 is enabled.
   10. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the IS-IS view.
9. Configure EVPN routes on the PEs to carry SIDs and recurse to SRv6 BE paths based on the SIDs.
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

After configuring EVPN L3VPN over SRv6 Flex-Algo, verify the configuration.

* Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ *network* [ *prefix-length* ] ] command to check BGP VPNv4 route information.
* Run the [**display bgp vpnv6**](cmdqueryname=display+bgp+vpnv6) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ *network* [ *prefix-length* ] ] command to check BGP VPNv6 route information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) **all** **routing-table** **prefix-route** *prefix* command to check EVPN IP prefix route information.
* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* or [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command to check information about the VPN routes received from the remote device.
* Run the [**display isis**](cmdqueryname=display+isis+flex-algo) *process-id* **flex-algo** [ *flex-algo-id* ] [ **level-1** | **level-2** ] command to check the preferred FAD in the LSDB.
* Run the [**display isis lsdb**](cmdqueryname=display+isis+lsdb) [ { **level-1** | **level-2** } | **verbose** | { **local** | *lsp-id* | **is-name** *symbolic-name* } ] \* [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check IS-IS LSDB information.
* Run the [**display isis**](cmdqueryname=display+isis)*process-id* **route****ipv6** **flex-algo** [ *flex-algo-id* ] [ **verbose** | [ **level-1** | **level-2** ] | *ipv6-address* [ *prefix-length* ] ] \* or [**display isis route**](cmdqueryname=display+isis+route)[ *process-id* ] **ipv6** **flex-algo** [ *flex-algo-id* ] [ **verbose** | [ **level-1** | **level-2** ] | *ipv6-address* [ *prefix-length* ] ] \* command to check Flex-Algo-related IS-IS route information.
* Run the [**display isis**](cmdqueryname=display+isis)[ *process-id* ] **spf-tree** [ **systemid** *systemid* ] **ipv6 flex-algo** [ *flex-algo-id* ] [ [ **level-1** | **level-2** ] | **verbose** ] \* command to check the SPF tree topology information of a specified Flex-Algo.