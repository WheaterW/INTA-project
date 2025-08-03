Configuring EVPN VPLS over IS-IS SRv6 BE
========================================

When the EVPN E-LAN model is used to carry multipoint-to-multipoint (MP2MP) VPLSs, EVPN VPLS over SRv6 BE can be configured to transmit EVPN E-LAN data over SRv6 BE paths on a public network.

#### Usage Scenario

EVPN VPLS uses the EVPN E-LAN model to carry MP2MP VPLSs. EVPN VPLS over SRv6 BE uses SRv6 BE paths on a public network to carry EVPN E-LAN services. The key implementation of EVPN VPLS over SRv6 BE involves establishing SRv6 BE paths, advertising EVPN routes, and forwarding data.

[Figure 1](#EN-US_TASK_0176593776__fig_dc_vrp_srv6_cfg_all_002101) shows an example where an IPv6 public network is established between PE1 and PE2. SRv6 BE can be deployed on the IPv6 public network to carry EVPN E-LAN services.

**Figure 1** EVPN VPLS over SRv6 BE networking  
![](figure/en-us_image_0210220978.png)

#### Pre-configuration Tasks

Before configuring EVPN VPLS over SRv6 BE, complete the following tasks:

* [Configure basic IPv6 IS-IS functions](dc_vrp_isis_cfg_1023.html) on the PEs and P.

#### Procedure

1. [Configure a BD EVPN instance](dc_vrp_evpn_cfg_0061.html) on each PE.
2. Configure an EVPN source address on each PE.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**evpn source-address**](cmdqueryname=evpn+source-address) *ip-address* command to configure an EVPN source address.
      
      
      
      In scenarios where a CE is dual-homed or multi-homed to PEs, you need to configure an EVPN source address on each PE to generate route distinguishers (RDs) for Ethernet segment routes and Ethernet auto-discovery per ES routes.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
3. [Configure an ESI](dc_vrp_evpn_cfg_0064.html) on each PE.
4. [Configure a BD and bind it to the EVPN instance](dc_vrp_evpn_cfg_0062.html) on each PE.
   
   
   
   For details about more optional functions, see [Configuring the BD EVPN Function](dc_vrp_evpn_cfg_0065.html).
5. Establish a BGP EVPN peer relationship between the PEs.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
      
      
      
      The BGP view is displayed.
   3. (Optional) Run [**router-id**](cmdqueryname=router-id) *ipv4-address*
      
      
      
      A BGP router ID is configured.
   4. Run [**peer**](cmdqueryname=peer) *ipv6-address* **as-number** { *as-number-plain* | *as-number-dot* }
      
      
      
      The remote PE is configured as a peer.
   5. Run [**peer**](cmdqueryname=peer) *ipv6-address* **connect-interface** **loopback** *interface-number*
      
      
      
      The interface on which a TCP connection to the specified BGP peer is established is specified.
   6. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP EVPN address family view is displayed.
   7. Run [**peer**](cmdqueryname=peer) *ipv6-address* **enable**
      
      
      
      The device is enabled to exchange EVPN routes with the specified peer.
   8. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } **advertise encap-type** **srv6** [ **advertise-srv6-locator** ]
      
      
      
      The device is enabled to send EVPN routes carrying SRv6-encapsulated attributes to the specified peer or peer group.
      
      
      
      In a scenario where BFD is used to check locator reachability, if locator routes are summarized by a P device between local and remote PEs, the remote PE can learn only the summary locator route, not the locator on the local PE. This leads to a BFD failure. To address this issue, specify the **advertise-srv6-locator** parameter in the command to allow the local PE to carry locator length information in the EVPN route to be advertised to the remote PE. In this way, after receiving the EVPN route, the remote PE can calculate the locator on the local PE, enabling BFD to take effect.
   9. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } **srv6-label-compatible**
      
      
      
      SRv6 label compatibility is enabled.
      
      
      
      According to relevant standards, the MPLS Label2 field of IRB routes and the ESI Label field of ES-AD routes sent to SRv6 peers should both be set to 3 in non-transposition scenarios. By default, however, the value of the MPLS Label2 field in IRB routes is a specific MPLS label, and that of the ESI Label field in ES-AD routes is a specific ESI. After the **peer srv6-label-compatible** command is run, the value of the MPLS Label2 field in IRB routes and that of the ESI Label field in ES-AD routes are both changed to 3. To ensure proper interworking between Huawei and non-Huawei devices, you can run this command.
   10. (Optional) Run [**peer**](cmdqueryname=peer+srv6-label-compatible+inclusive-route) { *ipv6-address* | *group-name* } **srv6-label-compatible inclusive-route**
       
       
       
       SRv6 label compatibility for inclusive routes is enabled.
       
       
       
       According to relevant standards, the MPLS Label field in the PMSI attribute of an inclusive route sent to an SRv6 peer should be set to 0 in non-transposition scenarios. By default, however, this field is set to 3 for such a route. After the **peer srv6-label-compatible inclusive-route** command is run, the value of this field is changed to 0. To ensure proper interworking between Huawei and non-Huawei devices, you can run this command.
   11. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP EVPN address family view.
   12. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP view.
   13. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
