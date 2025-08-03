Configuring Distributed NAT
===========================

Before configuring distributed NAT, familiarize yourself with the applicable environment, complete the pre-configuration tasks, and obtain the data required for the configuration.

#### Application Scenarios

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.


![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only dedicated boards support this configuration.

After configuring basic NAT functions and user group information, you can apply a NAT traffic diversion policy in the inbound direction of user traffic to distribute the user traffic to a service board for NAT translation. Meanwhile, you can apply a NAT translation policy to translate the private IPv4 addresses in user packets into public IPv4 addresses. In this way, users can access public network services.


#### Pre-configuration Tasks

Before configuring NAT for user traffic, complete the following tasks:

* Configure basic NAT functions.


[Configuring NAT User Group Information](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0069_1.html)

In a distributed NAT scenario, the NAT device identifies user traffic from each CPE by checking user identities. Therefore, NAT user group information must be configured on the NAT device.

[Configuring a NAT Traffic Diversion Policy on an Inbound Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0070_1.html)

You can configure a NAT traffic diversion policy to distribute user traffic to NAT service boards for NAT processing.

[Configuring a NAT Conversion Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0071_1.html)

Before converting private IP addresses of user traffic into public IP addresses from a NAT address pool, configure a NAT conversion policy to determine whether to filter the user traffic diverted to a NAT service board using ACL rules.

[Verifying the Configuration of Distributed NAT for User Traffic](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0072_1.html)

After configuring a NAT traffic policy, you can run **display** commands to check the configuration.