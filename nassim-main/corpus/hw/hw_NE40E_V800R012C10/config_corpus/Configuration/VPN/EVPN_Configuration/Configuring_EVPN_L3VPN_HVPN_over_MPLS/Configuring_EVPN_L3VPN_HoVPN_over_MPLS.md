Configuring EVPN L3VPN HoVPN over MPLS
======================================

On an EVPN L3VPN HoVPN over MPLS network, the UPE only needs to obtain a default route from the SPE. This implementation reduces the route storage space required on the UPE while ensuring route isolation.

#### Context

In EVPN L3VPN HoVPN over MPLS networking, you need to perform the following configurations:

1. [Create a VPN instance](dc_vrp_evpn_cfg_0039.html) on the UPE, SPE, and NPE. Then bind access-side interfaces to an [IPv4 VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0156.html) or [IPv6 VPN instance](dc_vrp_mpls-l3vpn-v6_cfg_2059.html) on the UPE and NPE. ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   According to related standards, the VPN instance status obtained through an NMS can be up only when at least one interface bound to the VPN instance is up. In an HoVPN scenario, an SPE does not require any interface to be bound to a VPN instance. Consequently, the VPN instance status obtained by an NMS is down according to the standards, which is opposite to the actual VPN instance status. In this case, you can run the [**transit-vpn**](cmdqueryname=transit-vpn) command in the VPN instance view or VPN instance IPv4/IPv6 address family view on the SPE. Then, the VPN instance status obtained by the NMS remains up, regardless of the binding status between the VPN instance and interface.
2. Configure BGP EVPN peer relationships between the UPE and SPE and between the SPE and NPE. For details, see [Configuring BGP EVPN Peer Relationships](dc_vrp_evpn_cfg_0006.html).
3. Configure routing protocols for the NPE and UPE to exchange routes with connected CEs. This configuration is similar to configuring the PE and CE to exchange routes on a basic BGP/MPLS IP VPN. For details, see [Configuring Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v4_cfg_0158.html) or [Configuring IPv6 Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v6_cfg_2061.html).
4. Configure the SPE to advertise only default or summary routes to the UPE. For details, see [Procedure](#EN-US_TASK_0172370557__process1).


#### Procedure

1. Configure the SPE to advertise only default or summary routes to the UPE.
   
   
   * Configure the SPE to advertise the default route to the UPE.
     
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-instance-name* **0.0.0.0** { **0.0.0.0** | **0** } { *nexthop-address* | *interface-type* *interface-number* [ *nexthop-address* ] } or [**ipv6 route-static vpn-instance**](cmdqueryname=ipv6+route-static+vpn-instance) *vpn-instance-name* **0::0** **0** { *nexthop-ipv6-address* | *interface-type* *interface-number* [ *nexthop-ipv6-address* ] } command to create the default VPN IPv4/IPv6 static route.
     3. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
     4. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* or [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv4/IPv6 address family view.
     5. Run the [**network**](cmdqueryname=network) **0.0.0.0** [ **0.0.0.0** | **0** ] [ **route-policy** *route-policy-name* ] or [**network**](cmdqueryname=network) **0::0** **0** [ **route-policy** *route-policy-name* ] command to import the default routes into the VRF table of the IPv4/IPv6 VPN instance.
     6. Run the [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn) command to configure the device to advertise IP prefix routes.
     7. Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
     8. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enter the BGP EVPN address family view.
     9. Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **upe** command to configure the UPE as the device's peer.
     10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     In this case, you also need to configure a routing policy on the NPE to prevent it from receiving the default route.
   * Configure the SPE to advertise a summary route to the UPE.
     
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
     3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* or [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv4/IPv6 address family view.
     4. Run the [**aggregate**](cmdqueryname=aggregate) *ipv4-address* { *mask* | *mask-length* } [ **as-set** | **attribute-policy** *route-policy-name1* | **detail-suppressed** | **origin-policy** *route-policy-name2* | **suppress-policy** *route-policy-name3* ] \* or [**aggregate**](cmdqueryname=aggregate) *ipv6-address* *prefix-length* [ **as-set** | **attribute-policy** *route-policy-name1* | **detail-suppressed** | **origin-policy** *route-policy-name2* | **suppress-policy** *route-policy-name3* ] \* command to configure a summary route.
     5. Run the [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn) command to configure the device to advertise IP prefix routes.
     6. Run the [**quit**](cmdqueryname=quit) Return to the BGP view.
     7. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enter the BGP EVPN address family view.
     8. Run the [**peer**](cmdqueryname=peer+upe) { *ipv4-address* | *group-name* } **upe** command to configure the UPE as the device's peer.
     9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. (Optional) Configure the SPE to change the next hops of routes. If the UPE and NPE are not in the same IGP routing domain, perform this step on the SPE.
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enter the BGP EVPN address family view.
   4. Run the [**peer**](cmdqueryname=peer+next-hop-local) { *ipv4-address* | *group-name* } **next-hop-local** command to configure the device to change the next hop address of a route to its own address before advertising the route to the NPE.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.