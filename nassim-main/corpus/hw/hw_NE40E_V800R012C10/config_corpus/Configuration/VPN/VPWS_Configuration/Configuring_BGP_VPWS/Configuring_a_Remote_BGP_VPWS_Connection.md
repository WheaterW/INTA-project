Configuring a Remote BGP VPWS Connection
========================================

If two CEs connect to different PEs, you can configure a remote BGP VPWS connection for the two CEs to communicate.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172369812__fig_dc_vrp_vpws_cfg_605601), CEs connect to different PEs. A remote BGP VPWS connection needs to be established between PEs for the two CEs to communicate.

**Figure 1** Network diagram of configuring a remote BGP VPWS connection  
![](images/fig_dc_vrp_vpws_cfg_605601.png)

#### Procedure

1. Configure MPLS L2VPN.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
      
      
      
      MPLS L2VPN is configured.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Enable BGP peers to exchange VPWS information.
   1. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   2. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *peer-as*
      
      
      
      A BGP peer and its AS number are specified.
   3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface** *interface-type* *interface-number*
      
      
      
      The source interface for sending BGP packets is specified.
   4. Run [**l2vpn-ad-family**](cmdqueryname=l2vpn-ad-family)
      
      
      
      The L2VPN-AD address family view is displayed.
   5. (Optional) Run [**vpn-orf enable**](cmdqueryname=vpn-orf+enable)
      
      
      
      ORF is enabled.
   6. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
      
      
      
      The route exchange capability is enabled.
   7. Run [**signaling vpws**](cmdqueryname=signaling+vpws) or [**peer**](cmdqueryname=peer) *ip-address* **signaling** **vpws**
      
      
      
      BGP VPWS is enabled.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Configure a remote VPWS connection.
   1. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn) *l2vpn-name* [ **encapsulation** *encapsulation-type* [ **control-word** | **no-control-word** ] ]
      
      
      
      A BGP VPWS VPN instance is created, and the MPLS L2VPN instance view is displayed.
      
      
      
      If heterogeneous interworking is required, specify *encapsulation-type* as **ip-interworking** for successful PW establishment.
   2. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      
      
      An RD is configured for the MPLS L2VPN instance.
   3. (Optional) Run [**mtu**](cmdqueryname=mtu) *mtu-value*
      
      
      
      An MTU is configured for the MPLS L2VPN instance.
      
      
      
      The MTU size determines the maximum packet size allowed by a VPWS network. If the MTU exceeds the maximum packet size allowed by a VPWS network or an intermediate node (P), packet fragmentation or even drop will occur, affecting network transmission. The MTU is one of the VPWS negotiation parameters. If the MTUs of the same MPLS L2VPN instance on the endpoint PEs are different, the two PEs cannot exchange reachability information or establish a PW. An appropriate MTU must be set for an MPLS L2VPN instance based on the MTU of the interface bound to the instance. Specifically, the MTU of an MPLS L2VPN instance must be smaller than or equal to the MTU of the interface bound to the instance.
   4. (Optional) Run [**ignore-mtu-match**](cmdqueryname=ignore-mtu-match)
      
      
      
      The current device is configured not to perform the MTU match check for the MPLS L2VPN instance.
      
      
      
      If the MTUs of the same MPLS L2VPN instance on the two endpoint PEs do not match, the VC cannot go up. If devices provided by other vendors do not support the MTU match check function provided by the MPLS L2VPN instance, run the **ignore-mtu-match** command to disable this function.
   5. Run [**vpn-target**](cmdqueryname=vpn-target) { *vpn-target* } & <1-16> [ **both** | **export-extcommunity** | **import-extcommunity** ]
      
      
      
      VPN targets are configured.
   6. Run [**ce**](cmdqueryname=ce) *ce-Name* [ **id** *ce-id* [ **range** *ce-range* ] [ **default-offset** *ce-offset* ] ]
      
      
      
      A CE is created in the MPLS L2VPN instance.
   7. Run [**connection**](cmdqueryname=connection) [ **ce-offset** *ce-offset-id* ] **interface** **interface-type** *interface-number* [ **tunnel-policy** *tunnel-policy-name* ] [ **raw** | **tagged** ] [ **secondary** ]
      
      
      
      A remote BGP VPWS connection is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.