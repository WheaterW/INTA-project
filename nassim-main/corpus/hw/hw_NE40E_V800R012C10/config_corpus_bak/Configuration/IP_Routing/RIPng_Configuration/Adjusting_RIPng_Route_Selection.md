Adjusting RIPng Route Selection
===============================

You can adjust RIPng route selection on a complicated network.

#### Usage Scenario

To flexibly apply RIPng on
a network and meet various requirements of users, you can change RIPng
route selection by setting different parameters.


#### Pre-configuration Tasks

Before adjusting RIPng
route selection, complete the following tasks:

* Configure IPv6 addresses for interfaces to ensure that neighboring
  nodes are reachable at the network layer.
* [Configuring Basic RIPng Functions](dc_vrp_ripng_cfg_0003.html)

#### Configuration Procedure

Perform one or more
of the following configurations as required.


[Configuring the Additional Metric on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0015.html)

The additional metric is the metric (hop count) to be added to the original metric of a RIPng route. You can set additional metrics for received RIPng routes and those to be sent.

[Configuring the Maximum Number of Equal-Cost Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0016.html)

By setting the maximum number of equal-cost RIPng routes, you can change the number of routes for load balancing.

[Verifying the Configuration of RIPng Route Selection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0017.html)

After adjusting RIPng route selection, verify the running status of RIPng, information about interfaces, and RIPng routing information.