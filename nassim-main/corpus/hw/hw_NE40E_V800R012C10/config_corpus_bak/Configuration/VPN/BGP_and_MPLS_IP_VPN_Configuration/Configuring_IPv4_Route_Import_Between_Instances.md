Configuring IPv4 Route Import Between Instances
===============================================

IPv4 route import between VPN and public network instances enables IPv4 VPN users to communicate with IPv4 public network users, whereas IPv4 route import between VPN instances enables IPv4 users in different VPNs to communicate.

#### Usage Scenario

In BGP/MPLS IPv4 VPN networking, IPv4 VPN users cannot communicate with IPv4 public network users and IPv4 users of two VPNs can communicate only if the two VPNs have matching VPN targets. To enable IPv4 VPN users to communicate with IPv4 public network users and IPv4 users of two VPNs with unmatching VPN targets to communicate, configure IPv4 route import between instances.

IPv4 route import between instances is further classified into the following types:

* IPv4 route import between VPN and public network instances. IPv4 routes are first imported into the VPN or public network instance's corresponding routing table. For example, VPN OSPF routes are first imported into the public network instance's OSPF routing table. If the imported routes are preferred in the corresponding routing table, they will also be imported into the VPN or public network instance's IP routing table to guide traffic forwarding. In addition, these routes can be advertised to other devices on the network.
* Route import between VPN instances. For example, VPNA's OSPF routes are first imported into VPNB's OSPF routing table. If the imported routes are preferred in VPNB's OSPF routing table, they will be further imported into VPNB's IP routing table to guide traffic forwarding. In addition, these routes can be advertised through OSPF to other devices on the network.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

BGP IPv4 route import between VPN and public network instances does not take effect for locally leaked routes or routes imported in import or network mode.


Currently, the following types of IPv4 routes can be imported between instances:

* Direct routes
* Static routes
* OSPF routes
* IS-IS routes
* BGP routes
* Vlink direct routes
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Traffic forwarding relies on direct routes (Vlink direct routes) generated based on user entries. When QinQ/dot1q VLAN tag termination sub-interfaces are used for route import between VPN and public network, Vlink direct routes cannot be imported. As a result, traffic forwarding is interrupted. To solve this problem, route import between VPN and public network newly supports import of Vlink direct routes.


#### Pre-configuration Tasks

Before configuring route import between instances, complete the following task:

[Configure a basic BGP/MPLS IP VPN.](dc_vrp_mpls-l3vpn-v4_cfg_0154.html)


[Configuring Route Import Between VPN and Public Network Instances](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2024.html)

Route import between VPN and public network instances enables VPN users and public network users to communicate.

[Configuring Route Import Between VPN Instances](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2025.html)

Route import between VPN instances enables users in different VPNs to communicate.

[Verifying the Configuration of IPv4 Route Import Between Instances](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2026.html)

After configuring IPv4 route import between instances on a device, you can check imported IPv4 routes on the device.