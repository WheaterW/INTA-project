Configuring a Basic BGP/MPLS IPv6 VPN
=====================================

A basic BGP/MPLS IPv6 VPN includes PEs, Ps, and CEs with the Ps residing in a single MPLS domain on the backbone network of one carrier. Each device plays only one role, either PE, CE, or P. After a basic BGP/MPLS IPv6 VPN is configured, the network can provide IPv6 VPN services for customers.

#### Usage Scenario

This section describes how to configure a basic BGP/MPLS IPv6 VPN. After the configurations are complete, the network can provide VPN services for users so that multiple private networks can communicate across the backbone network of the carrier. VPN routes are isolated from the public network routes on the backbone network, and the routes of VPN instances are isolated from each other.

As shown in [Figure 1](#EN-US_TASK_0172369579__fig_dc_vrp_mpls-l3vpn-v6_cfg_205701), the following functions need to be implemented on the network:

* Site 1 can communicate only with Site 3.
* Site 2 can communicate only with Site 4.
* The MPLS backbone network is unaware of the VPN routes in each site.

To meet the preceding requirements, configure a basic BGP/MPLS IPv6 VPN by adding Site 1 and Site 3 to a VPN (VPN1) and Site 2 and Site 4 to another VPN (VPN2). CEs and other devices deployed at sites only advertise and receive VPN routes. They are unaware of the public network. Ps residing on the public network do not receive VPN routes. PEs manage VPN routes and public network routes separately. VPN data packets are transmitted transparently over tunnels between the sites within the same VPN. The devices on the public network do not know the contents of VPN data packets, ensuring VPN data security.
**Figure 1** BGP/MPLS IPv6 VPN  
![](images/fig_dc_vrp_mpls-l3vpn-v6_cfg_205701.png)

#### Pre-configuration Tasks

Before configuring a basic BGP/MPLS IPv6 VPN, complete the following tasks:

* Configure the import or export route-policy to control the route acceptance or advertisement of the VPN instance IPv6 address family if needed.
* Enable IPv6 on PEs and related interfaces.
* Configure an IGP on the PEs and Ps to ensure IP connectivity on the MPLS backbone network.
* Configure basic MPLS functions on the PEs and Ps of the MPLS backbone network.
* Establish LSPs or MPLS TE tunnels between PEs.
* Configure IPv6 addresses on interfaces that connect CEs to PEs.


[Configuring a VPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2058.html)

A VPN instance of the IPv6 address family can be configured to manage IPv6 VPN routes.

[Binding Interfaces to a VPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2059.html)

After an interface is bound to a VPN instance, the interface becomes a part of the VPN. Packets entering the interface will be forwarded based on the VRF table of the VPN.

[(Optional) Setting a Router ID for a BGP VPN Instance IPv6 Address Family](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2082.html)

You can set different router IDs for BGP VPN instance IPv6 address families on the same device.

[Establishing MP-IBGP Peer Relationships Between PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2060.html)

MP-IBGP uses extended community attributes to advertise VPNv6 routes between PEs.

[Configuring Route Exchange Between PEs and CEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2061.html)

To enable CEs to communicate, the PEs and CEs must be capable of exchanging routes.

[Checking the Configurations of Basic BGP/MPLS IPv6 VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2062.html)

After configuring a basic BGP/MPLS IPv6 VPN, check information about the VPN instance IPv6 address family created on the PE, including the RD and other attributes and also information about the IPv6 VPN routes to the local and remote sites on the PE and CE.