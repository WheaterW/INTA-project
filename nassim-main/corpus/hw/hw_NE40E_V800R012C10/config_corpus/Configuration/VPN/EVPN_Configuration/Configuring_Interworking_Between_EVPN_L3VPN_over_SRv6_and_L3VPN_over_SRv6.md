Configuring Interworking Between EVPN L3VPN over SRv6 and L3VPN over SRv6
=========================================================================

During network evolution, EVPN L3VPN over SRv6 and L3VPN over SRv6 may coexist. To allow these two types of networking to interwork, perform this task.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0000001174649462__fig8412214518), EVPN L3VPN over SRv6 is deployed in area A, and L3VPN over SRv6 is deployed in area B. To ensure that these two types of networks can communicate with each other and services can run properly, configure interworking between EVPN L3VPN over SRv6 and L3VPN over SRv6 on each border leaf node.

**Figure 1** Interworking between EVPN L3VPN over SRv6 and L3VPN over SRv6  
![](figure/en-us_image_0000001186891556.png)

#### Pre-configuration Tasks

Before configuring interworking between EVPN L3VPN over SRv6 and L3VPN over SRv6, complete the following tasks:

* Configure EVPN L3VPN over IS-IS SRv6 BE on the network in area A. For details, see [Configuring EVPN L3VPN over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0252.html).
* Configure L3VPNv4 over IS-IS SRv6 BE or L3VPNv6 over SRv6 BE on the network in area B. For details, see [Configuring L3VPNv4 over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0012.html) or [Configuring L3VPNv6 over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0251.html).

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
   7. Configure the device to advertise routes re-originated by the BGP-EVPN address family to the BGP VPNv4/VPNv6 peer.
      
      
      * Run the [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv6-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **mac-ip** | **ip** } command in the BGP VPNv4 address family view to enable the device to advertise routes re-originated in the BGP-EVPN address family to its VPNv4 peer.
      * Run the [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv6-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **mac-ipv6** | **ipv6** } command in the BGP VPNv6 address family view to enable the device to advertise routes re-originated in the BGP-EVPN address family to its VPNv6 peer.
      
      
      
      After this step is performed, the border leaf node re-originates the SRv6-encapsulated EVPN routes received from the access leaf node, and then advertises them as SRv6-encapsulated BGP VPNv4/VPNv6 routes to PEs.
   8. (Optional) Run [**peer**](cmdqueryname=peer+reflect-client) { *ipv6-address* | *group-name* } [**reflect-client**](cmdqueryname=reflect-client)
      
      
      
      The device is configured as an RR, and its peer is specified as an RR client.
      
      
      
      If the peer is an IBGP peer, the Router with the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command configured functions as an RR, and the specified peer (group) functions as a client.
   9. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   10. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the BGP view.
   11. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
2. Configure the border leaf node to advertise the routes that are re-originated in the BGP-VPNv4/VPNv6 address family to a specified BGP EVPN IPv6 peer (access leaf node).
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv4-family vpnv4**](cmdqueryname=ipv4-family+vpnv4) or [**ipv6-family vpnv6**](cmdqueryname=ipv6-family+vpnv6)
      
      
      
      The BGP-VPNv4/VPNv6 address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+import+reoriginate) { *ipv6-address* | *group-name* } **import** **reoriginate**
      
      
      
      The device is configured to add a re-origination flag to routes received from VPNv4/VPNv6 peers.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   6. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   7. Run [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *peerIpv6Addr* | *peerGroupName* } **advertise** **route-reoriginated** { **vpnv4** | **vpnv6** }
      
      
      
      The device is configured to advertise the routes re-originated in the BGP-VPNv4/VPNv6 address family to the BGP EVPN IPv6 peer.
      
      
      
      After this step is performed, the border leaf node re-originates SRv6-encapsulated VPNv4/VPNv6 routes received from the PE and advertises them as SRv6-encapsulated EVPN routes to the access leaf node.
   8. (Optional) Run [**peer**](cmdqueryname=peer+reflect-client) { *peerIpv6Addr* | *peerGroupName* } [**reflect-client**](cmdqueryname=reflect-client)
      
      
      
      An RR and its client are configured.
      
      
      
      If the peer is an IBGP peer, the Router with the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command configured functions as an RR, and the specified peer (group) functions as a client.
   9. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   10. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the BGP view.
3. Enable EVPN route advertisement in the BGP-VPN instance address family view.
   1. Run [**ipv4-family vpn-instance**](cmdqueryname=ipv4-family+vpn-instance) *vpn-instance-name* or [**ipv6-family vpn-instance**](cmdqueryname=ipv6-family+vpn-instance) *vpn-instance-name*
      
      
      
      The BGP VPN instance IPv4/IPv6 address family view is displayed.
   2. Run [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn)
      
      
      
      The device is configured to advertise the host IPv4/IPv6 routes in the VPN instance as EVPN IPv4/IPv6 prefix routes.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

* Run the [**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table) command to check information about EVPN routes re-originated based on SRv6-encapsulated VPNv4/VPNv6 routes received by the border leaf node from PEs.
* Run the [**display bgp vpnv4 routing-table**](cmdqueryname=display+bgp+vpnv4+routing-table) command to check information about VPNv4 routes re-originated based on SRv6-encapsulated EVPN routes received by the border leaf node from access leaf nodes.
* Run the [**display bgp vpnv6 routing-table**](cmdqueryname=display+bgp+vpnv6+routing-table) command to check information about VPNv6 routes re-originated based on SRv6-encapsulated EVPN routes received by the border leaf node from access leaf nodes.