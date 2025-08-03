Configuring a Routing Protocol on the PE Connected to the MCE
=============================================================

To enable a provider edge (PE) to communicate with a multi-VPN-instance customer edge (MCE), configure routing protocol multi-VPN-instance on the MCE.

#### Context

A PE can communicate with an MCE using any of the following routing protocols: BGP4+, IPv6 static route, RIPng, OSPFv3, or IS-ISv6. Select one of the following configuration procedures:

* [Configure BGP4+ on the PE.](#EN-US_TASK_0172369671__step_dc_vrp_mpls-l3vpn-v6_cfg_207201)
* [Configure a static route on the PE.](#EN-US_TASK_0172369671__step_dc_vrp_mpls-l3vpn-v6_cfg_207203)
* [Configure RIPng on the PE.](#EN-US_TASK_0172369671__step_dc_vrp_mpls-l3vpn-v6_cfg_207204)
* [Configure OSPFv3 on the PE.](#EN-US_TASK_0172369671__step_dc_vrp_mpls-l3vpn-v6_cfg_207205)
* [Configure IS-ISv6 on the PE.](#EN-US_TASK_0172369671__step_dc_vrp_mpls-l3vpn-v6_cfg_207206)


#### Procedure

* Configure BGP4+ on the PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv6 address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer) *ipv6-address* **as-number** *as-number*
     
     
     
     An MCE is configured as a VPN BGP peer for the PE.
  5. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } [**ebgp-max-hop**](cmdqueryname=ebgp-max-hop) [ *hop-count* ]
     
     
     
     The maximum number of hops between the PE and its EBGP peer (the MCE) is set.
  6. (Optional) Run either of the following commands to enable the PE to import the direct routes destined for the MCE into the VPN routing and forwarding (VRF) table and advertise the routes to the remote PE:
     
     
     + [**import-route**](cmdqueryname=import-route) **direct** [ **med** *med* | **route-policy** *route-policy-name* ] \*
     + [**network**](cmdqueryname=network) *ipv6-address* *prefix-length* [ **route-policy** *route-policy-name* ]
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The PE automatically learns the direct routes destined for the MCE. The learned routes take precedence over the direct routes advertised from the MCE using EBGP. If this step is not performed, the PE does not use the Multi-protocol Extensions for Border Gateway Protocol (MP-BGP) to advertise the direct routes destined for the MCE to the remote PE.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a static route on the PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ipv6 route-static vpn-instance**](cmdqueryname=ipv6+route-static+vpn-instance) *vpn-source-name* *destination-ipv6-address* *prefix-length* *interface-type interface-number* [ *nexthop-ipv6-address* ] [ **preference** *preference* | **tag** *tag* ] \*
     
     
     
     A static route is configured for a specified VPN instance IPv6 address family.
  3. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  4. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv6 address family view is displayed.
  5. Run [**import-route**](cmdqueryname=import-route) **static** [ **med** *med* | **route-policy** *route-policy-name* ] \*
     
     
     
     The configured static route is added to the VRF table of the BGP-VPN instance IPv6 address family.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure RIPng on the PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ripng**](cmdqueryname=ripng) *process-id* **vpn-instance** *vpn-instance-name*
     
     
     
     A RIPng process is created on the PE, and the RIPng view is displayed.
     
     A RIPng process can be bound only to one VPN instance.
  3. Run [**import-route**](cmdqueryname=import-route) **bgp** [ **permit-ibgp** ] [ **cost** *cost* | **inherit-cost** | **route-policy** *route-policy-name* ] \*
     
     
     
     BGP routes are imported.
     
     After the [**import-route**](cmdqueryname=import-route) **bgp** command is run in the RIPng view, the PE can import the VPN-IPv6 routes learned from the remote PE into the RIPng routing table and advertise them to the attached MCE.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface connected to the MCE is displayed.
  6. Run [**ripng**](cmdqueryname=ripng) *process-id* **enable**
     
     
     
     RIPng is enabled on the interface.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If IPv6 is not enabled, this command cannot be run in the interface view.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  8. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  9. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv6 address family view is displayed.
  10. Run [**import-route**](cmdqueryname=import-route) **ripng** *process-id* [ **med** *med* | **route-policy** *route-policy-name* ] \*
      
      
      
      The configured RIPng route is added to the VRF table of the BGP-VPN instance IPv6 address family.
      
      After the [**import-route**](cmdqueryname=import-route) **ripng** command is run in the BGP-IPv6 VPN instance IPv6 address family view, the PE will import the IPv6 routes learned from the MCE into the BGP routing table and advertise VPN-IPv6 routes to the remote PE.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If a RIPng multi-instance process is deleted, RIPng will be disabled on all the interfaces in the process.
      
      Deleting a VPN instance or disabling a VPN instance IPv6 address family will delete all the RIPng processes bound to the VPN instance or VPN instance IPv6 address family on the PE.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Deleting a VPN instance or disabling a VPN instance IPv6 address family will also delete all the RIPng processes bound to this VPN instance or VPN instance IPv6 address family.
* Configure OSPFv3 on the PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ] **vpn-instance** *vpnname*
     
     
     
     An OSPFv3 process is created, and the OSPFv3 view is displayed.
     
     An OSPFv3 process can be bound only to one VPN instance.
  3. Run [**router-id**](cmdqueryname=router-id) *router-id*
     
     
     
     A router ID is configured. The router ID of each OSPFv3 process is unique in an AS. If no router ID is set, no OSPFv3 process can be run.
  4. (Optional) Run [**domain-id**](cmdqueryname=domain-id) { *domain-id-int* | *domain-id-ipaddr* }
     
     
     
     A domain ID is set.
     
     The domain ID can be an integer or in dotted decimal notation.
     
     Generally, the routes that are imported from a PE are advertised as External-LSAs. The routes that belong to different nodes of the same OSPFv3 domain are advertised as Type-3 LSAs (intra-domain routes). This requires that different nodes in the same OSPFv3 domain have the same domain ID.
  5. (Optional) Run [**route-tag**](cmdqueryname=route-tag) *tag-value*
     
     
     
     A VPN route tag is set.
  6. Run [**import-route**](cmdqueryname=import-route) **bgp** [ **cost** *cost* | **route-policy** *route-policy-name* | **tag** *tag* | **type** *type* ] \*
     
     
     
     BGP routes are imported into the OSPFv3 routing table so that the PE can advertise the routes to the MCE using OSPFv3.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  8. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface bound to the VPN instance is displayed.
  9. Run [**ospfv3**](cmdqueryname=ospfv3) *process-id* **area** *area-id* [ **instance** *instance-id* ]
     
     
     
     OSPFv3 is enabled on the interface.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
  11. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
  12. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv6 address family view is displayed.
  13. Run [**import-route**](cmdqueryname=import-route) **ospfv3** *process-id* [ **med** *med* | **route-policy** *route-policy-name* ]\*
      
      
      
      OSPFv3 routes are imported into the VRF table of the BGP-VPN instance IPv6 address family.
  14. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Deleting a VPN instance or disabling a VPN instance IPv6 address family will also delete all the OSPFv3 processes bound to this VPN instance or VPN instance IPv6 address family.
