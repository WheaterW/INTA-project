Configuring Static BGP VPN Flow Specification
=============================================

In VPNs, BGP VPN Flow Specification routes are generated manually to control traffic in static BGP VPN Flow Specification.

#### Usage Scenario

When deploying static BGP VPN Flow Specification, a BGP VPN Flow Specification route needs to be generated manually, and a BGP VPN Flow Specification peer relationship needs to be established between the device that generates the BGP VPN Flow Specification route and each ingress in the network to transmit BGP VPN Flow Specification routes.

In an AS with multiple ingresses, a BGP VPN Flow route reflector (Flow RR) can be deployed to reduce the number of BGP VPN Flow Specification peer relationships and save network resources.

If you want to filter traffic based on the address prefix but the BGP VPN Flow Specification route carrying the filtering rule cannot pass validation, disable the validation of BGP VPN Flow Specification routes received from a specified peer.


#### Pre-configuration Tasks

Before configuring static BGP VPN Flow Specification, [configure a VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0155.html) and [bind interfaces to a VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0156.html).


#### Procedure

1. Generate a BGP VPN Flow Specification route manually.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**flow-route**](cmdqueryname=flow-route+vpn-instance) *flowroute-name* **vpn-instance** *vpn-instance-name*
      
      
      
      A static BGP VPN Flow Specification route is created, and the Flow-Route VPN instance view is displayed.
      
      
      
      One BGP VPN Flow Specification route can include multiple if-match and apply clauses. **if-match** clauses define traffic filtering rules, and **apply** clauses define traffic behaviors. The relationships among clauses are as follows:
      * The relationship among **if-match** clauses of different types is "AND."
      * If **if-match** clauses of the same type are configured repeatedly, some rules override each other, and some other rules are in the OR relationship. For details, see the precautions for the [**if-match**](cmdqueryname=if-match) command.
      * The relationship among the traffic behaviors defined by **apply** clauses is "AND."The traffic behaviors defined by **apply** clauses apply to all traffic matching the filtering rules of **if-match** clauses.
   3. Based on the characteristics of the traffic to be controlled, choose one or multiple if-match clauses as the filtering rule.
      
      
      * To set a destination address-based traffic filtering rule, run the [**if-match destination**](cmdqueryname=if-match+destination) *ipv4-address* { *mask* | *mask-length* } command.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        Traffic control is performed based on a specified destination IP address specified in a rule configured using the [**if-match destination**](cmdqueryname=if-match+destination) command, but BGP VPN Flow Specification routes matching the rule cannot pass validation. In this situation, run the [**peer validation-disable**](cmdqueryname=peer+validation-disable) command to disable the validation.
        
        By default, 0.0.0.0/0 is used as the prefix of each BGP VPN Flow Specification route that matches the export or import policy of a peer. To enable a device to change the prefix of each BGP VPN Flow Specification route that matches the export or import policy of a peer to the destination IP address specified in the [**if-match destination**](cmdqueryname=if-match+destination) command, run the [**route match-destination**](cmdqueryname=route+match-destination) command.
      * To configure a filtering rule based on the source address, run the [**if-match source**](cmdqueryname=if-match+source) *ipv4-address* { *mask* | *mask-length* } command.
      * To set a port number-based traffic filtering rule, run the [**if-match port**](cmdqueryname=if-match+port+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *port* or [**if-match port**](cmdqueryname=if-match+port+greater-than+less-than) **greater-than** *port* **less-than** *upper-port-value* command.
      * To set a source port number-based traffic filtering rule, run the [**if-match source-port**](cmdqueryname=if-match+source-port+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *port* or [**if-match source-port**](cmdqueryname=if-match+source-port+greater-than+less-than) **greater-than** *source-port* **less-than** *upper-source-port-value* command.
      * To set a destination port number-based traffic filtering rule, run the [**if-match destination-port**](cmdqueryname=if-match+destination-port+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *port* or [**if-match destination-port greater-than**](cmdqueryname=if-match+destination-port+greater-than+less-than) *port* **less-than** *upper-port-value* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        [**if-match port**](cmdqueryname=if-match+port) and [**if-match destination-port**](cmdqueryname=if-match+destination-port) or [**if-match source-port**](cmdqueryname=if-match+source-port) are mutually exclusive.
      * To set a traffic bearing protocol-based traffic filtering rule, run the [**if-match protocol**](cmdqueryname=if-match+protocol+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *protocol* or [**if-match protocol**](cmdqueryname=if-match+protocol+greater-than+less-than) **greater-than** *protocol* **less-than** *upper-protocol-value* command.
      * To set a DSCP-based traffic filtering rule, run the [**if-match dscp**](cmdqueryname=if-match+dscp+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *dscp* or [**if-match dscp**](cmdqueryname=if-match+dscp+greater-than+less-than) **greater-than** *dscp* **less-than** *upper-dscp-value* command.
      * To set a TCP-flag value-based traffic filtering rule, run the [**if-match tcp-flags**](cmdqueryname=if-match+tcp-flags+match+not) { **match** | **not** | **any-match** } *tcp-flags* command.
        
        Network attackers may send a large number of invalid TCP packets to attack network devices. To control invalid TCP packets to ensure communication security, configure a filtering rule based on the TCP flag for the BGP VPN Flow Specification route using the [**if-match tcp-flags**](cmdqueryname=if-match+tcp-flags) command. Traffic matching the TCP flag is filtered or controlled using the actions specified in the apply clauses.
      * To configure a filtering rule based on the fragment type, run the [**if-match fragment-type**](cmdqueryname=if-match+fragment-type+match+not) { **match** | **not** } *fragment-type-name* command.
      * To set an ICMP message code-based traffic filtering rule, run the [**if-match icmp-code**](cmdqueryname=if-match+icmp-code+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *icmp-code* or [**if-match icmp-code**](cmdqueryname=if-match+icmp-code+greater-than+less-than) **greater-than** *icmp-code* **less-than** *upper-icmp-code-value* command.
      * To set an ICMP message type-based traffic filtering rule, run the [**if-match icmp-type**](cmdqueryname=if-match+icmp-type+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *icmp-type* or [**if-match icmp-type**](cmdqueryname=if-match+icmp-type+greater-than+less-than) **greater-than** *icmp-type* **less-than** *upper-icmp-type-value* command.
      * To set a filtering rule based on the packet length of a BGP VPN Flow Specification route, run the [**if-match packet-length**](cmdqueryname=if-match+packet-length+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *packet-length-value* or [**if-match packet-length**](cmdqueryname=if-match+packet-length+greater-than+less-than) **greater-than** *packet-length-value* **less-than** *upper-packet-length-value* command.
   4. Run the following command as required to configure actions for apply clauses:
      
      
      * To discard the matched traffic, run the [**apply deny**](cmdqueryname=apply+deny) command.
      * To redirect the matched traffic to the traffic cleaning device or blackhole, run the [**apply redirect**](cmdqueryname=apply+redirect+vpn-target+ip) { **vpn-target** *vpn-target-import* | **ip** *redirect-ip-rt* } command.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        The device can process the redirection next hop attribute configured using the [**apply redirect**](cmdqueryname=apply+redirect+ip) **ip** *redirect-ip-rt* command received from a peer only after the [**peer redirect ip**](cmdqueryname=peer+redirect+ip) command is run.
      * To redirect the matched traffic to an SRv6 TE Policy, run the [**apply redirect**](cmdqueryname=apply+redirect+ipv6+color+prefix-sid) **ipv6** *redirect-ipv6-rt* **color** *colorvalue* [ **prefix-sid** *prefix-sid-value* ] command.
      * To re-mark the service class of the matched traffic, run the [**apply remark-dscp**](cmdqueryname=apply+remark-dscp) command.
      * To limit the rate of the matched traffic, run the [**apply traffic-rate**](cmdqueryname=apply+traffic-rate) command.
      * To implement sampling for the matched traffic, run the [**apply traffic-action sample**](cmdqueryname=apply+traffic-action+sample) command.
        
        You can run the [**apply traffic-action sample**](cmdqueryname=apply+traffic-action+sample) command for a BGP VPN Flow Specification route to sample the traffic that matches the specified filtering rules. Through sampling, abnormal traffic can be identified and filtered out, which protects the attacked device and improves network security.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The [**apply deny**](cmdqueryname=apply+deny) and [**apply traffic-rate**](cmdqueryname=apply+traffic-rate) commands are mutually exclusive.
      
      If the configured BGP VPN Flow Specification route attribute does not need to take effect locally, run the [**routing-table rib-only**](cmdqueryname=routing-table+rib-only+route-policy) [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command to disable the device from delivering the BGP VPN Flow Specification route to the FES forwarding table.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Establish a BGP VPN Flow Specification peer relationship.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
      
      
      
      A BGP-VPN instance is created, and its view is displayed.
   4. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** *as-number*
      
      
      
      An IP address and AS number are specified for the peer.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      The BGP view is displayed.
   6. Run [**ipv4-flow vpn-instance**](cmdqueryname=ipv4-flow+vpn-instance) *vpn-instance-name*
      
      
      
      The BGP-Flow VPN instance IPv4 address family is enabled, and its view is displayed.
   7. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**enable**](cmdqueryname=enable)
      
      
      
      A BGP VPN Flow Specification peer is specified.
      
      
      
      After the BGP VPN Flow Specification peer relationship is established in the BGP-Flow VPN instance IPv4 address family view, the BGP VPN Flow Specification route generated by the traffic analysis server is imported automatically to the BGP routing table and then sent to the peer.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
3. (Optional) Configure a Flow RR.
   
   
   
   Before configuring a Flow RR, establish a BGP VPN Flow Specification peer relationship between the Flow RR and device on which the BGP VPN Flow Specification route is generated and between the Flow RR and every network ingress.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv4-flow vpn-instance**](cmdqueryname=ipv4-flow+vpn-instance) *vpn-instance-name*
      
      
      
      The BGP-Flow VPN instance IPv4 address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**reflect-client**](cmdqueryname=reflect-client)
      
      
      
      A Flow RR is configured, and clients are specified for it.
      
      
      
      The Router on which the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command is run functions as a Flow RR, and the specified peers function as clients.
   5. (Optional) Run [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients)
      
      
      
      Route reflection between clients through the RR is disabled.
      
      
      
      If the clients of a Flow RR are fully meshed, you can run the [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command on the Flow RR to disable route reflection between clients through the RR, which reduces costs.
   6. (Optional) Run [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) {*cluster-id-value* | *cluster-id-ipv4* }
      
      
      
      A cluster ID is configured for the Flow RR.
      
      
      
      If a cluster has multiple flow RRs, run this command to set the same *cluster-id* for these RRs.
      
      The [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) command is applicable only to Flow RRs.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
4. (Optional) Configure the device to check the AS\_Path attribute during BGP VPN Flow Specification route validation.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv4-flow vpn-instance**](cmdqueryname=ipv4-flow+vpn-instance) *vpn-instance-name*
      
      
      
      The BGP-Flow VPN instance IPv4 address family view is displayed.
   4. Run [**route validation-mode include-as**](cmdqueryname=route+validation-mode+include-as)
      
      
      
      The device is configured to check the AS\_Path attribute during BGP VPN Flow Specification route validation.
      
      
      
      BGP Flow Specification route validation is performed in either of the following modes:
      * Validation mode 1: After receiving a BGP Flow Specification route with a destination address-based filtering rule, the device checks the validity of the route using the rules described in [Figure 1](#EN-US_TASK_0172372349__en-us_task_0172372348_en-us_cliref_0172383989_fig_route_validation-mode_include-as01). The route is considered valid only if the validation succeeds.
      * Validation mode 2: After receiving a BGP Flow Specification route with a destination address-based filtering rule, the device checks the validity of the route by checking whether the AS\_Path attribute of the route carries the AS\_Set and AS\_Sequence fields. The route is considered valid only if its AS\_Path attribute does not carry the AS\_Set or AS\_Sequence field.Validation mode 2 is configured using the [**route validation-mode include-as**](cmdqueryname=route+validation-mode+include-as) command. If this command is configured, the device checks the validity of a BGP Flow Specification route using mode 2 first.
      * If the validation succeeds, the BGP Flow Specification route is considered valid, and mode 1 is not used.
      * If the validation fails, the device checks the validity of the BGP Flow Specification route using mode 1.If this command is not run, the device uses mode 1 to check the validity of BGP Flow Specification routes.**Figure 1** BGP Flow Specification validation rules  
      ![](figure/en-us_image_0000001228544747.png)
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
5. (Optional) Disable BGP VPN Flow Specification route validation.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv4-flow vpn-instance**](cmdqueryname=ipv4-flow+vpn-instance) *vpn-instance-name*
      
      
      
      The BGP-Flow VPN instance IPv4 address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+validation-disable) *ipv4-address* **validation-disable**
      
      
      
      The device is disabled from validating BGP VPN Flow Specification routes received from a specified peer.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
6. (Optional) Disable the device from validating the routes that carry a redirection extended community attribute and are received from a specified EBGP peer.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv4-flow vpn-instance**](cmdqueryname=ipv4-flow+vpn-instance) *vpn-instance-name*
      
      
      
      The BGP-Flow VPN instance IPv4 address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+redirect+ip+validation-disable) *ipv4-address* **redirect ip validation-disable**
      
      
      
      The device is disabled from validating the routes that carry a redirection extended community attribute and are received from a specified EBGP peer.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
7. (Optional) Configure a redirection next-hop attribute ID for BGP VPN Flow Specification routes.
   
   
   
   The redirection next-hop attribute ID can be 0x010C (defined in a related RFC) or 0x0800 (defined in a related draft). If a Huawei device needs to communicate with a non-Huawei device that does not support the redirection next-hop attribute ID of 0x010C or 0x0800, set the redirection next-hop attribute ID of BGP VPN Flow Specification routes as required. Perform one of the following configurations based on the ID supported by non-Huawei devices:
   
   * Set the redirection next-hop attribute ID to 0x010C (defined in a related RFC) for BGP VPN Flow Specification routes.
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**ipv4-flow vpn-instance**](cmdqueryname=ipv4-flow+vpn-instance) *vpn-instance-name*
        
        The BGP-Flow VPN instance IPv4 address family view is displayed.
     4. Run [**peer**](cmdqueryname=peer+redirect+ip+rfc-compatible) *ipv4-address* **redirect ip rfc-compatible**
        
        The redirection next hop attribute ID of BGP VPN Flow Specification routes is set to 0x010C (defined in a related RFC).
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Set the redirection next-hop attribute ID to 0x0800 (defined in a related draft) for BGP VPN Flow Specification routes.
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**ipv4-flow vpn-instance**](cmdqueryname=ipv4-flow+vpn-instance) *vpn-instance-name*
        
        The BGP-Flow VPN instance IPv4 address family view is displayed.
     4. Run [**peer**](cmdqueryname=peer+redirect+ip+draft-compatible) *ipv4-address* **redirect ip draft-compatible**
        
        The redirection next-hop attribute ID of BGP VPN Flow Specification routes is set to 0x0800 (defined in a related draft).
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
8. (Optional) Enable CAR statistics collection and packet loss statistics collection for BGP Flow Specification.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**flowspec statistic enable**](cmdqueryname=flowspec+statistic+enable)
      
      
      
      CAR statistics collection and packet loss statistics collection are enabled for BGP Flow Specification.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
