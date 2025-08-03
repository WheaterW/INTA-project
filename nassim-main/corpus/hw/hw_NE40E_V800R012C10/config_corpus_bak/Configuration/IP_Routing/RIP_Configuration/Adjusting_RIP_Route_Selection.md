Adjusting RIP Route Selection
=============================

You can adjust RIP route selection on a complicated network.

#### Usage Scenario

The implementation of RIP
is simple, and therefore, RIP is widely used in small and medium networks.
To flexibly apply RIP on the live network to meet various requirements
of users, you can change RIP route selection by setting different
parameters.


#### Pre-configuration Tasks

Before adjusting
RIP route selection, complete the following tasks:

* Configure IP addresses for interfaces to ensure that neighboring
  nodes are reachable at the network layer.
* [Configuring Basic RIP Functions](dc_vrp_rip_cfg_0003.html).

#### Configuration Procedure

Perform one or more
of the following configurations as required.


[Cancelling Classful Summarization in RIP-2](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0024.html)

On a network where subnets are incontiguous, you can cancel classful summarization in RIP-2 to obtain routing information that is more accurate.

[Configuring the Additional Metric on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0019.html)

The additional metric is a metric (number of hops) that is added to the original metric of an RIP route. You set additional metrics for received RIP routes and those to be sent.

[Configuring the Maximum Number of Equal-Cost Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0020.html)

By setting the maximum number of equal-cost RIP routes, you can change the number of routes for load balancing.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0021.html)

After adjusting RIP route selection, you can view the current running status of RIP, information about interfaces, and RIP routing information.