Configuring Route Exchange Between PEs and CEs
==============================================

To enable CEs to communicate, the PEs and CEs must be capable of exchanging routes.

#### Context

In BGP/MPLS IP VPN, a routing protocol or static route must be configured between a PE and a CE to allow them to communicate and allow the CE to obtain routes to other CEs. The routing protocol can be External Border Gateway Protocol (EBGP), Internal Border Gateway Protocol (IBGP), Routing Information Protocol (RIP), Open Shortest Path First (OSPF), or Intermediate System to Intermediate System (IS-IS). Choose one of the following configurations as needed:

* [Configure EBGP between a PE and a CE.](#EN-US_TASK_0172369257__step_dc_vrp_mpls-l3vpn-v4_cfg_015801)
* [Configure IBGP between a PE and a CE.](#EN-US_TASK_0172369257__step_dc_vrp_mpls-l3vpn-v4_cfg_015802)
* [Configure a static route between a PE and a CE.](#EN-US_TASK_0172369257__step_dc_vrp_mpls-l3vpn-v4_cfg_015803)
* [Configure RIP between a PE and a CE.](#EN-US_TASK_0172369257__step_dc_vrp_mpls-l3vpn-v4_cfg_015804)
* [Configure OSPF between a PE and a CE.](#EN-US_TASK_0172369257__step_dc_vrp_mpls-l3vpn-v4_cfg_015805)
* [Configure IS-IS between a PE and a CE.](#EN-US_TASK_0172369257__step_dc_vrp_mpls-l3vpn-v4_cfg_015806)
* [Configure a direct route between a PE and a CE.](#EN-US_TASK_0172369257__step_dc_vrp_mpls-l3vpn-v4_cfg_015807)

The routing protocol configurations on the CE and PE are different:

* The CE is located at the client side and unaware of the VPN. Therefore, you do not need to configure VPN parameters when configuring a routing protocol on the CE.
* The PE is located at the edge of the carrier's network. It connects to CEs and exchanges routing information with them. If the CEs that access a PE belong to different VPNs, the PE must maintain different VRF tables. When configuring a routing protocol on the PE, specify the name of the VPN instance to which the routing protocol applies and configure the routing protocol and MP-BGP to import routes from each other.


#### Procedure

* Configure EBGP between a PE and a CE.
  
  
  
  Perform the following steps on the PE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv4 address family view is displayed.
  4. (Optional) Run [**as-number**](cmdqueryname=as-number) { *as-number-plain* | *as-number-dot* }
     
     
     
     An independent AS number is configured for the VPN instance IPv4 address family.
     
     
     
     In scenarios such as network migration or service identification, to logically simulate a device as multiple BGP devices, run the [**as-number**](cmdqueryname=as-number) command to configure a different AS number for each VPN instance IPv4 address family.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The AS number configured in the BGP-VPN instance IPv4 address family view must be different from the AS number configured in the BGP view.
     
     After the [**bgp yang-mode enable**](cmdqueryname=bgp+yang-mode+enable) command is run, the [**as-number**](cmdqueryname=as-number) { *as-number-plain* | *as-number-dot* } command cannot be run. To configure a separate AS number for the VPN instance IPv4 address family, run the [**as-number ipv4**](cmdqueryname=as-number+ipv4) *ipv4-as* [ **no-prepend** ] command in the BGP-VPN instance view.
     
     If **no-prepend** is not configured, the AS\_Path attribute of a VPN route sent to the VPNv4 routing table carries the configured AS number. If **no-prepend** is configured, the AS\_Path attribute of a VPN route sent to the VPNv4 routing table does not carry the configured AS number.
  5. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
     
     
     
     The CE is configured as a VPN peer.
  6. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**ebgp-max-hop**](cmdqueryname=ebgp-max-hop) [ *hop-count* ]
     
     
     
     The maximum number of hops between the PE and its EBGP peer (the CE) is specified. This step is mandatory if the PE and CE are not directly connected.
     
     Generally, EBGP peers are connected by a direct physical link. If no direct physical link is available, the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command must be used to allow EBGP peers to establish a multi-hop TCP connection.
     
     
     
     If the maximum number of hops is set to 1, the device cannot establish an EBGP connection with a peer if they are not directly connected.
  7. (Optional) Run either of the following commands:
     
     
     + [**import-route**](cmdqueryname=import-route) **direct** [ **med** *med* | **route-policy** *route-policy-name* ]\*
     + [**network**](cmdqueryname=network) *ipv4-address* [ *mask* | *mask-length* ] [ **route-policy** *route-policy-name* ]
       
       The PE is enabled to import direct routes destined for the local CE into the IPv4 VPN instance routing table.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The PE can automatically learn direct routes destined for the local CE. The learned routes take precedence over the direct routes advertised from the local CE using EBGP. If this step is not performed, the PE does not use MP-BGP to advertise the direct routes destined for the local CE to the remote PE.
  8. (Optional) Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **soo** *site-of-origin*
     
     
     
     The Site of Origin (SoO) attribute is configured for the CE that has been specified as a peer of the PE.
     
     Several CEs at a VPN site may establish BGP connections with different PEs. The VPN routes advertised from the CEs to the PEs may be re-advertised to the same VPN site after the routes traverse the backbone network. This may cause route loops at the VPN site.
     
     If the SoO attribute is configured for a specified CE, the PE adds the attribute to a route sent from the CE and advertises the route to the remote PE. The remote PE checks the SoO attribute of the route before sending it to its attached CE. If the SoO attribute is the same as the local SoO attribute on the remote PE, the remote PE does not send the route to its attached CE.
  9. (Optional) Run [**peer**](cmdqueryname=peer) *ipv4-address* [**allow-as-loop**](cmdqueryname=allow-as-loop) [ *number* ]
     
     
     
     Routing loops are allowed.
     
     This step is used in hub & spoke networking.
     
     Generally, BGP uses the AS number to detect routing loops. On a hub & spoke network, if EBGP runs between a Hub-PE and a Hub-CE at a hub site, the route sent from the Hub-PE to the Hub-CE carries the AS number of the Hub-PE. If the Hub-CE sends a route update message to the Hub-PE, the Hub-PE will deny it because the route update message contains the AS number of the Hub-PE. To ensure proper route transmission on a hub & spoke network, configure all BGP peers on the path (along which the Hub-CE advertises VPN routes to the Spoke-CE) to accept the routes which have the AS number repeated once.
  10. (Optional) Run [**peer**](cmdqueryname=peer) *ipv4-address* **substitute-as**
      
      
      
      BGP AS number substitution is enabled.
      
      Perform this step on the PE in a scenario in which CEs at different sites use the same AS number.
      
      ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
      
      Enabling BGP AS number substitution may cause routing loops on a CE multi-homing network.
  11. (Optional) Run either of the following commands:
      
      
      + To configure the device to send only optimal routes in the BGP VPN routing table to the BGP VPNv4 routing table, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command.
        
        By default, when a local device receives a remotely leaked route (route A) that has the same prefix as that of a route (route B) in the local VPN routing table but route A and route B have different RDs, the device also sends route B to the BGP VPNv4 routing table even if the route selection priority of route B is lower than that of route A. If route B meets BGP VPNv4 route sending conditions, the device also sends it to other BGP VPNv4 peers. In this scenario, if you want only optimal BGP VPN routes to be transmitted between BGP VPNv4 peers on the network, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command on the local device, so that the device sends only optimal routes in the BGP VPN routing table to the BGP VPNv4 routing table.
      + To configure the device to send only valid routes in the BGP VPN routing table to the BGP VPNv4 routing table, run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command.
        
        By default, the device advertises all routes in the BGP VPN routing table to the BGP VPNv4 routing table. You can run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command to configure the device to send only valid routes to the BGP VPNv4 routing table.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
  
  
  
  Perform the following steps on the CE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
     
     
     
     The PE is configured as a peer.
  4. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **ebgp-max-hop** [ *hop-count* ]
     
     
     
     The maximum number of hops allowed for the EBGP connection is set.
     
     Generally, EBGP peers are directly connected by a physical link. If no direct physical link is available, the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command must be used to allow EBGP peers to establish a multi-hop TCP connection.
     
     If the maximum number of hops is set to 1, the device cannot establish an EBGP connection with a peer if they are not directly connected.
  5. Run either of the following commands:
     
     
     + [**import-route**](cmdqueryname=import-route) { **direct** | **static** | **rip** *process-id* | **ospf** *process-id* | **isis** *process-id* } [ **med** *med* | **route-policy** *route-policy-name* ] \*
     + [**network**](cmdqueryname=network) *ipv4-address* [ *mask* | *mask-length* ]
     
     
     
     The CE is configured to import local routes and advertise these routes to the connected PE, so that the PE can advertise them to the remote CE. The type of route imported using the first command varies according to the specified route type.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure IBGP between a PE and a CE.
  
  
  
  Perform the following steps on the PE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv4 address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
     
     
     
     The CE is configured as a VPN peer.
  5. (Optional) Run either of the following commands:
     
     
     + [**import-route**](cmdqueryname=import-route) **direct** [ **med** *med* | **route-policy** *route-policy-name* ] \*
     + [**network**](cmdqueryname=network) *ipv4-address* [ *mask* | *mask-length* ] [ **route-policy** *route-policy-name* ]
       
       The PE is configured to import the direct routes destined for the local CE into the VPN routing table and advertise them to the remote PE.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The PE can automatically learn the direct routes destined for the local CE. The learned routes take precedence over the direct routes advertised from the local CE using IBGP. If this step is not performed, the PE does not use MP-BGP to advertise the direct routes destined for the local CE to the remote PE.
  6. (Optional) Run either of the following commands:
     
     
     + To configure the device to send only optimal routes in the BGP VPN routing table to the BGP VPNv4 routing table, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command.
       
       By default, when a local device receives a remotely leaked route (route A) that has the same prefix as that of a route (route B) in the local VPN routing table but route A and route B have different RDs, the device also sends route B to the BGP VPNv4 routing table even if the route selection priority of route B is lower than that of route A. If route B meets BGP VPNv4 route sending conditions, the device also sends it to other BGP VPNv4 peers. In this scenario, if you want only optimal BGP VPN routes to be transmitted between BGP VPNv4 peers on the network, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command on the local device, so that the device sends only optimal routes in the BGP VPN routing table to the BGP VPNv4 routing table.
     + To configure the device to send only valid routes in the BGP VPN routing table to the BGP VPNv4 routing table, run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command.
       
       By default, the device advertises all routes in the BGP VPN routing table to the BGP VPNv4 routing table. You can run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command to configure the device to send only valid routes to the BGP VPNv4 routing table.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  
  
  Perform the following steps on the CE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
     
     
     
     The PE is configured as an IBGP peer.
  4. Run either of the following commands:
     
     
     + [**import-route**](cmdqueryname=import-route) { **direct** | **static** | **rip** *process-id* | **ospf** *process-id* | **isis** *process-id* } [ **med** *med* | **route-policy** *route-policy-name* ]\*
     + [**network**](cmdqueryname=network) *ipv4-address* [ *mask* | *mask-length* ]
     
     
     
     The CE is configured to import local routes and advertise these routes to the connected PE, so that the PE can advertise them to the remote CE. The type of route imported using the first command varies according to the specified route type.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a static route between a PE and a CE.
  
  
  
  Perform the following steps on the PE: Configuring a static route on the CE is not described here.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  For details about how to configure a static route, see ["IPv4 Static Route Configuration" in the *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - IP Routing*.](dc_vrp_static-route-ipv4_cfg_0000.html)
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } *interface-type interface-number* [ *nexthop-address* ] [ **preference** *preference* | **tag** *tag* ] \*
     
     
     
     A static route is configured for a specified VPN instance IPv4 address family.
  3. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  4. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv4 address family view is displayed.
  5. Run [**import-route**](cmdqueryname=import-route) **static** [ **med** *med* | **route-policy** *route-policy-name* ]\*
     
     
     
     The configured static route is added to the routing table of the BGP-VPN instance IPv4 address family.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A VPN that receives routes outside of itself from a device other than the PE and advertises these routes to the PE is called a transit VPN. A VPN that receives only routes within itself and routes advertised by the PE is called a stub VPN. Generally, a static route is used for route exchange between the CE and PE in a stub VPN only.
  6. (Optional) Run either of the following commands:
     
     
     + To configure the device to send only optimal routes in the BGP VPN routing table to the BGP VPNv4 routing table, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command.
       
       By default, when a local device receives a remotely leaked route (route A) that has the same prefix as that of a route (route B) in the local VPN routing table but route A and route B have different RDs, the device also sends route B to the BGP VPNv4 routing table even if the route selection priority of route B is lower than that of route A. If route B meets BGP VPNv4 route sending conditions, the device also sends it to other BGP VPNv4 peers. In this scenario, if you want only optimal BGP VPN routes to be transmitted between BGP VPNv4 peers on the network, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command on the local device, so that the device sends only optimal routes in the BGP VPN routing table to the BGP VPNv4 routing table.
     + To configure the device to send only valid routes in the BGP VPN routing table to the BGP VPNv4 routing table, run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command.
       
       By default, the device advertises all routes in the BGP VPN routing table to the BGP VPNv4 routing table. You can run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command to configure the device to send only valid routes to the BGP VPNv4 routing table.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure RIP between a PE and a CE.
  
  
  
  Perform the following steps on the PE. Configuring RIPv2 on the CE is not described here.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  For details about how to configure RIP, see "RIP Configuration" in the [*HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - IP Routing*.](dc_vrp_rip_cfg_0000.html)
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**rip**](cmdqueryname=rip) *process-id* **vpn-instance** *vpn-instance-name*
     
     
     
     A RIP process used between the PE and CE is created, and the RIP view is displayed.
     
     A RIP process can be bound to only one VPN instance. If a RIP process is not bound to any VPN instance before it is started, this process becomes a public network process and cannot be bound to a VPN instance later.
  3. Run [**network**](cmdqueryname=network) *network-address*
     
     
     
     RIP is enabled on the network segment where the interface bound to the VPN instance resides.
  4. Run [**import-route**](cmdqueryname=import-route) **bgp** [ **cost** { *cost* | **transparent** } | **route-policy** *route-policy-name* ] \*
     
     
     
     BGP routes are imported.
     
     After the [**import-route**](cmdqueryname=import-route) **bgp** command is run in the RIP view, the PE can import the VPNv4 routes learned from the remote PE into the RIP routing table and advertise them to the attached CE.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  7. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv4 address family view is displayed.
  8. Run [**import-route**](cmdqueryname=import-route) **rip** *process-id* [ **med** *med* | **route-policy** *route-policy-name* ] \*
     
     
     
     RIP routes are imported into the routing table of the BGP-VPN instance IPv4 address family.
     
     After the [**import-route**](cmdqueryname=import-route) **rip** command is run in the BGP-VPN instance IPv4 address family view, the PE imports the VPN routes learned from the attached CE into the BGP routing table and advertises generated VPNv4 routes to the remote PE.
  9. (Optional) Run either of the following commands:
     
     
     + To configure the device to send only optimal routes in the BGP VPN routing table to the BGP VPNv4 routing table, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command.
       
       By default, when a local device receives a remotely leaked route (route A) that has the same prefix as that of a route (route B) in the local VPN routing table but route A and route B have different RDs, the device also sends route B to the BGP VPNv4 routing table even if the route selection priority of route B is lower than that of route A. If route B meets BGP VPNv4 route sending conditions, the device also sends it to other BGP VPNv4 peers. In this scenario, if you want only optimal BGP VPN routes to be transmitted between BGP VPNv4 peers on the network, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command on the local device, so that the device sends only optimal routes in the BGP VPN routing table to the BGP VPNv4 routing table.
     + To configure the device to send only valid routes in the BGP VPN routing table to the BGP VPNv4 routing table, run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command.
       
       By default, the device advertises all routes in the BGP VPN routing table to the BGP VPNv4 routing table. You can run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command to configure the device to send only valid routes to the BGP VPNv4 routing table.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Deleting a VPN instance or disabling a VPN instance IPv4 address family will delete all the RIP processes bound to the VPN instance or the VPN instance IPv4 address family on the PE.
* Configure OSPF between a PE and a CE.
  
  
  
  Configure OSPF on the CE, and the CE configuration details are not provided here. Perform the following steps on the PE: Configuring OSPF on the CE is not described here.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  For details about how to configure OSPF, see ["OSPF Configuration" in the *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - IP Routing*](dc_vrp_ospf_cfg_0000.html).
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospf**](cmdqueryname=ospf) *process-id* [ **router-id** *router-id* ] **vpn-instance** *vpnname*
     
     
     
     An OSPF process used between the PE and CE is created, and the OSPF view is displayed.
     
     An OSPF process can be bound to only one VPN instance. If an OSPF process is not bound to any VPN instance before it is started, this process becomes a public network process and cannot be bound to a VPN instance later.
     
     A router ID needs to be specified when an OSPF process is started after it is bound to a VPN instance. The router ID must be different from the public network router ID configured in the system view. If the router ID is not specified, OSPF selects the IP address of one of the interfaces bound to the VPN instance as the router ID based on a certain rule.
  3. (Optional) Run [**domain-id**](cmdqueryname=domain-id) *domain-id* [ **secondary** ]
     
     
     
     The domain ID is configured.
     
     The domain ID can be an integer or in dotted decimal notation.
     
     Each OSPF process can be configured with two domain IDs. Different processes can have the same domain ID. There is no restriction on the domain IDs of the OSPF processes of different VPNs on a PE. The OSPF processes of the same VPN must be configured with the same domain ID to ensure proper route advertisement.
     
     The default domain ID is 0.
  4. (Optional) Run [**route-tag**](cmdqueryname=route-tag) *tag*
     
     
     
     The VPN route tag is configured.
     
     + If a BGP process is not started on the local device, the default VPN route tag is 0.
     + If a BGP process is started on the local device, the default VPN route tag is 3489660928 (0xD000 in the hexadecimal format) plus the local AS number of BGP.
  5. Run [**import-route**](cmdqueryname=import-route) **bgp** [ **cost** *cost* | **route-policy** *route-policy-name* | **tag** *tag* | **type** *type* ] \*
     
     
     
     BGP routes are imported.
  6. Run [**area**](cmdqueryname=area) *area-id*
     
     
     
     The OSPF area view is displayed.
  7. Run [**network**](cmdqueryname=network) *address* *wildcard-mask*
     
     
     
     OSPF is enabled on the network segment where the interface bound to the VPN instance resides.
     
     A network segment belongs to only one area. The area to which each OSPF interface belongs must be specified.
     
     OSPF can run on an interface properly only when the following conditions are met:
     
     + The mask length of the IP address of the interface is longer than or equal to that specified in the [**network**](cmdqueryname=network) command.
     + The primary IP address of the interface is on the network segment specified in the [**network**](cmdqueryname=network) command.
  8. Run [**quit**](cmdqueryname=quit)
     
     
     
     The OSPF view is displayed.
  9. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  10. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
  11. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv4 address family view is displayed.
  12. Run [**import-route**](cmdqueryname=import-route) **ospf** *process-id* [ **med** *med* | **route-policy** *route-policy-name* ] \*
      
      
      
      OSPF routes are imported into the routing table of the BGP-VPN instance IPv4 address family.
  13. (Optional) Run either of the following commands:
      
      
      + To configure the device to send only optimal routes in the BGP VPN routing table to the BGP VPNv4 routing table, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command.
        
        By default, when a local device receives a remotely leaked route (route A) that has the same prefix as that of a route (route B) in the local VPN routing table but route A and route B have different RDs, the device also sends route B to the BGP VPNv4 routing table even if the route selection priority of route B is lower than that of route A. If route B meets BGP VPNv4 route sending conditions, the device also sends it to other BGP VPNv4 peers. In this scenario, if you want only optimal BGP VPN routes to be transmitted between BGP VPNv4 peers on the network, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command on the local device, so that the device sends only optimal routes in the BGP VPN routing table to the BGP VPNv4 routing table.
      + To configure the device to send only valid routes in the BGP VPN routing table to the BGP VPNv4 routing table, run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command.
        
        By default, the device advertises all routes in the BGP VPN routing table to the BGP VPNv4 routing table. You can run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command to configure the device to send only valid routes to the BGP VPNv4 routing table.
  14. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Deleting a VPN instance or disabling a VPN instance IPv4 address family will delete all the OSPF processes bound to the VPN instance or the VPN instance IPv4 address family on the PE.
* Configure IS-IS between a PE and a CE.
  
  
  
  Perform the following steps on the PE: Configuring IS-IS on the CE is not described here.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  For details about how to configure IS-IS, see ["IS-IS Configuration" in the *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - IP Routing*](dc_vrp_isis_cfg_0000.html).
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) *process-id* **vpn-instance** *vpn-instance-name*
     
     
     
     An IS-IS process is created on the PE, and the IS-IS view is displayed.
     
     An IS-IS process can be bound to only one VPN instance. If an IS-IS process is not bound to any VPN instance before it is started, this process becomes a public network process and cannot be bound to a VPN instance later.
  3. Run [**network-entity**](cmdqueryname=network-entity) *net-addr*
     
     
     
     The network entity title (NET) is configured.
     
     A NET specifies the current IS-IS area address and the system ID of the Router.
  4. (Optional) Run [**is-level**](cmdqueryname=is-level) { **level-1** | **level-1-2** | **level-2** }
     
     
     
     The IS-IS level of the Router is specified.
     
     Configure the device level based on network planning. If no device level is configured, IS-IS establishes Level-1 and Level-2 neighbor relationships separately and maintains two identical LSDBs, consuming excessive system resources.
  5. Run [**import-route**](cmdqueryname=import-route) **bgp** [ **cost-type** { **external** | **internal** } | **cost** *cost* | **tag** *tag* | **route-policy** *route-policy-name* | [ **level-1** | **level-2** | **level-1-2** ] ] \*
     
     
     
     BGP routes are imported.
     
     If the IS-IS level is not specified in the command, BGP routes will be imported into the Level-2 IS-IS routing table.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface bound to the VPN instance is displayed.
  8. Run [**isis enable**](cmdqueryname=isis+enable) [ *process-id* ]
     
     
     
     IS-IS is enabled on the interface.
  9. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  10. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
  11. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv4 address family view is displayed.
  12. Run [**import-route**](cmdqueryname=import-route) **isis** *process-id* [ **med** *med* | **route-policy** *route-policy-name* ] \*
      
      
      
      IS-IS routes are imported into the routing table of the BGP-VPN instance IPv4 address family.
  13. (Optional) Run either of the following commands:
      
      
      + To configure the device to send only optimal routes in the BGP VPN routing table to the BGP VPNv4 routing table, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command.
        
        By default, when a local device receives a remotely leaked route (route A) that has the same prefix as that of a route (route B) in the local VPN routing table but route A and route B have different RDs, the device also sends route B to the BGP VPNv4 routing table even if the route selection priority of route B is lower than that of route A. If route B meets BGP VPNv4 route sending conditions, the device also sends it to other BGP VPNv4 peers. In this scenario, if you want only optimal BGP VPN routes to be transmitted between BGP VPNv4 peers on the network, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command on the local device, so that the device sends only optimal routes in the BGP VPN routing table to the BGP VPNv4 routing table.
      + To configure the device to send only valid routes in the BGP VPN routing table to the BGP VPNv4 routing table, run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command.
        
        By default, the device advertises all routes in the BGP VPN routing table to the BGP VPNv4 routing table. You can run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command to configure the device to send only valid routes to the BGP VPNv4 routing table.
  14. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Deleting a VPN instance or disabling a VPN instance IPv4 address family will delete all the IS-IS processes bound to the VPN instance or the VPN instance IPv4 address family on the PE.
* Configure a direct route between a PE and a CE.
  
  
  
  A direct route can be configured between a PE and a CE only if the CE is a host and connected to the PE using a VLANIF interface. Note that the direct route only needs to be configured on the PE.
  
  Perform the following steps on the PE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The VPN instance IPv4 address family view is displayed.
  4. Run [**arp vlink-direct-route advertise**](cmdqueryname=arp+vlink-direct-route+advertise) [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ]
     
     
     
     The function to advertise ARP Vlink direct routes is enabled.
     
     
     
     If **route-policy** or **route-filter** is configured, only matched routes can be advertised.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the VPN instance view.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  8. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv4 address family view is displayed.
  9. Run [**import-route**](cmdqueryname=import-route) **direct** [ **med** *med* | **route-policy** *route-policy-name* ]\*
     
     
     
     The direct route to the local CE is imported.
     
     
     
     After the direct route to the local CE is imported into the VPN routing table, the local PE uses MP-BGP to advertise the direct route to the remote PE. This allows the remote CE to access the local CE.
  10. (Optional) Run either of the following commands:
      
      
      + To configure the device to send only optimal routes in the BGP VPN routing table to the BGP VPNv4 routing table, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command.
        
        By default, when a local device receives a remotely leaked route (route A) that has the same prefix as that of a route (route B) in the local VPN routing table but route A and route B have different RDs, the device also sends route B to the BGP VPNv4 routing table even if the route selection priority of route B is lower than that of route A. If route B meets BGP VPNv4 route sending conditions, the device also sends it to other BGP VPNv4 peers. In this scenario, if you want only optimal BGP VPN routes to be transmitted between BGP VPNv4 peers on the network, run the [**advertise best-route**](cmdqueryname=advertise+best-route) command on the local device, so that the device sends only optimal routes in the BGP VPN routing table to the BGP VPNv4 routing table.
      + To configure the device to send only valid routes in the BGP VPN routing table to the BGP VPNv4 routing table, run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command.
        
        By default, the device advertises all routes in the BGP VPN routing table to the BGP VPNv4 routing table. You can run the [**advertise valid-routes**](cmdqueryname=advertise+valid-routes) command to configure the device to send only valid routes to the BGP VPNv4 routing table.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.