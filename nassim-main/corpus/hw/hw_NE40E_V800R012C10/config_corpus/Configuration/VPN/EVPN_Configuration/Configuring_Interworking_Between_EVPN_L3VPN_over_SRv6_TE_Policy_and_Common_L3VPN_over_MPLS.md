Configuring Interworking Between EVPN L3VPN over SRv6 TE Policy and Common L3VPN over MPLS
==========================================================================================

During network evolution, EVPN L3VPN over SRv6 TE Policy and common L3VPN over MPLS may coexist. To allow these two types of networks to communicate, perform this task.

#### Context

In [Figure 1](#EN-US_TASK_0188146564__fig_dc_vrp_evpn_cfg_015401), network A is newly deployed and runs EVPN L3VPN over SRv6 TE Policy. Network B is a legacy network and runs common L3VPN over MPLS. Alternatively, network A runs EVPN L3VPNv6 over SRv6 TE Policy, and network B runs common L3VPNv6 over MPLS. To ensure that these two types of networks can communicate and services can run properly, configure interworking between EVPN L3VPN over SRv6 TE Policy and common L3VPN over MPLS on each border leaf node.

**Figure 1** Configuring interworking between EVPN L3VPN over SRv6 TE Policy and common L3VPN over MPLS  
![](figure/en-us_image_0206400990.png)

#### Pre-configuration Tasks

Before configuring interworking between EVPN L3VPN over SRv6 TE Policy and common L3VPN over MPLS, complete the following tasks:

* Configure [EVPN L3VPN over SRv6 TE Policy](dc_vrp_cfg_evpn-l3vpn_over_srv6-te_policy.html) or [Configuring EVPN L3VPNv6 over SRv6 TE Policy](dc_vrp_cfg_evpn-l3vpnv6_over_srv6-te_policy.html) on the network that contains area A.
* [Configure basic BGP/MPLS IPv4 VPN](dc_vrp_mpls-l3vpn-v4_cfg_0154.html) or [basic BGP/MPLS IPv6 VPN](dc_vrp_mpls-l3vpn-v6_cfg_2057.html) on network B.

#### Procedure

1. Configure each border leaf node to advertise the re-originated BGP-EVPN address family routes to a specified VPNv4 or VPNv6 peer (PE) or peer group.
   1. Run **system-view**
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run **l2vpn-family evpn**
      
      
      
      The BGP-EVPN address family view is displayed.
   4. Run **peer** *ipv6-address* **import** **reoriginate**
      
      
      
      The border leaf node is configured to re-originate the routes received from a specified BGP EVPN IPv6 peer.
   5. Run **quit**
      
      
      
      Return to the BGP view.
   6. Run **ipv4-family** **vpnv4** or **ipv6-family** **vpnv6**
      
      
      
      The BGP-VPNv4 or BGP-VPNv6 address family view is displayed.
   7. Run **peer** { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **ip** | **ipv6** }
      
      
      
      The border leaf node is configured to advertise re-originated routes in the BGP-EVPN address family to a specified BGP VPNv4 or VPNv6 peer or peer group.
      
      
      
      After this step is performed, the border leaf node re-originates SRv6-encapsulated EVPN IPv4 or IPv6 prefix routes received from access leaf nodes. Then, the border leaf node advertises MPLS-encapsulated BGP VPNv4 or VPNv6 routes to the specified BGP VPN peer (PE) or peer group.
2. Configure the border leaf node to advertise the routes that are re-originated in the BGP-VPNv4 or BGP-VPNv6 address family to a specified BGP EVPN IPv6 peer (access leaf) or peer group.
   1. Run **peer** { *ipv4-address* | *group-name* } **import** **reoriginate**
      
      
      
      The border leaf node is configured to add a re-origination flag to routes received from a specified VPNv4 peer or peer group in the BGP-VPN address family view.
   2. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   3. Run **l2vpn-family evpn**
      
      
      
      The BGP-EVPN address family view is displayed.
   4. Run **peer** *ipv6-address* **advertise** **route-reoriginated** { **vpnv4** | **vpnv6** }
      
      
      
      The border leaf node is configured to advertise the routes re-originated in the BGP-VPNv4 or BGP-VPNv6 address family to a specified BGP EVPN IPv6 peer.
      
      
      
      After this step is performed, the border leaf node re-originates MPLS-encapsulated VPNv4 or VPNv6 routes that are received from the PEs. Then, the border leaf node advertises the SRv6-encapsulated EVPN routes to the specified access leaf node.
   5. Run **quit**
      
      
      
      Return to the BGP view.
3. Enable EVPN route advertisement in the BGP-VPN instance address family view.
   1. Run **ipv4-family** **vpn-instance** *vpn-instance-name* or **ipv6-family** **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv4 or IPv6 address family view is displayed.
   2. Run **advertise l2vpn evpn**
      
      
      
      The border leaf node is configured to advertise IPv4 or IPv6 routes in the VPN instance as EVPN IPv4 or IPv6 prefix routes.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the **display bgp evpn all routing-table** command to check information about EVPN routes re-originated after the border leaf node receives VPNv4 or VPNv6 routes encapsulated in MPLS packets from PEs.
* Run the **display bgp vpnv4 all routing-table** command to check information about VPNv4 routes re-originated after the border leaf node receives EVPN IP prefix routes encapsulated in SRv6 packets from access leaf nodes.
* Run the **display bgp vpnv6 all routing-table** command to check information about VPNv6 routes re-originated after the border leaf node receives EVPN IPv6 prefix routes encapsulated in SRv6 packets from access leaf nodes.