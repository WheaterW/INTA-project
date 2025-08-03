Configuring IGMP Snooping over EVPN MPLS
========================================

IGMP snooping over EVPN MPLS can be configured to save bandwidth resources for EVPN networks that carry multicast traffic.

#### Usage Scenario

By default, when the EVPN function is deployed on a network to carry Layer 2 multicast services, multicast data packets are broadcast on the network. The devices that do not need to receive the multicast data packets also receive these packets, wasting network bandwidth resources. To resolve this issue, deploy IGMP snooping over EVPN MPLS. After IGMP snooping over EVPN MPLS is deployed, IGMP snooping packets are transmitted on the network through EVPN routes, and multicast forwarding entries are generated on devices. Multicast data packets from a multicast source are advertised only to the devices that need these packets, saving network bandwidth resources.

**Figure 1** IGMP snooping over EVPN MPLS networking  
![](images/fig_dc_vrp_evpn_cfg_009101.png)
#### Pre-configuration Tasks

Before configuring IGMP snooping over EVPN MPLS, complete the following task:

* [Configure BD EVPN functions](dc_vrp_evpn_cfg_0065.html).


[Configuring EVPN VPLS over mLDP P2MP Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0077.html)

An EVPN can carry multicast services. To reduce redundant traffic and conserve bandwidth resources, you can configure EVPN to use mLDP P2MP tunnels for service transmission.

[Configuring IGMP Snooping and Proxy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0092.html)

To implement IGMP snooping over EVPN MPLS, you must configure basic IGMP snooping and proxy functions.

[Configuring the Access Side](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0093.html)

You can configure IGMP snooping over EVPN MPLS on the access side of an EVPN that carries multicast services for various scenarios.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0094.html)

After configuring IGMP snooping over EVPN, verify the received EVPN routes and VPN routes on devices.