9. (Optional) Disable BGP Flow Specification on the interface.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   3. Run [**flowspec disable**](cmdqueryname=flowspec+disable+ipv4+ipv6) [ **ipv4** | **ipv6** ]
      
      
      
      BGP Flow Specification is disabled on the interface.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      This command cannot be configured on Eth-Trunk member interfaces. The configuration on a main interface also takes effect on its sub-interfaces.
      
      If BGP Flow Specification does not need to be disabled on a sub-interface, run the [**flowspec disable**](cmdqueryname=flowspec+disable+ipv4+ipv6+sub-port-exclude) [ **ipv4** | **ipv6** ] **sub-port-exclude** command on the main interface to which the sub-interface belongs.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
10. (Optional) Disable BGP Flow Specification protection.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       
       
       The system view is displayed.
    2. Run [**flowspec protocol-protect**](cmdqueryname=flowspec+protocol-protect+ipv4+ipv6+disable) { **ipv4** | **ipv6** } **disable**
       
       
       
       BGP Flow Specification protection is disabled.
    3. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
11. (Optional) Enable the device to follow RFC 5575 when dealing with BGP Flow Specification IPv4 fragmentation rules.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       
       
       The system view is displayed.
    2. Run [**flowspec ipv4-fragment-rule switch**](cmdqueryname=flowspec+ipv4-fragment-rule+switch)
       
       
       
       The device is enabled to follow RFC 5575 when dealing with BGP Flow Specification IPv4 fragmentation rules.
    3. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
