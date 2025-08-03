Configuring Static BGP Flow Specification
=========================================

BGP Flow Specification routes are generated manually to control traffic in static BGP Flow Specification.

#### Usage Scenario

When static BGP Flow Specification is configured, a BGP Flow Specification route needs to be generated manually, and a BGP Flow Specification peer relationship needs to be established between the device that generates the BGP Flow Specification route and each ingress on the network to advertise BGP Flow Specification routes.

In an AS with multiple ingresses, a BGP Flow route reflector (Flow RR) can be deployed to reduce the number of BGP Flow Specification peer relationships to be established and save network resources.

If you want to filter traffic matching a specified address prefix but BGP Flow Specification routes matching the specified address prefix cannot pass validation, disable the validation of the BGP Flow Specification routes received from a specified peer.


#### Pre-configuration Tasks

Before configuring static BGP Flow Specification, [configure a BGP peer](dc_vrp_bgp_cfg_3006.html).


#### Procedure

1. Create a BGP Flow Specification route manually.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**flow-route**](cmdqueryname=flow-route) *flowroute-name* command to create a static BGP Flow Specification route and enter the Flow-Route view.
      
      One BGP Flow Specification route can include multiple **if-match** and **apply** clauses. **if-match** clauses define traffic filtering rules, and **apply** clauses define traffic behaviors. The relationships among clauses are as follows:
      * The relationship among **if-match** clauses of different types is "AND."
      * If **if-match** clauses of the same type are configured repeatedly, some rules override each other, and some other rules are in the OR relationship. For details, see the precautions for the [**if-match**](cmdqueryname=if-match) command.
      * The relationship among the traffic behaviors defined by **apply** clauses is "AND."The traffic behaviors defined by **apply** clauses apply to all traffic matching the filtering rules of **if-match** clauses.
   3. According to characteristics of the traffic to be controlled, you can configure one or more **if-match** clauses to define traffic filtering rules as needed:
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      **if-match** clauses take effect only when both the local and peer devices support the corresponding if-match rules.
      
      
      
      * To set a destination address-based traffic filtering rule, run the [**if-match destination**](cmdqueryname=if-match+destination) *ipv4-address* { *mask* | *mask-length* } command.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        Traffic control is performed based on a specified destination IP address specified in a rule configured using the [**if-match destination**](cmdqueryname=if-match+destination) command, but BGP Flow Specification routes matching the rule cannot pass validation. In this situation, run the [**peer validation-disable**](cmdqueryname=peer+validation-disable) command to disable the validation.
        
        By default, 0.0.0.0/0 is used as the prefix of each BGP Flow Specification route that matches the export or import policy configured for a peer. To enable a device to change the prefix of each BGP Flow Specification route that matches the export or import policy configured for a peer to the destination IP address specified in the [**if-match destination**](cmdqueryname=if-match+destination) command, run the [**route match-destination**](cmdqueryname=route+match-destination) command.
      * To set a destination community attribute-based traffic filtering rule:
        1. To control the range of destination community attribute-based traffic filtering rules that can take effect, run the [**match-community community-list**](cmdqueryname=match-community+community-list) **community-list-name** command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
           
           Before you run the [**match-community community-list**](cmdqueryname=match-community+community-list) **community-list-name** command to control the range of destination community attribute-based traffic filtering rules that can take effect, run the [**ip community-list**](cmdqueryname=ip+community-list) command to create a BGP community list, and run the [**community**](cmdqueryname=community) command to configure community attributes for the BGP community list.
        2. To set a destination community attribute-based traffic filtering rule, run the [**if-match destination-community**](cmdqueryname=if-match+destination-community+community-list) *community-value* command. The traffic filtering rule specified using *community-value* in this command takes effect only when it is in the range of destination community attribute-based traffic filtering rules configured using **community-list** *community-list-name*.
        
        If you want to control traffic based on an address prefix, run the [**if-match destination**](cmdqueryname=if-match+destination) command to configure a destination address-based traffic filtering rule. However, if there are a large number of routes of the same type, configuring destination address-based traffic filtering rules one by one for traffic control is complex and consumes many resources. To address this issue, you can configure traffic filtering through destination community attribute aggregation.
        
        After the configuration is complete, run the [**display bgp flow routing-table**](cmdqueryname=display+bgp+flow+routing-table+destination-community) *reIndex* **destination-community** command to check details about the traffic filtering rule that is based on the community attribute of the destination IP address in a BGP Flow Specification route.
      * To set a source address-based traffic filtering rule, run the [**if-match source**](cmdqueryname=if-match+source) *ipv4-address* { *mask* | *mask-length* } command.
      * To set a port number-based traffic filtering rule, run the [**if-match port**](cmdqueryname=if-match+port+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *port* or [**if-match port**](cmdqueryname=if-match+port+greater-than+less-than) **greater-than** *port* **less-than** *upper-port-value* command.
      * To set a source port number-based traffic filtering rule, run the [**if-match source-port**](cmdqueryname=if-match+source-port+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *port* or [**if-match source-port**](cmdqueryname=if-match+source-port+greater-than+less-than) **greater-than** *source-port* **less-than** *upper-source-port-value* command.
      * To set a destination port number-based traffic filtering rule, run the [**if-match destination-port**](cmdqueryname=if-match+destination-port+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *port* or [**if-match destination-port greater-than**](cmdqueryname=if-match+destination-port+greater-than+less-than) *port* **less-than** *upper-port-value* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        The [**if-match port**](cmdqueryname=if-match+port) command is mutually exclusive with the [**if-match destination-port**](cmdqueryname=if-match+destination-port) or [**if-match source-port**](cmdqueryname=if-match+source-port) command.
      * To set a traffic bearing protocol-based traffic filtering rule, run the [**if-match protocol**](cmdqueryname=if-match+protocol+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *protocol* or [**if-match protocol**](cmdqueryname=if-match+protocol+greater-than+less-than) **greater-than** *protocol* **less-than** *upper-protocol-value* command.
      * To set a DSCP-based traffic filtering rule, run the [**if-match dscp**](cmdqueryname=if-match+dscp+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *dscp* or [**if-match dscp**](cmdqueryname=if-match+dscp+greater-than+less-than) **greater-than** *dscp* **less-than** *upper-dscp-value* command.
      * To set a TCP-flag value-based traffic filtering rule, run the [**if-match tcp-flags**](cmdqueryname=if-match+tcp-flags+match+not) { **match** | **not** | **any-match** } *tcp-flags* command.
        
        Network attackers may send a large number of invalid TCP packets to attack network devices. To control the unidirectional traffic of TCP packets to ensure communication security, configure a filtering rule based on the TCP flag for the BGP Flow Specification route using the [**if-match tcp-flags**](cmdqueryname=if-match+tcp-flags) command. The traffic behavior specified in the **apply** clause applies to the traffic that matches the TCP flag value.
      * To set a fragment type-based traffic filtering rule, run the [**if-match fragment-type**](cmdqueryname=if-match+fragment-type+match+not) { **match** | **not** } *fragment-type-name* command.
      * To set an ICMP message code-based traffic filtering rule, run the [**if-match icmp-code**](cmdqueryname=if-match+icmp-code+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *icmp-code* or [**if-match icmp-code**](cmdqueryname=if-match+icmp-code+greater-than+less-than) **greater-than** *icmp-code* **less-than** *upper-icmp-code-value* command.
      * To set an ICMP message type-based traffic filtering rule, run the [**if-match icmp-type**](cmdqueryname=if-match+icmp-type+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *icmp-type* or [**if-match icmp-type**](cmdqueryname=if-match+icmp-type+greater-than+less-than) **greater-than** *icmp-type* **less-than** *upper-icmp-type-value* command.
        
        **Table 1** *icmp-type* and *icmp-code* values corresponding to ICMP message names
        | *icmp-name* | *icmp-type* | *icmp-code* |
        | --- | --- | --- |
        | Echo | 8 | 0 |
        | Echo-reply | 0 | 0 |
        | Parameter-problem | 12 | 0 |
        | Port-unreachable | 3 | 3 |
        | Protocol-unreachable | 3 | 2 |
        | Reassembly-timeout | 11 | 1 |
        | Source-quench | 4 | 0 |
        | Source-route-failed | 3 | 5 |
        | Timestamp-reply | 14 | 0 |
        | Timestamp-request | 13 | 0 |
        | Ttl-exceeded | 11 | 0 |
        | Fragmentneed-DFset | 3 | 4 |
        | Host-redirect | 5 | 1 |
        | Host-tos-redirect | 5 | 3 |
        | Host-unreachable | 3 | 1 |
        | Information-reply | 16 | 0 |
        | Information-request | 15 | 0 |
        | Net-redirect | 5 | 0 |
        | Net-tos-redirect | 5 | 2 |
        | Net-unreachable | 3 | 0 |
      * To set a filtering rule based on the packet length of a BGP Flow Specification route, run the [**if-match packet-length**](cmdqueryname=if-match+packet-length+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *packet-length-value* or [**if-match packet-length**](cmdqueryname=if-match+packet-length+greater-than+less-than) **greater-than** *packet-length-value* **less-than** *upper-packet-length-value* command.
   4. Run the following command as required to configure actions for **apply** clauses:
      
      
      * To discard the matched traffic, run the [**apply deny**](cmdqueryname=apply+deny) command. The [**apply deny**](cmdqueryname=apply+deny) and [**apply traffic-rate**](cmdqueryname=apply+traffic-rate) commands cannot be used together.
      * To redirect the matched traffic to the traffic cleaning device or blackhole, run the [**apply redirect**](cmdqueryname=apply+redirect+vpn-target+ip) { **vpn-target** *vpn-target-import* | **ip** *redirect-ip-rt* } command.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        The device can process the redirection next hop attribute configured using the [**apply redirect**](cmdqueryname=apply+redirect+ip) **ip** *redirect-ip-rt* command received from a peer only after the [**peer redirect ip**](cmdqueryname=peer+redirect+ip) command is run.
        
        The device can process the redirection next hop attribute configured using the [**apply redirect**](cmdqueryname=apply+redirect+ip+color) **ip** *redirect-ip-rt* **color** *colorvalue* command received from a peer only after the [**peer redirect ip**](cmdqueryname=peer+redirect+ip) command is run.
        
        The redirection load balancing function can be enabled on the device only after the [**redirect load-balancing**](cmdqueryname=redirect+load-balancing) command is run. A maximum of eight redirection routes can be used for load balancing.
      * To redirect the matched traffic to an SR-MPLS TE Policy, run the [**apply redirect**](cmdqueryname=apply+redirect+ip+color) **ip** *redirect-ip-rt* **color** *colorvalue* command.
      * To redirect the matched traffic to the IPv6 address of a specified next hop, run the [**apply redirect ipv6**](cmdqueryname=apply+redirect+ipv6) *redirect-ipv6-rt* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        A device can process the redirection next-hop attribute configured using the [**apply redirect**](cmdqueryname=apply+redirect+ipv6) **ipv6** *redirect-ipv6-rt* command and carried in the routes that are received from peers only after the **[**peer**](cmdqueryname=peer)** *ipv4-address* [**redirect ipv6**](cmdqueryname=redirect+ipv6) command is run.
        
        The [**apply redirect ipv6**](cmdqueryname=apply+redirect+ipv6) *redirect-ipv6-rt* command must be used together with the [**local-route redirect ipv6**](cmdqueryname=local-route+redirect+ipv6) command to trigger traffic redirection to a specified IPv6 next hop.
      * To redirect the matched traffic to an SRv6 TE Policy, run the [**apply redirect ipv6**](cmdqueryname=apply+redirect+ipv6+color+prefix-sid) *redirect-ipv6-rt* **color** *colorvalue* [ **prefix-sid** *prefix-sid-value* ] command.
      * To redirect the matched traffic to SR-MPLS TE Policies for load balancing (a maximum of eight redirection paths are supported for load balancing), run the [**apply redirect multi-ip**](cmdqueryname=apply+redirect+multi-ip+color) *redirectIP* [ ****color**** **color-value** ] [ **weight** **weight-value** ] command.
      * To redirect the matched traffic to SRv6 TE Policies for load balancing (a maximum of eight redirection paths are supported for load balancing), run the [**apply redirect multi-ipv6**](cmdqueryname=apply+redirect+multi-ipv6)*redirectIPv6* [ **color** **color-value** ] [ **weight** **weight-value** ] command.
      * To re-mark the service class of the matched traffic, run the [**apply remark-dscp**](cmdqueryname=apply+remark-dscp) command.
      * To limit the rate of the matched traffic, run the [**apply traffic-rate**](cmdqueryname=apply+traffic-rate) command. The [**apply deny**](cmdqueryname=apply+deny) and [**apply traffic-rate**](cmdqueryname=apply+traffic-rate) commands cannot be used together.
      * To implement sampling for the matched traffic, run the [**apply traffic-action sample**](cmdqueryname=apply+traffic-action+sample) command.
        
        You can run the [**apply traffic-action sample**](cmdqueryname=apply+traffic-action+sample) command for a BGP Flow Specification route to sample the traffic that matches the specified filtering rules. Through sampling, abnormal traffic can be identified and filtered out, which protects the attacked device and improves network security.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If the configured BGP Flow Specification route attribute does not need to take effect locally, run the [**routing-table rib-only**](cmdqueryname=routing-table+rib-only+route-policy) [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command to disable the device from delivering the BGP Flow Specification route to the FES forwarding table.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure BGP Flow Specification peer relationships.
   
   
   
   BGP Flow Specification peer relationships must be established between the network ingress and device on which the BGP Flow Specification route is manually created.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv4-family flow**](cmdqueryname=ipv4-family+flow)
      
      
      
      The BGP-Flow address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**enable**](cmdqueryname=enable)
      
      
      
      The BGP Flow Specification peer relationship is enabled.
      
      
      
      After the BGP Flow Specification peer relationship is established in the BGP-Flow address family view, the manually generated BGP Flow Specification route is imported to the BGP routing table and then sent to each peer.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
3. (Optional) Configure a Flow RR.
   
   
   
   Before configuring a Flow RR, establish a BGP Flow Specification peer relationship between the Flow RR and the device on which the BGP Flow Specification route is generated and between the Flow RR and every network ingress.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv4-family flow**](cmdqueryname=ipv4-family+flow)
      
      
      
      The BGP-Flow address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**reflect-client**](cmdqueryname=reflect-client)
      
      
      
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
4. (Optional) Configure the device to check the AS\_Path attribute during BGP Flow Specification route validation.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv4-family flow**](cmdqueryname=ipv4-family+flow)
      
      
      
      The BGP-Flow address family view is displayed.
   4. Run [**route validation-mode include-as**](cmdqueryname=route+validation-mode+include-as)
      
      
      
      The device is configured to check the AS\_Path attribute during BGP Flow Specification route validation.
      
      
      
      BGP Flow Specification route validation is performed in either of the following modes:
      * Validation mode 1: After receiving a BGP Flow Specification route with a destination address-based filtering rule, the device checks the validity of the route using the rules described in [Figure 1](#EN-US_TASK_0172372345__en-us_cliref_0172383989_fig_route_validation-mode_include-as01). The route is considered valid only if the validation succeeds.
      * Validation mode 2: After receiving a BGP Flow Specification route with a destination address-based filtering rule, the device checks the validity of the route by checking whether the AS\_Path attribute of the route carries the AS\_Set and AS\_Sequence fields. The route is considered valid only if its AS\_Path attribute does not carry the AS\_Set or AS\_Sequence field.Validation mode 2 is configured using the [**route validation-mode include-as**](cmdqueryname=route+validation-mode+include-as) command. If this command is configured, the device checks the validity of a BGP Flow Specification route using mode 2 first.
      * If the validation succeeds, the BGP Flow Specification route is considered valid, and mode 1 is not used.
      * If the validation fails, the device checks the validity of the BGP Flow Specification route using mode 1.If this command is not run, the device uses mode 1 to check the validity of BGP Flow Specification routes.**Figure 1** BGP Flow Specification validation rules  
      ![](figure/en-us_image_0000001183343598.png)
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
5. (Optional) Disable BGP Flow Specification route validation.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv4-family flow**](cmdqueryname=ipv4-family+flow)
      
      
      
      The BGP-Flow address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+validation-disable) *ipv4-address* **validation-disable**
      
      
      
      The device is disabled from validating BGP Flow Specification routes received from a specified peer.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
6. (Optional) Disable the device from validating the next hop of each route that carries the redirection next-hop attribute and is received from a specified EBGP peer.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv4-family flow**](cmdqueryname=ipv4-family+flow)
      
      
      
      The BGP-Flow address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+redirect+ip+validation-disable) *ipv4-address* **redirect ip validation-disable**
      
      
      
      The device is disabled from validating the routes that carry a redirection extended community attribute and are received from a specified EBGP peer.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
7. (Optional) Allow the device to recurse received routes with the next-hop IPv6 address, color attribute, and prefix SID attributes to tunnels.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv4-family flow**](cmdqueryname=ipv4-family+flow)
      
      
      
      The BGP-Flow address family view is displayed.
   4. Run [**redirect tunnelv6 tunnel-selector**](cmdqueryname=redirect+tunnelv6+tunnel-selector) *tunnel-selector-name*
      
      
      
      The device is configured to recurse received routes with the redirection next-hop IPv6 address, color, and prefix SID attributes to tunnels.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
