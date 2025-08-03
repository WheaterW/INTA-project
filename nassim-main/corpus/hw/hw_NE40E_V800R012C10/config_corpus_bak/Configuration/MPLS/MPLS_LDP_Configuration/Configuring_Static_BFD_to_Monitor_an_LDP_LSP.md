Configuring Static BFD to Monitor an LDP LSP
============================================

Static bidirectional forwarding detection (BFD) can be configured to detect faults in an LDP LSP.

#### Usage Scenario

BFD implements fast detection at the millisecond level. To enable a device to rapidly monitor whether LDP LSPs are faulty, establish BFD sessions.

When configuring static BFD to monitor an LDP LSP, note the following:

* You can bind a BFD session to an LDP LSP only on the ingress.
* An LDP LSP to be monitored by static BFD can be established only using host routes.

#### Pre-configuration Tasks

Before configuring static BFD to monitor an LDP LSP, complete the following tasks:

* Configure network layer parameters to implement network layer connectivity.
* Enable MPLS LDP on each node and set up an LDP session.
* Configure an LDP LSP.


[Enabling BFD Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_2034.html)

BFD must be enabled globally before BFD configurations are performed.

[Setting BFD Parameters on the Ingress](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_2035.html)

BFD parameters must be configured on the ingress before a BFD session is established to monitor an LDP LSP.

[Setting BFD Parameters on the Egress](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_2036.html)

BFD parameters must be configured on the egress before a BFD session is established to monitor an LDP LSP.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_2037.html)

After configuring BFD to monitor an LDP LSP, verify the configurations of the BFD session, such as the session type and status.