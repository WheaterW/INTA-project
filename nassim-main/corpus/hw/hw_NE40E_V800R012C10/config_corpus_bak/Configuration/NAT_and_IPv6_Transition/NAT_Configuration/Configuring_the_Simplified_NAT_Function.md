Configuring the Simplified NAT Function
=======================================

A simplified NAT configuration model makes NAT deployment easier.

#### Context

[To configure basic NAT functions](dc_ne_nat_cfg_0010.html), you have to manually perform the following operations:

1. Create a service-location group and bind it to a service board.
2. Create a service-instance group and bind it to the service-location group.
3. Create a NAT instance and bind it to the service-instance group.

The NAT configuration in non-simplified mode is complex. Simplifying the NAT configuration procedure facilitates NAT deployment.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this feature is supported only by the admin VS.



#### Prerequisites

Before configuring simplified NAT, complete the following tasks:

* Properly install a service board.


[Creating a Simplified NAT Instance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0101.html)

After a simplified NAT instance is configured, a device automatically generates a service-instance group named **\_default\_** and binds it to a service-location group and the NAT instance. This process does not requires manual intervention and therefore simplifies the NAT configuration.

[Binding a Simplified NAT Instance to a Service Board](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0102.html)

After a simplified NAT instance is configured, a device automatically generates a service-instance group named **\_default\_** and binds it to the NAT instance. Then the simplified NAT instance is bound to a service board, so that the device automatically generates a service-location group and binds it to the service-instance-group named **\_default\_**. Consequently, the NAT configuration is simplified by eliminating manual configurations.

[Creating an Address Pool in a Simplified NAT Instance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0103.html)

You can create a NAT address pool and assign available public IPv4 address segments to a specified NAT instance for translation between private and public IPv4 addresses.

[Configuring the Internal Server Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0104.html)

The internal server function can be configured on a private network so that external users can access the server through a NAT device.

[Configuring a NAT Traffic Policy on an Outbound Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0105.html)

A NAT-enabled device is deployed on the egress of an enterprise network, whereas NAT does not need to be performed for a great amount of traffic transmitted within the enterprise network. To prevent an inbound interface from enforcing a NAT traffic policy to direct intra-enterprise network traffic to a NAT service board for NAT processing, a NAT traffic policy can be configured on an outbound interface connected to a public network. This enables the device to match traffic only destined for a public network against the NAT traffic policy.

[Verifying the Simplified NAT Configurations](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0106.html)

After configuring a simplified NAT instance, you can check the configuration of the address pool and internal servers in that instance.