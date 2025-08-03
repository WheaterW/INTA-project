Configuring Duplicate Address Detection
=======================================

Duplicate address detection (DAD) is a process in which a node determines whether the address to be used is used by another node.

#### Usage Scenario

Before configuring an IPv6 unicast address for an interface, check whether this address is unique on the local link and is not used by another node.


#### Pre-configuration Tasks

Before configuring DAD, complete the following tasks:

* Connect interfaces and configure physical parameters for them to ensure that their physical status is up.
* Configure link layer protocol parameters for interfaces.
* Configure IPv6 addresses for interfaces.


[Configuring the Number of DAD Attempts](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0014.html)

A device can send NS messages to detect whether the IPv6 address to be configured is being used by another device. The number of DAD attempts refers to the number of times NS messages are sent. DAD is similar to gratuitous ARP in IPv4, but implemented using NS and NA messages.

[Setting a Timeout Period for DAD Messages](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_2010.html)

If many VLANs are configured on a VLAN tag termination sub-interface, DAD messages may fail to be transmitted within the default timeout period (1s). To resolve this issue, run the [**ipv6 nd dad timeout**](cmdqueryname=ipv6+nd+dad+timeout) command to prolong the timeout period for DAD messages.

[Disabling DAD from Continuing Detection in an Address Conflict Scenario](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_2012.html)



[Configuring a Limit on the Rate at Which NS Messages Are Sent for DAD to Continue Detection in an Address Conflict Scenario](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_2013.html)



[Configuring a Threshold for DAD to Consider an Address Available in an Address Conflict Self-Recovery Scenario](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_2014.html)



[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0015.html)

After configuring duplicate address detection, verify the configuration.