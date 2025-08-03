Configuring a Routing Protocol on an MCE
========================================

To enable an MCE to communicate with PEs and VPNs, configure a routing protocol for each type of service on the MCE.

#### Context

An MCE can communicate with PEs and VPNs using static routes or any of the following routing protocols: EBGP, IBGP, RIP, OSPF, and IS-IS. Choose one of the following configurations as needed:

* [Configure EBGP on the MCE.](#EN-US_TASK_0172369397__step_dc_vrp_mpls-l3vpn-v4_cfg_007001)
* [Configure IBGP on the MCE.](#EN-US_TASK_0172369397__step_dc_vrp_mpls-l3vpn-v4_cfg_007002)
* [Configure a static route on the MCE.](#EN-US_TASK_0172369397__step_dc_vrp_mpls-l3vpn-v4_cfg_007003)
* [Configure RIP on the MCE.](#EN-US_TASK_0172369397__step_dc_vrp_mpls-l3vpn-v4_cfg_007004)
* [Configure OSPF on the MCE.](#EN-US_TASK_0172369397__step_dc_vrp_mpls-l3vpn-v4_cfg_007005)
* [Configure IS-IS on the MCE.](#EN-US_TASK_0172369397__step_dc_vrp_mpls-l3vpn-v4_cfg_007006)


#### Procedure

* Configure EBGP on the MCE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
  4. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number* command to configure the PE as a VPN peer.
  5. (Optional) Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**ebgp-max-hop**](cmdqueryname=ebgp-max-hop) [ *hop-count* ] command to configure the maximum number of hops allowed for an EBGP connection. This step is mandatory if the MCE is not directly connected to the PE.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure IBGP on the MCE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
  4. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number* command to configure the PE as a VPN peer.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure a static route on the MCE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } *interface-type interface-number* [ *nexthop-address* ] [ **preference** *preference* | **tag** *tag* ] \* command to configure a static route for a specified VPN instance IPv4 address family.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure RIP on the MCE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**rip**](cmdqueryname=rip) *process-id* **vpn-instance** *vpn-instance-name* command to create a RIP instance and enter the RIP view.
     
     
     
     A RIP process can be bound to only one VPN instance. If a RIP process is not bound to any VPN instance before it is started, this process becomes a public network process and can no longer be bound to a VPN instance.
  3. Run the [**network**](cmdqueryname=network) *network-address* command to enable RIP on the network segment where the interface bound to the VPN instance resides.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Deleting a VPN instance or disabling a VPN instance IPv4 address family will also delete all the RIP processes bound to this VPN instance or VPN instance IPv4 address family.
* Configure OSPF on the MCE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ospf**](cmdqueryname=ospf) *process-id* [ **router-id** *router-id* ] **vpn-instance** *vpnname* command to create an OSPF instance on the MCE and enter the OSPF view.
     
     
     
     An OSPF process can be bound to only one VPN instance.
     
     Specify a router ID when creating an OSPF process and binding the OSPF process to a VPN instance. The OSPF process bound to the VPN instance cannot automatically use the public network router ID configured in the system view. If no router ID is specified, OSPF uses a specified rule to select an IP address from the IP addresses of the interfaces that are bound to the VPN instance as a router ID.
  3. (Optional) Run the [**domain-id**](cmdqueryname=domain-id) *domain-id* [ **secondary** ] command to configure a domain ID.
     
     
     
     The domain ID can be an integer or in dotted decimal notation.
     
     Two domain IDs can be configured for each OSPF process. Different processes can have the same domain ID. The same domain ID must be configured for all OSPF processes of the same VPN to ensure correct route advertisements.
  4. (Optional) Run the [**route-tag**](cmdqueryname=route-tag) *tag* command to configure a VPN route tag.
  5. Run the [**vpn-instance-capability simple**](cmdqueryname=vpn-instance-capability+simple) command to disable routing loop detection.
     
     
     
     If OSPF VPN multi-instance is deployed on the MCE, the PE sends the MCE a link-state advertisement (LSA) with the Down (DN) bit set to 1. Because VPN instances have been configured on the MCE, the MCE has routing loop detection enabled. If the MCE detects that the LSA contains the DN bit with the value 1, this LSA cannot be used to calculate routes. In this case, run the [**vpn-instance-capability simple**](cmdqueryname=vpn-instance-capability+simple) command to disable OSPF routing loop detection. After OSPF routing loop detection is disabled, the MCE calculates all OSPF routes without checking the DN bit and route tag.
  6. Run the [**area**](cmdqueryname=area) *area-id* command to enter the OSPF area view.
  7. Run the [**network**](cmdqueryname=network) *address* *wildcard-mask* command to advertise the IP address of the interface connected to the PE.
     
     
     
     OSPF can run properly on an interface only when both of the following conditions are met:
     
     + The mask length of the IP address of the interface is longer than or equal to that specified in the [**network**](cmdqueryname=network) command.
     + The primary IP address of the interface is on the network segment specified in the [**network**](cmdqueryname=network) command.
  8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Deleting a VPN instance or disabling a VPN instance IPv4 address family will also delete all the OSPF processes bound to this VPN instance or VPN instance IPv4 address family.
* Configure IS-IS on the MCE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**isis**](cmdqueryname=isis) *process-id* **vpn-instance** *vpn-instance-name* command to create an IS-IS instance on the MCE and enter the IS-IS view.
     
     
     
     An IS-IS process can be bound to only one VPN instance. If an IS-IS process is not bound to any VPN instance before it is started, this process becomes a public network process and can no longer be bound to a VPN instance.
  3. Run the [**network-entity**](cmdqueryname=network-entity) *net-addr* command to configure a network entity title (NET).
     
     
     
     A NET specifies the current IS-IS area address and the system ID of the Router.
  4. (Optional) Run the [**is-level**](cmdqueryname=is-level) { **level-1** | **level-1-2** | **level-2** } command to configure an IS-IS level for the Router.
  5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  6. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of the interface bound to the VPN instance.
  7. Run the [**isis enable**](cmdqueryname=isis+enable) [ *process-id* ] command to enable IS-IS on the interface.
  8. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Deleting a VPN instance or disabling a VPN instance IPv4 address family will also delete all the IS-IS processes bound to this VPN instance or VPN instance IPv4 address family.