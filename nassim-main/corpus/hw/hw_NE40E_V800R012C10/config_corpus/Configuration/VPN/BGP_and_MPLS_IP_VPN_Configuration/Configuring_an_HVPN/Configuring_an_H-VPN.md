Configuring an H-VPN
====================

On an H-VPN, SPEs function as RRs and UPEs function as
RR clients. UPEs receive specific routes from SPEs.

#### Context

For H-VPN networking, you must perform the following configurations:

* Configure a VPN instance on each UPE and NPE. For configuration
  details, see [Configuring a VPN Instance](dc_vrp_mpls-l3vpn-v4_cfg_0155.html).
* Configure an MP-BGP peer relationship between each SPE and
  NPE and between each UPE and SPE. This configuration is similar to
  configuring an MP-IBGP peer relationship between PEs on a BGP/MPLS
  IP VPN. For configuration details, see [Establishing MP-IBGP Peer Relationships Between PEs](dc_vrp_mpls-l3vpn-v4_cfg_0157.html).
* Configure routing protocols for NPEs and UPEs to exchange routes
  with CEs. This configuration is similar to configuring PEs and CEs
  to exchange routes on a BGP/MPLS IP VPN. For configuration details,
  see [Configuring Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v4_cfg_0158.html).
* Configure SPEs as RRs and configure UPEs as RR clients.

Perform the following steps on each SPE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4**
   
   
   
   The BGP-VPNv4 address family view
   is displayed.
4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**reflect-client**](cmdqueryname=reflect-client)
   
   
   
   The SPE is configured as an RR
   and the UPEs are configured as RR clients.
5. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**next-hop-local**](cmdqueryname=next-hop-local)
   
   
   
   The SPE is configured to use
   its own IP address as the next hops of routes when advertising these
   routes.
   
   
   
   To enable an SPE to use its own IP address as the next hops
   of routes when advertising these routes to UPEs and NPEs, run the [**peer next-hop-local**](cmdqueryname=peer+next-hop-local) command twice with different parameters specified on the
   SPE.
6. (Optional) Run [**apply-label per-nexthop**](cmdqueryname=apply-label+per-nexthop)
   
   
   
   One-label-per-next-hop label distribution is enabled on the SPE.
   
   
   
   In an H-VPN scenario, if an SPE needs to send large numbers of VPNv4 routes but the MPLS labels are inadequate, configure one-label-per-next-hop label distribution on the SPE.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) After one-label-per-next-hop label distribution is enabled or disabled on an SPE, the labels assigned by the SPE to routes change. As a result, temporary packet loss may occur.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.