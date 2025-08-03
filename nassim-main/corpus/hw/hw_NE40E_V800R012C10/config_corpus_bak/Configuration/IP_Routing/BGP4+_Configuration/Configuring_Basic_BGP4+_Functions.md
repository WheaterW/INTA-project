Configuring Basic BGP4+ Functions
=================================

Basic BGP4+ functions must be configured before you configure subsequent BGP4 functions on a BGP4+ network.

#### Usage Scenario

Basic BGP4+ functions must be configured first when you configure BGP4+ for inter-AS communication.


#### Pre-configuration Tasks

Before configuring basic BGP4+ functions, configure link layer protocol parameters and IP addresses for interfaces to ensure that the link layer protocol on the interfaces is Up.


[Starting a BGP Process](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0004.html)

A BGP process must be started before configuring BGP functions. When starting a BGP process, specify the number of the AS to which the device belongs.

[Configuring IPv6 Peers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0005.html)

Devices can exchange BGP4+ routing information only after the IPv6 peer relationship is established among them.

[Configuring BGP4+ to Import Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0010.html)

BGP4+ can import routes from other protocols. When routes are imported from dynamic routing protocols, the process IDs of the routing protocols must be specified. Importing routes from other protocols can enrich the BGP4+ routing table. When importing IGP routes, BGP4+ can filter the routes by routing protocol.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0007.html)

After configuring basic BGP4+ functions, verify BGP4+ peer information.