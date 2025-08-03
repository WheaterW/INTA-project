Configuring Basic BGP Functions
===============================

Before building a BGP network, you must configure basic BGP functions.

#### Usage Scenario

BGP can be configured on a network to implement communication among ASs. To build a BGP network, configure basic BGP functions, including the following steps:

* Start a BGP process. This step is a prerequisite for configuring basic BGP functions.
* Establish BGP peer relationships. Devices can exchange BGP routing information only after peer relationships are established.
* Import routes: BGP itself cannot discover routes. Instead, it needs to import routes discovered by other protocols to generate BGP routes.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Commands in the BGP-IPv4 unicast address family view can be run in the BGP view, which facilitates configuration. These commands are displayed in the BGP-IPv4 unicast address family view in configuration files.

To prevent the commands of the BGP-IPv4 unicast address family from being executed in the BGP view, run the [**bgp default ipv4-unicast-config disable**](cmdqueryname=bgp+default+ipv4-unicast-config+disable) command.



#### Pre-configuration Tasks

Before configuring basic BGP functions, configure parameters of the link layer protocol and IP addresses for interfaces to ensure that the link layer protocol on the interfaces is Up.


[Starting a BGP Process](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3005.html)

Starting a BGP process is a prerequisite for configuring BGP functions. When starting a BGP process on a device, you need to specify the number of the AS to which the device belongs.

[Configuring a BGP Peer](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3006.html)

Devices can exchange BGP routing information only after the BGP peer relationship is established.

[Configuring BGP to Import Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3007.html)

BGP can import the routes from other routing protocols. When routes are imported from dynamic routing protocols, the process IDs of the routing protocols must be specified. Importing routes from other protocols can enrich the BGP routing table. When importing IGP routes, BGP can filter the routes by routing protocol.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3008.html)

After configuring the basic BGP functions, verify BGP peer information.