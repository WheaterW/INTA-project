Configuring L3VPNv6 over IS-IS SRv6 BE
======================================

This section describes how to configure L3VPNv6 over SRv6 BE.

#### Usage Scenario

L3VPNv6 over SRv6 BE allows SRv6 BE paths on a public network to carry L3VPNv6 data. The key implementation of L3VPNv6 over SRv6 BE involves establishing SRv6 BE paths, advertising VPN routes, and forwarding data.

[Figure 1](#EN-US_TASK_0290562099__fig_dc_vrp_srv6_cfg_all_001201) shows an example where an IPv6 public network is established between PE1 and PE2 and the involved VPNs are also IPv6 networks. SRv6 BE paths can be deployed on the IPv6 public network to carry L3VPNv6 services.

**Figure 1** L3VPNv6 over SRv6 BE networking  
![](figure/en-us_image_0290562117.png)

#### Pre-configuration Tasks

Before configuring L3VPNv6 over SRv6 BE, complete the following tasks:

* Configure a link-layer protocol.
* Configure network-layer addresses for interfaces to ensure that neighboring devices are reachable at the network layer.

#### Procedure

1. Configure IPv6 IS-IS on the PEs and P. For configuration details, see [Configuring Basic IS-IS Functions (IPv6)](dc_vrp_isis_cfg_1023.html).
2. Configure a VPN instance on each PE and enable the IPv6 address family.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      
      
      A VPN instance is created, and its view is displayed.
   3. Run [**ipv6-family**](cmdqueryname=ipv6-family)
      
      
      
      The VPN instance IPv6 address family is enabled, and its view is displayed.
   4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      
      
      An RD is configured for the VPN instance IPv6 address family.
   5. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
      
      
      
      VPN targets are configured for the VPN instance IPv6 address family.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the VPN instance IPv6 address family view.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the VPN instance view.
   9. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The view of the interface to be bound to the VPN instance is displayed.
   10. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
       
       
       
       The interface is bound to the VPN instance.
       
       
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) command deletes IPv4 and IPv6 Layer 3 configurations on the interface, such as the configured IP addresses and routing protocols. You have to reconfigure them if they are required.
   11. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
       
       
       
       IPv6 is enabled on the interface.
   12. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* }
       
       
       
       An IPv6 address is configured for the interface.
       
       
       
       Layer 3 features such as PE-CE route exchange can be configured for PE-CE communication only after an IPv6 address is configured for the involved VPN interface.
   13. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
   14. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the interface view.
3. Configure PE-CE IPv6 route exchange. For configuration details, see [Configuring Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v6_cfg_2061.html).
4. Establish an MP-IBGP peer relationship between the PEs.
   1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
      
      
      
      The BGP view is displayed.
   2. Run [**router-id**](cmdqueryname=router-id) *ipv4-address*
      
      
      
      A router ID is configured.
   3. Run [**peer**](cmdqueryname=peer) *ipv6-address* **as-number** { *as-number-plain* | *as-number-dot* }
      
      
      
      The remote PE is configured as a peer.
   4. Run [**peer**](cmdqueryname=peer) *ipv6-address* [**connect-interface**](cmdqueryname=connect-interface) **loopback** *interface-number*
      
      
      
      The interface on which a TCP connection to the specified BGP peer is established is specified.
   5. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
      
      
      
      The BGP-VPNv6 address family view is displayed.
   6. Run [**peer**](cmdqueryname=peer) *ipv6-address* **enable**
      
      
      
      The device is enabled to exchange VPN-IPv6 routing information with the specified peer.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-VPNv6 address family view.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
