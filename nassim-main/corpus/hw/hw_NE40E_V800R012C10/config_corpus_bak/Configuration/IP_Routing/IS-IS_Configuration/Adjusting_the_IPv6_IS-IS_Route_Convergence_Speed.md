Adjusting the IPv6 IS-IS Route Convergence Speed
================================================

Accelerating IS-IS route convergence can improve the fault location efficiency and network reliability.

#### Usage Scenario

The procedure for implementing IS-IS is as follows:

* Establishment of neighboring relationships: establishes neighboring relationships by exchanging Hello packets between two devices.
* LSP flooding: implements LSDB synchronization between devices in the same area.
* SPF calculation: uses the SPF algorithm to calculate IS-IS routes, and delivers the IS-IS routes to the routing table.

To accelerate the IS-IS route convergence, configure the following parameters:

* Interval for detecting IS-IS neighboring device failures.
* Flooding parameters of CSNPs and LSPs.
* Interval for SPF calculation.

You can also configure convergence priorities for IPv6 IS-IS routes so that key routes can converge first if the network topology changes, which minimizes adverse impacts on key services.


#### Pre-configuration Tasks

Before configuring the IPv6 IS-IS route convergence speed, complete the following tasks:

* Configure the link layer protocol on interfaces.
* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic IPv6 IS-IS functions](dc_vrp_isis_cfg_1023.html).


[Configuring the Interval for Detecting IS-IS Neighboring Device Failures](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1041.html)

To minimize the effects caused by neighboring device failures on an IS-IS network, accelerate the speed of detecting IS-IS neighboring device failures.

[Setting Flooding Parameters of SNPs and LSPs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1042.html)

To speed up LSDB synchronization between devices, set flooding parameters of SNPs and LSPs to proper values.

[Adjusting the SPF Calculation Interval](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1043.html)

By adjusting the SPF calculation interval, you can ensure that IS-IS responds to network changes in time and reduce the system resources consumed by SPF calculation.

[Configuring Convergence Priorities for IPv6 IS-IS Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1044.html)

You can set a high convergence priority for key routes on an IS-IS network to ensure that these routes converge first if the network topology changes. This minimizes the impact on important services.

[Enabling IS-IS Intelligent Convergence (IPv6)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1160.html)

Enabling IS-IS IPv6 intelligent convergence can speed up IS-IS route convergence, thereby improving convergence performance.

[Configuring Interface Address Advertisement Suppression](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1050.html)

Interface address advertisement suppression ensures that interface addresses can be reused.

[Verifying the IPv6 IS-IS Route Convergence Speed Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1045.html)

After configuring parameters to adjust the IPv6 IS-IS route convergence speed, check the configurations.