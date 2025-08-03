Configuring 6VPE
================

With the 6VPE function, separate IPv6 networks belonging to the same VPN instance can be connected using an LSP.

#### Usage Scenario

[Figure 1](#EN-US_TASK_0172369593__fig_dc_vrp_mpls-l3vpn-v6_cfg_211201) shows a typical 6VPE network, where a BGP/MPLS IPv6 VPN (6VPE) is established between PE1 and PE2 and BGP VPN peer relationships are established between CE1 and PE1 and between CE2 and PE2. IPv6 users within the CE-side site communicate through the IPv4 network between each pair of a CE and a PE.

**Figure 1** 6VPE networking  
![](images/fig_dc_vrp_mpls-l3vpn-v6_cfg_211201.png)

#### Pre-configuration Tasks

Before configuring 6VPE, complete the following tasks:

* Configure IPv4 addresses for interfaces on PEs.
* Configure an IGP on the MPLS backbone network to implement IP connectivity.
* Configure basic MPLS functions on the MPLS backbone network.
* Establish LSPs or MPLS TE tunnels between PEs.
* Configure IPv4 addresses for CE interfaces connected to PEs.


[Configuring a VPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2116.html)

A VPN instance of the IPv6 address family can be configured to manage IPv6 VPN routes.

[Binding Interfaces to a VPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2120.html)

After an interface is bound to a VPN instance, the interface becomes a part of the VPN. Packets entering the interface will be forwarded based on the VRF table of the VPN.

[(Optional) Setting a Router ID for a BGP VPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2115.html)

To distinguish a BGP VPN instance from the other BGP VPN instances on the same device, specify a unique router ID for the BGP VPN instance. 

[Establishing MP-IBGP Peer Relationships Between PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2060a.html)

MP-IBGP uses extended community attributes to advertise VPNv6 routes between PEs.

[Configuring BGP VPN Peer Relationships Between PEs and CEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2113.html)

In a 6VPE scenario, BGP VPN peer relationships must be configured between PEs and CEs to allow them to communicate.

[Checking the Configurations](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2114.html)

After 6VPE is configured on a PE, check that the PE successfully establishes a BGP IPv4 peer relationship with the CE in the VPN instance IPv6 address family.