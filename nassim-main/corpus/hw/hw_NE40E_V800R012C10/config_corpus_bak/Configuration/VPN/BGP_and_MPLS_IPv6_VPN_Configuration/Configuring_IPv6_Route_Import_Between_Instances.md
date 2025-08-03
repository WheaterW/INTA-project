Configuring IPv6 Route Import Between Instances
===============================================

IPv6 route import between VPN and public network instances enables IPv6 VPN users to communicate with IPv6 public network users, whereas IPv6 route import between VPN instances enables IPv6 users in different VPNs to communicate.

#### Usage Scenario

In BGP/MPLS IPv6 VPN networking, IPv6 VPN users cannot communicate with IPv6 public network users and IPv6 users of two VPNs can communicate only if the two VPNs have matching VPN targets. To enable IPv6 VPN users to communicate with IPv6 public network users and IPv6 users of two VPNs with unmatching VPN targets to communicate, configure IPv6 route import between instances.

IPv6 route import between instances is further classified into the following types:

* IPv6 route import between VPN and public network instances
* IPv6 route import between VPN instances

IPv6 routes are first imported into the VPN or public network instance's corresponding routing table. For example, VPN OSPFv3 routes are first imported into the public network instance's OSPFv3 routing table. If the imported routes are preferred in the corresponding routing table, they will be further imported into the VPN or public network instance's IPv6 routing table to guide traffic forwarding. In addition, these routes can be advertised to other devices on the network.

Currently, the following types of IPv6 routes can be imported between instances:

* Direct routes
* Static routes
* OSPFv3 routes
* IS-IS routes
* BGP4+ routes
* Vlink direct routes
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Traffic forwarding relies on direct routes (Vlink direct routes) generated based on user entries. When QinQ/dot1q VLAN tag termination sub-interfaces are used for route import between VPN and public network, Vlink direct routes cannot be imported. As a result, traffic forwarding is interrupted. To solve this problem, route import between VPN and public network newly supports import of Vlink direct routes.


#### Pre-configuration Tasks

Before configuring IPv6 route import between instances, complete the following task:

[Configure a basic BGP/MPLS IPv6 VPN.](dc_vrp_mpls-l3vpn-v6_cfg_2057.html)


[Configuring IPv6 Route Import Between VPN and Public Network Instances](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2101.html)

IPv6 route import between VPN and public network instances enables IPv6 VPN users to communicate with IPv6 public network users.

[Configuring IPv6 Route Import Between VPN Instances](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2102.html)

IPv6 route import between VPN instances enables users in different VPNs to communicate.

[Verifying the Configuration of IPv6 Route Import Between Instances](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2103.html)

After configuring IPv6 route import between instances, you can check IPv6 route import results.