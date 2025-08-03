Configuring a Routing Protocol on the PE Connected to an MCE
============================================================

To enable a PE to communicate with an MCE, configure routing protocol multi-instance on the PE.

#### Context

An MCE can communicate with a PE using static routes or any of the following protocols: EBGP, IBGP, RIP, OSPF, and IS-IS. Choose one of the following configurations as needed:

* [EBGP](#EN-US_TASK_0172369398__step_dc_vrp_mpls-l3vpn-v4_cfg_007101)
* [IBGP](#EN-US_TASK_0172369398__step_dc_vrp_mpls-l3vpn-v4_cfg_007102)
* [Static route](#EN-US_TASK_0172369398__step_dc_vrp_mpls-l3vpn-v4_cfg_007103)
* [RIP](#EN-US_TASK_0172369398__step_dc_vrp_mpls-l3vpn-v4_cfg_007104)
* [OSPF](#EN-US_TASK_0172369398__step_dc_vrp_mpls-l3vpn-v4_cfg_007105)
* [IS-IS](#EN-US_TASK_0172369398__step_dc_vrp_mpls-l3vpn-v4_cfg_007106)


#### Procedure

* Configure EBGP on the PE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
  4. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number* command to configure the MCE as a VPN peer.
  5. (Optional) Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**ebgp-max-hop**](cmdqueryname=ebgp-max-hop) [ *hop-count* ] command to configure the maximum number of hops allowed for an EBGP connection. This step is mandatory if the PE is not directly connected to the CE.
  6. (Optional) Run either of the following commands to configure the device to import the direct routes destined for the MCE into the VPN routing table and advertise them to the remote PE:
     
     
     + [**import-route**](cmdqueryname=import-route) **direct** [ **med** *med* | **route-policy** *route-policy-name* ] \*
     + [**network**](cmdqueryname=network) *ipv4-address* [ *mask* | *mask-length* ] [ **route-policy** *route-policy-name* ]
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The PE automatically learns the direct routes destined for the MCE. The learned routes take precedence over the direct routes advertised from the MCE using EBGP. If this step is not performed, the PE does not use the Multi-protocol Extensions for MP-BGP to advertise the direct routes destined for the MCE to the remote PE.
  7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure IBGP on the PE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
  4. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number* command to configure the MCE as a VPN peer.
  5. (Optional) Run either of the following commands to configure the device to import the direct routes destined for the MCE into the VPN routing table and advertise them to the remote PE:
     
     
     + [**import-route**](cmdqueryname=import-route) **direct** [ **med** *med* | **route-policy** *route-policy-name* ] \*
     + [**network**](cmdqueryname=network) *ipv4-address* [ *mask* | *mask-length* ] [ **route-policy** *route-policy-name* ]![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The PE automatically learns the direct routes destined for the MCE. The learned routes take precedence over the direct routes advertised from the MCE using IBGP. If this step is not performed, the PE does not use MP-BGP to advertise direct routes destined for the MCE to the remote PE.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure a static route on the PE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } *interface-type interface-number* [ *nexthop-address* ] [ **preference** *preference* | **tag** *tag* ] \* command to configure a static route for a specified VPN instance IPv4 address family.
  3. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  4. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
  5. Run the [**import-route**](cmdqueryname=import-route) **static** [ **med** *med* | **route-policy** *route-policy-name* ] \* command to import the configured static route into the routing table of the BGP VPN instance IPv4 address family.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure RIP on the PE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**rip**](cmdqueryname=rip) *process-id* **vpn-instance** *vpn-instance-name* command to create a RIP instance on the PE and enter the RIP view. A RIP process can be bound to only one VPN instance.
  3. Run the [**network**](cmdqueryname=network) *network-address* command to enable RIP on the network segment where the interface bound to the VPN instance resides.
  4. Run the [**import-route**](cmdqueryname=import-route) **bgp** [ **cost** { *cost* | **transparent** } | **route-policy** *route-policy-name* ] \* command to import BGP routes.
     
     
     
     After the [**import-route**](cmdqueryname=import-route) **bgp** command is run in the RIP view, the PE can import the VPNv4 routes learned from the remote PE into the RIP routing table and advertise them to the MCE.
  5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  6. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  7. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
  8. Run the [**import-route**](cmdqueryname=import-route) **rip** *process-id* [ **med** *med* | **route-policy** *route-policy-name* ] \* command to import RIP routes into the routing table of the BGP VPN instance IPv4 address family.
     
     
     
     After the [**import-route**](cmdqueryname=import-route) **rip** command is run in the BGP VPN instance IPv4 address family view, the PE imports the VPN routes learned from the MCE into the BGP routing table and advertises VPNv4 routes to the remote PE.
  9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Deleting a VPN instance or disabling a VPN instance IPv4 address family will also delete all the RIP processes bound to this VPN instance or VPN instance IPv4 address family.
* Configure OSPF on the PE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ospf**](cmdqueryname=ospf) *process-id* [ **router-id** *router-id* ] **vpn-instance** *vpnname* command to create an OSPF instance on the PE and enter the OSPF view. An OSPF process can be bound to only one VPN instance.
     
     
     
     A router ID needs to be specified when an OSPF process is started after it is bound to a VPN instance. The router ID must be different from the public network router ID configured in the system view. If the router ID is not specified, OSPF selects the IP address of one of the interfaces bound to the VPN instance as the router ID based on a certain rule.
  3. (Optional) Run the [**domain-id**](cmdqueryname=domain-id) *domain-id* [ **secondary** ] command to configure a domain ID.
     
     
     
     The domain ID can be an integer or in dotted decimal notation.
     
     Two domain IDs can be configured for each OSPF process. Different processes can have the same domain ID. There is no restriction on the domain IDs of the OSPF processes of different VPNs on a PE. The same domain ID must be configured for all OSPF processes of the same VPN to ensure correct route advertisements.
     
     The domain ID of an OSPF process is contained in the routes generated by this OSPF process. When OSPF routes are imported into BGP, the domain ID is added to the BGP VPN routes and forwarded as the BGP extended community attribute.
  4. (Optional) Run the [**route-tag**](cmdqueryname=route-tag) *tag* command to configure a VPN route tag.
  5. Run the [**area**](cmdqueryname=area) *area-id* command to enter the OSPF area view.
  6. Run the [**network**](cmdqueryname=network) *address* *wildcard-mask* command to enable OSPF on the network segment where the interface bound to the VPN instance resides.
     
     
     
     A network segment belongs only to one area. The area to which each OSPF interface belongs must be specified.
     
     OSPF can run properly on an interface only when both of the following conditions are met:
     
     + The mask length of the IP address of the interface is longer than or equal to that specified in the [**network**](cmdqueryname=network) command.
     + The primary IP address of the interface is on the network segment specified in the [**network**](cmdqueryname=network) command.
  7. Run the [**quit**](cmdqueryname=quit) command to exit the OSPF view.
  8. Run the [**import-route**](cmdqueryname=import-route) **bgp** [ **cost** *cost* | **route-policy** *route-policy-name* | **tag** *tag* | **type** *type* ] \* command to import BGP routes.
  9. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  10. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  11. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
  12. Run the [**import-route**](cmdqueryname=import-route) **ospf** *process-id* [ **med** *med* | **route-policy** *route-policy-name* ] \* command to import OSPF routes into the routing table of the BGP VPN instance IPv4 address family.
  13. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Deleting a VPN instance or disabling a VPN instance IPv4 address family will also delete all the OSPF processes bound to this VPN instance or VPN instance IPv4 address family.
* Configure IS-IS on the PE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**isis**](cmdqueryname=isis) *process-id* **vpn-instance** *vpn-instance-name* command to create an IS-IS instance between the PE and CE and enter the IS-IS view. An IS-IS process can be bound to only one VPN instance.
  3. Run the [**network-entity**](cmdqueryname=network-entity) *net*-addr command to set a NET.
     
     
     
     A NET specifies the current IS-IS area address and the system ID of the Router.
  4. (Optional) Run the [**is-level**](cmdqueryname=is-level) { **level-1** | **level-1-2** | **level-2** } command to configure an IS-IS level for the Router.
  5. Run the [**import-route**](cmdqueryname=import-route) **bgp** [ **cost-type** { **external** | **internal** } | **cost** *cost* | **tag** *tag* | **route-policy** *route-policy-name* | [ **level-1** | **level-2** | **level-1-2** ] ] \* command to import BGP routes.
     
     
     
     If the IS-IS level is not specified in the command, BGP routes will be imported into the Level-2 IS-IS routing table.
  6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  7. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of the interface bound to the VPN instance.
  8. Run the [**isis enable**](cmdqueryname=isis+enable) [ *process-id* ] command to enable IS-IS on the interface.
  9. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  10. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  11. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
  12. Run the [**import-route**](cmdqueryname=import-route) **isis** *process-id* [ **med** *med* | **route-policy** *route-policy-name* ] \* command to import IS-IS routes into the routing table of the BGP VPN instance IPv4 address family.
  13. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Deleting a VPN instance or disabling a VPN instance IPv4 address family will also delete all the IS-IS processes bound to this VPN instance or VPN instance IPv4 address family.