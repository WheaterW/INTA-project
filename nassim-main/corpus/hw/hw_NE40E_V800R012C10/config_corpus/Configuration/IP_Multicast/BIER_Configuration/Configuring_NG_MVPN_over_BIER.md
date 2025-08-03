Configuring NG MVPN over BIER
=============================

Bit index Index explicit Explicit replication Replication (BIER) can replace mLDP P2MP and RSVP TE P2MP technologies, and provides public network tunnels to transmit next-generation multicast VPN (NG MVPN) traffic.

#### Usage Scenario

Multicast services, such as IPTV services, video conferences, and real-time multiplayer online games, are used increasingly in daily life. These services are transmitted over service bearer networks that need to:

* Forward multicast traffic smoothly even during traffic congestion.
* Detect network faults in time and quickly switch traffic from faulty links to normal links.
* Ensure multicast traffic security in real time.

To solve multicast service issues related to traffic congestion, transmission reliability, and data security, deploy NG MVPN over BIER on the service provider's backbone network. [Figure 1](#EN-US_TASK_0178645712__fig_dc_vrp_cfg_ngmvpn_000401) shows the basic NG MVPN over BIER model.**Figure 1** Typical NG MVPN over BIER scenario  
![](images/fig_dc_vrp_cfg_ngmvpn_000401.png)


#### Pre-configuration Tasks

Before configuring NG MVPN over BIER, [configure basic BGP/MPLS IP VPN functions.](dc_vrp_mpls-l3vpn-v4_cfg_0154.html)


[Configuring BIER on the Public Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_bier_cfg_011.html)

In the NG MVPN over BIER scenario, you need to configure all devices in each BIER sub-domain on the public network.

[Enabling BIER for an IGP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_bier_cfg_012.html)

Information such as the BFR-IDs and IP addresses of BIER nodes in each BIER sub-domain needs to be flooded through an IGP, and then BIER forwarding information is generated on each node on the network.

[Configuring BGP MVPN Peer Relationships](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_bier_cfg_013.html)

You need to configure BGP MVPN peer relationships between PEs in the same MVPN so that the PEs can use BGP to exchange BGP A-D and BGP C-multicast routes.

[Configuring a BIER Tunnel to Carry Multicast Traffic](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_bier_cfg_014.html)

NG MVPNs use BIER P2MP tunnels to carry multicast traffic. 

[(Optional) Configuring Switching Between I-PMSI and S-PMSI Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_bier_cfg_015.html)



[Configuring PIM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_bier_cfg_016.html)

Configuring PIM on a VPN allows a VPN multicast routing table to be established to guide multicast traffic forwarding.

[(Optional) Configuring IGMP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_bier_cfg_017.html)

Configuring IGMP on the interfaces connecting a multicast device to a user network segment allows the device to manage multicast group members on the network segment.

[Verifying the NG MVPN over BIER Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_bier_cfg_018.html)

After configuring NG MVPN over BIER, verify the configuration.