Configuring Static BGP VPNv6 Flow Specification
===============================================

Static BGP VPNv6 Flow Specification allows BGP VPNv6 Flow Specification routes to be transmitted and traffic filtering policies to be generated. The policies improve security of devices in VPNs.

#### Usage Scenario

To deploy static BGP VPNv6 Flow Specification, create a BGP IPv6 VPN Flow Specification route first, and then establish a BGP VPNv6 Flow Specification peer relationship between the device on which the BGP IPv6 VPN Flow Specification route is created and the network ingress to transmit the BGP VPNv6 Flow Specification route.

In an AS with multiple ingresses, a BGP Flow route reflector (Flow RR) can be deployed to reduce the number of BGP VPNv6 Flow Specification peer relationships and save network resources.

If you want to filter traffic based on an address prefix and the BGP VPNv6 Flow Specification route carrying the filtering rule cannot pass validation, disable the validation of the BGP VPNv6 Flow Specification routes received from a specified peer.


#### Pre-configuration Tasks

Before configuring static BGP VPNv6 Flow Specification, [configure a VPN instance](dc_vrp_mpls-l3vpn-v6_cfg_2058.html) and [bind an interface to the VPN instance](dc_vrp_mpls-l3vpn-v6_cfg_2059.html).


#### Procedure

