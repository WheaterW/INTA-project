Configuring Route Exchange Between PEs and CEs
==============================================

To enable CEs to communicate, the PEs and CEs must be capable of exchanging routes.

#### Context

In BGP/MPLS IPv6 VPN, a routing protocol or IPv6 static route must be configured between a PE and a CE to allow them to communicate and allow the CE to obtain routes to other CEs. The routing protocol can be BGP4+, IPv6 static route, RIPng, OSPFv3, or IS-ISv6. Choose one of the following configurations as needed:

* [Configure BGP4+ between a PE and a CE.](#EN-US_TASK_0172369590__step_dc_vrp_mpls-l3vpn-v6_cfg_206101)
* [Configure a static route between a PE and a CE.](#EN-US_TASK_0172369590__step_dc_vrp_mpls-l3vpn-v6_cfg_206102)
* [Configure RIPng between a PE and a CE.](#EN-US_TASK_0172369590__step_dc_vrp_mpls-l3vpn-v6_cfg_206103)
* [Configure OSPFv3 between a PE and a CE.](#EN-US_TASK_0172369590__step_dc_vrp_mpls-l3vpn-v6_cfg_206104)
* [Configure IS-ISv6 between a PE and a CE.](#EN-US_TASK_0172369590__step_dc_vrp_mpls-l3vpn-v6_cfg_206105)
* [Configure a direct route between a PE and a CE.](#EN-US_TASK_0172369590__step_dc_vrp_mpls-l3vpn-v6_cfg_206106)

The routing protocol configurations on the CE and PE are different:

* The CE is located at the client side and unaware of the VPN. Therefore, you do not need to configure VPN parameters when configuring a routing protocol on the CE.
* It connects to a CE and exchanges VPN routing information with other PEs. If the CEs that access a PE belong to different VPNs, the PE must maintain different VRF tables. When configuring a routing protocol on the PE, specify the name of the VPN instance to which the routing protocol applies and configure the routing protocol and MP-BGP to import routes from each other. The PE is located at the edge of the carrier's network.


#### Procedure

* Configure BGP4+ between a PE and a CE.
  
  
  
  Perform the following steps on the PE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv6 address family view is displayed.
  4. (Optional) Run [**as-number**](cmdqueryname=as-number) { *as-number-plain* | *as-number-dot* }
     
     
     
     A separate AS number is configured for the VPN instance IPv6 address family.
     
     
     
     In scenarios such as network migration or service identification, to logically simulate a device as multiple BGP devices, run the [**as-number**](cmdqueryname=as-number) command to configure a different AS number for each VPN instance IPv6 address family.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The AS number configured in the VPN instance IPv6 address family view must be different from the AS number configured in the BGP view.
     
     After the [**bgp yang-mode enable**](cmdqueryname=bgp+yang-mode+enable) command is run, the [**as-number**](cmdqueryname=as-number) { *as-number-plain* | *as-number-dot* } command cannot be run. To configure a separate AS number for the VPN instance IPv6 address family, run the [**as-number ipv6**](cmdqueryname=as-number+ipv6) *ipv6-as* [ **no-prepend** ] command in the BGP-VPN instance view.
     
     If **no-prepend** is not configured, the AS\_Path attribute of a VPN route sent to the VPNv6 routing table carries the configured AS number. If **no-prepend** is configured, the AS\_Path attribute of a VPN route sent to the VPNv6 routing table does not carry the configured AS number.
  5. Run [**peer**](cmdqueryname=peer) *ipv6-address* **as-number** *as-number*
     
     
     
     The CE is configured as an IPv6 VPN peer.
  6. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } **ebgp-max-hop** [ *hop-count* ]
     
     
     
     The maximum number of hops between the PE and its EBGP peer is specified. This step is mandatory if the PE and CE are not directly connected.
     
     If the maximum number of hops is set to 1, the PE cannot establish an EBGP connection to a peer if they are not directly connected.
  7. (Optional) Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv6-address* } **soo** *site-of-origin*
     
     
     
     The SoO attribute is configured for the CE that has been specified as an IPv6 VPN peer of the PE.
     
     
     
     Several CEs at a VPN site may establish BGP connections to different PEs. The VPN routes advertised from the CEs to the PEs may be re-advertised to the same VPN site after the routes traverse the backbone network. This may cause route loops at the VPN site.
     
     If the SoO attribute is configured for a specified CE, the PE adds the attribute to a route sent from the CE and advertises the route to the remote PE. The remote PE checks the SoO attribute of the route before sending it to its attached CE. If the SoO attribute is the same as the local SoO attribute on the remote PE, the remote PE does not send the route to its attached CE.
  8. (Optional) Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv6-address* } **allow-as-loop** [ *number* ]
     
     
     
     Routing loops are allowed. This step is used in hub-spoke networking.
     
     Generally, BGP uses AS numbers to detect routing loops. On a hub-spoke network, if EBGP runs between a hub-PE and a hub-CE at a hub site, the route sent from the hub-PE to the hub-CE carries the AS number of the hub-PE. If the hub-CE sends a route update message to the hub-PE, the hub-PE will deny it because the route update message contains the AS number of the hub-PE. To ensure proper route transmission on a hub-spoke network, configure all the BGP peers on the path (along which the hub-CE advertises VPN routes to the spoke-CE) to accept the routes which have the AS number repeated once.
  9. (Optional) Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv6-address* } **substitute-as**
     
     
     
     BGP AS number substitution is enabled.
     
     
     
     Perform this step on the PE in a scenario in which CEs at different sites use the same AS number.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     Enabling BGP AS number substitution may cause routing loops on a CE multi-homing network.
  10. (Optional) Run either of the following commands:
      
      
      + To configure the device to send only optimal routes in the BGP VPN routing table to the BGP VPNv6 routing table, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command.
        
        By default, when a local device receives a remotely leaked route (route A) that has the same prefix as that of a route (route B) in the local VPN routing table but route A and route B have different RDs, the device also sends route B to the BGP VPNv6 routing table even if the route selection priority of route B is lower than that of route A. If route B meets BGP VPNv6 route sending conditions, the device also sends it to other BGP VPNv6 peers. In this scenario, if you want only optimal BGP VPN routes to be transmitted between BGP VPNv6 peers on the network, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command on the local device, so that the device sends only optimal routes in the BGP VPN routing table to the BGP VPNv6 routing table.
      + To configure the device to send only valid routes in a BGP VPN routing table to a BGP VPNv6 routing table, run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command.
        
        By default, the device advertises all routes in the BGP VPN routing table to the BGP VPNv6 routing table. You can run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command to advertise valid routes to the BGP VPNv6 routing table.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
  
  
  
  Perform the following steps on the CE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. (Optional) Run [**router-id**](cmdqueryname=router-id) *ipv4-address*
     
     
     
     A router ID is set for the CE. If no interface on the local CE is assigned an IPv4 address, you must set the router ID for the local CE.
  4. Run [**peer**](cmdqueryname=peer) *ipv6-address* **as-number** *as-number*
     
     
     
     The PE is configured as an IPv6 VPN peer.
  5. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } **ebgp-max-hop** [ *hop-count* ]
     
     
     
     The maximum number of hops between the CE and its EBGP peer (the PE) is set. This step is mandatory if the PE and CE are not directly connected.
     
     If the maximum number of hops is set to 1, the CE cannot establish an EBGP connection to a peer if they are not directly connected.
  6. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The BGP-IPv6 unicast address family view is displayed.
  7. Run [**peer**](cmdqueryname=peer) *ipv6-address* **enable**
     
     
     
     The function to exchange BGP route information with the specified BGP IPv6 peer is enabled.
  8. Run [**import-route**](cmdqueryname=import-route) { **direct** | **static** | **ripng** *process-id* | **ospfv3** *process-id* | **isis** *process-id* } [ **med** *med* | **route-policy** *route-policy-name* ]\*
     
     
     
     Local routes are imported.
     
     The CE imports and advertises the local routes to the connected PE, which in turn advertises them to the remote CE. The type of route imported at this step varies according to specified route type.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure IPv6 static routes between a PE and a CE.
  
  
  
  Perform the following steps on the PE:
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Configuring an IPv6 static route on the CE is not described here. For details about how to configure an IPv6 static route, see ["IPv6 Static Route Configuration" in *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - IP Routing*](dc_vrp_static-route-ipv6_cfg_0000.html).
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ipv6 route-static vpn-instance**](cmdqueryname=ipv6+route-static+vpn-instance) *vpn-instance-name* *dest-ipv6-address* *prefix-length* { *interface-type* *interface-number* [ *nexthop-ipv6-address* ] | **vpn-instance** *vpn-destination-name* *nexthop-ipv6-address* | *nexthop-ipv6-address* [ **public** ] } [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]
     
     
     
     A static route is configured for a specified VPN instance IPv6 address family.
  3. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  4. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv6 address family view is displayed.
  5. Run [**import-route**](cmdqueryname=import-route) **static** [ **med** *med* | **route-policy** *route-policy-name* ] \*
     
     
     
     The configured static route is added to the routing table of the BGP-VPN instance IPv6 address family.
  6. (Optional) Run either of the following commands:
     
     
     + To configure the device to send only optimal routes in the BGP VPN routing table to the BGP VPNv6 routing table, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command.
       
       By default, when a local device receives a remotely leaked route (route A) that has the same prefix as that of a route (route B) in the local VPN routing table but route A and route B have different RDs, the device also sends route B to the BGP VPNv6 routing table even if the route selection priority of route B is lower than that of route A. If route B meets BGP VPNv6 route sending conditions, the device also sends it to other BGP VPNv6 peers. In this scenario, if you want only optimal BGP VPN routes to be transmitted between BGP VPNv6 peers on the network, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command on the local device, so that the device sends only optimal routes in the BGP VPN routing table to the BGP VPNv6 routing table.
     + To configure the device to send only valid routes in a BGP VPN routing table to a BGP VPNv6 routing table, run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command.
       
       By default, the device advertises all routes in the BGP VPN routing table to the BGP VPNv6 routing table. You can run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command to advertise valid routes to the BGP VPNv6 routing table.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  
  
  The configuration of the CE is the same as the configuration of common IPv6 static routes, and is not described here.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  A VPN that receives routes outside it from a device other than the PE and advertises the routes to the PE is called a transit VPN. A VPN that receives only routes in it and routes advertised by the PE is called a stub VPN. Generally, a static route is used for route exchange between the CE and PE in a stub VPN only.