8. (Optional) Configure the redirection next-hop attribute ID for BGP Flow Specification routes.
   
   
   
   The redirection next-hop attribute ID can be 0x010C (defined in a related RFC) or 0x0800 (defined in a related draft). If a Huawei device needs to communicate with a non-Huawei device that does not support the redirection next-hop attribute ID of 0x010C or 0x0800, set the redirection next-hop attribute ID of BGP Flow Specification routes as required. Perform one of the following configurations based on the ID supported by non-Huawei devices:
   
   * Set the redirection next-hop attribute ID to 0x010C (defined in a related RFC) for BGP Flow Specification routes.
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**ipv4-family flow**](cmdqueryname=ipv4-family+flow)
        
        The BGP-Flow address family view is displayed.
     4. Run [**peer**](cmdqueryname=peer+redirect+ip+rfc-compatible) *ipv4-address* **redirect ip rfc-compatible**
        
        The redirection next-hop attribute ID of the BGP Flow Specification route is set to 0x010C (defined in a related RFC).
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Change the redirection next-hop attribute ID of BGP Flow Specification routes to 0x0800 (defined in a related draft).
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**ipv4-family flow**](cmdqueryname=ipv4-family+flow)
        
        The BGP-Flow address family view is displayed.
     4. Run [**peer**](cmdqueryname=peer+redirect+ip+draft-compatible) *ipv4-address* **redirect ip draft-compatible**
        
        The redirection next-hop attribute ID of BGP Flow Specification routes is changed to 0x0800 (defined in a related draft).
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
9. (Optional) Configure the interface in the BGP Flow Specification as the traffic-injection interface of the cleaned traffic to prevent the injected traffic from matching the Flow Specification rules and being switched back to the cleaning device.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   3. Run [**flowspec refluence**](cmdqueryname=flowspec+refluence)
      
      
      
      The interface in BGP Flow Specification is configured as the traffic-injection interface for cleaning traffic.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      This configuration conflicts with MF classification. Therefore, after this command is configured on an interface, do not configure MF classification on the interface.
      
      This command cannot be configured on Eth-Trunk member interfaces. The configuration on a main interface also takes effect on its sub-interfaces.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