1. Create a BGP IPv6 VPN Flow Specification route.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**flow-route**](cmdqueryname=flow-route+ipv6+vpn-instance) *flowroute-name* **ipv6** **vpn-instance** *vpn-instance-name*
      
      
      
      A static BGP IPv6 VPN Flow Specification route is created, and the Flow-Route IPv6 VPN instance view is displayed.
      
      
      
      One BGP IPv6 VPN Flow Specification route can include multiple **if-match** and **apply** clauses. **if-match** clauses define traffic filtering rules, and **apply** clauses define traffic behaviors. The relationships among clauses are as follows:
      * The relationship among **if-match** clauses of different types is "AND."
      * If **if-match** clauses of the same type are configured repeatedly, some rules override each other, and some other rules are in the OR relationship. For details, see the precautions for the [**if-match**](cmdqueryname=if-match) command.
      * The relationship among the traffic behaviors defined by **apply** clauses is "AND."The traffic behaviors defined by **apply** clauses apply to all traffic matching the filtering rules of **if-match** clauses.
   3. According to characteristics of the traffic to be controlled, you can configure one or more **if-match** clauses to define traffic filtering rules as needed:
      
      
      * To set a traffic filtering rule that is based on a destination IP address, run the [**if-match destination**](cmdqueryname=if-match+destination) *ipv6-address* { *mask* | *mask-length* } command.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        Traffic control is performed based on a specified destination IP address specified in a rule configured using the [**if-match destination**](cmdqueryname=if-match+destination) command, but BGP IPv6 VPN Flow Specification routes matching the rule cannot pass validation. In this situation, run the [**peer validation-disable**](cmdqueryname=peer+validation-disable) command to disable the validation.
        
        By default, 0.0.0.0/0 is used as the prefix in the peer import or export policy against which BGP IPv6 VPN Flow Specification routes are matched. To use a peer import or export policy to match BGP IPv6 VPN Flow Specification routes against the destination IPv6 address specified in the [**if-match destination**](cmdqueryname=if-match+destination) command, run the [**route match-destination**](cmdqueryname=route+match-destination) command.
      * To set a traffic filtering rule that is based on a source IP address, run the [**if-match source**](cmdqueryname=if-match+source) *ipv6-address* { *mask* | *mask-length* } command.
      * To set a filtering rule based on the port number, run the [**if-match port**](cmdqueryname=if-match+port) *operator* *port* command.
      * To set a traffic filtering rule that is based on a source port number, run the [**if-match source-port**](cmdqueryname=if-match+source-port) *operator* *port* command.
      * To set a traffic filtering rule that is based on a destination port number, run the [**if-match destination-port**](cmdqueryname=if-match+destination-port) *operator* *port* command.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        [**if-match port**](cmdqueryname=if-match+port) and [**if-match destination-port**](cmdqueryname=if-match+destination-port) or [**if-match source-port**](cmdqueryname=if-match+source-port) are mutually exclusive.
      * To set a traffic filtering rule that is based on the protocol used to carry traffic, run the [**if-match protocol**](cmdqueryname=if-match+protocol) *operator* *protocol* command.
      * To set a traffic filtering rule that is based on a service type, run the [**if-match dscp**](cmdqueryname=if-match+dscp) *operator* *dscp* command.
      * To set a traffic filtering rule that is based on a TCP flag value, run the [**if-match tcp-flags**](cmdqueryname=if-match+tcp-flags+match+not) { **match** | **not** } *tcp-flags* command.
        
        Network attackers may send a large number of invalid TCP packets to attack network devices. To control the unidirectional traffic of TCP packets for the sake of communication security, you can run the [**if-match tcp-flags**](cmdqueryname=if-match+tcp-flags) command to match BGP VPN IPv6 Flow Specification routes against a specified TCP flag value. The traffic behavior specified in the apply clause applies to the traffic that matches the TCP flag value.
      * To set a traffic filtering rule that is based on a packet fragmentation type, run the [**if-match fragment-type**](cmdqueryname=if-match+fragment-type+match+not) { **match** | **not** } *fragment-type-name* command.
      * To set a traffic filtering rule that is based on an ICMP packet code, run the [**if-match icmp-code**](cmdqueryname=if-match+icmp-code) *operator* *icmp-code* command.
      * To set a traffic filtering rule that is based on an ICMP packet type, run the [**if-match icmp-type**](cmdqueryname=if-match+icmp-type+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *icmp-type* command.
      * To set a traffic filtering rule that is based on the length of the message carrying the BGP IPv6 VPN Flow Specification route, run the [**if-match packet-length**](cmdqueryname=if-match+packet-length+greater-than+less-than+equal) { **greater-than** | **less-than** | **equal** } *packet-length-value* command.
   4. Run the following command as required to configure actions for apply clauses:
      
      
      * To discard the matching traffic, run the [**apply deny**](cmdqueryname=apply+deny) command.
      * To redirect the matching traffic to the traffic cleaning device or blackhole, run the [**apply redirect**](cmdqueryname=apply+redirect+vpn-target) **vpn-target** *vpn-target-import* command.
      * To re-mark the service class of the matching traffic, run the [**apply remark-dscp**](cmdqueryname=apply+remark-dscp) command.
      * To limit the rate of the matching traffic, run the [**apply traffic-rate**](cmdqueryname=apply+traffic-rate) command.
      * To implement sampling for the matching traffic, run the [**apply traffic-action sample**](cmdqueryname=apply+traffic-action+sample) command.
        
        You can run the [**apply traffic-action sample**](cmdqueryname=apply+traffic-action+sample) command for a BGP IPv6 VPN Flow Specification route to sample the traffic that matches the specified filtering rules. Through sampling, abnormal traffic can be identified and filtered out, which protects the attacked device and improves network security.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The [**apply deny**](cmdqueryname=apply+deny) and [**apply traffic-rate**](cmdqueryname=apply+traffic-rate) commands are mutually exclusive.
      
      If a configured BGP IPv6 VPN Flow Specification route does not need to take effect locally, you can run the [**routing-table rib-only**](cmdqueryname=routing-table+rib-only+route-policy) [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command to disable the device from delivering the BGP IPv6 VPN Flow Specification route to the FES forwarding table.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Establish a BGP VPNv6 Flow Specification peer relationship.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
      
      
      
      A BGP-VPN instance is created, and its view is displayed.
   4. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**as-number**](cmdqueryname=as-number) *as-number*
      
      
      
      An IP address and AS number are specified for the peer.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      The BGP view is displayed.
   6. Run [**ipv6-flow vpnv6**](cmdqueryname=ipv6-flow+vpnv6)
      
      
      
      The BGP-Flow VPNv6 address family is enabled, and its view is displayed.
   7. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**enable**](cmdqueryname=enable)
      
      
      
      The BGP VPNv6 Flow Specification peer relationship is enabled.
      
      
      
      After the BGP VPNv6 Flow Specification peer relationship is established in the BGP-Flow VPNv6 address family view, the BGP IPv6 VPN Flow Specification route generated by the traffic analysis server is imported automatically to the BGP routing table and then sent to the peer.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
