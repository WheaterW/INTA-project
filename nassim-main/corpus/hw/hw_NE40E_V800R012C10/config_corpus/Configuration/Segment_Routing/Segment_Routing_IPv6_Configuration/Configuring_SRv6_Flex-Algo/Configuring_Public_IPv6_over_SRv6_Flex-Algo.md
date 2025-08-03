Configuring Public IPv6 over SRv6 Flex-Algo
===========================================

This section describes how to configure public IPv6 over SRv6 Flex-Algo.

#### Context

When SRv6 uses an IGP to calculate paths, it can associate locators with Flex-Algos to ensure that calculated SRv6 BE paths meet specific requirements.

Public IPv6 over SRv6 Flex-Algo uses forwarding paths calculated based on Flex-Algos to carry public IPv6 services on the public network.

On the network shown in [Figure 1](#EN-US_TASK_0279862423__fig_dc_vrp_srv6_cfg_all_001201), multiple links exist between PEs. You can configure the PEs to forward public network IPv6 services over a path calculated using a specified Flex-Algo.

**Figure 1** Public IPv6 over SRv6 Flex-Algo networking  
![](figure/en-us_image_0279964598.png)

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
3. Configure IPv6 IS-IS on the PEs and P. For configuration details, see [Configuring Basic IS-IS Functions (IPv6)](dc_vrp_isis_cfg_1023.html).
4. Establish an EBGP peer relationship between PE1 and DeviceA and another one between PE2 and DeviceB.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**router-id**](cmdqueryname=router-id) *ipv4-address*
      
      
      
      A BGP router ID is configured.
   4. Run [**peer**](cmdqueryname=peer) *ipv6-address* [**as-number**](cmdqueryname=as-number) *as-number*
      
      
      
      The IPv6 address of a peer and the number of the AS where the peer resides are specified.
   5. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
      
      
      
      The IPv6 unicast address family view is displayed.
   6. Run [**peer**](cmdqueryname=peer) *ipv6-address* [**enable**](cmdqueryname=enable)
      
      
      
      The device is enabled to exchange routing information with the specified IPv6 peer.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the IPv6 unicast address family view.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
5. Establish an MP-IBGP peer relationship between the PEs.
   1. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   2. Run [**router-id**](cmdqueryname=router-id) *ipv4-address*
      
      
      
      A BGP router ID is configured.
   3. Run [**peer**](cmdqueryname=peer) *ipv6-address* [**as-number**](cmdqueryname=as-number) *as-number*
      
      
      
      The IPv6 address of a peer and the number of the AS where the peer resides are specified.
   4. Run [**peer**](cmdqueryname=peer) *ipv6-address* [**connect-interface**](cmdqueryname=connect-interface) *interface-type* *interface-number*
      
      
      
      A source interface and a source address are specified for TCP connection setup.
   5. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
      
      
      
      The IPv6 unicast address family view is displayed.
   6. Run [**peer**](cmdqueryname=peer) *ipv6-address* [**enable**](cmdqueryname=enable)
      
      
      
      The device is enabled to exchange routing information with the specified IPv6 peer.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the IPv6 unicast address family view.
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
   4. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt6** or [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt46** **vpn-instance** *vpn-instance-name*
      
      
      
      An opcode for static SIDs is configured.
      
      
      
      A SID can be either dynamically allocated by BGP or manually configured. If a dynamically allocated SID and a manually configured SID both exist, the latter takes effect. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable dynamic End.DT6 SID allocation through BGP or the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46) command to enable dynamic End.DT46 SID allocation through BGP in the future, skip this step.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 locator view.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 view.
7. Enable IS-IS SRv6 on the PEs.
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
8. Configure public network routes on PEs to carry SIDs and recurse to SRv6 BE paths based on the SIDs.
   1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
      
      
      
      The BGP view is displayed.
   2. (Optional) Run [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46)
      
      
      
      The device is enabled to add SIDs to public network routes.
   3. Run [**ipv6-family unicast**](cmdqueryname=ipv6-family+unicast)
      
      
      
      The IPv6 unicast address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer) *peerIpv6Addr* **prefix-sid** [ **advertise-srv6-locator** ]
      
      
      
      The device is enabled to exchange prefix SIDs with the specified peer.
      
      
      
      In a scenario where BFD is used to check locator reachability and the P nodes between local and remote PEs summarize locator routes, you can specify the **advertise-srv6-locator** parameter to enable PE-advertised BGP routes to carry locator length information. In this way, when the peer IPv6 address bound to the BFD session matches the locator's IPv6 address, locator reachability can be checked using BFD to complete auto FRR path switching.
   5. Run [**segment-routing ipv6 best-effort**](cmdqueryname=segment-routing+ipv6+best-effort)
      
      
      
      The device is enabled to perform public route recursion based on the SIDs carried by routes.
   6. Run [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name*
      
      
      
      The device is enabled to add SIDs to public network routes.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46) command has been run in the BGP view, skip this step.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After configuring public IPv6 over SRv6 Flex-Algo, verify the configuration.

* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) *ipv6-address* [ *mask* | *mask-length* ] command to check BGP IPv6 routing table information.
* Run the [**display segment-routing ipv6 locator**](cmdqueryname=display+segment-routing+ipv6+locator) [ *locator-name* ] **verbose** command to check SRv6 locator information.
* Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) [ **locator** *locator-name* ] **forwarding** command to check information about the SRv6 local SID table.
* Run the [**display isis**](cmdqueryname=display+isis+flex-algo) *process-id* **flex-algo** [ *flex-algo-id* ] [ **level-1** | **level-2** ] command to check the preferred FAD in the LSDB.
* Run the [**display isis lsdb**](cmdqueryname=display+isis+lsdb) [ { **level-1** | **level-2** } | **verbose** | { **local** | *lsp-id* | **is-name** *symbolic-name* } ] \* [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check IS-IS LSDB information.
* Run the [**display isis**](cmdqueryname=display+isis)*process-id* **route****ipv6** **flex-algo** [ *flex-algo-id* ] [ **verbose** | [ **level-1** | **level-2** ] | *ipv6-address* [ *prefix-length* ] ] \* or [**display isis route**](cmdqueryname=display+isis+route)[ *process-id* ] **ipv6** **flex-algo** [ *flex-algo-id* ] [ **verbose** | [ **level-1** | **level-2** ] | *ipv6-address* [ *prefix-length* ] ] \* command to check Flex-Algo-related IS-IS route information.
* Run the [**display isis**](cmdqueryname=display+isis)[ *process-id* ] **spf-tree** [ **systemid** *systemid* ] **ipv6 flex-algo** [ *flex-algo-id* ] [ [ **level-1** | **level-2** ] | **verbose** ] \* command to check the SPF tree topology information of a specified Flex-Algo.