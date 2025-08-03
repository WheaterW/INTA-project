Configuring NAT Load Balancing
==============================

NAT load balancing works on multiple service board CPUs for the same NAT instance.

#### Usage Scenario

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.


![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only [dedicated boards](dc_ne_nat_feature_0008.html#EN-US_CONCEPT_0172359138__li1033371595) support this configuration.

NAT load balancing is not supported in NAT Server scenarios.

In centralized and distributed scenarios, although users grow, a NAT service is bound only to a single service board's CPU. Consequently, the service board to which the NAT instance is bound reaches the forwarding performance threshold. NAT load balancing allows a NAT instance to be bound to multiple service boards to increase NAT bandwidth for the same type of users. Adding service boards ([dedicated boards](dc_ne_nat_feature_0008.html#EN-US_CONCEPT_0172359138__li1033371595))in a NAT load balancing group reduces instance configurations, manual assignment of address pools, and human interference to traffic.


#### Pre-configuration Tasks

Before configuring NAT load balancing, complete the following tasks:

* Install a CGN license and wait for the service board to work properly.
* Configure data link layer protocol parameters and IP addresses for interfaces so that the data link layer protocol on each interface can go Up.


[Creating a NAT Load Balancing Instance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0078_1.html)

Multiple service-location groups need to be created and bound to the same service-instance group.

[Creating a Global Static Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0079_1.html)

A global static address pool is a prerequisite for CGN load balancing.

[Binding a Global Static Address Pool to a NAT Load-Balancing Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0080_1.html)

You can bind a global static address pool to a NAT load balancing instance to implement CGN load balancing.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0076_1.html)

After NAT load balancing is configured on a dedicated board, check NAT load balancing information.