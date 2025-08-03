(Optional) Configuring Centralized NAT64 Translation
====================================================

This section describes how to configure centralized NAT64 translation.

#### Usage Scenario

When multiple NAT64 instances are configured with the same prefix, you need to use ACL rules to divert user traffic to the correct service board to the inbound direction of user traffic to translate the private IPv6 addresses in user packets into public IPv4 addresses so that users can access the IPv4 network.


#### Pre-configuration Tasks

Before configuring centralized NAT64 translation, complete the following task:

* Configure basic NAT64 functions.


[Configuring a NAT64 Traffic Distribution Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0014.html)

You can configure a NAT64 traffic distribution policy to distribute user traffic to NAT64 service boards for translation.

[Configuring a NAT64 Conversion Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0015_m2k.html)

You can configure NAT64 conversion policies to determine whether to implement ACL-based filtering of the traffic introduced to a service board and to redistribute the traffic to different NAT64 address pools for NAT64 treatment.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0016.html)

After centralized Network Address Translation IPv6-to-IPv4 (NAT64) for user traffic is configured, run display commands to verify centralized NAT64 configurations.