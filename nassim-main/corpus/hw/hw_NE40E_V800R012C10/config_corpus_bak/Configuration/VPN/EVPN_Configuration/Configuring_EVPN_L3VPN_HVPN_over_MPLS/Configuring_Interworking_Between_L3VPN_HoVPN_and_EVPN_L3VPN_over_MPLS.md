Configuring Interworking Between L3VPN HoVPN and EVPN L3VPN over MPLS
=====================================================================

During evolution from L3VPN HoVPN to EVPN HoVPN over MPLS, interworking between L3VPN HoVPN and EVPN L3VPN over MPLS occurs. L3VPN HoVPN is deployed between the UPE and SPE, and EVPN L3VPN over MPLS is deployed between the SPE and NPE.

#### Context

In a scenario where L3VPN HoVPN interworks with EVPN L3VPN over MPLS, perform the following configurations:

* [Create a VPN instance](dc_vrp_evpn_cfg_0039.html) on the SPE and NPE and bind the access-side interface to the [IPv4 VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0156.html) or [IPv6 VPN instance](dc_vrp_mpls-l3vpn-v6_cfg_2059.html) on the NPE. ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  According to related standards, the VPN instance status obtained through an NMS can be up only when at least one interface bound to the VPN instance is up. In an HoVPN scenario, an SPE does not require any interface to be bound to a VPN instance. Consequently, the VPN instance status obtained by an NMS is down according to the standards, which is opposite to the actual VPN instance status. In this case, you can run the [**transit-vpn**](cmdqueryname=transit-vpn) command in the VPN instance view or VPN instance IPv4/IPv6 address family view on the SPE. Then, the VPN instance status obtained by the NMS remains up, regardless of the binding status between the VPN instance and interface.
* [Create a VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0155.html) and [bind the access-side interface to the VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0156.html) on the UPE.
* Configure a BGP EVPN peer relationship between the SPE and NPE. For details, see [Configuring BGP EVPN Peer Relationships](dc_vrp_evpn_cfg_0006.html).
* Configure a BGP VPNv4 peer relationship between the SPE and UPE. This configuration is similar to configuring a BGP VPNv4 peer relationship between PEs on a basic BGP/MPLS IP VPN. For details, see [Establishing MP-IBGP Peer Relationships Between PEs](dc_vrp_mpls-l3vpn-v4_cfg_0157.html).
* Configure routing protocols for the NPE and UPE to exchange routes with connected CEs. This configuration is similar to configuring the PE and CE to exchange routes on a basic BGP/MPLS IP VPN. For details, see [Configuring Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v4_cfg_0158.html).
* Configure the SPE to advertise only default or summary routes to the UPE.
* Configure the SPE to advertise re-encapsulated EVPN routes to the NPE. For details, see [Procedure](#EN-US_TASK_0172370560__process1).

Perform the following steps on the SPE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4**
   
   
   
   The BGP-VPNv4 address family view is displayed.
4. Run [**peer**](cmdqueryname=peer+import+reoriginate) { *ipv4-address* | *group-name* } **import** **reoriginate**
   
   
   
   The function to add a re-origination flag to routes received from the UPE is enabled.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the BGP view.
6. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The BGP-EVPN address family view is displayed.
7. Run [**peer**](cmdqueryname=peer+advertise+route-reoriginate+vpnv4d) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** **vpnv4**
   
   
   
   The SPE is configured to re-encapsulate the BGP VPNv4 routes received from the UPE into EVPN routes and advertise them to the NPE.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.