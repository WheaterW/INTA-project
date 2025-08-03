Configuring Public Network IPv6 over SRv6 TE Policy
===================================================

This section describes how to configure public network IPv6 over SRv6 TE Policy.

#### Usage Scenario

Public network IPv6 over SRv6 TE Policy uses SRv6 TE Policies on a public network to carry public network IPv6 services. The key implementation of public network IPv6 over SRv6 TE Policy includes establishing SRv6 TE Policies, advertising BGP routes, and forwarding data. As shown in [Figure 1](#EN-US_TASK_0304095422__fig_dc_vrp_srv6_cfg_all_001201), PE1 and PE2 communicate through an IPv6 public network. An SRv6 TE Policy can be established on the IPv6 public network to carry public network IPv6 services.

**Figure 1** Public network IPv6 over SRv6 TE Policy networking  
![](figure/en-us_image_0304095487.png)

#### Pre-configuration Tasks

Before configuring public network IPv6 over SRv6 TE Policy, complete the following tasks:

* Configure a link-layer protocol.
* Configure network-layer addresses for interfaces to ensure that neighboring devices are reachable at the network layer.

#### Procedure

1. Configure IPv6 IS-IS on the PEs and P. For configuration details, see [Configuring Basic IS-IS Functions (IPv6)](dc_vrp_isis_cfg_1023.html).
2. Establish an EBGP peer relationship between PE1 and DeviceA and another one between PE2 and DeviceB.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**router-id**](cmdqueryname=router-id) *ipv4-address* command to configure a BGP router ID.
   4. Run the [**peer**](cmdqueryname=peer) *ipv6-address* [**as-number**](cmdqueryname=as-number) *as-number* command to specify a peer address and the AS where the peer resides.
   5. Run the [**ipv6-family**](cmdqueryname=ipv6-family) **unicast** command to enter the BGP-IPv6 unicast address family view.
   6. Run the [**peer**](cmdqueryname=peer) *ipv6-address* [**enable**](cmdqueryname=enable) command to enable the device to exchange routing information with the specified IPv6 peer.
   7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   8. Run the [**quit**](cmdqueryname=quit) command to exit the BGP-IPv6 unicast address family view.
   9. Run the [**quit**](cmdqueryname=quit) command to exit the BGP view.
3. Establish an IBGP peer relationship between the PEs.
   1. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   2. Run the [**peer**](cmdqueryname=peer) *ipv6-address* [**as-number**](cmdqueryname=as-number) *as-number* command to specify a peer address and the AS where the peer resides.
   3. Run the [**peer**](cmdqueryname=peer) *ipv6-address* [**connect-interface**](cmdqueryname=connect-interface) *interface-type* *interface-number* command to specify the source interface and address used to establish a TCP connection.
   4. Run the [**ipv6-family**](cmdqueryname=ipv6-family) **unicast** command to enter the BGP-IPv6 unicast address family view.
   5. Run the [**peer**](cmdqueryname=peer) *ipv6-address* [**enable**](cmdqueryname=enable) command to enable the device to exchange routing information with the specified IPv6 peer.
   6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   7. Run the [**quit**](cmdqueryname=quit) command to exit the BGP-IPv6 unicast address family view.
   8. Run the [**quit**](cmdqueryname=quit) command to exit the BGP view.
4. Configure basic SRv6 functions.
   1. Run the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) command to enable SRv6 and enter its view.
   2. Configure a source address for SRv6 encapsulation. Note that you only need to perform one of the following operations. If both of the operations are performed, the latest configuration overrides the previous one.
      
      
      * Run the [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) *ipv6-address* [ **ip-ttl** *ttl-value* ] command to directly configure a source address for SRv6 encapsulation.
      * Run the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) { *intfname* | *interfaceType* *interfaceNum* } [ **ip-ttl** *ttl-value* ] command to specify the interface to which the source address used for SRv6 encapsulation belongs.
        
        If no IPv6 global address is configured for the interface specified using the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) command, the source address for SRv6 encapsulation is not configured.
   3. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ]
      
      
      
      An SRv6 locator is configured, and the SRv6 locator view is displayed.
   4. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt6** or [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt46** **vpn-instance** *vpn-instance-name*
      
      
      
      An opcode for static SIDs is configured.
      
      
      
      A SID can be either dynamically allocated by BGP or manually configured. If a dynamically allocated SID and a manually configured SID both exist, the latter takes effect. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable dynamic End.DT6 SID allocation through BGP or the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46) command to enable dynamic End.DT46 SID allocation through BGP in the future, skip this step.
   5. Run the [**quit**](cmdqueryname=quit) command to exit the SRv6 locator view.
   6. Run the [**quit**](cmdqueryname=quit) command to exit the SRv6 view.
