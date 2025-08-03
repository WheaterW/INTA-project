Configuring a Static Source Tracing Algorithm
=============================================

This section describes how to configure the static source tracing algorithm. The static source tracing algorithm applies to centralized and distributed NAT deployment scenarios and supports the NAT444 feature.

#### Usage Scenario

A static NAT source tracing algorithm is in essence a formula. The input is a private IP address range, public IP address range, port segment size, and port range. The output is the mapping between private IP addresses, public IP addresses, and port range. When a device uses a static source tracing algorithm to implement NAT, the mapping between the private IP addresses, public IP addresses, and port range is fixed. In this case, NAT source tracing can be performed for NAT source tracing NEs, such as the AAA server, based on the algorithm so long as the source tracing algorithm parameters that are the same as those on the NAT device are obtained, instead of depending on the source tracing logs sent by the NAT device.

The static source tracing algorithm applies to centralized and distributed NAT deployment scenarios. [Figure 1](#EN-US_CONCEPT_0172374535__fig_dc_ne_cfg_nat_009301) shows the centralized deployment scenario of the static source tracing algorithm.

**Figure 1** Networking diagram for a static source tracing algorithm  
![](images/fig_dc_ne_nat_cfg_0013.png)  


#### Pre-configuration Tasks

Before configuring a static NAT source tracing algorithm, complete the following tasks:

* Configure data link layer protocol parameters and IP addresses for interfaces so that the data link layer protocol on each interface can go Up.


[Configuring a Mapping Policy for a Static Source Tracing Algorithm](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0090.html)

With a mapping policy for a static source tracing algorithm, the mapping between the IP addresses in a private address pool, the IP addresses in a public address pool, and the port range can be manually specified.

[Applying a Static Source Tracing Algorithm to a NAT Instance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0091.html)

This section describes how to apply a static source tracing algorithm to a NAT instance so that the mapping between the IP addresses in the private and public address pools is applied to the NAT instance.

[Verifying the Configuration of the Static Source Tracing Algorithm](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0092.html)

After configuring a static NAT source tracing algorithm, check the configurations.