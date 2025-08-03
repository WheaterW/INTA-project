Configuring Basic RIP Functions
===============================

To use RIP features, start RIP and specify the network segment and RIP version first.

#### Usage Scenario

Configuring basic RIP functions is a prerequisite for building RIP networks.


#### Pre-configuration Tasks

Before configuring basic RIP functions, complete the following tasks:

* Configure the link layer protocol.
* Configure network layer addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.


[Creating a RIP process](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0004.html)

The creation of a RIP process is a precondition of all RIP configurations.

[Enabling RIP on Specified Network Segments](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0005.html)

To enable a RIP process to receive and send RIP routes on specified network segments, enable RIP for the network segments first.

[(Optional) Configuring the RIP Version Number](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0006.html)

RIP includes RIP-1 and RIP-2. The two versions have different functions.

[(Optional) Configuring a RIP Preference](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0023.html)

When there are routes discovered by multiple routing protocols on the same device, you can set a preference for RIP to control the route selection result.

[(Optional) Disabling the Source Address Check for Packets on a P2P Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0007.html)

On a P2P network, the IP addresses of the two ends of a link can belong to different networks. In this case, the two ends can accept packets from each other only if the source address check is disabled.

[(Optional) Enabling Check on Zero Fields of RIP-1 Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0008.html)

Certain fields in RIP-1 packets must be 0, and these fields are called zero fields.

[Configuring an NBMA Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0009.html)

RIP packets on a Non-Broadcast Multiple Access (NBMA) network are sent in a mode different from those on networks of other types, and therefore, special configurations are required.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0010.html)

After basic RIP functions are configured, you can view the current running status of RIP and RIP routing information.