Configuring EVPN L3VPN H-VPN over MPLS
======================================

On an EVPN L3VPN H-VPN over MPLS network, the SPE functions as an RR and the UPE and NPE function as RR clients, which receive specific routes from the RR.

#### Context

In EVPN L3VPN H-VPN over MPLS networking, you need to perform the following configurations:

1. On the UPE and NPE, [create a VPN instance](dc_vrp_evpn_cfg_0039.html) and bind access-side interfaces to the [IPv4 VPN instance](dc_vrp_mpls-l3vpn-v4_cfg_0156.html) or [IPv6 VPN instance](dc_vrp_mpls-l3vpn-v6_cfg_2059.html).
2. Configure BGP EVPN peer relationships between the UPE and SPE and between the SPE and NPE. For details, see [Configuring BGP EVPN Peer Relationships](dc_vrp_evpn_cfg_0006.html).
3. Configure routing protocols for the NPE and UPE to exchange routes with connected CEs. This configuration is similar to configuring the PE and CE to exchange routes on a basic BGP/MPLS IP VPN. For details, see [Configuring Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v4_cfg_0158.html) or [Configuring IPv6 Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v6_cfg_2061.html).
4. Configure the SPE as an RR and the UPE and NPE as RR clients. For detailed configurations, see [Procedure](#EN-US_TASK_0172370558__process1).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The BGP-EVPN address family view is displayed.
4. Run [**peer**](cmdqueryname=peer+reflect-client) { *ipv4-address* | *group-name* } [**reflect-client**](cmdqueryname=reflect-client)
   
   
   
   An RR is configured, and the UPE is specified as its client.
5. Run [**peer**](cmdqueryname=peer+next-hop-local) { *ipv4-address* | *group-name* } [**next-hop-local**](cmdqueryname=next-hop-local)
   
   
   
   The device is configured to change the next hop address of a route to its own address before advertising the route.
   
   
   
   To allow the SPE to use its own address as the next hop address of routes when advertising these routes to the UPE and NPE, run the [**peer next-hop-local**](cmdqueryname=peer+next-hop-local) command on the SPE twice with different parameters specified for the UPE and NPE.
6. (Optional) Run [**apply-label per-nexthop**](cmdqueryname=apply-label+per-nexthop)
   
   
   
   One-label-per-next-hop label distribution is enabled for EVPN routes.
   
   
   
   In an EVPN L3VPN H-VPN over MPLS scenario, if the SPE needs to advertise a large number of EVPN routes but MPLS labels are insufficient, configure one-label-per-next-hop label distribution for these routes.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   After one-label-per-next-hop label distribution is enabled or disabled on the SPE, the labels allocated by the SPE to routes change. As a result, temporary packet loss occurs.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.