5. Enable IS-IS SRv6.
   1. Run the [**isis**](cmdqueryname=isis) [ *process-id* ] command to enter the IS-IS view.
   2. Run the [**ipv6 enable topology ipv6**](cmdqueryname=ipv6+enable+topology+ipv6) command to enable the IPv6 capability for the IS-IS process in the IPv6 topology.
   3. Run the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6+%28IS-IS+view%29) **locator** *locator-name* [ **auto-sid-disable** ] command to enable IS-IS SRv6.
   4. Run the [**quit**](cmdqueryname=quit) command to exit the IS-IS view.
6. Configure each PE to carry color and SID attributes in public network routes to be advertised.
   1. Run the [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **permit** | **deny** } **node** *node* command to create a route-policy with a specified node and enter the route-policy view.
   2. Run the [**apply extcommunity color**](cmdqueryname=apply+extcommunity+color) *color* command to specify a color extended community attribute.
   3. Run the [**quit**](cmdqueryname=quit) command to exit the route-policy view.
   4. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   5. (Optional) Run [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46)
      
      
      
      The device is enabled to add SIDs to public network routes.
   6. Run the [**ipv6-family**](cmdqueryname=ipv6-family) **unicast** command to enter the BGP-IPv6 unicast address family view.
   7. Run the [**peer**](cmdqueryname=peer) *ipv6-address* **route-policy** *route-policy-name* **export** command to apply the export route-policy to routes to be advertised to the specified peer so that the color attribute can be carried in these routes.
   8. Run the [**peer**](cmdqueryname=peer) *peerIpv6Addr* **advertise-ext-community** command to enable the device to advertise extended community attributes to the specified peer.
   9. Run the [**peer**](cmdqueryname=peer) *ipv6-address* **prefix-sid** [ **advertise-srv6-locator** ] command to enable the device to exchange prefix SID and locator information with the specified peer.
   10. Run [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name*
       
       
       
       The device is enabled to add SIDs to public network routes.
       
       
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46) command has been run in the BGP view, skip this step.
   11. (Optional) Run [**segment-routing ipv6 color-only**](cmdqueryname=segment-routing+ipv6+color-only)
       
       
       
       The device is enabled to recurse public network routes to color-only SRv6 TE Policies.
       
       
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       This command applies only to color-only scenarios and supports only statically configured SRv6 TE Policies.
   12. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
7. Configure an SRv6 TE Policy. For configuration details, see [Configuring an SRv6 TE Policy (Manual Configuration + IS-IS as an IGP)](dc_vrp_srv6_cfg_all_0110.html) or [Configuring an SRv6 TE Policy (Dynamic Delivery by a Controller + IS-IS as an IGP)](dc_vrp_srv6_cfg_all_0116.html).
8. Configure public network routes to recurse to the SRv6 TE Policy.
   1. Run the [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name* command to create a tunnel policy and enter the tunnel policy view.
   2. Run the [**tunnel select-seq ipv6**](cmdqueryname=tunnel+select-seq+ipv6) **srv6-te-policy** **load-balance-number** *loadBalanceNumber* command to specify the tunnel type to be selected and the maximum number of tunnels that can participate in load balancing.
   3. Run the [**quit**](cmdqueryname=quit) command to exit the tunnel policy view.
   4. Run the [**tunnel-selector**](cmdqueryname=tunnel-selector) *name* { **permit** | **deny** } **node** *node* command to create a tunnel selector and enter the tunnel selector view.
   5. Run the [**apply tunnel-policy**](cmdqueryname=apply+tunnel-policy) *tunnel-policy-name* command to apply a tunnel policy to routes.
   6. Run the [**quit**](cmdqueryname=quit) command to exit the tunnel selector view.
   7. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   8. Run the [**ipv6-family**](cmdqueryname=ipv6-family) **unicast** command to enter the BGP-IPv6 unicast address family view.
   9. Run the [**unicast-route recursive-lookup tunnel-v6 tunnel-selector**](cmdqueryname=unicast-route+recursive-lookup+tunnel-v6+tunnel-selector) *tunnel-selector-name* command to enable the function to recurse public network routes to IPv6 tunnels.
   10. Run the [**segment-routing ipv6 traffic-engineer**](cmdqueryname=segment-routing+ipv6+traffic-engineer) command to enable the device to recurse routes to the SRv6 TE Policy based on the color and SID values carried in the routes.
   11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After configuring public network IPv6 over SRv6 TE Policy, verify the configuration.

* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) *ipv6-address* [ *mask* | *mask-length* ] command to check BGP IPv6 routing table information.
* Run the [**display segment-routing ipv6 locator**](cmdqueryname=display+segment-routing+ipv6+locator) [ *locator-name* ] **verbose** command to check SRv6 locator information.
* Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) [ **locator** *locator-name* ] **forwarding** command to check information about the SRv6 local SID table.