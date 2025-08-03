Configuring BFD to Monitor VPN Routes
=====================================

You can configure BFD to monitor a VPN route to check whether the VPN route is reachable.

#### Usage Scenario

To rapidly monitor a VPN route, configure BFD to monitor it.


#### Pre-configuration Tasks

Before configuring BFD to detect a VPN route, complete the following task:

* Configure network layer attributes for interfaces to ensure network connectivity.
* Configure a VPN instance on each PE.


[Enabling BFD Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0013.html)

BFD must be enabled globally before BFD is configured.

[Establishing a BFD Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0014.html)

You can establish a BFD session on both ends of a link to detect faults in a VPN route.

[(Optional) Configuring BFD Packets to Be Transparently Transmitted on an Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_bfd_cfg_0001a.html)

On a network, if a customer-side router that functions as a CE has the default BFD function enabled by using the **bfd bind peer-ip default-ip** command, the default BFD packets received by a PE are sent to the CPU instead of being transparently transmitted to the peer CE. In this case, you can adjust the forwarding mode of multicast IPv4 BFD packets on the interface and its sub-interfaces to enable the BFD packets to be transparently transmitted.

[(Optional) Changing the BFD Detection Time](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0007a.html)

This section describes how to change the BFD detection time so that the BFD session monitors links on a network more efficiently.

[(Optional) Setting the BFD WTR Time](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0034.html)

Setting a wait to restore (WTR) time for a BFD session can prevent applications from being frequently switched between the master and backup devices due to BFD session flapping.

[(Optional) Configuring a Description for a BFD Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0035.html)

You can configure a description for a BFD session to identify this session.

[(Optional) Setting the Priority of a BFD Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0036.html)

Setting the priority of a BFD session can ensure that packets with a higher priority are forwarded.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0015.html)

After configuring BFD to monitor a VPN route, verify the configurations, including the session type and status.