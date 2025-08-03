Configuring RIP Fast Convergence
================================

The network convergence speed is one of the key factors
used to evaluate network performance.

#### Usage Scenario

The route convergence speed
on a device is a performance index used to measure the network quality.
Fast route convergence can improve the accuracy of routing information
on the network.


#### Pre-configuration Tasks

Before configuring
RIP fast convergence, complete the following tasks:

* Configure IP addresses for interfaces to ensure that neighboring
  nodes are reachable at the network layer.
* [Configuring Basic RIP Functions](dc_vrp_rip_cfg_0003.html)

#### Configuration Procedure

Perform one or more
of the following configurations as required.


[Configuring RIP-2 Route Summarization](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0032.html)

Configuring RIP-2 route summarization reduces the routing table size, which improves system performance and network security.

[Configuring RIP Timers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0033.html)

There are four RIP timers: Update, Age, Suppress, and Garbage-collect timers. You can adjust the RIP convergence speed by changing the values of RIP timers.

[Configuring RIP Triggered Update](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0054.html)

You can speed up network convergence by changing the values of triggered update timers.

[Setting the Interval at Which Packets Are Sent and the Maximum Number of the Sent Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0034.html)

You can set the interval at which RIP packets are sent and the maximum number of packets that can be sent at a time to control the memory used by a device to process RIP update packets.

[Setting the Maximum Length of RIP packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0035.html)

You can increase the maximum length of RIP packets to enable them to carry more routes, which improves bandwidth utilization.

[Setting the Maximum Number of RIP Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0053.html)

You can set the maximum number of RIP routes to make full use of network resources and improve network performance.

[Configuring RIP Hardware Replication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0153.html)

After RIP hardware replication is configured, RIP packets can be forwarded in hardware replication mode. This implements fast forwarding and optimizes system performance.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0037.html)

After configuring fast RIP convergence, check the running status of RIP, RIP routing information, all active routes in the RIP database, and information about interfaces.