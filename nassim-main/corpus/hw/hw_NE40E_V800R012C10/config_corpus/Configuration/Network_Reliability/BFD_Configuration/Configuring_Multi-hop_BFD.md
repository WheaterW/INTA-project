Configuring Multi-hop BFD
=========================

Multi-hop BFD helps a device rapidly detect faults in a multi-hop link on a network.

#### Usage Scenario

To monitor IP route forwarding continuity, configure multi-hop BFD.


#### Pre-configuration Tasks

Before configuring multi-hop BFD, complete the following tasks:

* Set link layer protocol parameters for each interface to ensure that the link protocol status of the interface is Up.
* Assign an IP address to each interface.
* Configure a routing protocol to ensure that the network layer is reachable.


[Enabling BFD Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0023.html)

BFD must be enabled globally before BFD is configured.

[Establishing a BFD Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0024.html)

You can establish a BFD session on both ends of a multi-hop link to rapidly detect link faults.

[(Optional) Configuring BFD Packets to Be Transparently Transmitted on an Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_bfd_cfg_0001c.html)

On a network, if a customer-side router that functions as a CE has the default BFD function enabled by using the **bfd bind peer-ip default-ip** command, the default BFD packets received by a PE are sent to the CPU instead of being transparently transmitted to the peer CE. In this case, you can adjust the forwarding mode of multicast IPv4 BFD packets on the interface and its sub-interfaces to enable the BFD packets to be transparently transmitted.

[(Optional) Changing the BFD Detection Time](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0029.html)

This section describes how to change the BFD detection time so that the BFD session monitors links on a network more efficiently.

[(Optional) Setting the BFD WTR Time](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0030.html)

Setting a wait to restore (WTR) time for a BFD session can prevent applications from being frequently switched between the master and backup devices due to BFD session flapping.

[(Optional) Configuring a Description for a BFD Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0031.html)

You can configure a description for a BFD session to identify this session.

[(Optional) Setting the Priority of a BFD Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0038.html)

Setting the priority of a BFD session can ensure that packets with a higher priority are forwarded.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0025.html)

After configuring multi-hop BFD, verify the configurations, such as the type of the BFD session (multi-hop) and the status of the BFD session (up).