12. (Optional) Enable BGP Flow Specification to match inner packet information about the packets that leave an SRv6 TE Policy or SRv6 BE egress.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       
       
       The system view is displayed.
    2. Run [**flowspec match srv6-inner-ip enable**](cmdqueryname=flowspec+match+srv6-inner-ip+enable)
       
       
       
       BGP Flow Specification is enabled to match inner packet information about the packets that leave an SRv6 TE Policy or SRv6 BE egress.
    3. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the [**display bgp flow**](cmdqueryname=display+bgp+flow+vpnv4+vpn-instance+peer+verbose) **vpnv4** **vpn-instance** *vpn-instance-name* **peer** [ [ *ipv4-address* ] **verbose** ] command to check information about BGP VPN Flow Specification peers.
* Run the [**display bgp flow**](cmdqueryname=display+bgp+flow+vpnv4+vpn-instance+routing-table) **vpnv4** **vpn-instance** *vpn-instance-name* **routing-table** command to check information about BGP VPN Flow Specification routes.
* Run the [**display bgp flow**](cmdqueryname=display+bgp+flow+vpnv4+vpn-instance+routing-table+peer) **vpnv4** **vpn-instance** *vpn-instance-name* **routing-table** [ **peer** *ipv4-address* { **advertised-routes** | **received-routes** [ **active** ] } ] **statistics** command to check statistics about BGP VPN Flow Specification routes.
* Run the [**display flowspec**](cmdqueryname=display+flowspec+rule+slot) **rule** *reindex-value* **slot** *slot-id* command to check information about combined rules in the local BGP Flow Specification rule table.
* Run the [**display flowspec**](cmdqueryname=display+flowspec+rule+statistics+slot) **rule statistics slot** *slot-id* command to check statistics about the rules for BGP Flow Specification routes to take effect.
* Run the [**display flowspec resource rule**](cmdqueryname=display+flowspec+resource+rule+ipv4+ipv6+slot) { **ipv4** | **ipv6** } [ **slot** *slot-id* ] command to check the resource usage information about BGP Flow Specification route rules.