10. (Optional) Disable BGP Flow Specification on the interface.
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
11. (Optional) Configure BGP Flow Specification for the packets leaving the public network based on IP information.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       
       
       The system view is displayed.
    2. Run [**flowspec match-ip-layer mpls-pop**](cmdqueryname=flowspec+match-ip-layer+mpls-pop)
       
       
       
       BGP Flow Specification is configured for the packets leaving the public network based on IP information.
    3. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
12. (Optional) Enable CAR statistics collection and packet loss statistics collection for BGP Flow Specification.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       
       
       The system view is displayed.
    2. Run [**flowspec statistic enable**](cmdqueryname=flowspec+statistic+enable)
       
       
       
       CAR statistics collection and packet loss statistics collection for BGP Flow Specification are enabled.
    3. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
13. (Optional) Configure BGP Flow Specification for packets entering an IPv4 VXLAN tunnel.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       
       
       The system view is displayed.
    2. Run [**flowspec match vxlan-packet enable**](cmdqueryname=flowspec+match+vxlan-packet+enable)
       
       
       
       BGP Flow Specification is configured for packets entering an IPv4 VXLAN tunnel.
    3. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
14. (Optional) Enable BGP Flow Specification on a GRE tunnel interface.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       
       
       The system view is displayed.
    2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
       
       
       
       The tunnel interface view is displayed.
    3. Run [**tunnel-protocol**](cmdqueryname=tunnel-protocol+gre) **gre**
       
       
       
       The tunnel is encapsulated as a GRE tunnel.
    4. Run [**flowspec match tunnel-pop**](cmdqueryname=flowspec+match+tunnel-pop)
       
       
       
       BGP Flow Specification is enabled on the GRE tunnel interface.
    5. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