5. Configure basic SRv6 functions.
   1. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      SRv6 is enabled, and the SRv6 view is displayed.
   2. Configure a source address for SRv6 encapsulation. Note that you only need to perform one of the following operations. If both of the operations are performed, the latest configuration overrides the previous one.
      
      
      * Run the [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) *ipv6-address* [ **ip-ttl** *ttl-value* ] command to directly configure a source address for SRv6 encapsulation.
      * Run the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) { *intfname* | *interfaceType* *interfaceNum* } [ **ip-ttl** *ttl-value* ] command to specify the interface to which the source address used for SRv6 encapsulation belongs.
        
        If no IPv6 global address is configured for the interface specified using the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) command, the source address for SRv6 encapsulation is not configured.
   3. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ]
      
      
      
      An SRv6 locator is configured, and the SRv6 locator view is displayed.
   4. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt6** **vpn-instance** *vpn-instance-name* or [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt46** **vpn-instance** *vpn-instance-name*
      
      
      
      An opcode for static SIDs is configured.
      
      
      
      A SID can be either dynamically allocated by BGP or manually configured. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable dynamic End.DT6 SID allocation through BGP or the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46) command to enable dynamic End.DT46 SID allocation through BGP in the future, skip this step.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 locator view.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 view.
6. Enable IS-IS SRv6 on each PE.
   1. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
      
      
      
      The IS-IS view is displayed.
   2. Run [**ipv6 enable topology ipv6**](cmdqueryname=ipv6+enable+topology+ipv6)
      
      
      
      The IPv6 capability is enabled for the IS-IS process in the IPv6 topology.
   3. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name* [ **auto-sid-disable** ]
      
      
      
      IS-IS SRv6 is enabled.
   4. (Optional) Run [**segment-routing ipv6 auto-sid advertise**](cmdqueryname=segment-routing+ipv6+auto-sid+advertise) { **no-flavor** | **psp** | **psp-usp-usd** | **psp-usp-usd-coc** | **coc** | **psp-coc** | **psp-usp-usd-coc-next** | **psp-usd-next** } \*
      
      
      
      The function to adjust the flavors to be carried in dynamically allocated End and End.X SIDs is enabled.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the IS-IS view.
7. Configure each PE to carry SIDs in VPN routes and recurse the routes to SRv6 BE paths based on the SIDs.
   1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
      
      
      
      The BGP view is displayed.
   2. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
      
      
      
      The BGP-VPNv6 address family view is displayed.
   3. Run [**peer**](cmdqueryname=peer) *ipv6-address* **prefix-sid** [ **advertise-srv6-locator** ]
      
      
      
      The device is enabled to exchange IPv6 prefix SIDs with the specified IPv6 peer.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-VPNv6 address family view.
   5. Configure the device to add SIDs to VPN routes. Note that you need to perform configurations only in one of the following two views. If you perform configurations in both views, the configurations in these views are mutually exclusive.
      
      
      * Configurations in the BGP-VPN instance IPv6 address family view
        1. Run the [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv6 address family view.
        2. Run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable the device to add SIDs to VPN routes.
      * Configurations in the BGP-VPN instance view
        1. Run the [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* command to create a BGP-VPN instance and enter its view.
        2. Run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* **end-dt46** command to enable the device to add SIDs to VPN routes.
        3. Run the [**quit**](cmdqueryname=quit) command to exit the BGP-VPN instance view.
        4. Run the [**ipv4-family vpn-instance**](cmdqueryname=ipv4-family+vpn-instance) *vpn-instance-name* command to enter the BGP-VPN instance IPv6 address family view.
   6. Run [**segment-routing ipv6 best-effort**](cmdqueryname=segment-routing+ipv6+best-effort)
      
      
      
      The device is enabled to recurse VPN routes based on the SIDs carried in the routes.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After configuring L3VPNv6 over SRv6 BE, verify the configuration.

* Run the [**display segment-routing ipv6 locator**](cmdqueryname=display+segment-routing+ipv6+locator) [ *locator-name* ] **verbose** command to check SRv6 locator information.
* Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) { **end** | **end-x** | **end-dt6** | **end-dt46** } [ *sid* ] **forwarding** command to check information about the SRv6 local SID table.
* Run the [**display bgp vpnv6**](cmdqueryname=display+bgp+vpnv6) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** *ipv6-address* [ *prefix-length* ] command to check BGP VPNv6 routing information.
* Run the [**ping ipv6**](cmdqueryname=ping+ipv6) command to check the connectivity between CEs.