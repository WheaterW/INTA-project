Configuring CCC VPWS PWs
========================

This section describes how to establish a local CCC connection and a remote CCC connection for CEs to communicate.

#### Usage Scenario

CCC requires manual configuration by network administrators and is best suited for small MPLS networks with simple topologies. Because CCC does not require signaling negotiation or control packet exchange, it consumes relatively few resources. However, CCC has poor scalability and is difficult to maintain.


#### Pre-configuration Tasks

Before configuring CCC VPWS, complete the following tasks:

* Configure static routes or an IGP on the PEs and Ps of the MPLS backbone network to ensure IP connectivity.
* Configure basic MPLS functions on the PEs and Ps of the MPLS backbone network.
* Establish tunnels between PEs based on tunnel policies. If no tunnel policy is configured, LDP tunnels are established by default.


[Creating a Local CCC Connection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6023.html)

Creating a local CCC connection enables two CEs that connect to the same PE to communicate.

[Creating a Remote CCC Connection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6024.html)

Creating remote CCC connections enables two CEs that connect to different PEs to communicate.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6025.html)

After configuring a CCC VPWS PW, you can check CCC connection information, such as interfaces used by the CCC connection.