Configuring EVPN VPWS over SRv6 TE Policy
=========================================

This section describes how to configure EVPN virtual private wire service (VPWS) over SRv6 TE Policy so that EVPN VPWSs can be carried over SRv6 TE Policies.

#### Usage Scenario

EVPN VPWS over SRv6 TE Policy uses public SRv6 TE Policies to carry EVPN VPWSs. As shown in [Figure 1](#EN-US_TASK_0297800922__en-us_task_0179342422_fig1138145962319), PE1 and PE2 communicate through an IPv6 public network. An SRv6 TE Policy is deployed on the network to carry EVPN VPWSs.

**Figure 1** EVPN VPWS over SRv6 TE Policy networking  
![](figure/en-us_image_0256113586.png)

#### Pre-configuration Tasks

Before configuring EVPN VPWS over SRv6 TE Policy, complete the following tasks:

* [Configure an SRv6 TE Policy manually](dc_vrp_srv6_cfg_all_0110.html) or [use a controller to dynamically deliver an SRv6 TE Policy](dc_vrp_srv6_cfg_all_0116.html).

#### Procedure

1. Configure EVPN and EVPL instances on each PE.
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
   6. (Optional) Run [**default-color**](cmdqueryname=default-color) *color-value*
      
      
      
      The default color value is specified for the EVPN service to recurse to an SRv6 TE Policy.
      
      If a remote EVPN route without carrying the Color Extended Community is leaked to a local EVPN instance, the default color value is used for the recursion.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   8. Run [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id*
      
      
      
      An EVPL instance is created, and the EVPL instance view is displayed.
   9. Run [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name*
      
      
      
      A specified EVPN instance that works in VPWS mode is bound to the current EVPL instance.
   10. Run [**local-service-id**](cmdqueryname=local-service-id) *service-id* [**remote-service-id**](cmdqueryname=remote-service-id) *service-id*
       
       
       
       The packets of the current EVPL instance are configured to carry the local and remote service IDs.
   11. (Optional) Run [**mtu-match ignore**](cmdqueryname=mtu-match+ignore)
       
       
       
       The MTU matching check is ignored for the EVPL instance. In scenarios where a Huawei device interworks with a non-Huawei device through an EVPN VPWS, if the non-Huawei device does not support any MTU matching check for an EVPL instance, run the [**mtu-match ignore**](cmdqueryname=mtu-match+ignore) command to ignore the MTU matching check.
   12. (Optional) Run [**load-balancing ignore-esi**](cmdqueryname=load-balancing+ignore-esi)
       
       
       
       The device is enabled to ignore the ESI validity check during EVPL instance load balancing.
       
       
       
       In an EVPN VPWS scenario where active-active protection is deployed, if each access-side device is single-homed to an aggregation-side device and no ESI is configured on the access interface, to implement active-active load balancing, you can run this command on the aggregation-side device to enable the device to ignore the ESI validity check during EVPL instance load balancing.
   13. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
   14. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
2. Configure an AC interface.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2**
      
      
      
      A Layer 2 sub-interface is created, and the sub-interface view is displayed.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Before running this command, ensure that the corresponding Layer 2 main interface does not have the [**port link-type**](cmdqueryname=port+link-type) **dot1q-tunnel** command configuration. If this configuration exists, run the [**undo port link-type**](cmdqueryname=undo+port+link-type) command to delete the configuration.
      
      In addition to a Layer 2 sub-interface, an Ethernet main interface, Layer 3 sub-interface, or Eth-Trunk interface can also function as an AC interface.
   3. Run [**encapsulation**](cmdqueryname=encapsulation) { **dot1q** [ **vid** *low-pe-vid* [ **to** *high-pe-vid* ] ] | **untag** | **qinq** [ **vid** *pe-vid* **ce-vid** { *low-ce-vid* [ **to** *high-ce-vid* ] | **default** } ] }
      
      
      
      An encapsulation type is configured for packets allowed to pass through the sub-interface.
   4. Run [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id*
      
      
      
      A specified EVPL instance is bound to the Layer 2 sub-interface.
   5. (Optional) Run [**evpn-vpws ignore-ac-state**](cmdqueryname=evpn-vpws+ignore-ac-state)
      
      
      
      The interface is enabled to ignore the AC status.
      
      
      
      On a network with primary and backup links, if CFM is associated with an AC interface, run this command to ensure EVPN VPWS continuity. When the AC status of the interface becomes down, a primary/backup link switchover is triggered. As the interface has been enabled to ignore the AC status using this command, the EVPN VPWS does not need to be re-established during the link switchover.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the Layer 2 sub-interface view.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
3. Establish a BGP EVPN peer relationship between PEs.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
      
      
      
      The BGP view is displayed.
   3. Run [**router-id**](cmdqueryname=router-id) *ipv4-address*
      
      
      
      A BGP router ID is configured.
   4. Run [**peer**](cmdqueryname=peer) *ipv6-address* **as-number** { *as-number-plain* | *as-number-dot* }
      
      
      
      The remote PE is configured as a peer.
   5. Run [**peer**](cmdqueryname=peer) *ipv6-address* [**connect-interface**](cmdqueryname=connect-interface) **loopback** *interface-number*
      
      
      
      The interface used to set up a TCP connection with the specified BGP peer is specified.
   6. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP EVPN address family view is displayed.
   7. Run [**peer**](cmdqueryname=peer) *peerIpv6Addr* **enable**
      
      
      
      The device is enabled to exchange EVPN routes with the specified peer.
   8. Run [**peer**](cmdqueryname=peer) *ipv6-address* **advertise encap-type** **srv6**
      
      
      
      The device is enabled to send EVPN routes carrying SRv6-encapsulated attributes to the specified peer.
   9. (Optional) Run [**peer**](cmdqueryname=peer+srv6-label-compatible) *peerIpv6Addr* **srv6-label-compatible**
      
      
      
      SRv6 label compatibility is enabled.
      
      
      
      According to relevant standards, the MPLS Label2 field of IRB routes and the ESI Label field of ES-AD routes sent to SRv6 peers should both be set to 3 in non-transposition scenarios. By default, however, the value of the MPLS Label2 field in IRB routes is a specific MPLS label, and that of the ESI Label field in ES-AD routes is a specific ESI. After the **peer srv6-label-compatible** command is run, the value of the MPLS Label2 field in IRB routes and that of the ESI Label field in ES-AD routes are both changed to 3. To ensure proper interworking between Huawei and non-Huawei devices, you can run this command.
   10. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP EVPN address family view.
   11. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP view.
   12. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
4. On each PE, configure EVPN VPWSs to recurse to an SRv6 TE Policy.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. (Optional) Run [**evpn srv6 next-header-field**](cmdqueryname=evpn+srv6+next-header-field) { **59** | **143** }
      
      
      
      A value is set for the Next Header field in an SRv6 extension header.
      
      
      
      If the value is 59 in earlier versions, you can perform this step to change the value to 59 to ensure compatibility with the earlier versions.
   3. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      SRv6 is enabled, and the SRv6 view is displayed.
   4. Configure a source address for SRv6 encapsulation. Note that you only need to perform one of the following operations. If both of the operations are performed, the latest configuration overrides the previous one.
      
      
      * Run the [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) *ipv6-address* [ **ip-ttl** *ttl-value* ] command to directly configure a source address for SRv6 encapsulation.
      * Run the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) { *intfname* | *interfaceType* *interfaceNum* } [ **ip-ttl** *ttl-value* ] command to specify the interface to which the source address used for SRv6 encapsulation belongs.
        
        If no IPv6 global address is configured for the interface specified using the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) command, the source address for SRv6 encapsulation is not configured.
   5. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ]
      
      
      
      An SRv6 locator is configured, and the SRv6 locator view is displayed.
   6. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dx2** **evpl-instance** *evpl-instance-id*
      
      
      
      An opcode for static SIDs is configured.
      
      
      
      An End.DX2 SID can be either dynamically allocated through BGP or manually configured. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable dynamic End.DX2 SID allocation through BGP in the future, skip this step.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 locator view.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 view.
   9. Run [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id*
      
      
      
      The EVPL instance view is displayed.
   10. Run [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name*
       
       
       
       The device is enabled to add SIDs to EVPN routes to be sent.
       
       If there are static SIDs in the range of the locator specified using *locator-name*, use the static SIDs. Otherwise, use dynamically allocated SIDs.
   11. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the EVPL instance view.
   12. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **vpws**
       
       
       
       The VPWS-EVPN instance view is displayed.
   13. Run [**segment-routing ipv6 traffic-engineer**](cmdqueryname=segment-routing+ipv6+traffic-engineer) [ **best-effort** ]
       
       
       
       The function to recurse EVPN VPWSs to SRv6 TE Policies is enabled.
       
       If an SRv6 BE path exists on the network, you can set the **best-effort** parameter, allowing the SRv6 BE path to function as a best-effort path in the case of an SRv6 TE Policy fault.
   14. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
   15. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
   16. Apply a tunnel policy to services. For details, see [Applying a Tunnel Policy to Services](dc_vrp_srv6_cfg_all_0114.html).
5. (Optional) Verify EVPN VPWS connectivity.
   1. Configure an End.OP SID on the remote PE.
      
      
      1. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
         
         The SRv6 view is displayed.
      2. Run [**locator**](cmdqueryname=locator) *locator-name*
         
         The SRv6 locator view is displayed.
      3. Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-op**
         
         An opcode for End.OP SIDs is configured.
      4. Run [**commit**](cmdqueryname=commit)
         
         The configuration is committed.
   2. Perform the following steps on the local PE:
      
      
      1. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
         
         The SRv6 view is displayed.
      2. Run [**remote end-op**](cmdqueryname=remote+end-op) *op-sid* *prefix-length*
         
         A remote End.OP SID is configured.
      3. Run [**commit**](cmdqueryname=commit)
         
         The configuration is committed.
   3. Perform the following steps on the local PE:
      
      
      * Run [**ping evpn vpws**](cmdqueryname=ping+evpn+vpws) *local-ce-id* *remote-ce-id* **end-op** *endOp* [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-m** *interval* | **-s** *packet-size* | **-t** *time-out* | **-r** *reply-mode* | **-tc** *tc* ] \*
        
        A ping operation is performed to check the EVPN VPWS status.
      * Run [**tracert evpn vpws**](cmdqueryname=tracert+evpn+vpws) *local-ce-id* *remote-ce-id* **end-op** *endOp* [ **-a** *source-ip* | **-exp** *exp-value* | **-s** *packet-size* | **-t** *timeout* | **-h** *max-ttl* | **-r** *reply-mode* | **-tc** *tc* ] \* [ **pipe** | **uniform** ]
        
        A tracert operation is performed to check the EVPN VPWS status.

#### Verifying the Configuration

After configuring EVPN VPWS over SRv6 TE Policy, verify the configuration.

* Run the [**display bgp evpn evpl**](cmdqueryname=display+bgp+evpn+evpl) command to check all EVPL instance information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* ] command to check BGP EVPN route information. The command output shows that the value of **Relay Tunnel Out-Interface** is **SRv6 TE Policy**.
* Run the [**display evpn vpn-instance**](cmdqueryname=display+evpn+vpn-instance) [ **name** *vpn-instance-name* ] **tunnel-info** command to check information about the tunnel associated with a specified EVPN instance.
* Run the [**display evpn vpn-instance name**](cmdqueryname=display+evpn+vpn-instance+name)*vpn-instance-name* **tunnel-info** **nexthop** *nexthopIpv6Addr* command to check information about the tunnel that is associated with a specified EVPN instance and matches a specified next hop.