Configuring Interworking Between EVPN L3VPN HoVPN over MPLS and Common L3VPN
============================================================================

During evolution from L3VPN HoVPN to EVPN L3VPN HoVPN over MPLS, interworking between EVPN L3VPN HoVPN over MPLS and common L3VPN is required. EVPN L3VPN HoVPN over MPLS is deployed between the UPE and SPE, and common L3VPN is deployed between the SPE and NPE.

#### Context

In a scenario where EVPN L3VPN HoVPN over MPLS interworks with common L3VPN, perform the following configurations:

* [Create a VPN instance](dc_vrp_evpn_cfg_0039.html) on the UPE and SPE and bind the access-side interface to the [IPv4 VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0156.html) or [IPv6 VPN instance](dc_vrp_mpls-l3vpn-v6_cfg_2059.html) on the UPE. ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  According to related standards, the VPN instance status obtained through an NMS can be up only when at least one interface bound to the VPN instance is up. In an HoVPN scenario, an SPE does not require any interface to be bound to a VPN instance. Consequently, the VPN instance status obtained by an NMS is down according to the standards, which is opposite to the actual VPN instance status. In this case, you can run the [**transit-vpn**](cmdqueryname=transit-vpn) command in the VPN instance view or VPN instance IPv4/IPv6 address family view on the SPE. Then, the VPN instance status obtained by the NMS remains up, regardless of the binding status between the VPN instance and interface.
* For IPv4 services, [configure a VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0155.html) and bind the access-side interface to the [VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0156.html) on the NPE; for IPv6 services, [configure an IPv6 VPN instance](dc_vrp_mpls-l3vpn-v6_cfg_2058.html) and [bind the access-side interface to the IPv6 VPN instance](dc_vrp_mpls-l3vpn-v6_cfg_2059.html) on the NPE.
* Configure a default static VPN route on the SPE. For details, see [Creating IPv4 Static Routes](dc_vrp_static-route_disjoin_cfg_0004.html) or [Creating IPv6 Static Routes](dc_vrp_static-route_disjoin_cfg_0009.html).
* For IPv4 services, configure a BGP VPNv4 peer relationship between the SPE and NPE. This configuration is similar to configuring a BGP VPNv4 peer relationship between PEs on a basic BGP/MPLS IPv4 VPN. For details, see [Establishing MP-IBGP Peer Relationships Between PEs](dc_vrp_mpls-l3vpn-v4_cfg_0157.html). For IPv6 services, configure a BGP VPNv6 peer relationship between the SPE and NPE. This configuration is similar to configuring a BGP VPNv6 peer relationship between PEs on a basic BGP/MPLS IPv6 VPN. For details, see [Establishing MP-IBGP Peer Relationships Between PEs](dc_vrp_mpls-l3vpn-v6_cfg_2060.html).
* Configure a BGP EVPN peer relationship between the UPE and SPE. For details, see [Configuring BGP EVPN Peer Relationships](dc_vrp_evpn_cfg_0006.html).
* Configure the SPE to advertise only default or summary routes to the UPE. For details, see [Configuring EVPN L3VPN HoVPN](dc_vrp_evpn_cfg_0080.html).
* Configure routing protocols for the UPE and NPE to exchange routes with connected CEs. This configuration is similar to configuring the PE and CE to exchange routes on a basic BGP/MPLS IP VPN. For details, see [Configuring Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v4_cfg_0158.html) or [Configuring IPv6 Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v6_cfg_2061.html).
* Configure the SPE to advertise re-encapsulated VPNv4 routes to the NPE. For details, see [Procedure](#EN-US_TASK_0172370559__process1).

Perform the following steps on the SPE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The BGP-EVPN address family view is displayed.
4. Run [**peer**](cmdqueryname=peer+import+reoriginate) { *ipv4-address* | *group-name* } **import** **reoriginate**
   
   
   
   The function to add a re-origination flag to routes received from the UPE is enabled.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the BGP view.
6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** or [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
   
   
   
   The BGP-VPNv4/VPNv6 address family view is displayed.
7. Run [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **ip** | **ipv6** }
   
   
   
   The SPE is configured to re-encapsulate EVPN routes received from the UPE into BGP VPNv4/VPNv6 routes and advertise them to the NPE.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.