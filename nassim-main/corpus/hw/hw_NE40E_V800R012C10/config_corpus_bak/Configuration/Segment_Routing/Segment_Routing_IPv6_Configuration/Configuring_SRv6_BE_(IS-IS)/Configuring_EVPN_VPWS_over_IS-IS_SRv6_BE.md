Configuring EVPN VPWS over IS-IS SRv6 BE
========================================

This section describes how to configure EVPN VPWS over SRv6 BE.

#### Usage Scenario

EVPN VPWS over SRv6 BE uses SRv6 BE on a public network to carry EVPN services. The key implementation of EVPN VPWS over SRv6 BE involves establishing SRv6 BE paths, advertising EVPN routes, and forwarding data.

[Figure 1](#EN-US_TASK_0172368965__fig_dc_vrp_srv6_cfg_all_002101) shows an example where an IPv6 public network is established between PE1 and PE2. SRv6 BE can be deployed on the IPv6 public network to carry Layer 2 EVPN services.

**Figure 1** EVPN VPWS over SRv6 BE networking  
![](figure/en-us_image_0210219564.png)

#### Pre-configuration Tasks

Before configuring EVPN VPWS over SRv6 BE, complete the following tasks:

* Configure a link layer protocol.
* Configure network-layer addresses for interfaces to ensure that neighboring devices are reachable at the network layer.

#### Procedure

1. Configure IPv6 IS-IS on each PE and P. For configuration details, see [Configuring Basic IS-IS Functions (IPv6)](dc_vrp_isis_cfg_1023.html).
2. Configure EVPN and EVPL instances on each PE.
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
3. Configure an AC interface.
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
4. Establish a BGP EVPN peer relationship between the PEs.
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
5. Configure basic SRv6 functions.
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
      
      
      
      An SRv6 locator is configured, and the SRv6 locator view is displayed.
   5. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dx2** **evpl-instance** *evpl-instance-id*
      
      
      
      An opcode for static SIDs is configured.
      
      
      
      An End.DX2 SID can be either dynamically allocated through BGP or manually configured. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable dynamic End.DX2 SID allocation through BGP in the future, skip this step.
   6. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dx2l** **evpl-instance** *evpl-instance-id*
      
      
      
      An opcode for End.DX2L SIDs is configured. You can run this command to manually specify a SID for a bypass path.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 locator view.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 view.
6. Enable IS-IS SRv6.
   1. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
      
      
      
      The IS-IS view is displayed.
   2. Run [**ipv6 enable topology ipv6**](cmdqueryname=ipv6+enable+topology+ipv6)
      
      
      
      The IPv6 capability is enabled for the IS-IS process in the IPv6 topology.
   3. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name* [ **auto-sid-disable** ]
      
      
      
      IS-IS SRv6 is enabled.
      
      In this command, the value of *locator-name* must be the same as that specified using the [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ] command.
   4. (Optional) Run [**segment-routing ipv6 auto-sid advertise**](cmdqueryname=segment-routing+ipv6+auto-sid+advertise) { **no-flavor** | **psp** | **psp-usp-usd** | **psp-usp-usd-coc** | **coc** | **psp-coc** | **psp-usp-usd-coc-next** | **psp-usd-next** } \*
      
      
      
      The function to adjust the flavors to be carried in dynamically allocated End and End.X SIDs is enabled.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the IS-IS view.
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
8. (Optional) Verify EVPN VPWS connectivity.
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

After configuring EVPN VPWS over SRv6 BE, verify the configuration.

* Run the [**display bgp evpn evpl**](cmdqueryname=display+bgp+evpn+evpl) command to check all EVPL instance information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* ] command to check BGP EVPN route information.
* Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end-dx2** **evpl-instance** *evpl-id* **forwarding** command to check information about the SRv6 BE local SID table.