* Configure IS-ISv6 on the PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) *process-id* **vpn-instance** *vpn-instance-name*
     
     
     
     An IS-IS process is created on the PE, and the IS-IS view is displayed.
     
     An IS-IS multi-instance process can be bound to only one VPN instance. If an IS-IS process is not bound to any VPN instance before it is started, this process becomes a public network process. If only one IS-IS process, either a public network IS-IS process or a multi-instance IS-IS instance, runs on the router, you do not need to specify *process-id* in the command. The value of *process-id* defaults to 1.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If an IS-IS multi-instance process is deleted, IS-IS will be disabled on all the interfaces in the process.
  3. Run [**network-entity**](cmdqueryname=network-entity) *net-addr*
     
     
     
     The NET is set.
     
     A NET specifies the current IS-IS area address and the system ID of the router.
  4. (Optional) Run [**is-level**](cmdqueryname=is-level) { **level-1** | **level-1-2** | **level-2** }
     
     
     
     The IS-IS level of the Router is specified.
  5. Run [**ipv6 enable**](cmdqueryname=ipv6+enable+%28IS-IS+view%29) [ **topology** { **compatible** [ **enable-mt-spf** ] | **ipv6** | **standard** } ]
     
     
     
     IPv6 is enabled for the IS-IS process.
     
     IPv6 can be enabled for an IS-IS process only after being enabled in the system view.
  6. Run [**ipv6 import-route**](cmdqueryname=ipv6+import-route) **bgp** **inherit-cost** [ **tag** *tag* | **route-policy** *route-policy-name* | [ **level-1** | **level-2** | **level-1-2** ] ]\*
     
     
     
     BGP routes are imported.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  8. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  9. Run [**isis ipv6 enable**](cmdqueryname=isis+ipv6+enable) [ *process-id* ]
     
     
     
     IS-ISv6 is enabled on the interface.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
  11. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
  12. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv6 address family view is displayed.
  13. Run [**import-route**](cmdqueryname=import-route) **isis** *process-id* [ **med** *med* | **route-policy** *route-policy-name* ]\*
      
      
      
      IS-IS routes are imported into the VRF table of the BGP-VPN instance IPv6 address family.
  14. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Deleting a VPN instance or disabling a VPN instance IPv6 address family will also delete all the IS-IS processes bound to this VPN instance or VPN instance IPv6 address family.