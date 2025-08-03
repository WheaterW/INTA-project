Configuring L3VPNv4 HoVPN over SRv6 TE Policy
=============================================

This section describes how to configure L3VPNv4 HoVPN over SRv6 TE Policy.

#### Usage Scenario

Currently, the typical structure of a MAN consists of three layers: core layer, aggregation layer, and access layer. To implement VPN functions on a hierarchical network for achieving end-to-end VPN data transmission and improving the performance and scalability of the entire network, you need to deploy hierarchical VPN solutions, among which the hierarchy of VPN (HoVPN) solution is commonly used.

During network evolution, the core and aggregation layers may use different forwarding modes, that is, SRv6 forwarding and MPLS forwarding. When the HoVPN solution is used to implement hierarchical VPN deployment, the methods used to forward L3VPNv4 data over a public network fall into three categories (as shown in [Figure 1](#EN-US_TASK_0226968186__fig1910417183547)): L3VPNv4 over MPLS plus SRv6, L3VPNv4 over SRv6 plus MPLS, and L3VPNv4 over SRv6 plus SRv6.

**Figure 1** HoVPN solution networking  
![](figure/en-us_image_0235785614.png)

This section uses L3VPNv4 over SRv6 TE Policy plus SRv6 TE Policy as an example. As shown in [Figure 2](#EN-US_TASK_0226968186__fig1787914952211), L3VPNv4 HoVPN over SRv6 TE Policy allows SRv6 TE Policies on a public network to carry L3VPNv4 data on condition that hierarchical VPN deployment is implemented through the HoVPN solution.

**Figure 2** L3VPNv4 HoVPN over SRv6 TE Policy networking  
![](figure/en-us_image_0226997664.png)

#### Pre-configuration Tasks

Before configuring L3VPNv4 HoVPN over SRv6 TE Policy, complete the following tasks:

* Configure a link layer protocol.
* Configure IP addresses for interfaces to ensure that neighboring devices are reachable at the network layer.

#### Procedure

1. Configure IPv6 IS-IS on the UPE, SPE, and NPE. For configuration details, see [Configuring Basic IS-IS Functions (IPv6)](dc_vrp_isis_cfg_1023.html).
2. Configure IPv4 route exchange between the UPE and CE1 and between the NPE and CE2. For configuration details, see [Configuring Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v4_cfg_0158.html).
3. Establish an MP-IBGP peer relationship between the UPE and SPE and another one between the NPE and SPE. Configure a VPN instance and enable the IPv4 address family for the VPN instance on each of the three devices. In addition, enable the devices to add SIDs to VPN routes. For configuration details, see [Configuring L3VPNv4 over SRv6 TE Policy](dc_vrp_cfg_l3vpnv4_over_srv6-te_policy.html).
4. Configure an SRv6 TE Policy. For configuration details, see [Configuring an SRv6 TE Policy (Manual Configuration + IS-IS as an IGP)](dc_vrp_srv6_cfg_all_0110.html) or [Configuring an SRv6 TE Policy (Dynamic Delivery by a Controller + IS-IS as an IGP)](dc_vrp_srv6_cfg_all_0116.html).
5. Configure VPNv4 route recursion to the SRv6 TE Policy. For configuration details, see [Configuring L3VPNv4 over SRv6 TE Policy](dc_vrp_cfg_l3vpnv4_over_srv6-te_policy.html).
6. Specify the UPE as the peer of the SPE and configure the SPE to advertise the default route to the UPE.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run **bgp** { *as-number-plain* | *as-number-dot* }
      
      
      
      The BGP view is displayed.
   3. Run **ipv4-family** **vpnv4**
      
      
      
      The BGP-VPNv4 address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer) *peerIpv6Addr* **upe**
      
      
      
      The peer is specified as a UPE.
   5. Run [**peer**](cmdqueryname=peer) *ipv6-address* [**default-originate vpn-instance**](cmdqueryname=default-originate+vpn-instance) *vpn-instance-name*
      
      
      
      The device is configured to automatically generate a default route and advertise it to the UPE.
      
      If you do not run this command to automatically generate a default route, you can manually configure a static route with the next hop set to the NPE's public or private address. If the next hop is set to the SPE's address and a fault occurs on the link between the SPE and NPE, traffic black holes may occur. Then, run the [**ip route-static recursive-lookup inherit-label-route segment-routing-ipv6**](cmdqueryname=ip+route-static+recursive-lookup+inherit-label-route+segment-routing-ipv6) command to recurse the static route to an SRv6 route.
   6. Run **commit**
      
      
      
      The configuration is committed.
   7. Run **quit**
      
      
      
      Exit the BGP-VPNv4 address family view.
7. Enable route regeneration on the SPE and configure the SPE to advertise regenerated routes to the NPE.
   1. Run [**ipv4-family vpn-instance**](cmdqueryname=ipv4-family+vpn-instance) *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv4 address family view is displayed.
   2. Run [**advertise best-route route-reoriginate**](cmdqueryname=advertise+best-route+route-reoriginate)
      
      
      
      Route regeneration is enabled.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-VPN instance IPv4 address family view.
   4. Run **ipv4-family** **vpnv4**
      
      
      
      The BGP-VPNv4 address family view is displayed.
   5. Run [**peer**](cmdqueryname=peer) *ipv6-address* **advertise route-reoriginated vpnv4**
      
      
      
      The SPE is configured to advertise regenerated routes in the BGP-VPNv4 address family to the NPE.
   6. Run **commit**
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After configuring L3VPNv4 HoVPN over SRv6 TE Policy, verify the configuration.

* Run the [**display bgp vpnv4 all routing-table**](cmdqueryname=display+bgp+vpnv4+all+routing-table) command to check BGP VPNv4 routing information.
* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance* command to check the routing tables of the NPE and UPE.