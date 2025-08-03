Configuring NAT Security
========================

NAT security can be implemented by setting the maximum number of NAT sessions that can be established and the rate at which the first packet is sent to create a flow for a specific user.

#### Usage Scenario

You can deploy the NAT security function to guarantee secure operations on a NAT device and prevent attacks.


#### Pre-configuration Tasks

Before configuring the NAT security function, complete the following task:

* Configure basic NAT functions.
* Configure NAT for traffic.


[Configuring a Limit on the Maximum Number of User-to-Network NAT Sessions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0039.html)

A forward session is established for packets transmitted from the user side to the network side. To prevent individual users from consuming excessive session resources to cause failures to establish connections for other users, you can set a limit on the maximum number of user-to-network NAT sessions that can be established for a specific user.

[Configuring a Limit on the Maximum Number of Network-to-User NAT Sessions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0040.html)

A reverse session is established for packets transmitted from the network side to the user side. To prevent individual users from consuming excessive session resources to cause failures to establish connections for other users, you can set a limit on the maximum number of network-to-user NAT sessions that can be established for a specific user.

[Configuring the Limit on the Number of NAT Ports](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0041_1.html)

To prevent individual users from occupying excessive port resources to cause the connection failure of other users, you can enable the NAT port number limit function.

[Setting an Aging Time for NAT Sessions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0053.html)

To accelerate aging of expired NAT sessions of a protocol, set an aging time. After the aging time elapses, NAT sessions age, and system resources are released.

[Configuring NAT Port Filtering](../../../../software/nev8r10_vrpv8r16/../../toctopics/en-us_task_0000001482697861.html)

To maintain network security and prevent virus intrusion, deploy the port filtering function for NAT services. The function prevents a port from being converted into a filtered port after NAT. Without this function, packets fail to be forwarded.

[Enabling Port Load Balancing in a Public NAT Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0107_1.html)

To prevent user services from being compromised due to high port usage within a public address pool, the port load balancing is enabled for public NAT address pools. With this function enabled, new online users preferentially select public IP addresses with lower port usage, which leads to even use of ports within a public address pool.

[Setting the Maximum Number of Private Network Users Sharing the Same Public IP Address](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0064_1.html)

In PAT mode, multiple uses can use the same public IP address for access. However, excessive users may lead to network congestion. To address this issue, you can set the maximum number of private network users sharing the same public IP address.

[Configuring the Processing Mode for Non-NAT Service Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0042_1.html)

Non-NAT service packets distributed to a service board can be either discarded or transparently transmitted.

[Setting the Rate at Which Packets Are Sent to Create a Flow for a User](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0043.html)

A device can be configured to dynamically detect the traffic forwarding rate and limit the rate at which packets are sent to create a flow for each user.

[Configuring a NAT Blacklist and Limiting the Rate at Which Packets Are Sent to Create Sessions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0044.html)

The NAT blacklist and session creation rate limit are used to prevent users from occupying a large number of CPU resources through traffic attacks, which affects the forwarding of common traffic.

[Verifying the NAT Security Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0045.html)

After configuring the NAT security functions, you can run **display** commands to check the configuration.