Configuring Multicast Control
=============================

With the large-scaled deployment of IPTV services, telecommunication operators have to authenticate users. Users have the rights to access multicast programs (by joining multicast groups) only after they pay the fee.

#### Usage Scenario

To control the rights of users to join related multicast groups, you can configure controllable multicast. To implement controllable multicast, you can configure a multicast profile, apply the profile to the domain to which the users belong, and enable controllable multicast on a bas interface.


#### Pre-configuration Tasks

Before configuring controllable multicast, complete the following tasks:

* Configuring a routing protocol on the backbone network to implement IP interworking
* Configuring access services to enable users to access the Internet normally


[Configuring a Multicast List](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mcontrol_cfg_0006.html)

A multicast list consists of one or more multicast addresses that are used to define one or more channels or programs.

[Configuring a Multicast Profile](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mcontrol_cfg_0007.html)

To authorize multicast users, you must bind a configured multicast list to a created multicast profile.

[Applying the Multicast Profile in a Domain](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mcontrol_cfg_0008.html)

After a multicast profile is bound to a domain, the users in this domain have the rights to access the multicast lists bound to the multicast profile.

[Enabling Controllable Multicast on the BAS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mcontrol_cfg_0009.html)

After controllable multicast is enabled on an interface, the interface controls the users' rights to access the multicast groups based on multicast configurations in the AAA view.

[Setting the Maximum Number of Multicast Lists that a User Is Allowed to Access at a Time](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mcontrol_cfg_0010.html)

A multicast list records multiple multicast addresses, that is, multicast programs. You can set the maximum number of multicast programs that a user is allowed to access at a time.

[Configuring Multicast Replication](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mcontrol_cfg_0011.html)

This section describes how to configure multicast replication. The NE40E uses a configured multicast replication method to copy multicast packets to its downstream Layer 2 devices.

[Verifying the Controllable Multicast Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mcontrol_cfg_0013.html)

After configuring controllable multicast successfully, verify information about the multicast list and multicast profile.