3. (Optional) Configure a Flow RR.
   
   
   
   Before configuring a Flow RR, establish a BGP VPNv6 Flow Specification peer relationship between the Flow RR and device on which the BGP IPv6 VPN Flow Specification route is generated, and between the Flow RR and each network ingress.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv6-flow vpnv6**](cmdqueryname=ipv6-flow+vpnv6)
      
      
      
      The BGP-Flow VPNv6 address family is enabled, and its view is displayed.
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
4. (Optional) Disable BGP Flow Specification protection.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**flowspec protocol-protect**](cmdqueryname=flowspec+protocol-protect+ipv4+ipv6+disable) { **ipv4** | **ipv6** } **disable**
      
      
      
      BGP Flow Specification protection is disabled.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
5. (Optional) Enable the DSCP-based BGP IPv6 Flow Specification traffic filtering rule.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**flowspec allow ipv6 dscp**](cmdqueryname=flowspec+allow+ipv6+dscp)
      
      
      
      The DSCP-based BGP IPv6 Flow Specification traffic filtering rule is enabled.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
6. (Optional) Enable BGP Flow Specification to match inner packet information about the packets that leave an SRv6 TE Policy or SRv6 BE egress.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**flowspec match srv6-inner-ip enable**](cmdqueryname=flowspec+match+srv6-inner-ip+enable)
      
      
      
      BGP Flow Specification is enabled to match inner packet information about the packets that leave an SRv6 TE Policy or SRv6 BE egress.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
7. (Optional) Enable BGP IPv6 Flow Specification to match the internal protocol number in the header of an IPv6 fragment.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**flowspec match ipv6 fragment-inner-protocol enable**](cmdqueryname=flowspec+match+ipv6+fragment-inner-protocol+enable)
      
      
      
      BGP IPv6 Flow Specification is enabled to match the internal protocol number in the header of an IPv6 fragment.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the [**display bgp flow**](cmdqueryname=display+bgp+flow+vpnv6+all+peer+verbose) **vpnv6 all** **peer** [ [ *ipv4-address* ] **verbose** ] command to check information about all BGP VPNv6 Flow Specification peers.
* Run the [**display bgp flow**](cmdqueryname=display+bgp+flow+vpnv6+all+route-distinguisher+routing-table) **vpnv6** { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** [ *reindex* ] command to check information about all BGP VPNv6 Flow Specification routes or about the BGP VPNv6 Flow Specification routes with a specified RD.
* Run the [**display bgp flow**](cmdqueryname=display+bgp+flow+vpnv6+all+route-distinguisher+routing-table) **vpnv6** { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** **statistics** command to check statistics about all BGP VPNv6 Flow Specification routes or about the BGP VPNv6 Flow Specification routes with a specified RD.
* Run the [**display flowspec**](cmdqueryname=display+flowspec+ipv6+rule+slot) **ipv6** **rule** *reindex-value* **slot** *slot-id* command to check information about combined rules in the BGP IPv6 Flow Specification route rule table.
* Run the [**display flowspec**](cmdqueryname=display+flowspec+ipv6+rule+statistics+slot) **ipv6** **rule statistics slot** *slot-id* command to check statistics about the rules for BGP IPv6 Flow Specification routes to take effect.
* Run the [**display flowspec resource rule**](cmdqueryname=display+flowspec+resource+rule+ipv4+ipv6+slot) { **ipv4** | **ipv6** } [ **slot** *slot-id* ] command to check the resource usage information about BGP Flow Specification route rules.