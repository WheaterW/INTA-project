Configuring Static BGP IPv6 Flow Specification
==============================================

Static BGP IPv6 Flow Specification allows BGP IPv6 Flow Specification routes to be manually created to control traffic.

#### Usage Scenario

Before deploying static BGP IPv6 Flow Specification, you need to manually create a BGP IPv6 Flow Specification route and establish a BGP IPv6 Flow Specification peer relationship between the device on which the BGP Flow Specification route is created and each ingress on the network to transmit BGP IPv6 Flow Specification routes.

In an AS with multiple ingresses, a BGP IPv6 Flow route reflector (Flow RR) can be deployed to reduce the number of BGP IPv6 Flow Specification peer relationships and save network resources.

If you want to filter traffic based on the address prefix but the BGP IPv6 Flow Specification route carrying the filtering rule cannot pass validation, disable the validation of BGP IPv6 Flow Specification routes received from a specified peer.


#### Pre-configuration Tasks

Before configuring static BGP IPv6 Flow Specification, complete the following task:

* [Configure a BGP4+ peer](dc_vrp_bgp6_cfg_0005.html) or [configure a BGP peer](dc_vrp_bgp_cfg_3006.html).

#### Procedure

1. Generate a BGP IPv6 Flow Specification route manually.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run the [**flow-route**](cmdqueryname=flow-route+ipv6) *flowroute-name* **ipv6** command to create a static BGP IPv6 Flow Specification route and enter the Flow-Route-IPv6 view.
      
      One BGP IPv6 Flow Specification route can include multiple **if-match** and **apply** clauses. **if-match** clauses define traffic filtering rules, and **apply** clauses define traffic behaviors. The relationships among clauses are as follows:
      * The relationship among **if-match** clauses of different types is "AND."
      * If **if-match** clauses of the same type are configured repeatedly, some rules override each other, and some other rules are in the OR relationship. For details, see the precautions for the [**if-match**](cmdqueryname=if-match) command.
      * The relationship among the traffic behaviors defined by **apply** clauses is "AND."The traffic behaviors defined by **apply** clauses apply to all traffic matching the filtering rules of **if-match** clauses.
   3. According to characteristics of the traffic to be controlled, you can configure one or more **if-match** clauses to define traffic filtering rules as needed:
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      **if-match** clauses take effect only when both the local and peer devices support the corresponding if-match rules.
      
      
      
      * To filter traffic based on the destination IPv6 address, run the [**if-match destination**](cmdqueryname=if-match+destination) *ipv6-address* *ipv6-mask-length* command.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        If traffic must be filtered based on a destination IP address but the BGP IPv6 Flow Specification rule carrying the rule defined by the [**if-match destination**](cmdqueryname=if-match+destination) command cannot pass validation, run the [**peer validation-disable**](cmdqueryname=peer+validation-disable) command to disable the validation of BGP IPv6 Flow Specification routes.
        
        By default, 0::0/0 is used as the prefix of each BGP IPv6 Flow Specification route that matches the export or import policy of a peer. To enable a device to change the prefix of each BGP IPv6 Flow Specification route that matches the export or import policy configured for a peer to the destination IP address specified in the [**if-match destination**](cmdqueryname=if-match+destination) command, run the [**route match-destination**](cmdqueryname=route+match-destination) command.
      * To set a traffic filtering rule that is based on a source address, run the [**if-match source**](cmdqueryname=if-match+source) *ipv6-address* *ipv6-mask-length* command.
      * To set a port number-based traffic filtering rule, run the [**if-match port**](cmdqueryname=if-match+port+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *port* or [**if-match port**](cmdqueryname=if-match+port+greater-than+less-than) **greater-than** *port* **less-than** *upper-port-value* command.
      * To set a source port number-based traffic filtering rule, run the [**if-match source-port**](cmdqueryname=if-match+source-port+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *port* or [**if-match source-port**](cmdqueryname=if-match+source-port+greater-than+less-than) **greater-than** *source-port* **less-than** *upper-source-port-value* command.
      * To set a destination port number-based traffic filtering rule, run the [**if-match destination-port**](cmdqueryname=if-match+destination-port+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *port* or [**if-match destination-port greater-than**](cmdqueryname=if-match+destination-port+greater-than+less-than) *port* **less-than** *upper-port-value* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        The [**if-match port**](cmdqueryname=if-match+port) command is mutually exclusive with the [**if-match destination-port**](cmdqueryname=if-match+destination-port) or [**if-match source-port**](cmdqueryname=if-match+source-port) command.
      * To set a traffic bearing protocol-based traffic filtering rule, run the [**if-match protocol**](cmdqueryname=if-match+protocol+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *protocol* or [**if-match protocol**](cmdqueryname=if-match+protocol+greater-than+less-than) **greater-than** *protocol* **less-than** *upper-protocol-value* command.
      * To set a DSCP-based traffic filtering rule, run the [**if-match dscp**](cmdqueryname=if-match+dscp+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *dscp* or [**if-match dscp**](cmdqueryname=if-match+dscp+greater-than+less-than) **greater-than** *dscp* **less-than** *upper-dscp-value* command.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        After the [**flow-route**](cmdqueryname=flow-route+ipv6) *flowroute-name* **ipv6** command is run, the [**if-match dscp**](cmdqueryname=if-match+dscp) command can be successfully run but does not take effect. To enable it to take effect in this case, run the [**flowspec allow ipv6 dscp**](cmdqueryname=flowspec+allow+ipv6+dscp) command to enable the DSCP-based BGP IPv6 Flow Specification traffic filtering rule.
      * To set a TCP-flag value-based traffic filtering rule, run the [**if-match tcp-flags**](cmdqueryname=if-match+tcp-flags+match+not) { **match** | **not** | **any-match** } *tcp-flags* command.
        
        Network attackers may send a large number of invalid TCP packets to attack network devices. To control the unidirectional traffic of TCP packets to ensure communication security, configure a filtering rule based on the TCP flag for the BGP IPv6 Flow Specification route using the [**if-match tcp-flags**](cmdqueryname=if-match+tcp-flags) command. Traffic matching the TCP flag is controlled using the actions specified in the apply clauses.
      * To set a fragment type-based traffic filtering rule, run the [**if-match fragment-type**](cmdqueryname=if-match+fragment-type+match+not) { **match** | **not** } *fragment-type-name* command.
      * To set an ICMP message code-based traffic filtering rule, run the [**if-match icmp-code**](cmdqueryname=if-match+icmp-code+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *icmp-code* or [**if-match icmp-code**](cmdqueryname=if-match+icmp-code+greater-than+less-than) **greater-than** *icmp-code* **less-than** *upper-icmp-code-value* command.
      * To set an ICMP message type-based traffic filtering rule, run the [**if-match icmp-type**](cmdqueryname=if-match+icmp-type+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *icmp-type* or [**if-match icmp-type**](cmdqueryname=if-match+icmp-type+greater-than+less-than) **greater-than** *icmp-type* **less-than** *upper-icmp-type-value* command.
      * To set a filtering rule based on the packet length of a BGP IPv6 Flow Specification route, run the [**if-match packet-length**](cmdqueryname=if-match+packet-length+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *packet-length-value* or [**if-match packet-length**](cmdqueryname=if-match+packet-length+greater-than+less-than) **greater-than** *packet-length-value* **less-than** *upper-packet-length-value* command.
   4. Run the following command as required to configure actions for apply clauses:
      
      
      * To discard the matched traffic, run the [**apply deny**](cmdqueryname=apply+deny) command.
      * To redirect the matched traffic to the traffic cleaning device or blackhole, run the **apply redirect vpn-target** *vpn-target-import* command.
      * To redirect the matched traffic to the IPv6 address of a specified next hop, run the [**apply redirect ipv6**](cmdqueryname=apply+redirect+ipv6) *redirect-ipv6-rt* command. This command must be used together with the [**local-route redirect ipv6 recursive-lookup ip**](cmdqueryname=local-route+redirect+ipv6+recursive-lookup+ip) command to trigger the redirection.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        A device can process the redirection next hop attribute configured using the [**apply redirect**](cmdqueryname=apply+redirect+ip) **ip** *redirect-ip-rt* command received from a peer only after the **[**peer**](cmdqueryname=peer)** { **ipv4-address** | **ipv6-address** } [**redirect ipv6 recursive-lookup ip**](cmdqueryname=redirect+ipv6+recursive-lookup+ip) command is run.
        
        A device can process the redirection next-hop attribute configured using the [**apply redirect**](cmdqueryname=apply+redirect+ip+color) **ip** *redirect-ip-rt* **color** *colorvalue* command and carried in routes that are received from a peer only after the **[**peer**](cmdqueryname=peer)** { *ipv4-address* | *ipv6-address* } [**redirect ipv6 recursive-lookup tunnel**](cmdqueryname=redirect+ipv6+recursive-lookup+tunnel+tunnel-selector) ****tunnel-selector**** **tunnel-selector-name** command is run.
        
        The redirection load balancing function can be enabled on the device only after the [**redirect load-balancing**](cmdqueryname=redirect+load-balancing) command is run. A maximum of eight redirection routes can be used for load balancing.
        
        After the [**apply redirect ipv6**](cmdqueryname=apply+redirect+ipv6+vpn-target) **vpn-target** *vpn-target-import* command is run, the filtered traffic is redirected to the L3VPN instance that matches the *vpn-target-import* value. In addition, after the [**redirect vpn-target include-evpn-preferred**](cmdqueryname=redirect+vpn-target+include-evpn-preferred) command is run, the filtered traffic is preferentially redirected to the L3EVPN instance that matches the *vpn-target-import* value.
      * To redirect the matched traffic to an SRv6 TE Policy, run the [**apply redirect ipv6**](cmdqueryname=apply+redirect+ipv6+color+prefix-sid) *redirect-ipv6-rt* **color** *colorvalue* [ **prefix-sid** *prefix-sid-value* ] command. This command must be used together with the [**local-route redirect ipv6 recursive-lookup tunnel**](cmdqueryname=local-route+redirect+ipv6+recursive-lookup+tunnel) **tunnel-selector** *tunnel-selector-name* command so that traffic recursion to the SRv6 TE Policy can be triggered.
      * To redirect the matched traffic to the IPv6 address of the specified next hop for load balancing (a maximum of eight redirection paths are supported for load balancing), run the [**apply redirect multi-ipv6**](cmdqueryname=apply+redirect+multi-ipv6) *redirectIPv6* command.
      * To redirect the matched traffic to SRv6 TE Policies for load balancing (a maximum of eight redirection paths are supported for load balancing), run the [**apply redirect multi-ipv6**](cmdqueryname=apply+redirect+multi-ipv6) *redirectIPv6* [ **color** **color-value** ] [ **weight** **weight-value** ] command.
      * To re-mark the service class of the matched traffic, run the [**apply remark-dscp**](cmdqueryname=apply+remark-dscp) command.
      * To limit the rate of the matched traffic, run the [**apply traffic-rate**](cmdqueryname=apply+traffic-rate) command.
      * To implement sampling for the matched traffic, run the [**apply traffic-action sample**](cmdqueryname=apply+traffic-action+sample) command.
        
        You can run the [**apply traffic-action sample**](cmdqueryname=apply+traffic-action+sample) command for a BGP IPv6 Flow Specification route to sample the traffic that matches the specified filtering rules. Through sampling, abnormal traffic can be identified and filtered out, which protects the attacked device and improves network security.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The [**apply deny**](cmdqueryname=apply+deny) and [**apply traffic-rate**](cmdqueryname=apply+traffic-rate) commands are mutually exclusive.
      
      If the configured BGP IPv6 Flow Specification route attribute does not need to take effect locally, run the [**routing-table rib-only**](cmdqueryname=routing-table+rib-only+route-policy) [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command to disable the device from delivering the BGP IPv6 Flow Specification route to the FES forwarding table.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Establish a BGP IPv6 Flow Specification peer relationship.
   
   
   
   BGP IPv6 Flow Specification peer relationships must be established between the network ingress and device on which the BGP IPv6 Flow Specification route is manually created.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv6-family flow**](cmdqueryname=ipv6-family+flow)
      
      
      
      The BGP-IPv6-Flow address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+enable) { *ipv4-address* | *ipv6-address* } **enable**
      
      
      
      A BGP IPv6 Flow Specification peer relationship is established.
      
      
      
      After the peer relationship is established in the BGP-IPv6-Flow address family view, the manually generated BGP Flow Specification route is automatically imported to the BGP routing table and then sent to the peer.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
3. (Optional) Configure a Flow RR.
   
   
   
   Before configuring a Flow RR, establish a BGP IPv6 Flow Specification peer relationship between the Flow RR and the device on which the BGP IPv6 Flow Specification route is generated and between the Flow RR and every network ingress.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv6-family flow**](cmdqueryname=ipv6-family+flow)
      
      
      
      The BGP-IPv6-Flow address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+reflect-client) { *ipv4-address* | *ipv6-address* } **reflect-client**
      
      
      
      A Flow RR is configured, and clients are specified for it.
      
      
      
      The Router on which the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command is run functions as a Flow RR, and the specified peers function as clients.
   5. (Optional) Run [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients)
      
      
      
      Route reflection between clients through the RR is disabled.
      
      
      
      If the clients of a Flow RR are fully meshed, you can run the [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command on the Flow RR to disable route reflection between clients through the RR, which reduces costs.
   6. (Optional) Run [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) { *cluster-id-value* | *cluster-id-ipv4* }
      
      
      
      A cluster ID is configured for the Flow RR.
      
      
      
      If a cluster has multiple Flow RRs, run this command to set the same *cluster-id* for these RRs.
      
      The [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) command is applicable only to Flow RRs.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
4. (Optional) Disable BGP IPv6 Flow Specification route validation.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv6-family flow**](cmdqueryname=ipv6-family+flow)
      
      
      
      The BGP-IPv6-Flow address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+validation-disable) *ipv6-address* **validation-disable**
      
      
      
      The device is disabled from validating BGP IPv6 Flow Specification routes received from a specified peer.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
5. (Optional) Enable CAR statistics collection and packet loss statistics collection for BGP Flow Specification.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**flowspec statistic enable**](cmdqueryname=flowspec+statistic+enable)
      
      
      
      CAR statistics collection and packet loss statistics collection for BGP Flow Specification are enabled.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
6. (Optional) Disable BGP Flow Specification on the interface.
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
7. (Optional) Disable BGP Flow Specification protection.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**flowspec protocol-protect**](cmdqueryname=flowspec+protocol-protect+ipv4+ipv6+disable) { **ipv4** | **ipv6** } **disable**
      
      
      
      BGP Flow Specification protection is disabled.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
8. (Optional) Enable the device to redirect traffic to a specified IPv6 next hop based on a static BGP IPv6 Flow Specification route.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv6-family flow**](cmdqueryname=ipv6-family+flow)
      
      
      
      The BGP-IPv6-Flow address family view is displayed.
   4. Run [**local-route redirect ipv6 recursive-lookup ip**](cmdqueryname=local-route+redirect+ipv6+recursive-lookup+ip)
      
      
      
      The device is enabled to redirect traffic to a specified IPv6 next hop based on a static BGP IPv6 Flow Specification route.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
9. (Optional) Allow the device to recurse static BGP IPv6 Flow Specification routes to tunnels.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv6-family flow**](cmdqueryname=ipv6-family+flow)
      
      
      
      The BGP-IPv6-Flow address family view is displayed.
   4. Run [**local-route redirect ipv6 recursive-lookup tunne**](cmdqueryname=local-route+redirect+ipv6+recursive-lookup+tunne+tunnel-selector)l **tunnel-selector** *tunnel-selector-name*
      
      
      
      The device is allowed to recurse static BGP IPv6 Flow Specification routes to tunnels.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