* Configure RIPng between a PE and a CE.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Configuring RIPng on the CE is not described here. For details about how to configure RIPng, see "RIPng Configuration" in the [*HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - IP Routing*.](dc_vrp_ripng_cfg_0000.html)
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ripng**](cmdqueryname=ripng) [ *process-id* ] **vpn-instance** *vpn-instance-name*
     
     
     
     A RIPng process is created on the PE. A RIPng multi-instance process can be bound to only one VPN instance. If a RIPng process is not bound to any VPN instance before it is started, this process becomes a public network process.
     
     If only one RIPng process, either a public network RIPng process or a RIPng multi-instance process, runs on the Router, you do not need to specify *process-id* in the command. The value of *process-id* is 1 by default.
  3. Run [**import-route**](cmdqueryname=import-route) **bgp** [ **permit-ibgp** ] [ **cost** *cost* | **inherit-cost** | **route-policy** *route-policy-name* ] \*
     
     
     
     BGP routes are imported. After the **import-route bgp** command is run in the RIPng view, the PE can import the VPNv6 routes learned from the remote PE into the RIPng routing table and advertise them to the attached CE.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
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
      
      
      
      The learned RIPng route is added to the routing table of the BGP-IPv6 VPN instance IPv6 address family. After the **import-route** **ripng** command is run in the BGP-IPv6 VPN instance IPv6 address family view, the PE imports the IPv6 routes learned from the attached CE into the BGP routing table and advertises VPN-IPv6 routes to the remote PE.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If a RIPng multi-instance process is deleted, RIPng will be disabled on all the interfaces in the process.
      
      Deleting a VPN instance or disabling a VPN instance IPv6 address family will delete all the RIPng processes bound to the VPN instance or the VPN instance IPv6 address family on the PE.
  11. (Optional) Run either of the following commands:
      
      
      + To configure the device to send only optimal routes in the BGP VPN routing table to the BGP VPNv6 routing table, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command.
        
        By default, when a local device receives a remotely leaked route (route A) that has the same prefix as that of a route (route B) in the local VPN routing table but route A and route B have different RDs, the device also sends route B to the BGP VPNv6 routing table even if the route selection priority of route B is lower than that of route A. If route B meets BGP VPNv6 route sending conditions, the device also sends it to other BGP VPNv6 peers. In this scenario, if you want only optimal BGP VPN routes to be transmitted between BGP VPNv6 peers on the network, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command on the local device, so that the device sends only optimal routes in the BGP VPN routing table to the BGP VPNv6 routing table.
      + To configure the device to send only valid routes in a BGP VPN routing table to a BGP VPNv6 routing table, run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command.
        
        By default, the device advertises all routes in the BGP VPN routing table to the BGP VPNv6 routing table. You can run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command to advertise valid routes to the BGP VPNv6 routing table.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure OSPFv3 between a PE and a CE.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Configuring OSPFv3 on the CE is not described here. For details about how to configure OSPFv3, see ["OSPFv3 Configuration" in *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - IP Routing*](dc_vrp_ospfv3_cfg_2000.html).
  
  Perform the following steps on the PE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ] [ **vpn-instance** *vpnname* ]
     
     
     
     An OSPFv3 multi-instance process is started, and its view is displayed. An OSPFv3 process can be bound to only one VPN instance. If an OSPFv3 process is not bound to any VPN instance before it is started, this process becomes a public network process and cannot be bound to a VPN instance later.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Deleting a VPN instance or disabling a VPN instance IPv6 address family will delete all the OSPFv3 processes bound to the VPN instance or the VPN instance IPv6 address family on the PE.
  3. Run [**router-id**](cmdqueryname=router-id) *router-id*
     
     
     
     A router ID is configured. The router ID of each OSPFv3 process is unique in an AS. If no router ID is set, no OSPFv3 process can be run.
  4. (Optional) Run [**domain-id**](cmdqueryname=domain-id) { *domain-id-int* | *domain-id-ipaddr* }
     
     
     
     The domain ID is configured. The domain ID can be an integer or in dotted decimal notation.
     
     Generally, the routes that are imported from a PE are advertised as External-LSAs. The routes that belong to different nodes of the same OSPFv3 domain are advertised as Type-3 LSAs (intra-domain routes). This requires that different nodes in the same OSPFv3 domain have the same domain ID.
  5. (Optional) Run [**route-tag**](cmdqueryname=route-tag) *tag-value*
     
     
     
     A VPN route tag is set.
  6. Run [**import-route**](cmdqueryname=import-route) **bgp** [ **cost** *cost* | **route-policy** *route-policy-name* | **tag** *tag* | **type** *type* ] \*
     
     
     
     BGP routes are imported into the OSPFv3 routing table so that the PE can advertise the routes to the CE using OSPFv3.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  8. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  9. Run [**ospfv3**](cmdqueryname=ospfv3) *process-id* **area** *area-id* [ **instance** *instance-id* ]
     
     
     
     OSPFv3 is enabled on the interface.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
  11. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
  12. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv6 address family view is displayed.
  13. Run [**import-route**](cmdqueryname=import-route) **ospfv3** *process-id* [ **med** *med* | **route-policy** *route-policy-name* ]\*
      
      
      
      OSPFv3 routes are imported into the routing table of the BGP-VPN instance IPv6 address family.
  14. (Optional) Run either of the following commands:
      
      
      + To configure the device to send only optimal routes in the BGP VPN routing table to the BGP VPNv6 routing table, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command.
        
        By default, when a local device receives a remotely leaked route (route A) that has the same prefix as that of a route (route B) in the local VPN routing table but route A and route B have different RDs, the device also sends route B to the BGP VPNv6 routing table even if the route selection priority of route B is lower than that of route A. If route B meets BGP VPNv6 route sending conditions, the device also sends it to other BGP VPNv6 peers. In this scenario, if you want only optimal BGP VPN routes to be transmitted between BGP VPNv6 peers on the network, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command on the local device, so that the device sends only optimal routes in the BGP VPN routing table to the BGP VPNv6 routing table.
      + To configure the device to send only valid routes in a BGP VPN routing table to a BGP VPNv6 routing table, run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command.
        
        By default, the device advertises all routes in the BGP VPN routing table to the BGP VPNv6 routing table. You can run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command to advertise valid routes to the BGP VPNv6 routing table.
  15. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure IS-ISv6 between a PE and a CE.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  This configuration is performed on the PE. On the CE, you only need to configure the common IS-ISv6 protocol. For details about how to configure IS-ISv6, see "IS-IS Configuration" in [*HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - IP Routing*](dc_vrp_isis_cfg_0000.html).
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) *process-id* **vpn-instance** *vpn-instance-name*
     
     
     
     An IS-IS process used between the PE and CE is created, and the IS-IS view is displayed.
     
     
     
     An IS-IS multi-instance process can be bound to only one VPN instance. If an IS-IS process is not bound to any VPN instance before it is started, this process becomes a public network process.
     
     If only one IS-IS process, either a public network IS-IS process or multi-instance IS-IS process, runs on the Router, you do not need to specify *process-id* in the command. The value of *process-id* is 1 by default.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If an IS-IS multi-instance process is deleted, IS-IS will be disabled on all the interfaces in the process.
     
     Deleting a VPN instance or disabling a VPN instance IPv6 address family will delete all the IS-IS processes bound to the VPN instance or VPN instance IPv6 address family.
  3. Run [**network-entity**](cmdqueryname=network-entity) *net-addr*
     
     
     
     A NET value is set. A NET specifies the current IS-IS area address and the system ID of the router.
  4. (Optional) Run [**is-level**](cmdqueryname=is-level) { **level-1** | **level-1-2** | **level-2** }
     
     
     
     An IS-IS level is configured for the Router.
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
      
      
      
      IS-IS routes are imported into the routing table of the BGP-VPN instance IPv6 address family.
  14. (Optional) Run either of the following commands:
      
      
      + To configure the device to send only optimal routes in the BGP VPN routing table to the BGP VPNv6 routing table, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command.
        
        By default, when a local device receives a remotely leaked route (route A) that has the same prefix as that of a route (route B) in the local VPN routing table but route A and route B have different RDs, the device also sends route B to the BGP VPNv6 routing table even if the route selection priority of route B is lower than that of route A. If route B meets BGP VPNv6 route sending conditions, the device also sends it to other BGP VPNv6 peers. In this scenario, if you want only optimal BGP VPN routes to be transmitted between BGP VPNv6 peers on the network, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command on the local device, so that the device sends only optimal routes in the BGP VPN routing table to the BGP VPNv6 routing table.
      + To configure the device to send only valid routes in a BGP VPN routing table to a BGP VPNv6 routing table, run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command.
        
        By default, the device advertises all routes in the BGP VPN routing table to the BGP VPNv6 routing table. You can run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command to advertise valid routes to the BGP VPNv6 routing table.
  15. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure a direct route between a PE and a CE.
  
  
  
  A direct route can be configured between a PE and a CE only if the CE is a host and connected to the PE using a VLANIF interface. Note that the direct route only needs to be configured on the PE.
  
  Perform the following steps on the PE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family)
     
     
     
     The VPN instance IPv6 address family view is displayed.
  4. Run [**nd vlink-direct-route advertise**](cmdqueryname=nd+vlink-direct-route+advertise) [ **route-policy** *route-policy-name* ]
     
     
     
     The function to advertise NDP Vlink direct routes is enabled.
     
     
     
     If **route-policy** is configured, only matched routes can be advertised.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the VPN instance view.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  8. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv6 address family view is displayed.
  9. Run [**import-route**](cmdqueryname=import-route) **direct** [ **med** *med* | **route-policy** *route-policy-name* ]\*
     
     
     
     The direct route to the local CE is imported.
     
     
     
     After the direct route to the local CE is imported into the VPN routing table, the local PE uses MP-BGP to advertise the direct route to the remote PE. This allows the remote CE to access the local CE.
  10. (Optional) Run either of the following commands:
      
      
      + To configure the device to send only optimal routes in the BGP VPN routing table to the BGP VPNv6 routing table, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command.
        
        By default, when a local device receives a remotely leaked route (route A) that has the same prefix as that of a route (route B) in the local VPN routing table but route A and route B have different RDs, the device also sends route B to the BGP VPNv6 routing table even if the route selection priority of route B is lower than that of route A. If route B meets BGP VPNv6 route sending conditions, the device also sends it to other BGP VPNv6 peers. In this scenario, if you want only optimal BGP VPN routes to be transmitted between BGP VPNv6 peers on the network, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command on the local device, so that the device sends only optimal routes in the BGP VPN routing table to the BGP VPNv6 routing table.
      + To configure the device to send only valid routes in a BGP VPN routing table to a BGP VPNv6 routing table, run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command.
        
        By default, the device advertises all routes in the BGP VPN routing table to the BGP VPNv6 routing table. You can run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command to advertise valid routes to the BGP VPNv6 routing table.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.