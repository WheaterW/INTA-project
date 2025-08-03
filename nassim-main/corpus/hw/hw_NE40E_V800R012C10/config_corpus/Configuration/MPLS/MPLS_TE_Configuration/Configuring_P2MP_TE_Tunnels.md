Configuring P2MP TE Tunnels
===========================

A P2MP TE tunnel provides sufficient network bandwidth and high reliability for multicast service transmission on an IP/MPLS backbone network.

#### Usage Scenario

The demand for multicast services, such as IPTV, multimedia conferences, and massively multiplayer online role-playing games (MMORPGs), has steadily increased on IP/MPLS backbone networks. These services require sufficient network bandwidth, assured quality of service (QoS), and high reliability. The following multicast solutions are available, but are insufficient for the requirements of multicast services or network carriers:

* IP multicast technology: deployed on a live P2P network with upgraded software. This solution reduces upgrade and maintenance costs. IP multicast, similar to IP unicast, does not support QoS or TE capabilities and has low reliability.
* Dedicated multicast network: deployed using Asynchronous Transfer Mode (ATM) or synchronous optical network (SONET)/synchronous digital hierarchy (SDH) technologies. This solution provides high reliability and transmission rates, but has high construction costs and requires separate maintenance.

IP/MPLS backbone network carriers require a multicast solution that has high TE capabilities and can be implemented by upgrading existing devices.

P2MP TE is such a solution. It provides high reliability and QoS as well as TE capabilities. P2MP TE can be implemented on an IP/MPLS backbone network by simple configuration to provide multicast services, which reduces upgrade and maintenance costs and helps network convergence.

P2MP TE tunnels can be manually or automatically established. [Table 1](#EN-US_TASK_0172368135__tab_dc_vrp_te-p2p_cfg_013301) compares manual P2MP tunnels with automatic P2MP TE tunnels.

**Table 1** Comparison between manual and automatic P2MP TE tunnels
| Item | Manual P2MP TE Tunnel | Automatic P2MP TE Tunnel |
| --- | --- | --- |
| Trigger method | Manually triggered by users. | Automatically triggered by services. |
| Usage scenario | Multicast services, excluding NG MVPN or multicast VPLS, are transmitted. | NG MVPN or multicast VPLS services are transmitted. |
| Traffic import method | PIM or static IGMP is used to direct services to LSPs. | Services are automatically directed to LSPs. |




#### Pre-configuration Tasks

Before configuring P2MP TE tunnels, complete the following tasks:

* Configure OSPF or IS-IS to implement IP connectivity between nodes on the P2MP TE tunnel.
* [Enable MPLS TE and RSVP-TE.](dc_vrp_te-p2p_cfg_0004.html)
* [Configure CSPF.](dc_vrp_te-p2p_cfg_0009.html)
* [Configure OSPF or IS-IS TE.](dc_vrp_te-p2p_cfg_0005.html)
* [(Optional) Configure MPLS TE attributes for links.](dc_vrp_te-p2p_cfg_0006.html)

#### Configuration Procedures

**Figure 1** Flowchart for configuring P2MP TE tunnels  
![](images/fig_dc_vrp_te-p2p_cfg_013303.png)


[Enabling P2MP TE Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0134.html)

This section describes how to enable P2MP TE globally on each node before a P2MP TE tunnel is established.

[(Optional) Disabling P2MP TE on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0193.html)

You can disable P2MP TE on a specific interface during the network planning.

[(Optional) Setting Leaf Switching and Deletion Delays](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0216.html)

To prevent two copies of traffic on a P2MP TE tunnel's egress, a leaf CR-LSP switchover hold-off time and a deletion hold-off time can be set for MBB.

[Configuring Leaf Lists](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0135.html)

Configuring a leaf list on an ingress specifies all leaf nodes on a P2MP TE tunnel. A leaf list helps you configure and manage these leaf nodes uniformly. The steps in this section must be performed if P2MP TE tunnels are manually established. The steps in this section are optional if the establishment of P2MP TE tunnels is automatically triggered by a service.

[Configuring a P2MP TE Tunnel Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0136.html)

Configuring a tunnel interface on an ingress helps you to manage and maintain the P2MP TE tunnel.

[(Optional) Configuring a P2MP Tunnel Template](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0194.html)

Attributes can be set in a P2MP tunnel template that is used to automatically establish P2MP TE tunnels.

[(Optional) Configuring a P2MP TE Tunnel to Support Soft Preemption](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0251.html)

Priorities and preemption are used to allow TE tunnels to be established preferentially to transmit important services, preventing resource competition during tunnel establishment.

[(Optional) Configuring the Reliability Enhancement Function for a P2MP Tunnel](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_te-p2p_cfg_6014.html)

Configure a function to improve service reliability as needed.

[Verifying the P2MP TE Tunnel Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0137.html)

After configuring a P2MP TE tunnel, you can view information about the tunnel when it is in the Up state.