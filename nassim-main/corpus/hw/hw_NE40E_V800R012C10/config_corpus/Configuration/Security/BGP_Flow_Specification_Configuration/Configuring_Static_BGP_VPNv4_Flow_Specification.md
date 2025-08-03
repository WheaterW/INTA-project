Configuring Static BGP VPNv4 Flow Specification
===============================================

Static BGP VPNv4 Flow Specification allows BGP VPNv4 Flow Specification routes to be transmitted and traffic filtering policies to be generated. The policies improve security of devices in VPNs.

#### Usage Scenario

To deploy static BGP VPNv4 Flow Specification, a BGP VPN Flow Specification route needs to be created manually first. After the BGP-Flow VPNv4 address family is enabled, a BGP VPNv4 Flow Specification route is generated automatically. Then a BGP VPNv4 Flow Specification peer relationship needs be established between the device on which the BGP VPN Flow Specification route is created and the network ingress device to transmit the BGP VPNv4 Flow Specification route.

In an AS with multiple ingresses, a BGP VPNv4 Flow route reflector (Flow RR) can be deployed to reduce the number of BGP VPN Flow Specification peer relationships and save network resources.


#### Pre-configuration Tasks

Before configuring static BGP VPNv4 Flow Specification, complete the following tasks:

* [Configure BGP peer relationships.](dc_vrp_bgp_cfg_3006.html)
* Enable the BGP-Flow VPN instance IPv4 address family.

#### Procedure

