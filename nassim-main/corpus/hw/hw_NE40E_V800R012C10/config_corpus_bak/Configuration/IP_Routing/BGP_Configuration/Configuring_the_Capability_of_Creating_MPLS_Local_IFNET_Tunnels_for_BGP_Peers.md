Configuring the Capability of Creating MPLS Local IFNET Tunnels for BGP Peers
=============================================================================

The MPLS local IFNET tunnels created by BGP peers can be used to carry BGP LSP traffic.

#### Usage Scenario

You can enable BGP peers to establish MPLS local IFNET tunnels to carry BGP LSP traffic.


#### Pre-configuration Tasks

Before configuring the capability of creating MPLS local IFNET tunnels for BGP peers, complete the following tasks:

* [Configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).

#### Procedure

1. Run **[**system-view**](cmdqueryname=system-view)**
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**undo peer**](cmdqueryname=undo+peer+mpls-local-ifnet+disable) { *peerGroupName* | *peerIpv4Addr* } **mpls-local-ifnet** **disable**
   
   
   
   The capability of creating MPLS local IFNET tunnels is enabled for the specified IBGP peer.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   MPLS local IFNET tunnels can be established between IBGP peers only in the BGP-IPv4 unicast address family and BGP unicast labeled address family. To enable the capability of creating MPLS local IFNET tunnels to take effect in the BGP-IPv4 unicast address family, you also need to run the [**peer label-route-capability**](cmdqueryname=peer+label-route-capability) command in the BGP-IPv4 unicast address family view to enable the function of sending or receiving labeled routes.
4. Run **[**quit**](cmdqueryname=quit)**
   
   
   
   The system view is displayed.
5. (Optional) Configure MPLS local IFNET traffic statistics collection.
   1. Run the [**mpls**](cmdqueryname=mpls) command to enable MPLS globally and enter the MPLS view.
   2. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   3. Run the [**mpls traffic-statistics**](cmdqueryname=mpls+traffic-statistics) command to enable MPLS traffic statistics collection globally and enter the traffic statistics collection view.
   4. Run the [**bgp host**](cmdqueryname=bgp+host+ip-prefix+ip-prefix) [ **ip-prefix** *ip-prefix-name* ] command to enable MPLS local IFNET traffic statistics collection. If you want statistics to be collected based on an IP prefix list (specified by **ip-prefix**), ensure that the IP prefix list has been created using the [**ip ip-prefix**](cmdqueryname=ip+ip-prefix) command.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display mpls lsp protocol bgp local-ifnet traffic-statistics outbound**](cmdqueryname=display+mpls+lsp+protocol+bgp+local-ifnet+traffic-statistics+outbound) command to query statistics about outgoing traffic in MPLS local IFNET tunnels.