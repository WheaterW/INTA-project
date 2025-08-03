Configuring Interworking Between EVPN L3VPN over MPLS and L3VPN over SRv6
=========================================================================

During network evolution, EVPN L3VPN over MPLS and L3VPN over SRv6 may coexist. To allow these two networks to communicate, perform this configuration task.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0000001174489514__fig_dc_vrp_evpn_cfg_015401), EVPN L3VPN over MPLS is deployed in area A, and L3VPN over SRv6 is deployed in area B. To ensure that these two types of networks can communicate with each other and services can run properly, configure interworking between EVPN L3VPN over MPLS and L3VPN over SRv6 on each border leaf node.

**Figure 1** Interworking between EVPN L3VPN over MPLS and L3VPN over SRv6  
![](figure/en-us_image_0000001174171002.png)

#### Pre-configuration Tasks

Before configuring interworking between EVPN L3VPN over SRv6 and L3VPN over SRv6, complete the following tasks:

* [Configure EVPN L3VPN over MPLS](dc_vrp_evpn_cfg_0038.html) on the network in area A.
* [Configure L3VPNv4 over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0012.html) or [L3VPNv6 over SRv6 BE](dc_vrp_srv6_cfg_all_0251.html) on the network in area B.

#### Procedure

1. Configure each border leaf node to advertise the re-originated BGP-EVPN address family routes to a specified VPNv4 or VPNv6 peer (PE).
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+import+reoriginate) { *ipv4-address* | *group-name* } **import** **reoriginate**
      
      
      
      The device is configured to add a re-origination flag to routes received from the BGP EVPN peer.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   6. Run [**ipv4-family vpnv4**](cmdqueryname=ipv4-family+vpnv4) or [**ipv6-family vpnv6**](cmdqueryname=ipv6-family+vpnv6)
      
      
      
      The BGP-VPNv4/VPNv6 address family view is displayed.
   7. Configure the device to advertise routes re-originated by the BGP EVPN address family to the BGP VPNv4/VPNv6 peer.
      
      
      * Run the [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv6-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **mac-ip** | **ip** } command in the BGP VPNv4 address family view to enable the device to advertise routes re-originated in the BGP-EVPN address family to VPNv4 peers.
      * Run the [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv6-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **mac-ipv6** | **ipv6** } command in the BGP VPNv6 address family view to enable the device to advertise routes re-originated in the BGP-EVPN address family to VPNv6 peers.
      
      
      
      After this step is performed, the border leaf node re-originates the MPLS-encapsulated EVPN routes received from the access leaf node, and then advertises them as SRv6-encapsulated BGP VPNv4/VPNv6 routes to PEs.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Configure the border leaf node to advertise routes re-originated in the BGP VPNv4/VPNv6 address family to a specified BGP EVPN peer (access leaf node).
   1. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   2. Run [**ipv4-family vpnv4**](cmdqueryname=ipv4-family+vpnv4) or [**ipv6-family vpnv6**](cmdqueryname=ipv6-family+vpnv6)
      
      
      
      The BGP-VPNv4/VPNv6 address family view is displayed.
   3. Run [**peer**](cmdqueryname=peer+import+reoriginate) { *ipv6-address* | *group-name* } **import** **reoriginate**
      
      
      
      The device is configured to add a re-origination flag to routes received from VPNv4/VPNv6 peers.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   5. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   6. Run [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** { **vpnv4** | **vpnv6** }
      
      
      
      The device is configured to advertise routes re-originated in the BGP VPNv4/VPNv6 address family to a BGP EVPN peer.
      
      
      
      After this step is performed, the border leaf node re-originates SRv6-encapsulated VPNv4/VPNv6 routes received from the PE and advertises them as MPLS-encapsulated EVPN routes to the access leaf node.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
3. Enable EVPN route advertisement in the BGP-VPN instance address family view.
   1. Run [**ipv4-family vpn-instance**](cmdqueryname=ipv4-family+vpn-instance) *vpn-instance-name* or [**ipv6-family vpn-instance**](cmdqueryname=ipv6-family+vpn-instance) *vpn-instance-name*
      
      
      
      The BGP VPN instance IPv4/IPv6 address family view is displayed.
   2. Run [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn)
      
      
      
      The device is configured to advertise the host IPv4/IPv6 routes in the VPN instance as EVPN IPv4/IPv6 prefix routes.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table) command to check information about EVPN routes re-originated based on SRv6-encapsulated VPNv4/VPNv6 routes received by the border leaf node from PEs.
* Run the [**display bgp vpnv4 routing-table**](cmdqueryname=display+bgp+vpnv4+routing-table) command to check information about VPNv4 routes re-originated based on MPLS-encapsulated EVPN routes received by the border leaf node from access leaf nodes.
* Run the [**display bgp vpnv6 routing-table**](cmdqueryname=display+bgp+vpnv6+routing-table) command to check information about VPNv6 routes re-originated based on MPLS-encapsulated EVPN routes received by the border leaf node from access leaf nodes.