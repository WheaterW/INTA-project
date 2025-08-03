Improving OSPFv3 Network Stability
==================================

A stable OSPFv3 network features less route flapping, normal router performance, and high network performance.

#### Usage Scenario

By setting timers, you can reduce the number of unnecessary packets on networks and the load on the device, and improve network performance.

By adjusting the SPF calculation interval, you can mitigate resource consumption due to frequent network changes.


#### Pre-configuration Tasks

Before improving the security of an OSPFv3 network, complete the following tasks:

* Configure a link layer protocol.
* Configure IPv6 addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2003.html).


[Setting the OSPFv3 Preference](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2050.html)

If multiple dynamic routing protocols run on a device, the device needs to select optimal routes from the routes of these protocols. In this case, you can set a priority for each routing protocol. In this manner, when different protocols discover the routes to the same destination, the route discovered by the protocol with the highest priority is selected.

[Setting the Delay in Transmitting LSAs on the Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2051.html)

It takes time to transmit OSPFv3 packets on a link. Therefore, a certain delay is added to the aging time of an LSA before the LSA is sent. This configuration is especially necessary on low-speed links.

[Setting the Interval at Which LSAs Are Retransmitted Between Adjacent Routers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2052.html)

You can set an appropriate interval at which LSAs are retransmitted based on network conditions in order to accelerate convergence.

[Configuring a Route Calculation Delay to Suppress Frequent LSA Flapping](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2086.html)



[Configuring the SPF Timer](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2077.html)

By setting the interval for Shortest Path First (SPF) calculation, you can reduce resource consumption caused by frequent network changes.

[Configuring a Stub Router](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2053.html)

When the device is overloaded and cannot forward any other packets, you can configure it as a stub Router. After the Router is configured as a stub Router, other OSPFv3 devices do not use this device to forward data, but they can have a route to this stub Router.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2056.html)

After improving the OSPFv3 network stability, verify brief information about OSPFv3 and the IP routing table.