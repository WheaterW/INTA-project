Configuring the LDP Entropy Label Capability
============================================

The entropy label can be used to improve load balancing in traffic forwarding.

#### Usage Scenario

As user networks and the scope of network services continue to expand, load-balancing techniques are usually used to improve bandwidth between nodes. A great amount of traffic results in load imbalance on transit nodes. To address this problem, the entropy label capability can be configured to improve load balancing.

The entropy label feature applies to public network LDP tunnels in service scenarios such as IPv4/IPv6 over LDP, L3VPNv4/v6 over LDP, VPLS/VPWS over LDP, and EVPN over LDP.


[Configuring an LSR to Deeply Parse IP Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ldp-p2p_cfg_0004.html)

This section describes how to enable an LSR to deeply parse IP packets.

[Configuring an LDP Entropy Label on the Ingress of an LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0204.html)

An LDP entropy label can be configured on the ingress of an LSP to implement load balancing.

[Enabling the Entropy Label Capability on the Egress of an LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0206.html)

The entropy label capability can be configured on the egress of an LSP to load-balance traffic.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0207.html)

After configuring the LDP entropy label capability, you can check the entropy label information of tunnels.