15. (Optional) Disable BGP Flow Specification protection.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       
       
       The system view is displayed.
    2. Run [**flowspec protocol-protect**](cmdqueryname=flowspec+protocol-protect+ipv4+ipv6+disable) { **ipv4** | **ipv6** } **disable**
       
       
       
       BGP Flow Specification protection is disabled.
    3. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
16. (Optional) Enable the device to follow RFC 5575 when dealing with BGP Flow Specification IPv4 fragmentation rules.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       
       
       The system view is displayed.
    2. Run [**flowspec ipv4-fragment-rule switch**](cmdqueryname=flowspec+ipv4-fragment-rule+switch)
       
       
       
       The device is enabled to follow RFC 5575 when dealing with BGP Flow Specification IPv4 fragmentation rules.
    3. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
17. (Optional) Enable BGP Flow Specification to match inner packet information about the packets that leave an SRv6 TE Policy or SRv6 BE egress.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       
       
       The system view is displayed.
    2. Run [**flowspec match srv6-inner-ip enable**](cmdqueryname=flowspec+match+srv6-inner-ip+enable)
       
       
       
       BGP Flow Specification is enabled to match inner packet information about the packets that leave an SRv6 TE Policy or SRv6 BE egress.
    3. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
18. (Optional) Disable the device from sending routes that carry the destination community attribute rule to a specified peer.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       
       
       The system view is displayed.
    2. Run [**bgp**](cmdqueryname=bgp) *as-number*
       
       
       
       The BGP view is displayed.
    3. Run [**ipv4-family flow**](cmdqueryname=ipv4-family+flow)
       
       
       
       The BGP-Flow address family view is displayed.
    4. Run **[**peer**](cmdqueryname=peer+advertise+destination-community+disable)** *peerIPv4Addr* [**advertise destination-community disable**](cmdqueryname=peer+advertise+destination-community+disable)
       
       
       
       The device is disabled from sending routes that carry the destination community attribute rule to a specified peer. Perform this step if you do not want the device to send routes that carry the destination community attribute rule to a specified BGP Flow Specification peer.
    5. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
