Configuring EVPN VPLS over SRv6 TE Policy
=========================================

This section describes how to configure EVPN VPLS over SRv6 TE Policy so that EVPN VPLSs can be carried over SRv6 TE Policies.

#### Usage Scenario

EVPN VPLS uses the EVPN E-LAN model to carry MP2MP VPLSs. EVPN VPLS over SRv6 TE Policy uses public SRv6 TE Policies to carry EVPN VPLSs. As shown in [Figure 1](#EN-US_TASK_0297800920__en-us_task_0194319216_fig_dc_vrp_srv6_cfg_all_002101), PE1 and PE2 communicate through an IPv6 public network. An SRv6 TE Policy is deployed on the network to carry EVPN VPLSs.

**Figure 1** EVPN VPLS over SRv6 TE Policy networking  
![](figure/en-us_image_0194320129.png)
#### Pre-configuration Tasks

Before configuring EVPN VPLS over SRv6 TE Policy, complete the following tasks:

* [Configure an SRv6 TE Policy manually](dc_vrp_srv6_cfg_all_0110.html) or [use a controller to dynamically deliver an SRv6 TE Policy](dc_vrp_srv6_cfg_all_0116.html).

* [Configure BD EVPN](dc_vrp_evpn_cfg_0065.html) between PE1 and PE2.


#### Procedure

1. Establish a BGP EVPN peer relationship between PEs.
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
   8. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } **advertise encap-type srv6**
      
      
      
      The device is enabled to send EVPN routes carrying SRv6-encapsulated attributes to the specified peer or peer group.
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
2. On each PE, configure EVPN VPLSs to recurse to an SRv6 TE Policy.
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
   9. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
      
      
      
      The IS-IS view is displayed.
   10. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name* [ **auto-sid-disable** ]
       
       
       
       IS-IS SRv6 is enabled.
       
       
       
       In this command, the value of *locator-name* must be the same as that specified using the [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ] command. If a separate locator is configured for each of BUM traffic and known unicast traffic of EVPN VPLS services, you need to run this command once for each locator for IS-IS to advertise them both.
   11. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the IS-IS view.
   12. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode**
       
       
       
       The view of the EVPN instance that works in BD mode is displayed.
   13. Run [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [ **unicast-locator***unicast-locator-name* ]
       
       
       
       The device is enabled to add SIDs to EVPN routes to be advertised.
       
       
       
       For the command:
       * *locator-name* must be set to an End.DT2M SID, with the **args** parameter specified. *unicast-locator-name* must be set to an End.DT2U or End.DT2UL SID, without having the **args** parameter specified. If the *locator-name* and *unicast-locator-name* parameters are both required, you need to run the [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ] command to create two corresponding locators before setting the two parameters.
       * In EVPN VPLS dual-homing scenarios, the **args** parameter is used to stitch ESI labels for End.DT2M SIDs only, which causes a waste of End.DT2U SIDs. In this case, you can separately configure a locator for End.DT2U SIDs and another locator for End.DT2M SIDs. The former locator does not require the **args** parameter to be specified. The two locators can then be bound to the same EVPN instance to conserve SIDs.
       * If static SIDs are configured for the locator specified using *locator-name* or *unicast-locator-name*, use the static SIDs. Otherwise, use dynamically allocated SIDs.
   14. Run [**segment-routing ipv6 traffic-engineer**](cmdqueryname=segment-routing+ipv6+traffic-engineer) [ **best-effort** ]
       
       
       
       The function to recurse EVPN VPLSs to SRv6 TE Policies is enabled.
       
       If an SRv6 BE path exists on the network, you can set the **best-effort** parameter, allowing the SRv6 BE path to function as a best-effort path in the case of an SRv6 TE Policy fault.
   15. (Optional) Run [**default-color**](cmdqueryname=default-color) *color-value*
       
       
       
       The default color value is specified for the EVPN service to recurse to an SRv6 TE Policy.
       
       If a remote EVPN route without carrying the Color Extended Community is leaked to a local EVPN instance, the default color value is used for the recursion.
   16. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
   17. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
   18. Apply a tunnel policy to services. For details, see [Applying a Tunnel Policy to Services](dc_vrp_srv6_cfg_all_0114.html).
3. (Optional) Configure the tunnel ID carried in the inclusive multicast route to be sent to an IPv6 neighbor.
   
   
   1. Run [**evpn**](cmdqueryname=evpn)
      
      The global EVPN configuration view is displayed.
   2. Run [**evpn tunnel-id**](cmdqueryname=evpn+tunnel-id) *tunnel-id-value*
      
      The tunnel ID carried in the inclusive multicast route to be sent to an IPv6 neighbor is specified.
   3. Run [**quit**](cmdqueryname=quit)
      
      Return to the system view.
   4. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.

#### Verifying the Configuration

After configuring EVPN VPLS over SRv6 TE Policy, verify the configuration.

* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* ] command to check BGP EVPN route information. The command output shows that the value of **Relay Tunnel Out-Interface** is **SRv6 TE Policy**.
* Run the [**display evpn vpn-instance**](cmdqueryname=display+evpn+vpn-instance) [ **name** *vpn-instance-name* ] **tunnel-info** command to check information about the tunnel associated with a specified EVPN instance.
* Run the [**display evpn vpn-instance name**](cmdqueryname=display+evpn+vpn-instance+name)*vpn-instance-name* **tunnel-info** **nexthop** *nexthopIpv6Addr* command to check information about the tunnel that is associated with a specified EVPN instance and matches a specified next hop.