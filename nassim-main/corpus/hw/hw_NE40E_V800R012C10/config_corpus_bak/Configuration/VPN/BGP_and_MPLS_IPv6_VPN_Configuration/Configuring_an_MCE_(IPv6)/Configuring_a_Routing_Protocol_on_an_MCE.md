Configuring a Routing Protocol on an MCE
========================================

To enable a multi-VPN-instance customer edge (MCE) to communicate with provider edge (PE) and virtual private network (VPN) devices, configure a routing protocol for each type of service on the MCE.

#### Context

An MCE can communicate with PEs and VPN devices using any of the following routing protocols: BGP4+, IPv6 static route, RIPng, OSPFv3, or IS-ISv6. Select one of the following configuration procedures:

* [Configure BGP4+ on the MCE.](#EN-US_TASK_0172369670__step_dc_vrp_mpls-l3vpn-v6_cfg_207101)
* [Configure a static route on the MCE.](#EN-US_TASK_0172369670__step_dc_vrp_mpls-l3vpn-v6_cfg_207103)
* [Configure RIPng on the MCE.](#EN-US_TASK_0172369670__step_dc_vrp_mpls-l3vpn-v6_cfg_207104)
* [Configure OSPFv3 on the MCE.](#EN-US_TASK_0172369670__step_dc_vrp_mpls-l3vpn-v6_cfg_207105)
* [Configure IS-ISv6 on the MCE.](#EN-US_TASK_0172369670__step_dc_vrp_mpls-l3vpn-v6_cfg_207106)


#### Procedure

* Configure BGP4+ on the MCE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv6 address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer) *ipv6-address* **as-number** *as-number*
     
     
     
     A PE is configured as a VPN BGP peer for the MCE.
  5. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } [**ebgp-max-hop**](cmdqueryname=ebgp-max-hop) [ *hop-count* ]
     
     
     
     The maximum number of hops between the MCE and its EBGP peer (the PE) is set.
     
     
     
     This step is mandatory if the MCE is not directly connected to the PE. Generally, EBGP peers are directly connected. If they are not directly connected, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command so that EBGP peers can establish a multi-hop Transmission Control Protocol (TCP) connection.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a static route on the MCE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ipv6 route-static vpn-instance**](cmdqueryname=ipv6+route-static+vpn-instance) *vpn-source-name* *destination-ipv6-address* *prefix-length* *interface-type interface-number* [ *nexthop-ipv6-address* ] [ **preference** *preference* | **tag** *tag* ] \*
     
     
     
     A static route is configured for a specified VPN instance IPv6 address family.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure RIPng on the MCE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ripng**](cmdqueryname=ripng) *process-id* **vpn-instance** *vpn-instance-name*
     
     
     
     A RIPng process is created, and the RIPng view is displayed. A RIPng process can be bound only to one VPN instance. If you do not specify a VPN instance when creating a RIPng process, this RIPng process is a public network process and can no longer be bound to a VPN instance.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Deleting a VPN instance or disabling a VPN instance IPv6 address family will also delete all the RIPng processes bound to this VPN instance or VPN instance IPv6 address family.
* Configure OSPFv3 on the MCE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ] **vpn-instance** *vpnname*
     
     
     
     An OSPFv3 process is created, and the OSPFv3 view is displayed.
     
     
     
     Create the same OSPFv3 process on the MCE and its connected PE. An OSPFv3 process can be bound only to one VPN instance.
  3. (Optional) Run [**domain-id**](cmdqueryname=domain-id) { *domain-id-int* | *domain-id-ipaddr* }
     
     
     
     A domain ID is set.
     
     The domain ID can be an integer or in dotted decimal notation.
     
     Generally, the routes that are imported from a PE are advertised as External-LSAs. The routes that belong to different nodes of the same OSPFv3 domain are advertised as Type-3 LSAs (intra-domain routes). This requires that different nodes in the same OSPFv3 domain have the same domain ID.
  4. (Optional) Run [**route-tag**](cmdqueryname=route-tag) *tag-value*
     
     
     
     A tag value is set.
  5. Run [**vpn-instance-capability simple**](cmdqueryname=vpn-instance-capability+simple)
     
     
     
     Rout loop detection is disabled.
     
     If OSPFv3 VPN multi-VPN-instance has been deployed on the MCE and PE, the PE sends the MCE a link-state advertisement (LSA) with the Down (DN) bit set to 1. Because VPN instances have been configured on the MCE, the MCE has routing loop detection enabled. If the MCE detects that the LSA contains the DN bit with the value 1, this LSA cannot be used to calculate routes. Run the [**vpn-instance-capability simple**](cmdqueryname=vpn-instance-capability+simple) command to disable OSPFv3 routing loop detection. When OSPFv3 routing loop detection is disabled, the MCE calculates all OSPFv3 routes without checking the DN bit and route tag.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface bound to the VPN instance is displayed.
  8. Run [**ospfv3**](cmdqueryname=ospfv3) *process-id* **area** *area-id* [ **instance** *instance-id* ]
     
     
     
     OSPFv3 is enabled on the interface.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Deleting a VPN instance or disabling a VPN instance IPv6 address family will also delete all the OSPFv3 processes bound to this VPN instance or VPN instance IPv6 address family.
* Configure IS-ISv6 on the MCE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) *process-id* **vpn-instance** *vpn-instance-name*
     
     
     
     An IS-IS instance is created on the MCE, and the IS-IS view is displayed.
     
     An IS-IS process can be bound only to one VPN instance. If you do not specify a VPN instance when creating an IS-IS process, this IS-IS process is a public network process and can no longer be bound to a VPN instance.
  3. Run [**network-entity**](cmdqueryname=network-entity) *net-addr*
     
     
     
     The network entity title (NET) is set.
     
     A NET contains the current IS-IS area address and the system ID of the router. A maximum of three NETs can be set in one IS-IS process.
  4. (Optional) Run [**is-level**](cmdqueryname=is-level) { **level-1** | **level-1-2** | **level-2** }
     
     
     
     An IS-IS level is specified for the router.
  5. Run [**ipv6 enable**](cmdqueryname=ipv6+enable+%28IS-IS+view%29) [ **topology** { **compatible** [ **enable-mt-spf** ] | **ipv6** | **standard** } ]
     
     
     
     IPv6 is enabled for the IS-IS process.
     
     IPv6 can be enabled for an IS-IS process only after being enabled in the system view.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface to be bound to the VPN instance is displayed.
  8. Run [**isis ipv6 enable**](cmdqueryname=isis+ipv6+enable) [ *process-id* ]
     
     
     
     IS-ISv6 is enabled on the interface.
  9. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Deleting a VPN instance or disabling a VPN instance IPv6 address family will also delete all the IS-IS processes bound to this VPN instance or VPN instance IPv6 address family.