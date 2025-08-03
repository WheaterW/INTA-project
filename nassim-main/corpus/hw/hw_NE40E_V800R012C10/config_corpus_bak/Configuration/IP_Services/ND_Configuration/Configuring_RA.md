Configuring RA
==============

A routing device periodically sends router advertisement (RA) messages carrying network prefixes and flags, or responds to RS messages with RA messages.

#### Usage Scenario

RA messages contain parameters of the hosts on the local link.


#### Pre-configuration Tasks

Before configuring RA, complete the following tasks:

* Connect interfaces and configure physical parameters for them to ensure that their physical status is up.
* Configure link layer protocol parameters for the interfaces to ensure that the link layer protocol status of the interfaces is Up.
* Configure IPv6 addresses for interfaces.


[Enabling RA Message Sending](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0043.html)

A routing device periodically sends RA messages carrying network prefixes and flags, or responds to RS messages with RA messages.

[Configuring Parameters Carried in RA Messages](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0019.html)

An RA message carries the hop limit, prefix option, neighbor reachable time, and lifetime.

[(Optional) Configuring RA Message Advertisement Intervals](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0018.html)

You can set a smaller RA message advertisement interval to speed up the RA process.

[(Optional) Configuring the Default Router Preference and Route Information](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0038.html)

RA messages that carry the default router preference and route information can be advertised on the local link to help hosts select a proper Router for packet forwarding.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0020.html)

After configuring RA, verify the configuration.