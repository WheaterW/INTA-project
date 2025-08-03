Configuring and Applying a Tunnel Policy
========================================

After a tunnel policy is applied to a VPN service, the system will flexibly select a tunnel based on the policy, increasing tunnel selection diversity.

#### Context

VPN (including L2VPN and L3VPN) data is forwarded along tunnels on the backbone network.

* Currently, the following IPv4 tunnel types are available: LSP, GRE, MPLS TE, Flex-Algo LSP, and SR-MPLS TE Policy.
  
  By default, the system selects LSPs to transmit VPN data without performing load balancing, which cannot meet VPN requirements in the following situations:
  
  + GRE or TE tunnels need to be selected for service transmission.
  + Load balancing among tunnels needs to be implemented to fully utilize network resources when multiple tunnels are available for VPN service transmission.
  + Some VPN services demand Quality of Service (QoS) guarantee and must be carried by dedicated TE tunnels.
* The IPv6 tunnel type can be SRv6 TE Policy or SRv6 TE flow group.

In these situations, tunnel policies need to be configured and applied to VPNs. The following types of VPNs can apply tunnel policies:

* BGP/MPLS IP VPN
* BGP/MPLS IPv6 VPN
* Static virtual circuit (SVC) virtual private wire service (VPWS)
* LDP VPWS
* LDP VPLS
* BGP VPLS
* BGP A-D VPLS
* EVPN

The mode in which a tunnel policy is applied to VPN services varies according to the VPN type.


#### Pre-configuration Tasks

Before configuring and applying a tunnel policy, complete the following tasks:

* Create a tunnel for the VPN service.
  + For details about how to create an LSP, see [Configuring an LDP LSP](dc_vrp_ldp-p2p_cfg_0015.html), [Configuring an IS-IS SR-MPLS BE Path](dc_vrp_sr-be_cfg_0008.html), and [Configuring an OSPF SR-MPLS BE Path](dc_vrp_sr_all_cfg_0001.html).
  + For details about how to create and configure a TE tunnel, see [Configuring an RSVP-TE Tunnel](dc_vrp_te-p2p_cfg_0003.html).
  + For details about how to create and configure a GRE tunnel, see [Configuring a GRE Tunnel](dc_vrp_gre_cfg_2003.html).
  + For details about how to create an SR-MPLS TE Policy, see [Configuring an SR-MPLS TE Policy (Manual Configuration)](dc_vrp_sr_all_cfg_0059.html) or [Configuring an SR-MPLS TE Policy (Dynamic Delivery by a Controller)](dc_vrp_sr_all_cfg_0067.html).
  + For details about how to create an SRv6 TE Policy or SRv6 TE flow group, see [Configuring an SRv6 TE Policy (Manual Configuration + IS-IS as an IGP)](dc_vrp_srv6_cfg_all_0110.html) or [Configuring an SRv6 TE Policy (Dynamic Delivery by a Controller + IS-IS as an IGP)](dc_vrp_srv6_cfg_all_0116.html).
* Establish the basic network for VPNs of different types.
  
  + For details about how to configure a BGP/MPLS IP VPN, see [Configuring a Basic BGP/MPLS IP VPN](dc_vrp_mpls-l3vpn-v4_cfg_0154.html).
  + For details about how to configure a BGP/MPLS IPv6 VPN, see [Configuring a Basic BGP/MPLS IPv6 VPN](dc_vrp_mpls-l3vpn-v6_cfg_2057.html).
  + For details about how to configure SVC VPWS, see [Configuring SVC VPWS](dc_vrp_vpws_cfg_6000.html).
  + For details about how to configure LDP VPWS, see [Configuring LDP VPWS](dc_vrp_vpws_cfg_3004.html).
  + For details about how to configure LDP VPLS, see [Configuring LDP VPLS](dc_vrp_vpls_cfg_5003.html).
  + For details about how to configure BGP VPLS, see [Configuring BGP VPLS](dc_vrp_vpls_cfg_6005.html).
  + For details about how to configure BGP A-D VPLS, see [Configuring BGP AD VPLS](dc_vrp_vpls_cfg_5057.html).
  + For details about how to configure EVPN, see [Configuring EVPN](dc_vrp_evpn_cfg_0000.html).


[Configuring a Tunnel Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_tnlm_cfg_0037.html)

Tunnel policies are divided into tunnel type prioritizing policies and tunnel binding policies.

[Applying a Tunnel Policy to a VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_tnlm_cfg_0038.html)

After configuring a tunnel policy, you need to apply it to a VPN service. The mode in which a tunnel policy is applied to VPN services varies according to the VPN type.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_tnlm_cfg_0039.html)

After configuring a tunnel policy and applying it to a VPN instance, you can check information about the tunnel policy applied to the VPN instance and tunnels in the system.