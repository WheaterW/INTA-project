Configuring Dynamic BGP VPNv6 Flow Specification
================================================

Dynamic BGP VPNv6 Flow Specification allows BGP VPNv6 Flow Specification routes to be transmitted and traffic filtering policies to be generated. The policies improve security of devices in VPNs.

#### Usage Scenario

When deploying dynamic BGP VPNv6 Flow Specification, a BGP VPNv6 Flow Specification peer relationship needs to be established between the traffic analysis server and each ingress of the network to transmit BGP VPNv6 Flow Specification routes.

In an AS with multiple ingresses, a Flow RR can be deployed to reduce the number of BGP VPNv6 Flow Specification peer relationships and save network resources.


#### Pre-configuration Tasks

Before configuring dynamic BGP VPNv6 Flow Specification, complete the following tasks:

* [Configure BGP peer relationships](dc_vrp_bgp_cfg_3006.html).

#### Procedure

1. Establish a BGP VPNv6 Flow Specification peer relationship.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** *as-number*
      
      
      
      The IP address of a peer and the number of the AS where the peer resides are specified.
   4. Run [**ipv6-flow vpnv6**](cmdqueryname=ipv6-flow+vpnv6)
      
      
      
      The BGP-Flow VPNv6 address family is enabled, and the BGP-Flow VPNv6 address family view is displayed.
   5. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**enable**](cmdqueryname=enable)
      
      
      
      A BGP VPNv6 Flow Specification peer is specified.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. (Optional) Configure a Flow RR.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv6-flow vpnv6**](cmdqueryname=ipv6-flow+vpnv6)
      
      
      
      The BGP-Flow VPNv6 address family is enabled, and the BGP-Flow VPNv6 address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**reflect-client**](cmdqueryname=reflect-client)
      
      
      
      A Flow RR is configured, and clients are specified for it.
      
      
      
      The Router on which the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command is run functions as a Flow RR, and the network ingress and traffic analysis server function as clients.
   5. (Optional) Run [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients)
      
      
      
      Route reflection between clients through the RR is disabled.
      
      
      
      If the clients of a Flow RR are fully meshed, you can run the [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command on the Flow RR to disable route reflection between clients through the RR, which reduces costs.
   6. (Optional) Run [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) { *cluster-id-value* | *cluster-id-ipv4* }
      
      
      
      A cluster ID is configured for the Flow RR.
      
      
      
      If a cluster has multiple flow RRs, run this command to set the same *cluster-id* for these RRs.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) command is applicable only to Flow RRs.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
3. (Optional) Disable BGP Flow Specification protection.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**flowspec protocol-protect**](cmdqueryname=flowspec+protocol-protect+ipv4+ipv6+disable) { **ipv4** | **ipv6** } **disable**
      
      
      
      BGP Flow Specification protection is disabled.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
4. (Optional) Enable the DSCP-based BGP IPv6 Flow Specification traffic filtering rule.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**flowspec allow ipv6 dscp**](cmdqueryname=flowspec+allow+ipv6+dscp)
      
      
      
      The DSCP-based BGP IPv6 Flow Specification traffic filtering rule is enabled.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
5. (Optional) Enable BGP Flow Specification to match inner packet information about the packets that leave an SRv6 TE Policy or SRv6 BE egress.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**flowspec match srv6-inner-ip enable**](cmdqueryname=flowspec+match+srv6-inner-ip+enable)
      
      
      
      BGP Flow Specification is enabled to match inner packet information about the packets that leave an SRv6 TE Policy or SRv6 BE egress.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
6. (Optional) Enable BGP IPv6 Flow Specification to match the internal protocol number in the header of an IPv6 fragment.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**flowspec match ipv6 fragment-inner-protocol enable**](cmdqueryname=flowspec+match+ipv6+fragment-inner-protocol+enable)
      
      
      
      BGP IPv6 Flow Specification is enabled to match the internal protocol number in the header of an IPv6 fragment.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the [**display bgp flow**](cmdqueryname=display+bgp+flow+vpnv6+all+peer+verbose) **vpnv6 all** **peer** [ [ *ipv4-address* ] **verbose** ] command to check information about all BGP IPv6 VPN Flow Specification peers and BGP VPNv6 Flow Specification peers.
* Run the [**display bgp flow**](cmdqueryname=display+bgp+flow+vpnv6+all+route-distinguisher+routing-table) **vpnv6** { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** [ *reindex* ] command to check information about all BGP IPv6 VPN Flow Specification routes and BGP VPNv6 Flow Specification routes or the BGP IPv6 VPN Flow Specification routes and BGP VPNv6 Flow Specification routes with a specified RD.
* Run the [**display bgp flow**](cmdqueryname=display+bgp+flow+vpnv6+all+route-distinguisher+routing-table) **vpnv6** { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** **statistics** command to check statistics about all BGP IPv6 VPN Flow Specification routes and BGP VPNv6 Flow Specification routes or the BGP IPv6 VPN Flow Specification routes and BGP VPNv6 Flow Specification routes with a specified RD.
* Run the [**display flowspec**](cmdqueryname=display+flowspec+ipv6+rule+slot) **ipv6** **rule** *reindex-value* **slot** *slot-id* command to check information about combined rules in the BGP IPv6 Flow Specification route rule table.
* Run the [**display flowspec**](cmdqueryname=display+flowspec+ipv6+rule+statistics+slot) **ipv6** **rule statistics slot** *slot-id* command to check statistics about the rules for BGP IPv6 Flow Specification routes to take effect.
* Run the [**display flowspec resource rule**](cmdqueryname=display+flowspec+resource+rule+ipv4+ipv6+slot) { **ipv4** | **ipv6** } [ **slot** *slot-id* ] command to check the resource usage information about BGP Flow Specification route rules.