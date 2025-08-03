Configuring TCP6
================

The network performance can be improved by setting TCP6 packet attributes.

#### Usage Scenario

To optimize network performance, adjust TCP6 parameters.


#### Pre-configuration Tasks

Before configuring TCP6, complete the following tasks:

* Connect interfaces and configure physical parameters for the interfaces to ensure that the physical status of the interfaces is Up.
* Configure link layer protocol parameters for the interfaces to ensure that the link layer protocol status of the interfaces is Up.


[Configuring TCP6 Timers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_2004.html)

Set two TCP6 timers to control the TCP6 connection time.

[Specifying the Size of a TCP6 Sliding Window](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_2005.html)

The TCP6 sliding window size determines the size of the receiving buffer and transmitting buffer in the socket. This function improves network performance.

[Setting the MSS Value for a TCP6 Connection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0039.html)

The minimum MSS value and maximum MSS value can be configured for TCP6 connections.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_2006.html)

After configuring TCP6, verify the configuration.