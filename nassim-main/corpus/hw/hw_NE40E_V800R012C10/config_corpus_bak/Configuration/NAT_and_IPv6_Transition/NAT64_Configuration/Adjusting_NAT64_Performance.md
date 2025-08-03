Adjusting NAT64 Performance
===========================

This section describes how to adjust NAT64 performance.

#### Usage Scenario

You can improve the operational performance of NAT64 by adjusting NAT64 performance.


#### Pre-configuration Tasks

Before you adjust NAT64 performance, complete the following tasks:

* Configure basic NAT64 functions.
* Configure NAT64 translation for user traffic.


[Setting the Aging Time for NAT64 Sessions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0038.html)



[Setting the MTU Value for NAT64 Services](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0039.html)

You can change the MTU value so that the packets for NAT64 are not fragmented, improving NAT64 translation efficiency.

[Setting an MSS Value for NAT64 Services](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0054.html)

The maximum segment size (MSS) value defined in TCP specifies the maximum length of a TCP packet to be sent without fragmentation. Two devices exchange SYN packets to negotiate the MSS value for a TCP connection to be established.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0040.html)

After basic NAT64 functions are configured, you can verify the basic NAT64 configuration.