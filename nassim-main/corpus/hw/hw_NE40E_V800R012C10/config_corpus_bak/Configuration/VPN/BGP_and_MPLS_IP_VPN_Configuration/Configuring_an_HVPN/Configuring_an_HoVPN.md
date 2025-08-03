Configuring an HoVPN
====================

On an HoVPN, a UPE only needs to obtain a default route from an SPE. This implementation mechanism reduces the route storage space required on a UPE.

#### Context

HoVPN networking requires the following configurations:

* Configure a VPN instance on each UPE, SPE, and NPE. For configuration details, see [Configuring a VPN Instance](dc_vrp_mpls-l3vpn-v4_cfg_0155.html).![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  According to relevant standards, the VPN instance status obtained from an NMS is Up only if at least one interface bound to the VPN instance is Up. On an HoVPN, VPN instances on SPEs are not bound to interfaces. As a result, the VPN instance status obtained from an NMS is always Down. To solve this problem, run the [**transit-vpn**](cmdqueryname=transit-vpn) command in the VPN instance view or VPN instance IPv4 address family view of an SPE. Then, the VPN instance status obtained from an NMS is always Up, no matter whether the VPN instance is bound to interfaces.
* Configure an MP-BGP peer relationship between each SPE and NPE. This configuration is similar to configuring an MP-IBGP peer relationship between PEs on a BGP/MPLS IP VPN. For more information, see [Establishing MP-IBGP Peer Relationships Between PEs](dc_vrp_mpls-l3vpn-v4_cfg_0157.html).
* Configure routing protocols for NPEs and UPEs to exchange routes with CEs. This configuration is similar to configuring PEs and CEs to exchange routes on a BGP/MPLS IP VPN. For more information, see [Configuring Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v4_cfg_0158.html).
* Configure an MP-BGP peer relationship between each UPE and SPE. Configure the SPE to send the default route to the UPE in either of the following modes:
  + Route filtering mode: You can configure the default static route and routing policy to enable the SPE to send the default route to the UPE.
  + Command control mode: You can run the [**peer default-originate vpn-instance**](cmdqueryname=peer+default-originate+vpn-instance) command to enable the SPE to automatically generate the default route and send it to the UPE.
  
  The default route generated using the [**peer default-originate vpn-instance**](cmdqueryname=peer+default-originate+vpn-instance) command cannot be associated with an interface. When the primary link connecting the SPE to the UPE fails, the default route may be sent to the UPE over another interface, which affects network reaction sensitivity to faults. Therefore, the route filtering mode is recommended.


#### Procedure

1. Configure a UPE to establish an MP-BGP peer relationship with an SPE.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **as-number** *as-number* command to specify the SPE as a BGP peer of the UPE.
   4. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** command to enter the BGP-VPNv4 address family view.
   5. Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **enable** command to enable the function to exchange BGP-VPNv4 routes with the specified peer.
   6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Configure the SPE to send the default or summary route to the UPE. 
   
   
   * Configure the SPE to send the default route to the UPE.
     
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* **0.0.0.0** { **0.0.0.0** | **0** }{ *interface-type* *interface-number* } [ *nexthop-address* ] [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ] command to create a static default VPN IPv4 route.
     3. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
     4. Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **as-number** *as-number* command to specify the UPE as a BGP peer of the SPE.
     5. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** command to enter the BGP-VPNv4 address family view.
     6. Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **upe** command to specify the UPE as a lower-level PE of the SPE.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        This step can be performed only if a VPNv4 peer relationship has been established between the SPE and UPE.
     7. Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
     8. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
     9. Run [**network**](cmdqueryname=network) **0.0.0.0** [ **0.0.0.0** | **0** ] [ **route-policy** *route-policy-name* ] command to import the default route into the IPv4 VPN instance routing table.
     10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   * Configure the SPE to send summary routes to the UPE.
     
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
     3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
     4. Run the [**aggregate**](cmdqueryname=aggregate) *ipv4-address* { *mask* | *mask-length* } [ **as-set** | **attribute-policy** *route-policy-name1* | **detail-suppressed** | **origin-policy** *route-policy-name2* | **suppress-policy** *route-policy-name3* ] \* command to configure route summarization.
     5. Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
     6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     7. Run the [**ip ip-prefix**](cmdqueryname=ip+ip-prefix) *ip-prefix-name* [ **index** *index-number* ] { **permit** | **deny** } *ip-address* *mask-length* [ **greater-equal** *greater-equal-value* ] [ **less-equal** *less-equal-value* ] command to configure an IPv4 prefix list.
     8. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
     9. Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **as-number** *as-number* command to specify the UPE as a BGP peer of the SPE.
     10. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** command to enter the BGP-VPNv4 address family view.
     11. Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **ip-prefix** *ip-prefix-name* **export** command to configure the SPE to advertise filtered routes to the UPE.
     12. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
3. (Optional) Configure one-label-per-next-hop label distribution on the SPE. 
   
   
   
   In an HoVPN scenario, if an SPE needs to send large numbers of VPNv4 routes but the MPLS labels are inadequate, configure one-label-per-next-hop label distribution on the SPE.
   
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** command to enter the BGP-VPNv4 address family view.
   4. Run the [**apply-label per-nexthop**](cmdqueryname=apply-label+per-nexthop) command to enable one-label-per-next-hop label distribution for VPNv4 routes on the SPE.
      
      ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
      
      After one-label-per-next-hop label distribution is enabled or disabled on an SPE, the labels assigned by the SPE to routes change. As a result, temporary packet loss occurs.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.