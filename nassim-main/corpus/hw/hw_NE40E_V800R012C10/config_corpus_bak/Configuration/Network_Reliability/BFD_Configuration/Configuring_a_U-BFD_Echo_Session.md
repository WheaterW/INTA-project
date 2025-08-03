Configuring a U-BFD Echo Session
================================

This section describes how to configure a U-BFD echo session to rapidly monitor a direct link on a network.

#### Usage Scenario

U-BFD echo is used when two devices are directly connected and only one of them supports BFD. To rapidly detect faults on the link between the two devices, configure a U-BFD echo session on the device that supports BFD. After receiving a BFD echo packet, the device that does not support BFD immediately loops back the packet for quick link monitoring.


#### Pre-configuration Tasks

Before configuring a U-BFD echo session, complete the following tasks:

* Connect interfaces.
* Assign an IP address to each Layer 3 interface.


[Enabling BFD Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0109.html)

BFD must be enabled globally before BFD is configured.

[Creating a U-BFD Echo Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0110.html)

A BFD session can be established on a BFD-enabled device to rapidly detect faults in a direct link.

[(Optional) Configuring BFD Packets to Be Transparently Transmitted on an Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_bfd_cfg_0001g.html)

On a network, if a customer-side router that functions as a CE has the default BFD function enabled by using the **bfd bind peer-ip default-ip** command, the default BFD packets received by a PE are sent to the CPU instead of being transparently transmitted to the peer CE. In this case, you can adjust the forwarding mode of multicast IPv4 BFD packets on the interface and its sub-interfaces to enable the BFD packets to be transparently transmitted.

[(Optional) Changing the BFD Detection Time](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0111.html)

This section describes how to change the BFD detection time to more efficiently use a BFD session to monitor links on a network.

[(Optional) Setting the BFD WTR Time](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_000800.html)

You can set the BFD wait to restore (WTR) time to prevent an application from switching between the master and slave devices due to BFD session flapping.

[(Optional) Configuring a Description for a BFD session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0043.html)

You can configure a description for a BFD session to identify this session.

[(Optional) Setting the Priority of a BFD Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0044.html)

Setting the priority of a BFD session can ensure that packets with a higher priority are forwarded.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0112.html)

After configuring the BFD detection parameters, verify the configurations, including the minimum intervals at which packets are sent and received, WTR time, and description of the session.