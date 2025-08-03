Configuring PMTUs
=================

After a PMTU is configured, devices on a network send packets based on the same MTU so that packets do not need to be fragmented in the transmission process and the burden of intermediate devices is reduced. Therefore, network resources are efficiently utilized to achieve the optimal traffic throughput.

#### Usage Scenario

Devices can determine the dynamic PMTU by default. The dynamic PMTU is the smallest MTU of all interface MTUs on the path along the source to the destination.

To protect a device against attacks initiated by sending jumbo packets, configure a static PMTU that defines the maximum length of a packet that can be sent from the source to the destination.

The static PMTU is usually less than or equal to an IPv6 MTU of an interface along the link. If a static PMTU value is greater than the IPv6 MTU value of an interface, the device fragments packets based on the IPv6 MTU.


#### Pre-configuration Tasks

Before configuring PMTUs, complete the following tasks:

* Set the IPv6 MTU for an interface. For details, see [(Optional) Setting Interface Parameters](dc_vrp_ifm_cfg_0027.html).


[Configuring a Static PMTU](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0023.html)

You can manually configure a static PMTU according to the minimum MTU of the path along which packets are sent, resulting in higher transmission efficiency.

[Setting the Aging Time of Dynamic PMTU Entries](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0024.html)

The PMTU aging time changes the lifetime of dynamic PMTU entries in the buffer. Static PMTU entries do not age.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0025.html)

After configuring PMTUs, verify the configuration.