Configuring a Static BFD Session with Automatically Negotiated Discriminators
=============================================================================

You can configure a static BFD session with automatically negotiated discriminators on a local device to enable the local device to interwork with the device on which a BFD session is dynamically set up. The static BFD session with automatically negotiated discriminators is used to monitor static routes.

#### Usage Scenario

If a dynamic BFD session is set up on the remote device, you must configure a static BFD session with automatically negotiated discriminators on the local device to interwork with the remote device and to allow static routes to track BFD.


#### Pre-configuration Tasks

Before configuring a static BFD session with automatically negotiated discriminators, complete the following tasks:

* Connect interfaces.
* Assign an IP address to each Layer 3 interface.


[Enabling BFD Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0018.html)

BFD must be enabled globally before BFD is configured.

[Establishing a BFD Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0019.html)

You can establish a static BFD session with automatically negotiated discriminators on both ends of the link to rapidly detect link faults.

[(Optional) Configuring BFD Packets to Be Transparently Transmitted on an Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_bfd_cfg_0001b.html)

On a network, if a customer-side router that functions as a CE has the default BFD function enabled by using the **bfd bind peer-ip default-ip** command, the default BFD packets received by a PE are sent to the CPU instead of being transparently transmitted to the peer CE. In this case, you can adjust the forwarding mode of multicast IPv4 BFD packets on the interface and its sub-interfaces to enable the BFD packets to be transparently transmitted.

[(Optional) Changing the BFD Detection Time](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0026.html)

This section describes how to change the BFD detection time so that the BFD session monitors links on a network more efficiently.

[(Optional) Setting the BFD WTR Time](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0027.html)

Setting a wait to restore (WTR) time for a BFD session can prevent applications from being frequently switched between the master and backup devices due to BFD session flapping.

[(Optional) Configuring a Description for a BFD Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0028.html)

You can configure a description for a BFD session to identify this session.

[(Optional) Configuring a Priority for a BFD Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0121.html)

Setting the priority of a BFD session can ensure that packets with a higher priority are forwarded.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0020.html)

After a static BFD session with automatically negotiated discriminators is successfully set up, verify the configurations, such as the type of the BFD session and automatically negotiated discriminators.