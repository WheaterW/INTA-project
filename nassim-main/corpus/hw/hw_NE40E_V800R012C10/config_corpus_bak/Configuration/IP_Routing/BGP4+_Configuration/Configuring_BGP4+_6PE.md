Configuring BGP4+ 6PE
=====================

By configuring the 6PE function, you can connect separated IPv6 networks through LSPs.

#### Usage Scenario

6PE enables IPv6 networks separated by IPv4/MPLS networks to communicate.

Separated IPv6 networks can be connected using various tunneling techniques. A 6PE tunnel is established on Internet Service Provider's (ISP's) PEs that support the IPv4/IPv6 dual stack. The 6PE tunnel identifies IPv6 routes by label assigned by the Multiprotocol Border Gateway Protocol (MP-BGP), and implements IPv6 forwarding using LSPs between PEs.

As shown in [Figure 1](#EN-US_TASK_0172366497__fig_dc_vrp_bgp6_cfg_005601), the IPv6 network where CE1 and CE2 reside are separated by an IPv4/MPLS network. Configuring 6PE enables CE1 and CE2 to communicate across the IPv4 network.

**Figure 1** Networking with 6PE  
![](images/fig_dc_vrp_bgp6_cfg_005601.png)

#### Pre-configuration Tasks

Before configuring 6PE, complete the following tasks:

* Connect interfaces and setting parameters for the interfaces to ensure that the physical-layer status of the interfaces is Up.
* Configure the link layer protocol parameters for interfaces.
* Ensure that routes on the IPv4/MPLS backbone network are reachable.


[Configuring the IPv4/IPv6 Dual Stack](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0069.html)

The IPv4/IPv6 dual stack needs to be configured on the Router at the edge of an IPv6 network and an IPv4 network.

[Configuring an LDP LSP on an IPv4 Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0070.html)

An LDP LSP is configured on an IPv4/MPLS backbone network to forward IPv6 packets.

[Establishing a 6PE Peer Relationship Between PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0071.html)

6PE peers can exchange IPv6 routes learned from their attached CEs.

[(Optional) Enabling 6PE Routes Sharing the Explicit Null Label](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0087.html)

By enabling IPv6 provider edge (6PE) routes sharing the explicit null label, you can save label resources on 6PE devices.

[Configuring Route Exchange Between a PE and a CE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0072.html)

An IPv6 routing protocol needs to be configured on a PE and a CE to enable them to learn IPv6 routes from each other.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0073.html)

After configuring BGP4+ 6PE, check whether CEs can learn routes to each other.