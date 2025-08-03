Configuring mLDP In-Band MVPN
=============================

mLDP in-band MVPN allows IP multicast services to run on a BGP/MPLS IP VPN, ensuring reliability, security, and efficiency of IP multicast services.

#### Usage Scenario

Multicast services, such as IPTV, multimedia conferencing, and real-time multiplayer online games, continue to grow in popularity. Transmission of these services has the following requirements on the service bearer network:

* Multicast traffic can be forwarded smoothly, even during traffic congestion.
* Network faults can be detected in time, and traffic can be switched to a backup path immediately upon fault detection.
* Multicast traffic security can be ensured in real time.

To solve multicast service issues related to traffic congestion, reliability, and security, you can deploy mLDP in-band MVPN on the service provider's backbone network. [Figure 1](#EN-US_TASK_0000001270194457__fig_dc_vrp_cfg_ngmvpn_000401) shows the typical networking of mLDP in-band MVPN.**Figure 1** Typical networking of mLDP in-band MVPN  
![](figure/en-us_image_0000001270154553.png)


#### Pre-configuration Tasks

Before configuring mLDP in-band MVPN, complete the following tasks:

* [Configure a basic BGP/MPLS IP VPN](dc_vrp_mpls-l3vpn-v4_cfg_0154.html).
* [Configure an automatic mLDP P2MP tunnel](dc_vrp_ldp-p2p_cfg_0062.html) on the root and leaf nodes.


[Configuring Multicast Traffic Transmission over P2MP Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_mldp-in-band_0004.html)

mLDP in-band MVPN uses mLDP P2MP tunnels to carry multicast traffic.

[Configuring PIM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_mldp-in-band_0005.html)

Configuring PIM on a VPN allows a VPN multicast routing table to be established to guide multicast traffic forwarding.

[(Optional) Configuring IGMP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_mldp-in-band_0006.html)

Configuring IGMP on the interfaces connecting a multicast device to a user network segment allows the device to manage multicast group members on that network segment.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_mldp-in-band_0007.html)

After configuring mLDP in-band MVPN, check the BGP unicast peer relationships, unicast routes, and PIM routing tables of VPN instances on a PE.