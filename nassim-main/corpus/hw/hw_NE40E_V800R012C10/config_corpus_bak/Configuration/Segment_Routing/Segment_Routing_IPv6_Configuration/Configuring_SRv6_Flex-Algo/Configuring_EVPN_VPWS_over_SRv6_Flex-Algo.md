Configuring EVPN VPWS over SRv6 Flex-Algo
=========================================

This section describes how to configure EVPN VPWS over SRv6 Flex-Algo.

#### Context

EVPN VPWS uses the EVPN E-Line model to carry P2P VPWS services.

EVPN VPWS over SRv6 Flex-Algo uses forwarding paths calculated based on Flex-Algos to carry VPWS services on the public network.

On the network shown in [Figure 1](#EN-US_TASK_0279862420__fig_dc_vrp_srv6_cfg_all_001201), multiple links exist between PEs. You can configure the PEs to forward VPWS services over a path calculated using a specified Flex-Algo.

**Figure 1** EVPN VPWS over SRv6 Flex-Algo networking  
![](figure/en-us_image_0279955299.png)

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
4. Configure EVPN and EVPL instances on each PE.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**evpn source-address**](cmdqueryname=evpn+source-address) *ip-address*
      
      
      
      An EVPN source address is configured.
      
      
      
      In scenarios where a CE is dual-homed or multi-homed to PEs, you need to configure an EVPN source address on each PE to generate route distinguishers (RDs) for Ethernet segment routes and Ethernet auto-discovery per ES routes.
   3. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **vpws**
      
      
      
      A VPWS EVPN instance is created, and the VPWS-EVPN instance view is displayed.
   4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      
      
      An RD is configured for the EVPN instance.
      
      
      
      An EVPN instance takes effect only after an RD is configured for it. The RDs of different EVPN instances on the same PE must be different.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If you need to create a large number of EVPN instances and plan a large number of RDs, you can run the **evpn route-distinguisher auto** *rd-ip* command in the system view to enable automatic RD allocation, thereby avoiding RD conflicts. The *rd-ip* parameter specifies an IPv4 address, enabling a device to allocate RDs in the format of *X.X.X.X*:*index* to all EVPN instances that are not allocated with RDs. *X.X.X.X* indicates a user-defined RD-IP value, and *index* is a 2-byte value automatically allocated by the system in the range from 1 to 65535.
   5. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
      
      
      
      VPN targets are configured for the EVPN instance.
      
      
      
      VPN targets are BGP extended community attributes used to control the receiving and advertisement of EVPN routes. A maximum of eight VPN targets can be configured using the [**vpn-target**](cmdqueryname=vpn-target) command. To configure more VPN targets for an EVPN instance address family, run the [**vpn-target**](cmdqueryname=vpn-target) command multiple times.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      An RT of an Ethernet segment route is generated using the middle six bytes of an ESI. For example, if the ESI is 0011.1001.1001.1001.1002, the Ethernet segment route uses 11.1001.1001.10 as its RT.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   7. Run [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id*
      
      
      
      An EVPL instance is created, and the EVPL instance view is displayed.
   8. Run [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name*
      
      
      
      A specified EVPN instance that works in VPWS mode is bound to the current EVPL instance.
   9. Run [**local-service-id**](cmdqueryname=local-service-id) *service-id* [**remote-service-id**](cmdqueryname=remote-service-id) *service-id*
      
      
      
      The packets of the current EVPL instance are configured to carry the local and remote service IDs.
   10. (Optional) Run [**mtu-match ignore**](cmdqueryname=mtu-match+ignore)
       
       
       
       The MTU matching check is ignored for the EVPL instance. In scenarios where a Huawei device interworks with a non-Huawei device through an EVPN VPWS, if the non-Huawei device does not support any MTU matching check for an EVPL instance, run the [**mtu-match ignore**](cmdqueryname=mtu-match+ignore) command to ignore the MTU matching check.
   11. (Optional) Run [**load-balancing ignore-esi**](cmdqueryname=load-balancing+ignore-esi)
       
       
       
       The device is enabled to ignore the ESI validity check during EVPL instance load balancing.
       
       
       
       In an EVPN VPWS scenario where active-active protection is deployed, if each access-side device is single-homed to an aggregation-side device and no ESI is configured on the access interface, to implement active-active load balancing, you can run this command on the aggregation-side device to enable the device to ignore the ESI validity check during EVPL instance load balancing.
   12. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
5. Configure an AC interface.
   1. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2**
      
      
      
      A Layer 2 sub-interface is created, and the sub-interface view is displayed.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Before running this command, ensure that the corresponding Layer 2 main interface does not have the [**port link-type**](cmdqueryname=port+link-type) **dot1q-tunnel** command configuration. If this configuration exists, run the [**undo port link-type**](cmdqueryname=undo+port+link-type) command to delete the configuration.
      
      In addition to a Layer 2 sub-interface, an Ethernet main interface, Layer 3 sub-interface, or Eth-Trunk interface can also function as an AC interface.
   2. Run [**encapsulation**](cmdqueryname=encapsulation) { **dot1q** [ **vid** *low-pe-vid* [ **to** *high-pe-vid* ] ] | **untag** | **qinq** [ **vid** *pe-vid* **ce-vid** { *low-ce-vid* [ **to** *high-ce-vid* ] | **default** } ] }
      
      
      
      An encapsulation type is configured for packets allowed to pass through the sub-interface.
   3. Run [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id*
      
      
      
      A specified EVPL instance is bound to the Layer 2 sub-interface.
   4. (Optional) Run [**evpn-vpws ignore-ac-state**](cmdqueryname=evpn-vpws+ignore-ac-state)
      
      
      
      The interface is enabled to ignore the AC status.
      
      
      
      On a network with primary and backup links, if CFM is associated with an AC interface, run this command to ensure EVPN VPWS continuity. When the AC status of the interface becomes down, a primary/backup link switchover is triggered. As the interface has been enabled to ignore the AC status using this command, the EVPN VPWS does not need to be re-established during the link switchover.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the Layer 2 sub-interface view.
6. Establish a BGP EVPN peer relationship between the PEs.
   1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
      
      
      
      The BGP view is displayed.
   2. Run [**router-id**](cmdqueryname=router-id) *ipv4-address*
      
      
      
      A BGP router ID is configured.
   3. Run [**peer**](cmdqueryname=peer) *ipv6-address* **as-number** { *as-number-plain* | *as-number-dot* }
      
      
      
      The remote PE is configured as a peer.
   4. Run [**peer**](cmdqueryname=peer) *ipv6-address* [**connect-interface**](cmdqueryname=connect-interface) **loopback** *interface-number*
      
      
      
      The interface used to set up a TCP connection with the specified BGP peer is specified.
   5. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP EVPN address family view is displayed.
   6. Run [**peer**](cmdqueryname=peer) *ipv6-address* **enable**
      
      
      
      The device is enabled to exchange EVPN routes with the specified peer.
   7. (Optional) Run [**peer**](cmdqueryname=peer+srv6-label-compatible) *peerIpv6Addr* **srv6-label-compatible**
      
      
      
      SRv6 label compatibility is enabled.
      
      
      
      According to relevant standards, the MPLS Label2 field of IRB routes and the ESI Label field of ES-AD routes sent to SRv6 peers should both be set to 3 in non-transposition scenarios. By default, however, the value of the MPLS Label2 field in IRB routes is a specific MPLS label, and that of the ESI Label field in ES-AD routes is a specific ESI. After the **peer srv6-label-compatible** command is run, the value of the MPLS Label2 field in IRB routes and that of the ESI Label field in ES-AD routes are both changed to 3. To ensure proper interworking between Huawei and non-Huawei devices, you can run this command.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP EVPN address family view.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
   10. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
7. Configure basic SRv6 functions.
   1. (Optional) Run [**evpn srv6 next-header-field**](cmdqueryname=evpn+srv6+next-header-field) { **59** | **143** }
      
      
      
      A value is set for the Next Header field in an SRv6 extension header.
      
      
      
      If the value is 59 in earlier versions, you can perform this step to change the value to 59 to ensure compatibility with the earlier versions.
   2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      SRv6 is enabled, and the SRv6 view is displayed.
   3. Configure a source address for SRv6 encapsulation. Note that you only need to perform one of the following operations. If both of the operations are performed, the latest configuration overrides the previous one.
      
      
      * Run the [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) *ipv6-address* [ **ip-ttl** *ttl-value* ] command to directly configure a source address for SRv6 encapsulation.
      * Run the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) { *intfname* | *interfaceType* *interfaceNum* } [ **ip-ttl** *ttl-value* ] command to specify the interface to which the source address used for SRv6 encapsulation belongs.
        
        If no IPv6 global address is configured for the interface specified using the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) command, the source address for SRv6 encapsulation is not configured.
   4. Run the [**locator**](cmdqueryname=locator) *locator-name* **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* | **flex-algo** *flexAlgoId* ] \* command to configure an SRv6 locator.
      
      
      
      If **flex-algo** *flexAlgoId* is specified, the IGP uses the specified Flex-Algo to calculate locator routes.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      In SRv6 Flex-Algo scenarios, locators must be configured on both PEs and Ps, and IS-IS SRv6 must be enabled using the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name* command in the IS-IS view. Otherwise, SRv6 locator routes cannot be advertised, and PEs at both ends cannot learn locator routes from each other.
   5. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dx2** **evpl-instance** *evpl-instance-id*
      
      
      
      An opcode for static SIDs is configured.
      
      
      
      An End.DX2 SID can be either dynamically allocated through BGP or manually configured. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable dynamic End.DX2 SID allocation through BGP in the future, skip this step.
   6. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dx2l** **evpl-instance** *evpl-instance-id*
      
      
      
      An opcode for End.DX2L SIDs is configured. You can run this command to manually specify a SID for a bypass path.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 locator view.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
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
   9. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name* [ **auto-sid-disable** ]
      
      
      
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
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
   6. Run [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id*
      
      
      
      The EVPL instance view is displayed.
   7. Run [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name*
      
      
      
      The device is enabled to add SIDs to EVPN routes to be sent.
      
      
      
      If there are static SIDs in the range of the locator specified using *locator-name*, use the static SIDs. Otherwise, use dynamically allocated SIDs.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the EVPL instance view.
   9. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **vpws**
      
      
      
      The view of the EVPN instance that works in VPWS mode is displayed.
   10. Run [**segment-routing ipv6 best-effort**](cmdqueryname=segment-routing+ipv6+best-effort)
       
       
       
       The device is enabled to perform route recursion to SRv6 BE paths based on the SIDs carried by routes.
   11. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
   12. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.

#### Verifying the Configuration

After configuring EVPN VPWS over SRv6 Flex-Algo, verify the configuration.

* Run the [**display bgp evpn evpl**](cmdqueryname=display+bgp+evpn+evpl) command to check all EVPL instance information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix* ] command to check BGP EVPN route information.
* Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end-dx2** **evpl-instance** *evpl-id* **forwarding** command to check information about the SRv6 BE local SID table.
* Run the [**display isis**](cmdqueryname=display+isis+flex-algo) *process-id* **flex-algo** [ *flex-algo-id* ] [ **level-1** | **level-2** ] command to check the preferred FAD in the LSDB.
* Run the [**display isis lsdb**](cmdqueryname=display+isis+lsdb) [ { **level-1** | **level-2** } | **verbose** | { **local** | *lsp-id* | **is-name** *symbolic-name* } ] \* [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check IS-IS LSDB information.
* Run the [**display isis**](cmdqueryname=display+isis)*process-id* **route****ipv6** **flex-algo** [ *flex-algo-id* ] [ **verbose** | [ **level-1** | **level-2** ] | *ipv6-address* [ *prefix-length* ] ] \* or [**display isis route**](cmdqueryname=display+isis+route)[ *process-id* ] **ipv6** **flex-algo** [ *flex-algo-id* ] [ **verbose** | [ **level-1** | **level-2** ] | *ipv6-address* [ *prefix-length* ] ] \* command to check Flex-Algo-related IS-IS route information.
* Run the [**display isis**](cmdqueryname=display+isis)[ *process-id* ] **spf-tree** [ **systemid** *systemid* ] **ipv6 flex-algo** [ *flex-algo-id* ] [ [ **level-1** | **level-2** ] | **verbose** ] \* command to check the SPF tree topology information of a specified Flex-Algo.