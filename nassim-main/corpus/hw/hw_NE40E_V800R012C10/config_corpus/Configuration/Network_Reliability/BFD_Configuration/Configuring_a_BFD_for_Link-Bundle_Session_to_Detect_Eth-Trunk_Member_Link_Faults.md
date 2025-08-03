Configuring a BFD for Link-Bundle Session to Detect Eth-Trunk Member Link Faults
================================================================================

You can configure a BFD for link-bundle session to monitor Eth-Trunk member links and rapidly detect link faults.

#### Usage Scenario

Two routing devices are connected through an Eth-Trunk that has multiple member interfaces. To detect faults on the Eth-Trunk link between the two devices, you can configure a BFD for link-bundle or multicast BFD session.


#### Pre-configuration Tasks

Before configuring a BFD for link-bundle session to detect Eth-Trunk member link faults, complete the following tasks:

* Configure an Eth-Trunk interface and ensure that the link layer protocol on the interface is up.


[Enabling BFD Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0122.html)

BFD must be enabled globally before BFD is configured.

[Establishing BFD for Eth-Trunk Member Links](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0115.html)

BFD for link-bundle sessions are used to detect faults on Eth-Trunk member links.

[(Optional) Configuring BFD Packets to Be Transparently Transmitted on an Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_bfd_cfg_0001f.html)

On a network, if a customer-side router that functions as a CE has the default BFD function enabled by using the **bfd bind peer-ip default-ip** command, the default BFD packets received by a PE are sent to the CPU instead of being transparently transmitted to the peer CE. In this case, you can adjust the forwarding mode of multicast IPv4 BFD packets on the interface and its sub-interfaces to enable the BFD packets to be transparently transmitted.

[(Optional) Changing the BFD Detection Time](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0119.html)

This section describes how to change the BFD detection time so that the BFD session monitors links on a network more efficiently.

[(Optional) Setting the BFD WTR Time](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_01200.html)

Setting a wait to restore (WTR) time for a BFD session can prevent applications from being frequently switched between the master and backup devices due to BFD session flapping.

[(Optional) Configuring a Priority of a BFD Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0037.html)

Setting the priority of a BFD session can ensure that packets with a higher priority are forwarded.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0118.html)

After configuring a BFD for link-bundle session to detect Eth-Trunk member link faults, verify the configuration.