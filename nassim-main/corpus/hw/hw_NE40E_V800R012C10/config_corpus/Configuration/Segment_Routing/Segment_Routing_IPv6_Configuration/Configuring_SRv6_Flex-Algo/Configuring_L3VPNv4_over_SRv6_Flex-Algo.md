Configuring L3VPNv4 over SRv6 Flex-Algo
=======================================

This section describes how to configure L3VPNv4 over SRv6 Flex-Algo.

#### Context

When SRv6 uses an IGP to calculate paths, it can associate locators with Flex-Algos to ensure that calculated SRv6 BE paths meet specific requirements.

L3VPNv4 over SRv6 Flex-Algo uses forwarding paths calculated based on Flex-Algos to carry L3VPNv4 services on the public network.

On the network shown in [Figure 1](#EN-US_TASK_0279788926__fig_dc_vrp_srv6_cfg_all_001201), multiple links exist between PEs. You can configure the PEs to forward L3VPNv4 services over a path calculated using a specified Flex-Algo.

**Figure 1** L3VPNv4 over SRv6 Flex-Algo networking  
![](figure/en-us_image_0279946435.png)

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
4. Configure a VPN instance on each PE and enable the IPv4 address family for the instance.
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
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the VPN instance IPv4 address family view.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the VPN instance view.
   9. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The view of the interface to be bound to the VPN instance is displayed.
   10. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
       
       
       
       The interface is bound to the VPN instance.
       
       
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) command deletes IPv4 and IPv6 Layer 3 configurations on the interface, such as the configured IP addresses and routing protocols. You have to reconfigure them if they are required.
   11. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
       
       
       
       An IP address is configured for the interface.
       
       
       
       Layer 3 features such as PE-CE route exchange can be configured for PE-CE communication only after an IP address is configured for the involved VPN interface.
   12. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
   13. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the interface view.
5. Establish an MP-IBGP peer relationship between the PEs.
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
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP VPNv4 address family view.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
6. Configure basic SRv6 functions.
   1. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      SRv6 is enabled, and the SRv6 view is displayed.
   2. Configure a source address for SRv6 encapsulation. Note that you only need to perform one of the following operations. If both of the operations are performed, the latest configuration overrides the previous one.
      
      
      * Run the [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) *ipv6-address* [ **ip-ttl** *ttl-value* ] command to directly configure a source address for SRv6 encapsulation.
      * Run the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) { *intfname* | *interfaceType* *interfaceNum* } [ **ip-ttl** *ttl-value* ] command to specify the interface to which the source address used for SRv6 encapsulation belongs.
        
        If no IPv6 global address is configured for the interface specified using the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) command, the source address for SRv6 encapsulation is not configured.
   3. Run [**locator**](cmdqueryname=locator) *locator-name* **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* | **flex-algo** *flexAlgoId* ] \*
      
      
      
      An SRv6 locator is configured.
      
      
      
      If **flex-algo** *flexAlgoId* is specified, the IGP uses the specified Flex-Algo to calculate locator routes.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      In SRv6 Flex-Algo scenarios, locators must be configured on both PEs and Ps, and IS-IS SRv6 must be enabled using the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name* command in the IS-IS view. Otherwise, SRv6 locator routes cannot be advertised, and PEs at both ends cannot learn locator routes from each other.
   4. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt4** **vpn-instance** *vpn-instance-name* or [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt46** **vpn-instance** *vpn-instance-name*
      
      
      
      An opcode for static SIDs is configured.
      
      
      
      A SID can be either dynamically allocated by BGP or manually configured. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable dynamic End.DT4 SID allocation through BGP or the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46) command to enable dynamic End.DT46 SID allocation through BGP in the future, skip this step.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 locator view.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 view.
7. Enable IS-IS SRv6 on the PEs and Ps, and configure IS-IS Flex-Algo.
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
   9. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name* [ **auto-sid-disable** ]
      
      
      
      IS-IS SRv6 is enabled.
   10. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the IS-IS view.
8. Configure each PE to carry SIDs in VPN routes and recurse the routes to SRv6 BE paths based on the SIDs.
   1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
      
      
      
      The BGP view is displayed.
   2. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4**
      
      
      
      The BGP VPNv4 address family view is displayed.
   3. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *peerGroupName* } **prefix-sid** [ **sid-type5**[**advertise-srv6-locator** ] ]
      
      
      
      The device is enabled to exchange IPv4 prefix SIDs with the specified IPv6 peer.
      
      
      
      In a scenario where BFD is used to check locator reachability and the P nodes between local and remote PEs summarize locator routes, you can specify the **advertise-srv6-locator** parameter to enable PE-advertised BGP routes to carry locator length information. In this way, when the peer IPv6 address bound to the BFD session matches the locator's IPv6 address, locator reachability can be checked using BFD to complete VPN FRR or auto FRR path switching.
      
      If *peerGroupName* is specified, the command configuration takes effect on all peers in the specified peer group.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP VPNv4 address family view.
   5. Configure the device to add SIDs to VPN routes. Note that you need to perform configurations only in one of the following two views. If you perform configurations in both views, the configurations in these views are mutually exclusive.
      
      
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
   6. Run [**segment-routing ipv6 best-effort**](cmdqueryname=segment-routing+ipv6+best-effort)
      
      
      
      The device is enabled to recurse VPN routes based on the SIDs carried in the routes.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After configuring L3VPNv4 over SRv6 Flex-Algo, verify the configuration.

* Run the [**display segment-routing ipv6 locator**](cmdqueryname=display+segment-routing+ipv6+locator) [ *locator-name* ] **verbose** command to check SRv6 locator information.
* Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) { **end** | **end-x** | **end-dt4** | **end-dt46** } [ *sid* ] **forwarding** command to check information about the SRv6 local SID table.
* Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ *network* [ *prefix-length* ] ] command to check BGP VPNv4 route information.
* Run the [**display isis**](cmdqueryname=display+isis+flex-algo) *process-id* **flex-algo** [ *flex-algo-id* ] [ **level-1** | **level-2** ] command to check the preferred FAD in the LSDB.
* Run the [**display isis lsdb**](cmdqueryname=display+isis+lsdb) [ { **level-1** | **level-2** } | **verbose** | { **local** | *lsp-id* | **is-name** *symbolic-name* } ] \* [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check IS-IS LSDB information.
* Run the [**display isis**](cmdqueryname=display+isis)*process-id* **route****ipv6** **flex-algo** [ *flex-algo-id* ] [ **verbose** | [ **level-1** | **level-2** ] | *ipv6-address* [ *prefix-length* ] ] \* or [**display isis route**](cmdqueryname=display+isis+route)[ *process-id* ] **ipv6** **flex-algo** [ *flex-algo-id* ] [ **verbose** | [ **level-1** | **level-2** ] | *ipv6-address* [ *prefix-length* ] ] \* command to check Flex-Algo-related IS-IS route information.
* Run the [**display isis**](cmdqueryname=display+isis)[ *process-id* ] **spf-tree** [ **systemid** *systemid* ] **ipv6 flex-algo** [ *flex-algo-id* ] [ [ **level-1** | **level-2** ] | **verbose** ] \* command to check the SPF tree topology information of a specified Flex-Algo.
* Run the [**ping**](cmdqueryname=ping) command to check the connectivity between CEs.