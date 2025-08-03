Configuring Basic MLD Functions
===============================

To implement communication between user hosts and an IPv6 multicast network, configure basic MLD functions on the interfaces that connect multicast devices to user network segments.

#### Usage Scenario

MLD runs on the network segments that connect Routers to user hosts and must be configured on both routers and user hosts. This section describes how to configure MLD on a Router.

Before configuring MLD, enable IPv6 multicast routing, which is the prerequisite for configuring any other IPv6 multicast functions. When IPv6 multicast routing is disabled, all IPv6 multicast-related configurations will be deleted.

Configure an MLD version on a router's interface that connects to user hosts before you perform other MLD configurations on the router. A Router interface's MLD version is backward compatible with a user host's MLD version. Therefore, a Router interface's MLD version must be the same as or later than its connected user hosts' MLD versions.

By configuring Router interfaces to statically join an MLD multicast group, you can enable the Router to rapidly respond to users' requests, shortening the channel switching delay.

To make hosts on the network segment on which Router interfaces reside join specified MLD groups and receive multicast packets for these groups, define an ACL rule as a filter to restrict the range of MLD groups that the hosts can join. This improves MLD security.


#### Pre-configuration Tasks

Before configuring basic MLD functions, complete the following tasks:

* Configure link layer protocol parameters and assign IPv6 addresses to interfaces to ensure that the status of the link layer protocol on the interfaces is Up.
* Configure a unicast routing protocol to ensure that unicast routes are reachable.


[Enabling IPv6 Multicast Routing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2185b.html)

Enable IPv6 multicast routing on a Router before you configure other IPv6 multicast features on the Router.

[Enabling IPv6 PIM-SM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2186b.html)

To enable a Router interface to establish IPv6 PIM neighbor relationships with other Routers, enable IPv6 PIM-SM.

[Enabling MLD](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2074.html)

To enable an interface to process user MLD join requests, enable MLD on the interface.

[(Optional) Setting an MLD Version](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2075.html)

Interfaces that connect multicast devices to the same user network segment must run the same MLD version; otherwise, these multicast devices fail to communicate.

[(Optional) Configuring an Interface to Statically Join an MLD Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2076.html)

After an interface on a multicast device is configured to statically join an MLD group, the multicast device considers that the interface has a static multicast group member and forwards multicast packets to this interface, irrespective of whether hosts connected to this interface request the multicast packets.

[(Optional) Setting the Range of IPv6 Multicast Groups that an Interface Can Join](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2077.html)

To limit the range of IPv6 multicast groups that an interface can join, configure a filtering policy on the multicast device's interface connected to the user network segment. Then, the interface can join only IPv6 multicast groups that are permitted in this policy.

[Verifying the Basic MLD Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2078.html)

After configuring basic MLD functions, verify the MLD configurations, MLD operating status, and information about MLD group members.