1. Generate a BGP VPN Flow Specification route manually.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**flow-route**](cmdqueryname=flow-route+vpn-instance) *flowroute-name* **vpn-instance** *vpn-instance-name*
      
      
      
      A static BGP VPN Flow Specification route is created, and the Flow-Route VPN instance view is displayed.
      
      
      
      One BGP VPN Flow Specification route can include multiple **if-match** and **apply** clauses. **if-match** clauses define traffic filtering rules, and **apply** clauses define traffic behaviors. The relationships among clauses are as follows:
      * The relationship among **if-match** clauses of different types is "AND."
      * If **if-match** clauses of the same type are configured repeatedly, some rules override each other, and some other rules are in the OR relationship. For details, see the precautions for the [**if-match**](cmdqueryname=if-match) command.
      * The relationship among the traffic behaviors defined by **apply** clauses is "AND."The traffic behaviors defined by **apply** clauses apply to all traffic matching the filtering rules of **if-match** clauses.
   3. According to characteristics of the traffic to be controlled, you can configure one or more **if-match** clauses to define traffic filtering rules as needed:
      
      
      * To set a destination address-based traffic filtering rule, run the [**if-match destination**](cmdqueryname=if-match+destination) *ipv4-address* { *mask* | *mask-length* } command.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        Traffic control is performed based on a specified destination IP address specified in a rule configured using the [**if-match destination**](cmdqueryname=if-match+destination) command, but BGP VPN Flow Specification routes matching the rule cannot pass validation. In this situation, run the [**peer validation-disable**](cmdqueryname=peer+validation-disable) command to disable the validation.
        
        By default, 0.0.0.0/0 is used as the prefix of each BGP VPN Flow Specification route that matches the export or import policy of a peer. To enable a device to change the prefix of each BGP VPN Flow Specification route that matches the export or import policy of a peer to the destination IP address specified in the [**if-match destination**](cmdqueryname=if-match+destination) command, run the [**route match-destination**](cmdqueryname=route+match-destination) command.
      * To configure a filtering rule based on the source address, run the [**if-match source**](cmdqueryname=if-match+source) *ipv4-address* { *mask* | *mask-length* } command.
      * To set a filtering rule based on the port number, run the [**if-match port**](cmdqueryname=if-match+port) *operator* *port* command.
      * To configure a filtering rule based on the source port number, run the [**if-match source-port**](cmdqueryname=if-match+source-port) *operator* *port* command.
      * To configure a filtering rule based on the destination port number, run the [**if-match destination-port**](cmdqueryname=if-match+destination-port) *operator* *port* command.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        [**if-match port**](cmdqueryname=if-match+port) and [**if-match destination-port**](cmdqueryname=if-match+destination-port) or [**if-match source-port**](cmdqueryname=if-match+source-port) are mutually exclusive.
      * To set a traffic filtering rule that is based on the protocol used to carry traffic, run the [**if-match protocol**](cmdqueryname=if-match+protocol) *operator* *protocol* command.
      * To configure a filtering rule based on the service type, run the [**if-match dscp**](cmdqueryname=if-match+dscp) *operator* *dscp* command.
      * To configure a filtering rule based on the TCP flag, run the [**if-match tcp-flags**](cmdqueryname=if-match+tcp-flags+match+not) { **match** | **not** } *tcp-flags* command.
        
        Network attackers may send a large number of invalid TCP packets to attack network devices. To control invalid TCP packets to ensure communication security, configure a filtering rule based on the TCP flag for the BGP VPN Flow Specification route using the [**if-match tcp-flags**](cmdqueryname=if-match+tcp-flags) command. Traffic matching the TCP flag is filtered or controlled using the actions specified in the apply clauses.
      * To configure a filtering rule based on the fragment type, run the [**if-match fragment-type**](cmdqueryname=if-match+fragment-type+match+not) { **match** | **not** } *fragment-type-name* command.
      * To set a traffic filtering rule that is based on an ICMP packet code, run the [**if-match icmp-code**](cmdqueryname=if-match+icmp-code) *operator* *icmp-code* command.
      * To set a traffic filtering rule that is based on an ICMP packet type, run the [**if-match icmp-type**](cmdqueryname=if-match+icmp-type+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *icmp-type* command.
      * To configure a filtering rule based on the packet length of BGP VPN Flow Specification routes, run the [**if-match packet-length**](cmdqueryname=if-match+packet-length+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *packet-length-value* command.
   4. Run the following command as required to configure actions for apply clauses:
      
      
      * To discard the matched traffic, run the [**apply deny**](cmdqueryname=apply+deny) command.
      * To redirect the matching traffic to the traffic cleaning device or blackhole, run the [**apply redirect**](cmdqueryname=apply+redirect+vpn-target+ip) { **vpn-target** *vpn-target-import* | **ip** *redirect-ip-rt* } command.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        The device can process the redirection next hop attribute configured using the [**apply redirect**](cmdqueryname=apply+redirect+ip) **ip** *redirect-ip-rt* command received from a peer only after the [**peer redirect ip**](cmdqueryname=peer+redirect+ip) command is run.
      * To re-mark the service class of the matching traffic, run the [**apply remark-dscp**](cmdqueryname=apply+remark-dscp) command.
      * To limit the rate of the matched traffic, run the [**apply traffic-rate**](cmdqueryname=apply+traffic-rate) command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The [**apply deny**](cmdqueryname=apply+deny) and [**apply traffic-rate**](cmdqueryname=apply+traffic-rate) commands are mutually exclusive.
      
      If the configured BGP VPN Flow Specification route attribute does not need to take effect locally, run the [**routing-table rib-only**](cmdqueryname=routing-table+rib-only+route-policy) [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command to disable the device from delivering the BGP VPN Flow Specification route to the FES forwarding table.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Establish a BGP VPNv4 Flow Specification peer relationship.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** *as-number*
      
      
      
      An IP address and AS number are specified for the peer.
   4. Run [**ipv4-flow vpnv4**](cmdqueryname=ipv4-flow+vpnv4)
      
      
      
      The BGP-Flow VPNv4 address family is enabled, and its view is displayed.
   5. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**enable**](cmdqueryname=enable)
      
      
      
      A BGP VPNv4 Flow Specification peer relationship is established.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
3. (Optional) Configure a Flow RR.
   
   
   
   Before configuring a Flow RR, establish a BGP VPNv4 Flow Specification peer relationship between the Flow RR with the device that generates the BGP VPN Flow Specification route and every ingress.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv4-flow vpnv4**](cmdqueryname=ipv4-flow+vpnv4)
      
      
      
      The BGP-Flow VPNv4 address family is enabled, and its view is displayed.
   4. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**reflect-client**](cmdqueryname=reflect-client)
      
      
      
      A Flow RR is configured, and clients are specified for it.
      
      
      
      The Router on which the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command is run functions as a Flow RR, and the specified peers function as clients.
   5. (Optional) Run [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients)
      
      
      
      Route reflection between clients through the RR is disabled.
      
      
      
      If the clients of a Flow RR are fully meshed, you can run the [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command on the Flow RR to disable route reflection between clients through the RR, which reduces costs.
   6. (Optional) Run [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) { *cluster-id-value* | *cluster-id-ipv4* }
      
      
      
      A cluster ID is configured for the Flow RR.
      
      
      
      If a cluster has multiple flow RRs, run this command to set the same *cluster-id* for these RRs.
      
      The [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) command is applicable only to Flow RRs.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
4. (Optional) Configure the redirection next-hop attribute ID for BGP VPNv4 Flow Specification routes.
   
   
   
   The redirection next-hop attribute ID can be 0x010C (defined in a related RFC) or 0x0800 (defined in a related draft). If a Huawei device needs to communicate with a non-Huawei device that does not support the redirection next-hop attribute ID of 0x010C or 0x0800, set the redirection next-hop attribute ID of BGP VPNv4 Flow Specification routes as required. Perform one of the following configurations based on the ID supported by non-Huawei devices:
   
   * Set the redirection next-hop attribute ID to 0x010C (defined in a related RFC) for BGP VPNv4 Flow Specification routes.
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**ipv4-flow vpnv4**](cmdqueryname=ipv4-flow+vpnv4)
        
        The BGP-Flow VPNv4 address family is enabled, and the BGP-Flow VPNv4 address family view is displayed.
     4. Run [**peer**](cmdqueryname=peer+redirect+ip+rfc-compatible) *ipv4-address* **redirect ip rfc-compatible**
        
        The redirection next hop attribute ID of BGP VPNv4 Flow Specification routes is set to 0x010C (defined in a related RFC).
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Set the redirection next-hop attribute ID to 0x0800 (defined in a related draft) for BGP VPNv4 Flow Specification routes.
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**ipv4-flow vpnv4**](cmdqueryname=ipv4-flow+vpnv4)
        
        The BGP-Flow VPNv4 address family is enabled, and the BGP-Flow VPNv4 address family view is displayed.
     4. Run [**peer**](cmdqueryname=peer+redirect+ip+draft-compatible) *ipv4-address* **redirect ip draft-compatible**
        
        The redirection next-hop attribute ID of BGP VPNv4 Flow Specification routes is set to 0x0800 (defined in a related draft).
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
5. (Optional) Disable BGP Flow Specification protection.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**flowspec protocol-protect**](cmdqueryname=flowspec+protocol-protect+ipv4+ipv6+disable) { **ipv4** | **ipv6** } **disable**
      
      
      
      BGP Flow Specification protection is disabled.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
