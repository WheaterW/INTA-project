Configuring BGP VPWS
====================

BGP VPWS uses BGP as the signaling protocol to transmit
Layer 2 information and VC labels and implements VPWS in a point-to-point
manner on an MPLS network.

#### Usage Scenario

BGP VPWS uses VPN targets
to control route exchange, creating greater networking flexibility.

BGP VPWS uses label blocks to allocate labels. A PE can allocate
a label block to every CE connecting to the PE. The label block size
determines the number of connections that can be established between
the local CE and other CEs. VC labels for transmitting packets are
calculated based on label blocks. BGP VPWS allows for allocation of
additional labels to a CE for future VPN capacity expansion.

Typical BGP VPWS scenarios include:

* [Configuring a Local BGP VPWS Connection](dc_vrp_vpws_cfg_6055.html)
* [Configuring a Remote BGP VPWS Connection](dc_vrp_vpws_cfg_6056.html)


#### Pre-configuration Tasks

Before configuring
BGP VPWS, complete the following tasks:

* Configure static routes or an IGP on the PEs and Ps of the
  MPLS backbone network to ensure IP connectivity.
* Configure basic MPLS functions on the PEs and Ps of the MPLS
  backbone network.
* Establish tunnels between PEs based on the tunnel policy.


[Configuring a Local BGP VPWS Connection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6055.html)

If two CEs connect to the same PE, you can configure a local BGP VPWS connection for the two CEs to communicate.

[Configuring a Remote BGP VPWS Connection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6056.html)

If two CEs connect to different PEs, you can configure a remote BGP VPWS connection for the two CEs to communicate.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6057.html)