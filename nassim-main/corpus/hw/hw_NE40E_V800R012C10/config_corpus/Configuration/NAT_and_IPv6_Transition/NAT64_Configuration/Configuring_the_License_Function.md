Configuring the License Function
================================

The license function is a prerequisite for configuring NAT64 functions. The license function allows you to adjust NAT64 bandwidth and session table resources.

#### Usage Scenario

NAT64 bandwidth and session table resources are controlled using a license. A device is assigned no NAT64 bandwidth and session table resources by default. Before you configure NAT64 functions, adjust NAT64 bandwidth and session table resources.


#### Pre-configuration Tasks

Before configuring the license function, load a license file on a NAT64 device and ensure that involved service board works properly.


[Enabling the NAT64 Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0043_m2k.html)

The NAT64 function must be enabled in the license view before basic NAT64 functions are configured.

[Configuring Session Table Resources](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0050_m2k.html)

Session resources are essential for dedicated NAT64. Insufficient resources will cause NAT64 services to become unavailable.

[(Optional) Setting Bandwidth Resources](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0049_m2k.html)

To improve NAT64 forwarding performance on a , configure NAT64 bandwidth resources to increase available bandwidth of the .

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat64_cfg_0051_m2k.html)

After you configure session and bandwidth resources for a dedicated board, you can check the resources assigned by the license.