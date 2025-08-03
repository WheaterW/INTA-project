Configuring Dynamic BFD to Monitor an LDP Tunnel
================================================

Dynamic BFD can be configured to establish a dynamic BFD session to monitor both primary and backup LDP LSPs in an LDP tunnel. If BFD detects a fault, BFD instructs a specific LDP upper-layer application to perform a protection switchover.

#### Usage Scenario

When LDP LSPs transmit application traffic, for example, VPN traffic, to improve network reliability, LDP FRR and an LDP upper-layer protection mechanism, such as VPN FRR or VPN equal-cost multipath (ECMP), are used. BFD for LDP LSP only detects primary LSP faults and switches traffic to an FRR LSP. If the primary and FRR LSP fail simultaneously, the BFD mechanism does not take effect. In this situation, LDP can instruct its upper-layer application to perform a protection switchover only after LDP detects the FRR LSP failure. As a result, a great number of packets are dropped.![](../../../../public_sys-resources/note_3.0-en-us.png) 

For applications, for example, VPN, which are transmitted over LDP LSPs, the primary and backup LDP LSPs are collectively called LDP tunnels.


To minimize packet loss, dynamic BFD can be configured to establish dynamic BFD sessions to monitor both the primary and FRR LSPs. If both primary and FRR LSPs fail, BFD rapidly detects the failures and instructs a specific LDP upper-layer application to perform a protection switchover.


#### Pre-configuration Tasks

Before configuring dynamic BFD to monitor an LDP tunnel, complete the following tasks:

* Configure basic MPLS functions.
* Configure MPLS LDP.
* (Optional) Configure an IP address prefix list if it is used to trigger LDP LSP establishment.
* (Optional) Configure a FEC list if it is used to trigger LDP LSP establishment.


[Enabling an MPLS Device to Dynamically Establish a BFD Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0074.html)

A dynamic BFD session that monitors both the primary and FRR LSPs can be established only after an MPLS device is enabled to dynamically establish the BFD session.

[Configuring a Policy for Triggering Dynamic BFD for LDP Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0075.html)

Either the host address-based policy or FEC list-based policy can be used to dynamically establish BFD sessions to monitor LDP tunnels.

[(Optional) Modifying BFD Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_00761.html)

BFD parameters, such as BFD detection intervals and detection multipliers, can be modified.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0076.html)

After configuring dynamic BFD to monitor an LDP tunnel, you can view BFD session information on the ingress on which an LDP tunnel is established.