Configuring Access to an Internal IPv6 Host Using an IPv4 Address
=================================================================

Configuring internal host access through a public IP address allows external users to access internal users using the specified public IP address and port number.

#### Usage Scenario

NAT64 can be configured to allow IPv6 users on a private network to access public network IPv4 services and prevent IPv4 users from accessing IPv6 users because the IPv4 users cannot obtain IPv6 user information. The NE40E supports the internal server function in a NAT64 instance, allowing external IPv4 users to communicate with IPv6 users by accessing the public IPv4 address of a specified private IPv6 server.


#### Pre-configuration Tasks

Before configuring an IPv4 address used to access an internal IPv6 host, complete the following tasks:

* Configure basic NAT64 functions.
* (Optional) Configure NAT64 user information.
* Configure NAT64 translation for user traffic.


[Configuring the NAT64 Server Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0056.html)

IPv4 users can access an IPv6 server if the device is configured with NAT64.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0057.html)

You can verify the configuration of the internal server function in a NAT64 instance.