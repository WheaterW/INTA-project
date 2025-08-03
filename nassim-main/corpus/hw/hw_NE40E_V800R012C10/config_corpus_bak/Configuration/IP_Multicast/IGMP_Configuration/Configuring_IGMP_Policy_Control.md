Configuring IGMP Policy Control
===============================

IGMP policy control restricts or extends IGMP actions, without affecting the IGMP implementation.

#### Usage Scenario

To implement IGMP policy control, perform the following configurations:

* [Configure the maximum number of IGMP entries on an interface](dc_vrp_multicast_cfg_2255.html) to limit the number of multicast groups, including source-specific groups, on the interface. This mechanism enables users who have successfully joined multicast groups to enjoy smoother multicast services.
* [Set the range of multicast groups that an interface can join](dc_vrp_multicast_cfg_2048.html) by configuring a group policy on a Router interface. This configuration allows the Router interface to set restrictions on specific multicast groups, so that entries will not be created for the restricted multicast groups. This improves IGMP security.
* [Configure source address-based IGMP message filtering](dc_vrp_multicast_cfg_2223.html) by specifying multicast source addresses used to filter IGMP messages. This configuration prevents forged IGMP message attacks and enhances multicast network security.


#### Pre-configuration Tasks

Before configuring IGMP Policy Control, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure basic IGMP functions](dc_vrp_multicast_cfg_2044.html).


[Configuring the maximum number of IGMP entries on an interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2255.html)

IGMP-limit is configured on Router interfaces connected to users to limit the maximum number of multicast groups, including source-specific multicast groups. This mechanism enables users who have successfully joined multicast groups to enjoy smoother multicast services.

[Setting the Range of Multicast Groups that an Interface Can Join](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2048.html)

To limit the range of multicast groups that an interface can join, configure an IGMP group policy. Then, the interface can join only IGMP groups that are permitted in this policy.

[Configuring Source Address-based IGMP Message Filtering](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2223.html)

Source address-based IGMP message filtering is a security policy used for filtering IGMP message on the Router's interface connected to user hosts.

[Configuring the Rate at Which IGMP Packets Are Sent to the CPU](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mcast_cfg_2004.html)

You can configure the rate at which IGMP packets are sent to the CPU to reduce CPU usage of a device and protect the device against attacks.

[Configuring Micro-Isolation CAR for IGMP](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mcast_cfg_2005.html)



[Verifying the IGMP Policy Control Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2256.html)

After configuring IGMP Policy Control, verify the IGMP configuration and IGMP operating status.