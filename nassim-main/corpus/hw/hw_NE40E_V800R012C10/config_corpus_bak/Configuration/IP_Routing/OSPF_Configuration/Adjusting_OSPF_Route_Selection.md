Adjusting OSPF Route Selection
==============================

By adjusting OSPF route selection, you can enable OSPF to meet the requirements of complex networks.

#### Usage Scenario

In real world situations, you can configure an OSPF route selection rule by setting OSPF route attributes to meet the requirements of complex networks.

* Set the cost of an interface. The link connected to the interface with a smaller cost value preferentially transmits routing information.
* Configure equal-cost routes to implement load balancing.
* Configure a stub router during the maintenance operations such as upgrade to ensure stable data transmission through key routes.
* Suppress interfaces from sending or receiving packets to help select the optimal route.
* Configuring an OSPF interface to automatically adjust the link cost based on link quality that facilitates route selection control and improves network reliability.

#### Pre-configuration Tasks

Before adjusting OSPF route selection, complete the following tasks:

* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPF functions](dc_vrp_ospf_cfg_0003.html).


[Setting the Interface Cost](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0036.html)

You can adjust and optimize route selection by setting the OSPF interface cost.

[Configuring Equal-Cost Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0039.html)

You can set the maximum number of OSPF equal-cost routes and weights to implement load balancing and adjust route selection.

[Setting the convergence priority for OSPF routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0035.html)

You can adjust and optimize route selection by setting the convergence priority for OSPF routes.

[Configuring a Stub Router](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2036.html)

To ensure that a route is not interrupted during flapping-triggering maintenance operations such as upgrade, you can configure a Router as a stub router to allow traffic to bypass the route on the stub router.

[Suppressing an Interface from Receiving and Sending OSPF Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2037.html)

After an interface is suppressed from receiving and sending OSPF packets, routing information can bypass a specific Router and the local Router can reject routing information advertised by another Router.

[Configuring an OSPF Interface to Automatically Adjust the Link Cost](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2050.html)

Configuring an OSPF interface to automatically adjust the link cost based on link quality facilitates route selection control and improves network reliability.

[Configuring a Fallback Cost for an Eth-Trunk Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2064.html)

A fallback cost of an Eth-Trunk interface helps adjust route selection dynamically.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0040.html)

After OSPF route selection is adjusted, you can check OSPF routing table and interface information.