6. (Optional) Enable the device to follow RFC 5575 when dealing with BGP Flow Specification IPv4 fragmentation rules.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**flowspec ipv4-fragment-rule switch**](cmdqueryname=flowspec+ipv4-fragment-rule+switch)
      
      
      
      BGP Flow Specification IPv4 fragmentation rules are enabled to comply with RFC 5575.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
7. (Optional) Enable BGP Flow Specification to match inner packet information about the packets that leave an SRv6 TE Policy or SRv6 BE egress.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**flowspec match srv6-inner-ip enable**](cmdqueryname=flowspec+match+srv6-inner-ip+enable)
      
      
      
      BGP Flow Specification is enabled to match inner packet information about the packets that leave an SRv6 TE Policy or SRv6 BE egress.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After completing the configuration, verify it.

* Run the [**display bgp flow**](cmdqueryname=display+bgp+flow+vpnv4+all+peer+verbose) **vpnv4 all** **peer** [ [ *ipv4-address* ] **verbose** ] command to check information about all BGP VPN Flow Specification peers and BGP VPNv4 Flow Specification peers.
* Run the [**display bgp flow**](cmdqueryname=display+bgp+flow+vpnv4+all+route-distinguisher+routing-table) **vpnv4** { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** [ *reindex* ] command to check information about all BGP VPN Flow Specification routes and BGP VPNv4 Flow Specification routes or the BGP VPN Flow Specification routes and BGP VPNv4 Flow Specification routes with a specified RD.
* Run the [**display bgp flow**](cmdqueryname=display+bgp+flow+vpnv4+all+route-distinguisher+routing-table) **vpnv4** { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** **statistics** command to check statistics about all BGP VPN Flow Specification routes and BGP VPNv4 Flow Specification routes or the BGP VPN Flow Specification routes and BGP VPNv4 Flow Specification routes with a specified RD.
* Run the [**display flowspec**](cmdqueryname=display+flowspec+rule+slot) **rule** *reindex-value* **slot** *slot-id* command to check information about combined rules in the local BGP Flow Specification rule table.
* Run the [**display flowspec**](cmdqueryname=display+flowspec+rule+statistics+slot) **rule statistics slot** *slot-id* command to check statistics about the rules for BGP Flow Specification routes to take effect.
* Run the [**display flowspec resource rule**](cmdqueryname=display+flowspec+resource+rule+ipv4+ipv6+slot) { **ipv4** | **ipv6** } [ **slot** *slot-id* ] command to check the resource usage information about BGP Flow Specification route rules.