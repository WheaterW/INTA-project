Adjusting NAT Performance
=========================

You can improve NAT performance on a NAT device.

#### Usage Scenario

You can set the following parameters to improve NAT performance:

* Aging time of NAT session entries: Increasing the NAT session aging time can speed up the aging of NAT entries.
* TCP MSS: If the size of packets for NAT processing is larger than a link MTU, the packets are fragmented. You can reduce the MSS value in TCP, which prevents a NAT service board from fragmenting packets and helps improve NAT efficiency.


#### Pre-configuration Tasks

Before adjusting NAT performance, complete the following tasks:

* Configure basic NAT functions.
* Configure NAT for traffic.


[Setting the MSS Value for NAT Services](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0054.html)

The MSS value defined in TCP specifies the length of a TCP packet. Two devices exchange SYN packets to negotiate the MSS value for a TCP connection to be established.

[Verifying the Configuration of Adjusting NAT Performance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0055.html)

After configuring the NAT performance parameters, you can run display commands to verify the configuration.