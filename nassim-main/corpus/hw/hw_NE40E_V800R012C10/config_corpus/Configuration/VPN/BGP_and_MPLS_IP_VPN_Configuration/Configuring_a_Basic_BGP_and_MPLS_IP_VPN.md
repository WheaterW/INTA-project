Configuring a Basic BGP/MPLS IP VPN
===================================

A basic BGP/MPLS IP VPN applies to the scenario in which there is only one carrier or the backbone networks of multiple carriers belong to the same AS, and each device plays only one role, either PE, P, or CE. After a basic BGP/MPLS IP VPN is configured, different sites in a VPN can communicate with each other.

#### Usage Scenario

After a basic BGP/MPLS IP VPN is configured, the network can provide VPN services for users so that multiple private networks can communicate across the backbone network of the carrier. VPN routes are isolated from the public network routes on the backbone network, and the routes of VPN instances are isolated from each other.

On the network shown in [Figure 1](#EN-US_TASK_0172369246__fig1224152141810), the following functions need to be implemented:

* Site 1 can communicate with only Site 3.
* Site 2 can communicate with only Site 4.
* The MPLS backbone network is unaware of the VPN routes in each site.

To meet the preceding requirements, configure a basic BGP/MPLS IP VPN by adding Site 1 and Site 3 to a VPN (VPN 1) and Site 2 and Site 4 to another VPN (VPN 2). CEs and other devices deployed at sites only advertise and receive VPN routes. They are unaware of the public network. Ps residing on the public network do not receive VPN routes. PEs manage VPN routes and public network routes separately. VPN data packets are transmitted transparently over tunnels between the sites within the same VPN. The devices on the public network do not know the contents of VPN data packets, ensuring VPN data security.
**Figure 1** BGP/MPLS IP VPN  
![](figure/en-us_image_0000001431152178.png)

#### Pre-configuration Tasks

Before configuring a basic BGP/MPLS IP VPN, complete the following tasks:

* Configure the routing policy to control the route receiving and sending of the VPN instance IPv4 address family if needed.
* Configure an IGP on the PEs and Ps of the MPLS backbone network to ensure IP connectivity on the backbone network.
* Establish non-LDP LSP tunnels based on tunnel policies or LDP LSPs on the MPLS backbone network.
* Configure IP addresses on interfaces that connect CEs to PEs.


[Configuring a VPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0155.html)

A VPN instance can be configured on a PE to manage VPN routes.

[Binding Interfaces to a VPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0156.html)

After an interface is bound to a VPN instance, the interface becomes a part of the VPN. Packets entering the interface will be forwarded based on the VRF table of the VPN.

[(Optional) Configuring a Router ID for a BGP-VPN Instance IPv4 Address Family](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_2005.html)

You can configure different router IDs for BGP VPN instance IPv4 address families on the same device.

[Establishing MP-IBGP Peer Relationships Between PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0157.html)

By introducing extended community attributes into BGP, MP-IBGP can advertise VPNv4 routes between PEs.

[Configuring Route Exchange Between PEs and CEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0158.html)

To enable CEs to communicate, the PEs and CEs must be capable of exchanging routes.

[(Optional) Configuring One-Label-per-Next-Hop Label Distribution](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0300.html)

To save label resources on a PE, configure one-label-per-next-hop label distribution on the PE. Only one label is allocated to the VPNv4 routes that have the same next-hop address and outgoing label.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0159.html)

After configuring a basic BGP/MPLS IP VPN, check information about the VPN instance IPv4 address family created on the PE, including the RD and other attributes. You can also check information about IPv4 VPN routes to the local and remote sites on the PE and CE.