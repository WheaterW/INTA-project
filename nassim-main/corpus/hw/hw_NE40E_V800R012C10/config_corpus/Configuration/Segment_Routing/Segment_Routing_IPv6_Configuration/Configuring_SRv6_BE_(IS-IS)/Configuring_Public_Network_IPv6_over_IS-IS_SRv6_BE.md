Configuring Public Network IPv6 over IS-IS SRv6 BE
==================================================

This section describes how to configure public network IPv6 over SRv6 BE.

#### Usage Scenario

Public network IPv6 over SRv6 BE allows SRv6 BE paths on a public network to carry public network IPv6 data. The key implementation of public network IPv6 over SRv6 BE involves establishing SRv6 BE paths, advertising BGP routes, and forwarding data. [Figure 1](#EN-US_TASK_0233810266__fig_dc_vrp_srv6_cfg_all_001201) shows an example where an IPv6 public network is established between PE1 and PE2. An SRv6 BE path can be deployed on the IPv6 public network to carry public network IPv6 services.

**Figure 1** Public network IPv6 over SRv6 BE networking  
![](figure/en-us_image_0233810268.png)

#### Pre-configuration Tasks

Before configuring public network IPv6 over SRv6 BE, complete the following tasks:

* Configure a link layer protocol.
* Configure network-layer addresses for interfaces to ensure that neighboring devices are reachable at the network layer.

#### Procedure

1. Configure IPv6 IS-IS on the PEs and P. For configuration details, see [Configuring Basic IS-IS Functions (IPv6)](dc_vrp_isis_cfg_1023.html).
2. Establish an EBGP peer relationship between PE1 and DeviceA and another one between PE2 and DeviceB.
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
3. Establish an MP-IBGP peer relationship between the PEs.
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
4. Configure basic SRv6 functions.
   1. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      SRv6 is enabled, and the SRv6 view is displayed.
   2. Configure a source address for SRv6 encapsulation. Note that you only need to perform one of the following operations. If both of the operations are performed, the latest configuration overrides the previous one.
      
      
      * Run the [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) *ipv6-address* [ **ip-ttl** *ttl-value* ] command to directly configure a source address for SRv6 encapsulation.
      * Run the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) { *intfname* | *interfaceType* *interfaceNum* } [ **ip-ttl** *ttl-value* ] command to specify the interface to which the source address used for SRv6 encapsulation belongs.
        
        If no IPv6 global address is configured for the interface specified using the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) command, the source address for SRv6 encapsulation is not configured.
   3. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ]
      
      
      
      An SRv6 locator is configured, and the SRv6 locator view is displayed.
   4. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt6** or [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt46** **vpn-instance** *vpn-instance-name*
      
      
      
      An opcode for static SIDs is configured.
      
      
      
      A SID can be either dynamically allocated by BGP or manually configured. If a dynamically allocated SID and a manually configured SID both exist, the latter takes effect. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable dynamic End.DT6 SID allocation through BGP or the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46) command to enable dynamic End.DT46 SID allocation through BGP in the future, skip this step.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 locator view.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SRv6 view.
5. Enable IS-IS SRv6.
   1. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
      
      
      
      The IS-IS view is displayed.
   2. Run [**ipv6 enable topology ipv6**](cmdqueryname=ipv6+enable+topology+ipv6)
      
      
      
      IPv6 is enabled for the IS-IS process in the IPv6 topology.
   3. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6+%28IS-IS+view%29) **locator** *locator-name* [ **auto-sid-disable** ]
      
      
      
      IS-IS SRv6 is enabled.
   4. (Optional) Run [**segment-routing ipv6 auto-sid advertise**](cmdqueryname=segment-routing+ipv6+auto-sid+advertise) { **no-flavor** | **psp** | **psp-usp-usd** | **psp-usp-usd-coc** | **coc** | **psp-coc** | **psp-usp-usd-coc-next** | **psp-usd-next** } \*
      
      
      
      The function to adjust the flavors to be carried in dynamically allocated End and End.X SIDs is enabled.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the IS-IS view.
6. Configure public network routes on PEs to carry SIDs and recurse to SRv6 BE paths based on the SIDs.
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

After configuring public network IPv6 over SRv6 BE, verify the configuration.

* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) *ipv6-address* [ *mask* | *mask-length* ] command to check BGP IPv6 routing table information.
* Run the [**display segment-routing ipv6 locator**](cmdqueryname=display+segment-routing+ipv6+locator) [ *locator-name* ] **verbose** command to check SRv6 locator information.
* Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) [ **locator** *locator-name* ] **forwarding** command to check information about the SRv6 local SID table.