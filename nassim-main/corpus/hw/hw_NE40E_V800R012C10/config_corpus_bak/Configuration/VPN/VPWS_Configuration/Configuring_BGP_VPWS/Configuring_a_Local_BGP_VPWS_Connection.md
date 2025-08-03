Configuring a Local BGP VPWS Connection
=======================================

If two CEs connect to the same PE, you can configure a local BGP VPWS connection for the two CEs to communicate.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172369809__fig_dc_vrp_vpws_cfg_605501), CE1 and CE2 connect to the same PE. A local BGP VPWS connection needs to be established between CE1 and CE2 for them to communicate. After the connection is established, the PE can function like a Layer 2 switch to directly transmit packets, without using any static LSP.

**Figure 1** Configuring a local BGP VPWS connection  
![](images/fig_dc_vrp_vpws_cfg_605501.png)  


#### Procedure

1. Configure MPLS L2VPN.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
      
      
      
      MPLS L2VPN is configured.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Configure a local VPWS connection.
   1. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn) *l2vpn-name* [ **encapsulation** *encapsulation-type* [ **control-word** | **no-control-word** ] ]
      
      
      
      A BGP VPWS instance is created, and its view is displayed.
      
      
      
      If heterogeneous interworking is required, specify *encapsulation-type* as **ip-interworking** for successful PW establishment.
   2. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      
      
      An RD is configured for the L2VPN instance.
   3. (Optional) Run [**mtu**](cmdqueryname=mtu) *mtu-value*
      
      
      
      An MTU is configured for the MPLS L2VPN instance.
      
      
      
      The MTU size determines the maximum packet size allowed by a VPWS network. If the MTU exceeds the maximum packet size allowed by a VPWS network or an intermediate node (P), packet fragmentation or even drop will occur, affecting network transmission. The MTU is one of the VPWS negotiation parameters. If the MTUs of the same L2VPN instance on the endpoint PEs are different, the two PEs cannot exchange reachability information or establish a PW. An appropriate MTU must be set for an L2VPN instance based on the MTU of the interface bound to the L2VPN instance. Specifically, the MTU of an MPLS L2VPN instance must be smaller than or equal to the MTU of the interface bound to the MPLS L2VPN instance.
   4. (Optional) Run [**ignore-mtu-match**](cmdqueryname=ignore-mtu-match)
      
      
      
      The current device is configured not to perform the MTU match check.
      
      
      
      If the MTUs of the same L2VPN instance on the two endpoint PEs do not match, the VC cannot go up. If devices provided by other vendors do not support the MTU match check function provided by the MPLS L2VPN instance, run the [**ignore-mtu-match**](cmdqueryname=ignore-mtu-match) command to disable this function.
   5. Run [**ce**](cmdqueryname=ce) *ce-name* [ **id** *ce-id* [ **range** *ce-range* ] [ **default-offset** *ce-offset* ] ]
      
      
      
      A CE is created in the L2VPN instance.
   6. Run [**connection**](cmdqueryname=connection) [ **ce-offset** *ce-offset-id* ] **interface** *interface-type* *interface-number* [ **tunnel-policy** *tunnel-policy-name* ] [ **raw** | **tagged** ] [ **secondary** ]
      
      
      
      A local BGP VPWS connection is configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.