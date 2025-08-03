Configuring a VPN Instance
==========================

A VPN instance of the IPv6 address family can be configured to manage IPv6 VPN routes.

#### Context

An instance is created to comprise the VPN forwarding information for each VPN in a BGP/MPLS IPv6 VPN. This instance is called a VPN instance or a VPN routing and forwarding (VRF) table. In related standards (BGP/MPLS IP VPNs), the VPN instance is also called a per-site forwarding table. VPN instances must be created in all BGP/MPLS IPv6 VPN solutions.

In a 6VPE scenario, both IPv4 and IPv6 address families must be enabled in a VPN instance. The IPv4 routing table of the VPN instance manages routes used to establish VPN LDP LSPs, whereas the IPv6 routing table of the VPN instance manages received VPN IPv6 routes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
   
   
   
   A VPN instance is created, and its view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A VPN instance name is case sensitive. For example, "vpn1" and "VPN1" are different VPN instances.
3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
   
   
   
   A description is configured for the VPN instance.
   
   Similar to a host name or an interface description, the VPN instance description helps users memorize the VPN instance.
4. Run [**ipv4-family**](cmdqueryname=ipv4-family)
   
   
   
   The IPv4 address family is enabled for the VPN instance, and the VPN instance IPv4 address family view is displayed.
   
   Configurations in a VPN instance can be performed only after an address family is enabled for the VPN instance based on the advertised route and forwarding data type.
5. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
   
   
   
   An RD is configured for the VPN instance IPv4 address family.
   
   
   
   A VPN instance IPv4 address family takes effect only after being assigned an RD. The RDs of different VPN instance IPv4 address families on a PE must be different.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If you configure an RD for the VPN instance IPv4 address family in the created VPN instance view, the VPN instance IPv4 address family is automatically enabled, and its view is automatically displayed.
6. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
   
   
   
   One or multiple VPN targets are configured for the VPN instance IPv4 address family.
   
   A VPN target is a BGP extended community attribute. It is used to control the acceptance and advertisement of VPN routing information. A maximum of eight VPN targets can be configured using the **vpn-target** command. If you want to configure multiple VPN targets in the VPN instance IPv4 address family view, run the **vpn-target** command multiple times.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit from the VPN instance IPv4 address family view.
8. Run [**ipv6-family**](cmdqueryname=ipv6-family)
   
   
   
   The IPv6 address family is enabled for the VPN instance, and the VPN instance IPv6 address family view is displayed.
   
   VPN instances support both the IPv4 and IPv6 address families. Configurations in a VPN instance can be performed only after an address family is enabled for the VPN instance based on the advertised route and forwarding data type.
9. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
   
   
   
   An RD is configured for the VPN instance IPv6 address family.
   
   
   
   A VPN instance IPv6 address family takes effect only after having an RD configured. The RDs of different VPN instance IPv6 address families on a PE must be different.
10. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
    
    
    
    One or multiple VPN targets are configured for the VPN instance IPv6 address family.
    
    A VPN target is a BGP extended community attribute. They are used to control the import and export of VPN-IPv6 routes. A maximum of eight VPN targets can be configured using the **vpn-target** command. If you want to configure more VPN targets in the VPN instance IPv6 address family view, run the **vpn-target** command more than once.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Follow-up Procedure

You can configure a route-policy in a VPN instance to implement functions, such as filtering routes and limiting the number of allowed routes. For configuration details, see [Configuring an IPv4 VPN Instance](dc_vrp_mpls-l3vpn-v4_cfg_0155.html) and [Configuring an IPv6 VPN Instance](dc_vrp_mpls-l3vpn-v6_cfg_2058.html).