Configuring IS-IS SR-MPLS Flex-Algo
===================================

Flex-Algo allows an IGP to automatically calculate eligible paths based on the link cost, delay, or TE constraint to flexibly meet TE requirements.

#### Usage Scenario

Traditionally, IGPs can use only the SPF algorithm to calculate the shortest paths to destination addresses based on link costs. As the SPF algorithm is fixed and cannot be adjusted by users, the optimal paths cannot be calculated according to users' diverse requirements, such as the requirement for traffic forwarding along the lowest-delay path or without passing through certain links.

On a network, constraints used for path calculation may be different. For example, as autonomous driving requires an ultra-low delay, an IGP needs to use delay as the constraint to calculate paths on such a network. Another constraint that needs to be considered is cost, so some links with high costs need to be excluded in path calculation. These constraints may also be combined.

To make path calculation more flexible, users may want to customize IGP route calculation algorithms to meet their varying requirements. They can define an algorithm value to identify a fixed algorithm. When all devices on a network use the same algorithm, their calculation results are also the same, preventing loops. Since users, not standards organizations, are the ones to define these algorithms, they are called Flex-Algos.

When SR-MPLS uses an IGP to calculate paths, prefix SIDs can be associated with Flex-Algos to calculate SR-MPLS BE tunnels that meet different requirements.


#### Pre-configuration Tasks

Before configuring IS-IS SR-MPLS Flex-Algo, complete the following tasks:

* Configure IS-IS to ensure network layer connectivity.
* [Enable the advertisement of IPv4 delay information](dc_vrp_isis_cfg_1053.html) if the Flex-Algo metric type is **delay**.


[Configuring Flex-Algo Link Attributes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0132.html)

Flex-Algo link attributes are used by the IGP to calculate Flex-Algo-based SR-MPLS BE tunnels (Flex-Algo LSPs). The IGP selects Flex-Algo links based on the corresponding FAD.

[Configuring FADs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0131.html)

After a Flex-Algo is defined by a user based on service requirements, the IGP can use this Flex-Algo to calculate paths that meet the requirements.

[Configuring IS-IS Flex-Algo Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0133.html)

The Flex-Algos associated with the local prefix SIDs of a device as well as the FADs on the device all need to be advertised through IS-IS.

[Configuring the Color Extended Community](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0134.html)

The Color Extended Community attribute is added to routes based on route-policies. This attribute can be associated with Flex-Algos.

[Configuring the Mapping Between the Color Extended Community Attribute and Flex-Algo](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0135.html)

Service routes can be associated with Flex-Algo-based SR-MPLS BE tunnels only after mappings between their color attributes and Flex-Algos are configured.

[Configuring Traffic Steering into a Flex-Algo LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0136.html)

The traffic steering configuration allows you to recurse routes to Flex-Algo-based SR-MPLS BE tunnels (also called Flex-Algo LSPs) for traffic forwarding.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0137.html)

After IS-IS SR-MPLS Flex-Algo is configured, you can view associated information.