19. (Optional) Enable the device to redirect traffic to a specified IPv6 next hop based on a static BGP Flow Specification route.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       
       
       The system view is displayed.
    2. Run [**bgp**](cmdqueryname=bgp) *as-number*
       
       
       
       The BGP view is displayed.
    3. Run [**ipv4-family flow**](cmdqueryname=ipv4-family+flow)
       
       
       
       The BGP-Flow address family view is displayed.
    4. Run **[**local-route redirect ipv6**](cmdqueryname=local-route+redirect+ipv6)**
       
       
       
       The device is enabled to redirect traffic to a specified IPv6 next hop based on a static BGP Flow Specification route.
    5. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
20. (Optional) Enable BGP Flow Specification to match an IPv4 destination community attribute-based traffic filtering rule.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       
       
       The system view is displayed.
    2. Run [**flowspec match-rule enhance enable**](cmdqueryname=flowspec+match-rule+enhance+enable)
       
       
       
       BGP Flow Specification is enabled to match an IPv4 destination community attribute-based traffic filtering rule.
    3. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the [**display bgp flow peer**](cmdqueryname=display+bgp+flow+peer+verbose) [ [ *ipv4-address* ] **verbose** ] command to check information about BGP Flow Specification peers.
* Run the [**display bgp flow routing-table**](cmdqueryname=display+bgp+flow+routing-table) command to check BGP Flow Specification routing information.
* Run the [**display bgp flow routing-table**](cmdqueryname=display+bgp+flow+routing-table+peer+advertised-routes) [ **peer** *ipv4-address* ] [ **advertised-routes** | **received-routes** [ **active** ] ] [**statistics**](cmdqueryname=statistics) command to check BGP Flow Specification route statistics.
* Run the [**display flowspec statistics**](cmdqueryname=display+flowspec+statistics) *reindex* command to check statistics about the traffic matching a specified BGP Flow Specification route.
* Run the [**display flowspec**](cmdqueryname=display+flowspec+rule+slot) **rule** *reindex-value* **slot** *slot-id* command to check information about combined rules in the local BGP Flow Specification rule table.
* Run the [**display flowspec**](cmdqueryname=display+flowspec+rule+statistics+slot) **rule statistics slot** *slot-id* command to check statistics about the rules for BGP Flow Specification routes to take effect.
* Run the [**display flowspec resource rule**](cmdqueryname=display+flowspec+resource+rule+ipv4+ipv6+slot) { **ipv4** | **ipv6** } [ **slot** *slot-id* ] command to check the resource usage information about BGP Flow Specification route rules.