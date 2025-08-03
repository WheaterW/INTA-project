Configuring Dynamic BFD for TE CR-LSP
=====================================

Dynamic BFD for TE CR-LSP can be configured to monitor an RSVP CR-LSP and protect traffic along a CR-LSP.

#### Usage Scenario

Compared with static BFD, dynamically creating BFD sessions simplifies configurations and reduces configuration errors.

Currently, dynamic BFD for TE CR-LSP cannot detect faults in the entire TE tunnel.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

BFD for LSP can function properly though the forward path is an LSP and the reverse path is an IP link. The forward and reverse paths must be established over the same link. If a fault occurs, BFD cannot identify the faulty path. Before deploying BFD, ensure that the forward and reverse paths are over the same link so that BFD can correctly identify the faulty path.



#### Pre-configuration Tasks

Before configuring dynamic BFD for TE CR-LSP, configure an RSVP-TE tunnel.


[Enabling BFD Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0145.html)

To configure dynamic BFD for CR-LSP, enable BFD globally on the ingress node and the egress node of a tunnel.

[Enabling the Capability of Dynamically Creating BFD Sessions on the Ingress](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0146.html)

You can enable the ingress node to dynamically create BFD sessions on a TE tunnel either globally or on a specified tunnel interface.

[Enabling the Capability of Passively Creating BFD Sessions on the Egress](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0147.html)

On a unidirectional LSP, creating a BFD session on the ingress playing the active role triggers the sending of LSP ping request messages to the egress node playing the passive role. Only after the passive role receives the ping packets, a BFD session can be automatically established.

[(Optional) Adjusting BFD Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0148.html)

BFD parameters are adjusted on the ingress of a tunnel either globally or on a tunnel interface.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0149.html)

After configuring dynamic BFD for TE CR-LSP, you can verify that a CR-LSP is Up and a BFD session is successfully established.