10. (Optional) Enable the DSCP-based BGP IPv6 Flow Specification traffic filtering rule.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       
       
       The system view is displayed.
    2. Run [**flowspec allow ipv6 dscp**](cmdqueryname=flowspec+allow+ipv6+dscp)
       
       
       
       The DSCP-based BGP IPv6 Flow Specification traffic filtering rule is enabled.
    3. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
11. (Optional) Enable BGP Flow Specification to match inner packet information about the packets that leave an SRv6 TE Policy or SRv6 BE egress.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       
       
       The system view is displayed.
    2. Run [**flowspec match srv6-inner-ip enable**](cmdqueryname=flowspec+match+srv6-inner-ip+enable)
       
       
       
       BGP Flow Specification is enabled to match inner packet information about the packets that leave an SRv6 TE Policy or SRv6 BE egress.
    3. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
12. (Optional) Enable BGP IPv6 Flow Specification to match the internal protocol number in the header of an IPv6 fragment.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       
       
       The system view is displayed.
    2. Run [**flowspec match ipv6 fragment-inner-protocol enable**](cmdqueryname=flowspec+match+ipv6+fragment-inner-protocol+enable)
       
       
       
       BGP IPv6 Flow Specification is enabled to match the internal protocol number in the header of an IPv6 fragment.
    3. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
