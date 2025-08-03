Controlling RIP Routing Information
===================================

In most cases, multiple protocols run on the same network.
Therefore, you need to control routing information of every protocol
to meet different networking requirements.

#### Usage Scenario

To meet the requirements
of complex networking, accurately control the sending and receiving
of RIP routing information.


#### Pre-configuration Tasks

Before configuring
a router to control RIP routing information, complete the following
tasks:

* Configure IP addresses for interfaces to ensure that neighboring
  nodes are reachable at the network layer
* [Configuring Basic RIP Functions](dc_vrp_rip_cfg_0003.html)

#### Configuration Procedure

Perform one or more
of the following configurations as required.


[Configuring RIP to Import External Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0026.html)

A RIP process can import the routes learned by other processes or routing protocols to enrich routing entries.

[Configuring RIP to Advertise Default Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0025.html)

Default routes are destined for 0.0.0.0.

[Configuring RIP to Filter Received Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0027.html)

You can configure an import policy for a device so that the device receives only required routes.

[Configuring RIP to Filter the Routes to Be Advertised](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0028.html)

You can set conditions to filter the routes to be advertised. Only the routes that meet the conditions can be advertised.

[Disabling RIP from Receiving Host Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0036.html)

You can disable RIP from receiving host routes on a device to prevent the device from receiving a large number of unwanted routes. Such configuration can reduce network resource consumption.

[Disabling RIP from Checking the RIP Packets with Metric 0](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0039.html)

To ensure communication between two devices, only one of which accepts RIP packets with metric 0, you can disable the device that does not accept such packets from checking the RIP packets with metric 0.

[Disabling an Interface from Sending Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0015.html)

When you do not need an interface connected to an external network to send routing information, disable the interface from sending RIP packets.

[Disabling an Interface from Receiving Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0016.html)

If an interface does not need to learn routing information from neighbors, you can disable the interface from receiving RIP packets.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0052.html)

After RIP routing information is successfully controlled, you can view all active routes in the RIP database and the current running status.