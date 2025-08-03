Configuring Interworking Between EVPN L3VPN over SRv6 and Common L3VPN over MPLS
================================================================================

During network evolution, EVPN L3VPN over SRv6 and common L3VPN over MPLS may coexist. To allow these two types of networking to interwork, perform this task.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0176716902__fig6660849125212), area A is a newly built network deployed with the EVPN L3VPN over SRv6 service, and area B is the legacy network deployed with the common L3VPN over MPLS service. To ensure normal communication between the two types of networking, configure interworking between EVPN L3VPN over SRv6 and common L3VPN over MPLS on each border leaf node.

**Figure 1** Interworking between EVPN L3VPN over SRv6 and common L3VPN over MPLS  
![](figure/en-us_image_0000001193380426.png)

#### Pre-configuration Tasks

Before configuring interworking between an EVPN L3VPN over SRv6 and a common L3VPN over MPLS, complete the following tasks:

* On the network in area A, [Configuring EVPN L3VPN over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0252.html).
* On the network in area B, [Configuring a Basic BGP/MPLS IP VPN](dc_vrp_mpls-l3vpn-v4_cfg_0154.html) or [Configuring a Basic BGP/MPLS IPv6 VPN](dc_vrp_mpls-l3vpn-v6_cfg_2057.html).

#### Procedure

1. Configure each border leaf node to advertise the re-originated routes in the BGP-EVPN address family to a VPNv4 or VPNv6 peer (PE).
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+import+reoriginate) *peerIpv6Addr* **import** **reoriginate**
      
      
      
      The device is enabled to add a re-origination flag to routes received from BGP EVPN IPv6 peers.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   6. Run [**ipv4-family vpnv4**](cmdqueryname=ipv4-family+vpnv4) or [**ipv6-family vpnv6**](cmdqueryname=ipv6-family+vpnv6)
      
      
      
      The BGP-VPNv4/VPNv6 address family view is displayed.
   7. Run [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **ip** | **ipv6** }
      
      
      
      The function to advertise the routes re-originated in the BGP-EVPN address family to a BGP VPNv4/VPNv6 peer is enabled.
      
      After this step is performed, the border leaf node re-originates the SRv6-encapsulated EVPN IPv4/IPv6 prefix routes that are received from access leaf nodes and then advertises the MPLS-encapsulated BGP VPNv4/VPNv6 routes to its BGP VPNv4/VPNv6 peer (PE).
   8. (Optional) Run [**peer**](cmdqueryname=peer+reflect-client) { *ipv4-address* | *group-name* } [**reflect-client**](cmdqueryname=reflect-client)
      
      
      
      The device is configured as an RR, and its peer is specified as an RR client.
      
      
      
      If the peer is an IBGP peer, the Router with the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command configured functions as an RR, and the specified peer (group) functions as its client.
2. Configure the border leaf node to advertise the routes that are re-originated in the BGP-VPNv4/VPNv6 address family to a specified BGP EVPN IPv6 peer (access leaf node).
   1. Run [**peer**](cmdqueryname=peer+import+reoriginate) { *ipv4-address* | *group-name* } **import** **reoriginate**
      
      
      
      The device is enabled to re-originate the routes received from a BGP VPNv4 peer in the BGP-VPNv4/VPNv6 address family view.
   2. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *peerIpv6Addr* | *peerGroupName* } **advertise** **route-reoriginated** { **vpnv4** | **vpnv6** }
      
      
      
      The device is configured to advertise the routes re-originated in the BGP VPNv4/VPNv6 address family to the BGP VPN IPv6 peer.
      
      After this step is performed, the border leaf node re-originates the MPLS-encapsulated VPNv4/VPNv6 routes that are received from the BGP VPNv4/VPNv6 peer (PE) and then advertises SRv6-encapsulated EVPN routes to the BGP EVPN IPv6 peer (access leaf node).
   5. (Optional) Run [**peer**](cmdqueryname=peer+reflect-client) { *peerIpv6Addr* | *peerGroupName* } [**reflect-client**](cmdqueryname=reflect-client)
      
      
      
      An RR and its client are configured.
      
      
      
      If the peer is an IBGP peer, the Router with the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command configured functions as an RR, and the specified peer (group) functions as a client.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
3. Enable EVPN route advertisement in the BGP-VPN instance address family view.
   1. Run [**ipv4-family vpn-instance**](cmdqueryname=ipv4-family+vpn-instance) *vpn-instance-name* or [**ipv6-family vpn-instance**](cmdqueryname=ipv6-family+vpn-instance) *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv4/IPv6 address family view is displayed.
   2. Run [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn)
      
      
      
      The device is configured to advertise the host IPv4/IPv6 routes in the VPN instance as EVPN IPv4/IPv6 prefix routes.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table) command to check information about EVPN routes re-originated based on MPLS-encapsulated VPNv4/VPNv6 routes received by the border leaf node from PEs.
* Run the [**display bgp vpnv4 routing-table**](cmdqueryname=display+bgp+vpnv4+routing-table) command to check information about VPNv4 routes re-originated based on SRv6-encapsulated EVPN IPv4 prefix routes received by the border leaf node from the access leaf nodes.
* Run the [**display bgp vpnv6 routing-table**](cmdqueryname=display+bgp+vpnv6+routing-table) command to check information about VPNv6 routes re-originated based on SRv6-encapsulated EVPN IPv6 prefix routes received by the border leaf node from the access leaf nodes.