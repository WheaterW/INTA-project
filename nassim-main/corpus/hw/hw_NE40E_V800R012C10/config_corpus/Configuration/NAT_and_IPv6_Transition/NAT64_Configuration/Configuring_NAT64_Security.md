Configuring NAT64 Security
==========================

Before configuring Network Address Translation IPv6-to-IPv4 (NAT64) security, familiarize yourself with the applicable environment, complete the pre-configuration tasks, and obtain the data required for the configuration.

#### Usage Scenario

You can deploy the NAT64 security function to guarantee secure operations of a NAT64 device and prevent malicious attacks to the system.


#### Pre-configuration Tasks

Before you configure the NAT64 security function, complete the following tasks:

* Configure basic NAT64 functions.
* Configure centralized NAT64 translation.


[Configuring the Limit on the Number of User-to-Network NAT64 Sessions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0028.html)

To prevent individual users from consuming excessive session table resources to cause connection failures of other users, enable the NAT64 session number limit function.

[Setting a Limit on the Number of NAT64 Reverse Sessions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0058.html)

A reverse session refers to a session initiated from the IPv4 side to the IPv6 side. If individual users consume excessive session table resources, other users may fail to establish connections. To address this problem, set a limit on the maximum number of IPv4-to-IPv6 reverse NAT64 sessions that can be established for a specific user.

[Setting the Rate at Which Packets Are Sent to Create a Flow for a User](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0052.html)

A device can be configured to dynamically detect the traffic forwarding rate and limit the rate at which packets are sent to create a flow for each user.

[Setting the Maximum Number of Private Network Users Who Use Public IP addresses Translated by NAT64 to Get Online](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0053_m2k.html)

If a device working in PAT mode creates a large number of NAT sessions for each of users sharing a public IP address, user traffic may fail to be forwarded. To prevent the problem, set the maximum number of private network users who can get online using the same public IP address.

[Filtering a Port Number and a Port Range](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0047.html)

To secure networks from virus, configure the port filter function on a CGN service board to prevent an unwanted port from being translated to a filtered port and resulting in a packet forwarding failure.

[Verifying the NAT64 Security Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0030.html)

After the Network Address Translation IPv6-to-IPv4 (NAT64) security function is configured, you can check NAT64 security configurations.