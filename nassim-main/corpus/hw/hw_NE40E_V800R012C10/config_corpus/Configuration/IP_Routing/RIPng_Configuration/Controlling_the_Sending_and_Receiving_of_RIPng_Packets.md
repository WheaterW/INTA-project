Controlling the Sending and Receiving of RIPng Packets
======================================================

By controlling the sending and receiving of RIPng packets, you can optimize the RIPng performance.

#### Applicable Environment

To meet the requirements of complex networking, accurately control the sending and receiving of RIPng packets.


#### Pre-configuration Tasks

Before configuring a Router to control the sending and receiving of RIPng packets, complete the following tasks:

* Configure IPv6 addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configuring Basic RIPng Functions](dc_vrp_ripng_cfg_0003.html)

#### Configuration Procedure

Perform one or more of the following configuration tasks (excluding "Checking the Configuration") as required.


[Disabling Receiving of RIPng Packets on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0035.html)

Disabling interfaces from receiving RIPng packets is a method of preventing routing loops.

[Disabling Sending of RIPng Packets on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0036.html)

Disabling an interface from sending RIPng packets is a method of preventing routing loops.

[Setting the Interval for Sending Update Packets and the Maximum Number of Packets Sent Each Time](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0037.html)

By setting the interval for sending packets and the maximum number of packets to be sent each time, you can optimize the RIPng performance.

[Verifying the Configuration of Controlling the Sending and Receiving of RIPng Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0038.html)

After controlling the sending and receiving of RIPng packets, verify the routing information in the RIPng database.