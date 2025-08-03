Configuring BGP to Preferentially Select the Prefix Routes That Are Learned from VPNv4, VPNv6, or EVPN Peers and Are Leaked to a VPN Instance
=============================================================================================================================================

Configuring_BGP_to_Preferentially_Select_the_Prefix_Routes_That_Are_Learned_from_VPNv4,_VPNv6,_or_EVPN_Peers_and_Are_Leaked_to_a_VPN_Instance

#### Usage Scenario

When VPNv4 and EVPN L3VPNv4 services, or VPNv6 and EVPN L3VPNv6 services coexist, a BGP IPv4/IPv6 VPN instance may have two routes with the same prefix but different VPN address family types, with one route learned from a VPNv4 or VPNv6 peer and leaked to a VPN instance, and the other learned from an EVPNv4 or EVPNv6 peer and leaked to a VPN instance. In this case, you can configure BGP to preferentially select either type of the preceding routes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
   
   
   
   A VPN instance is created and its view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
   
   
   
   The VPN instance IPv4 address family is enabled, and the view of this address family is displayed.
   
   Or run [**ipv6-family**](cmdqueryname=ipv6-family)
   
   The VPN instance IPv6 address family is enabled, and the view of this address family is displayed.
4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
   
   
   
   An RD is configured.
5. Run [**vpn-target**](cmdqueryname=vpn-target+both+export-extcommunity+import-extcommunity) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
   
   
   
   VPN targets are configured.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   The VPN instance view is displayed.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   The system view is displayed.
8. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
9. Run [**ipv4-family**](cmdqueryname=ipv4-family+vpn-instance) **vpn-instance** *vpn-instance-name*
   
   
   
   The BGP VPN instance IPv4 address family view is displayed.
   
   Or run [**ipv6-family**](cmdqueryname=ipv6-family+vpn-instance) **vpn-instance** *vpn-instance-name*
   
   The BGP VPN instance IPv6 address family view is displayed.
10. Perform the following configurations as required:
    
    
    * To configure BGP to compare the VPN address family types of routes when selecting the optimal route and preferentially select the IPv4 prefix routes leaked from VPNv4 over those leaked from EVPNv4, run the [**bestroute address-family-priority vpnv4 high-level**](cmdqueryname=bestroute+address-family-priority+vpnv4+high-level) command in the BGP VPN instance IPv4 address family view.
    * To configure BGP to compare the VPN address family types of routes when selecting the optimal route and preferentially select the IPv4 prefix routes leaked from EVPNv4 over those leaked from VPNv4, run the [**bestroute address-family-priority evpnv4 high-level**](cmdqueryname=bestroute+address-family-priority+evpnv4+high-level) command in the BGP VPN instance IPv4 address family view.
    * To configure BGP to compare the VPN address family types of routes when selecting the optimal route and preferentially select the IPv6 prefix routes leaked from VPNv6 over those leaked from EVPNv6, run the [**bestroute address-family-priority vpnv6 high-level**](cmdqueryname=bestroute+address-family-priority+vpnv6+high-level) command in the BGP VPN instance IPv6 address family view.
    * To configure BGP to compare the VPN address family types of routes when selecting the optimal route and preferentially select the IPv6 prefix routes leaked from EVPNv6 over those leaked from VPNv6, run the [**bestroute address-family-priority evpnv6 high-level**](cmdqueryname=bestroute+address-family-priority+evpnv6+high-level) command in the BGP VPN instance IPv6 address family view.![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    If there are a large number of BGP IPv4 VPN instances and the [**bestroute address-family-priority**](cmdqueryname=bestroute+address-family-priority+vpnv4+evpnv4+high-level) { **vpnv4** | **evpnv4** } **high-level** command needs to be run for each instance, you can run the [**bestroute address-family-priority**](cmdqueryname=bestroute+address-family-priority+vpnv4+evpnv4) { **vpnv4** | **evpnv4** } **high-level all-vpn-instance** command instead to simplify the configuration because the latter command takes effect for all BGP IPv4 VPN address families.
    
    If there are a large number of BGP IPv6 VPN instances and the [**bestroute address-family-priority**](cmdqueryname=bestroute+address-family-priority+vpnv6+evpnv6+high-level) { **vpnv6** | **evpnv6** } **high-level** command needs to be run for each instance, you can run the [**bestroute address-family-priority**](cmdqueryname=bestroute+address-family-priority+vpnv6+evpnv6+high-level) { **vpnv6** | **evpnv6** } **high-level** **all-vpn-instance** command instead to simplify the configuration because the latter command takes effect for all BGP IPv6 VPN address families.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

* Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4+vpn-instance+routing-table) **vpn-instance** *vpn-instance-name* **routing-table***ipv4-address* [ *mask-length* | *mask* ] command to check the BGP routes of an IPv4 VPN instance.
* Run the [**display bgp vpnv6**](cmdqueryname=display+bgp+vpnv6+vpn-instance+routing-table) **vpn-instance** *vpn-instance-name* **routing-table***ipv6-address* [ *prefix-length* ] command to check the BGP routes of an IPv6 VPN instance.