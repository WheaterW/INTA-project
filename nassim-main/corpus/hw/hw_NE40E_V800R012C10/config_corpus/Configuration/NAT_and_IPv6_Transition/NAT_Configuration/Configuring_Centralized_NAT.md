Configuring Centralized NAT
===========================

Before configuring NAT, familiarize yourself with the applicable environment, complete the pre-configuration tasks, and obtain the data required for the configuration.

#### Usage Scenario

After configuring basic NAT functions, you can apply a NAT traffic diversion policy for inbound traffic received by a NAT service board. You can also apply a NAT traffic conversion policy to translate a private IPv4 address in each data packet into a public IPv4 address, allowing a user to access public network services.


#### Pre-configuration Tasks

Before configuring centralized NAT for traffic, complete the following task:

* Configure basic NAT functions.


[Configuring a NAT Traffic Diversion Policy on an Inbound Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0020.html)

You can configure a NAT traffic policy on an inbound interface to perform NAT translation on user traffic.

[(Optional) Configuring a NAT Traffic Diversion Policy on an Outbound Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0027.html)

You can configure a NAT traffic diversion policy on an outbound interface so that traffic destined for the public network matches the NAT policy.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0022.html)

After configuring a NAT traffic policy, you can run **display** commands to check the configuration.