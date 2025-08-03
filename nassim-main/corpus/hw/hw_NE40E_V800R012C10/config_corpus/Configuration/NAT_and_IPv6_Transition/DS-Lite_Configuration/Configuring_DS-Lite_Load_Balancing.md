Configuring DS-Lite Load Balancing
==================================

DS-Lite load balancing works on multiple service board CPUs for the same DS-Lite instance.

#### Usage Scenario

In both centralized scenarios, if one DS-Lite service can be bound to only one service board CPU, the service board of a single DS-Lite instance may reach the performance threshold when the number of users goes up. With DS-Lite load balancing, a DS-Lite instance can be bound to multiple service boards, which increases the DS-Lite bandwidth for a specific type of users. Increasing the number of service boards in a DS-Lite load balancing group saves the workload in configuring instances and assigning IP addresses and reduces manual intervention in traffic forwarding.


#### Pre-configuration Tasks

Before configuring DS-Lite load balancing, complete the following tasks:

* Install a CGN license and wait for the service board to work properly.
* Configure link layer protocol parameters and IP addresses for interfaces to go Up.


[Creating a DS-Lite Load Balancing Instance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0065.html)

Multiple service-location groups need to be created and be bound to the same service-instance group.

[Configuring a DS-Lite Tunnel](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0012_a.html)

This section describes how to configure a DS-Lite tunnel. A DS-Lite tunnel allows users with private IPv4 addresses to pass through IPv6-only carrier networks.

[Creating a Global Static Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0066.html)

Creating a global static address pool is mandatory for DS-Lite load balancing. To allow for DS-Lite load balancing, a DS-Lite instance needs to be created and be bound to a global static address pool.

[Binding a DS-Lite Load Balancing Group to a Global Static Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0067.html)

To allow for DS-Lite load balancing, bind a DS-Lite load balancing group to a global static address pool.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0068.html)

After DS-Lite load balancing is configured on the centralized board, you can view information about DS-Lite load balancing.