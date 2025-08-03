Adjusting the IPv4 IS-IS Route Convergence Speed
================================================

Accelerating IS-IS route convergence can improve the fault location efficiency and network reliability.

#### Usage Scenario

The procedure for implementing IS-IS is as follows:

* Establishment of neighbor relationships: establishes neighbor relationships by exchanging Hello packets between two devices.
* LSP flooding: implements LSDB synchronization between devices in the same area.
* SPF calculation: uses the SPF algorithm to calculate IS-IS routes, and delivers IS-IS routes to the routing table.

To accelerate the IS-IS route convergence, configure the following parameters:

* Interval for detecting failures on IS-IS neighboring devices
* Flooding parameters of CSNPs and LSPs
* Interval for SPF calculation

You can also configure convergence priorities for IPv4 IS-IS routes so that key routes can converge first if the network topology changes, which minimizes adverse impacts on key services.


#### Pre-configuration Tasks

Before adjusting the IPv4 IS-IS route convergence speed, complete the following tasks:

* Configure the link layer protocol on interfaces.
* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic IPv4 IS-IS functions](dc_vrp_isis_cfg_1000.html).


[Configuring the Interval for Detecting IS-IS Neighboring Device Failures](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1018.html)

To minimize the impacts of neighboring device failures on IS-IS networks, accelerate the detection IS-IS neighboring device failures.

[Setting Flooding Parameters of SNPs and LSPs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1019.html)

To speed up LSDB synchronization between devices, set proper values for flooding parameters of SNPs and LSPs.

[Adjusting the SPF Calculation Interval](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1020.html)

By adjusting the SPF calculation interval, you can ensure that IS-IS responds to network changes in time and reduce the system resources consumed by SPF calculation.

[Configuring Convergence Priorities for IPv4 IS-IS Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1021.html)

You can set a high convergence priority for key routes on an IS-IS network to ensure that these routes converge first if the network topology changes. This minimizes the impact on important services.

[Enabling IS-IS Intelligent Convergence](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1060.html)

Enabling IS-IS intelligent convergence can speed up IS-IS route convergence, thereby improving convergence performance.

[Verifying the IPv4 IS-IS Route Convergence Speed Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1022.html)

After configuring parameters to adjust the IPv4 IS-IS route convergence speed, check the configurations.