Adjusting OSPFv3 Route Selection
================================

By adjusting OSPFv3 route selection, you can enable OSPF to meet the requirements of complex networks.

#### Usage Scenario

To meet the requirements of complex networks, you can adjust OSPFv3 route selection rule by configuring the following OSPFv3 route attributes:

* Cost on the OSPFv3 interface
* Load balancing among equal-cost routes

#### Pre-configuration Tasks

Before adjusting OSPFv3 route selection, complete the following tasks:

* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2003.html).


[Setting the Link Cost on an OSPFv3 Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2021.html)

OSPFv3 can automatically calculate the link cost for an interface based on the interface bandwidth. You can also set the link cost for the interface.

[Configuring OSPFv3 Equal-Cost Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2023.html)

Routes that are discovered by the same routing protocol and have the same destination and cost can implement load balancing.

[Setting the convergence priority for OSPFv3 routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2095.html)

You can adjust and optimize route selection by setting the convergence priority for OSPFv3 routes.

[Configuring an OSPFv3 Interface to Automatically Adjust the Link Cost](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_3000.html)

Configuring an OSPFv3 interface to automatically adjust the link cost based on link quality facilitates route selection control and improves network reliability.

[Verifying the Configuration of OSPFv3 Route Selection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2024.html)

After setting OSPFv3 route attributes, verify information about OSPFv3 interfaces and the routing table.