13. (Optional) Enable the device to redirect traffic to a specified IPv6 next hop based on a static BGP Flow Specification route.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       
       
       The system view is displayed.
    2. Run [**bgp**](cmdqueryname=bgp) *as-number*
       
       
       
       The BGP view is displayed.
    3. Run [**ipv6-family flow**](cmdqueryname=ipv6-family+flow)
       
       
       
       The BGP-IPv6-Flow address family view is displayed.
    4. Run **local-route redirect ipv6 recursive-lookup ip**
       
       
       
       The device is enabled to redirect traffic to a specified IPv6 next hop based on a static BGP IPv6 Flow Specification route.
    5. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the [**display bgp flow ipv6 peer**](cmdqueryname=display+bgp+flow+ipv6+peer) command to check information about the BGP IPv6 Flow Specification peers.
* Run the [**display bgp flow ipv6 routing-table**](cmdqueryname=display+bgp+flow+ipv6+routing-table) command to check information about BGP IPv6 Flow Specification routes.
* Run the [**display bgp flow ipv6 routing-table**](cmdqueryname=display+bgp+flow+ipv6+routing-table) [**statistics**](cmdqueryname=statistics) command to check statistics about BGP IPv6 Flow Specification routes.
* Run the [**display flowspec ipv6 statistics**](cmdqueryname=display+flowspec+ipv6+statistics) *reIndex* command to check statistics about traffic matching a specified BGP IPv6 Flow Specification route.
* Run the [**display flowspec**](cmdqueryname=display+flowspec+ipv6+rule+slot) **ipv6** **rule** *reindex-value* **slot** *slot-id* command to check information about combined rules in the BGP IPv6 Flow Specification route rule table.
* Run the [**display flowspec**](cmdqueryname=display+flowspec+ipv6+rule+statistics+slot) **ipv6** **rule statistics slot** *slot-id* command to check statistics about the rules for BGP IPv6 Flow Specification routes to take effect.
* Run the [**display flowspec resource rule**](cmdqueryname=display+flowspec+resource+rule+ipv4+ipv6+slot) { **ipv4** | **ipv6** } [ **slot** *slot-id* ] command to check the resource usage information about BGP Flow Specification route rules.