Configuring BFD to Monitor an IP Link
=====================================

This section describes how to configure a single-hop BFD session to rapidly monitor IP links on a network.

#### Usage Scenario

To rapidly monitor an IP link on a network, configure BFD to detect faults in the IP link.


#### Pre-configuration Tasks

Before configuring BFD to monitor an IP link, complete the following tasks:

* Set link layer protocol parameters for each interface to ensure that the link protocol status of the interface is Up.
* Assign an IP address to each interface.


[Enabling BFD Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0005.html)

BFD must be enabled globally before BFD is configured.

[Establishing a BFD Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0006.html)

You can establish a BFD session on both ends of a direct link to rapidly detect link faults.

[(Optional) Configuring BFD Packets to Be Transparently Transmitted on an Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_bfd_cfg_0001.html)

On a network, if a customer-side router that functions as a CE has the default BFD function enabled by using the **bfd bind peer-ip default-ip** command, the default BFD packets received by a PE are sent to the CPU instead of being transparently transmitted to the peer CE. In this case, you can adjust the forwarding mode of multicast IPv4 BFD packets on the interface and its sub-interfaces to enable the BFD packets to be transparently transmitted.

[(Optional) Changing the BFD Detection Time](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0007.html)

This section describes how to change the BFD detection time so that the BFD session monitors links on a network more efficiently.

[(Optional) Setting the BFD WTR Time](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0008.html)

Setting a wait to restore (WTR) time for a BFD session can prevent applications from being frequently switched between the master and backup devices due to BFD session flapping.

[(Optional) Configuring a Description for a BFD Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0009.html)

You can configure a description for a BFD session to identify this session.

[(Optional) Setting the Priority of a BFD Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0080.html)

Setting the priority of a BFD session can ensure that packets with a higher priority are forwarded.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0010.html)

After configuring the BFD detection parameters, verify the configurations, including the minimum intervals at which BFD control packets are sent and received, WTR time, and description of the BFD session.