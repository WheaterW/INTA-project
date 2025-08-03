Configuring SVC VPWS
====================

Configuring_SVC_VPWS

#### Usage Scenario

A static PW does not use signaling protocols to send L2VPN packets. Packets are transmitted between PEs over a tunnel.

The tunnel carrying a static PW can be an LDP LSP, or CR-LSP, or GRE tunnel.


#### Pre-configuration Tasks

Before configuring SVC VPWS, complete the following tasks:

* Configure static routes or an IGP on PEs and Ps of the MPLS backbone network to ensure IP connectivity.
* Configure basic MPLS functions on PEs and Ps of the MPLS backbone network.
* Establish tunnels between PEs based on the tunnel policy (if no tunnel policy is configured, LDP tunnels are used by default).


[(Optional) Configuring Flow Label-based Load Balancing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6014-01.html)

Flow label-based load balancing enables L2VPN data flows on a PW to be load-balanced over tunnels between P devices based on flow labels, improving forwarding efficiency.

[(Optional) Configuring an AC Interface to Transparently Transmitting TDM Frames/ATM Cells](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6006-01.html)

A PW can be configured on an AC interface only after the AC interface has been configured to transparently transmit TDM frames/ATM cells.

[(Optional) Configuring a PW Template](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6001.html)

A PW template is a collection of common PW attributes. Configuring PWs using a PW template helps save configuration workload.

[Configuring a VPWS PW](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6002.html)

Before configuring a static PW, you must specify the VC label. Configuring a dynamic PW does not require this operation.

[Configuring VPWS Heterogeneous Interworking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6003.html)

If AC types at the two ends of a VPWS PW are different, configure VPWS heterogeneous interworking for the two CEs to communicate.

[(Optional) Configuring a Secondary VPWS Connection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6004.html)

This section describes how to configure a secondary VPWS connection for VLL FRR, so that L2VPN traffic can be quickly switched to the backup path if the primary path fails. After the primary path recovers, the L2VPN traffic can be switched back to it according to the revertive switching policy.

[(Optional) Disabling the PW Source Interface Check Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_vpls_cfg_5011_vpws.html)

On a VPLS/VPWS network, the PW source interface check function is enabled by default, affecting system performance.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6005.html)

After configuring a static PW, check information about the PW.