6. Configure basic SRv6 functions.
   1. (Optional) Run [**evpn srv6 next-header-field**](cmdqueryname=evpn+srv6+next-header-field) { **59** | **143** }
      
      
      
      A value is set for the Next Header field in an SRv6 extension header.
      
      
      
      If the value is 59 in earlier versions, you can perform this step to change the value to 59 to ensure compatibility with the earlier versions.
   2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      SRv6 is enabled, and the SRv6 view is displayed.
   3. Configure a source address for SRv6 encapsulation. Note that you only need to perform one of the following operations. If both of the operations are performed, the latest configuration overrides the previous one.
      
      
      * Run the [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) *ipv6-address* [ **ip-ttl** *ttl-value* ] command to directly configure a source address for SRv6 encapsulation.
      * Run the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) { *intfname* | *interfaceType* *interfaceNum* } [ **ip-ttl** *ttl-value* ] command to specify the interface to which the source address used for SRv6 encapsulation belongs.
        
        If no IPv6 global address is configured for the interface specified using the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) command, the source address for SRv6 encapsulation is not configured.
   4. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ]
      
      
      
      An SRv6 locator is configured.
   5. (Optional) Run [**opcode**](cmdqueryname=opcode) **func-opcode** **end-dt2m** **bridge-domain** **bd-id**
      
      
      
      A static End.DT2M SID operation code (opcode) is configured.
      
      Perform this step if a static locator is configured using the **static** *static-length* parameter. End.DT2M SIDs are used for BUM traffic forwarding through VPLS.
   6. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* { **end-dt2u** | **end-dt2ul** } **bridge-domain** *bd-id*
      
      
      
      An opcode for static End.DT2U and End.DT2UL SIDs is configured.
      
      
      
      Perform this step if a static locator is configured through the **static** *static-length* parameter. End.DT2U SIDs are used for the forwarding of known unicast traffic over VPLS. In a dual-homing scenario, you need to specify an End.DT2UL opcode for the bypass path to prevent traffic loops between PEs.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 locator view.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 view.
7. Enable IS-IS SRv6.
   1. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
      
      
      
      The IS-IS view is displayed.
   2. Run [**ipv6 enable topology ipv6**](cmdqueryname=ipv6+enable+topology+ipv6)
      
      
      
      The IPv6 capability is enabled for the IS-IS process in the IPv6 topology.
   3. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name* [ **auto-sid-disable** ]
      
      
      
      IS-IS SRv6 is enabled.
      
      
      
      In this command, the value of *locator-name* must be the same as that specified using the [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ] command. If a separate locator is configured for each of BUM traffic and known unicast traffic of EVPN VPLS services, you need to run this command once for each locator for IS-IS to advertise them both.
   4. (Optional) Run [**segment-routing ipv6 auto-sid advertise**](cmdqueryname=segment-routing+ipv6+auto-sid+advertise) { **no-flavor** | **psp** | **psp-usp-usd** | **psp-usp-usd-coc** | **coc** | **psp-coc** | **psp-usp-usd-coc-next** | **psp-usd-next** } \*
      
      
      
      The function to adjust the flavors to be carried in dynamically allocated End and End.X SIDs is enabled.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the IS-IS view.
8. Configure EVPN routes to carry SIDs and recurse to SRv6 BE paths based on the SIDs.
   1. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode**
      
      
      
      The view of the EVPN instance that works in BD mode is displayed.
   2. Run [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [ **unicast-locator***unicast-locator-name* ]
      
      
      
      The device is enabled to add SIDs to EVPN routes to be advertised.
      
      In this command:
      * *locator-name* must be set to an End.DT2M SID, with the **args** parameter specified. *unicast-locator-name* must be set to an End.DT2U or End.DT2UL SID, without having the **args** parameter specified. If the *locator-name* and *unicast-locator-name* parameters are both required, you need to run the [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ] command to create two corresponding locators before setting the two parameters.
      * In EVPN VPLS dual-homing scenarios, the **args** parameter is used to stitch ESI labels for End.DT2M SIDs only, which causes a waste of End.DT2U SIDs. In this case, you can separately configure a locator for End.DT2U SIDs and another locator for End.DT2M SIDs. The former locator does not require the **args** parameter to be specified. The two locators can then be bound to the same EVPN instance to conserve SIDs.
      * If static SIDs are configured for the locator specified using *locator-name* or *unicast-locator-name*, use the static SIDs. Otherwise, use dynamically allocated SIDs.
   3. Run [**segment-routing ipv6 best-effort**](cmdqueryname=segment-routing+ipv6+best-effort)
      
      
      
      The device is enabled to perform route recursion to SRv6 BE paths based on the SIDs carried by routes.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
9. (Optional) Configure the tunnel ID carried in the inclusive multicast route to be sent to an IPv6 neighbor.
   
   
   1. Run [**evpn**](cmdqueryname=evpn)
      
      The global EVPN configuration view is displayed.
   2. Run [**evpn tunnel-id**](cmdqueryname=evpn+tunnel-id) *tunnel-id-value*
      
      The tunnel ID carried in the inclusive multicast route to be sent to an IPv6 neighbor is specified.
   3. Run [**quit**](cmdqueryname=quit)
      
      Return to the system view.
   4. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.

#### Verifying the Configuration

After configuring EVPN VPLS over SRv6 BE, verify the configuration.

* Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) { **end-dt2u** | **end-dt2ul** | **end-dt2m** } [ *sid* ] [ **bridge-domain** *bd-id* ] **forwarding** command to check information about the SRv6 BE local SID table.

* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* ] command to check BGP EVPN route information.