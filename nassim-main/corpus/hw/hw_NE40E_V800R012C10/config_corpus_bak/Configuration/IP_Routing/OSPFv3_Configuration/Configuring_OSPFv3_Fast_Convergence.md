Configuring OSPFv3 Fast Convergence
===================================

By adjusting OSPFv3 timers, you can implement OSPF fast network convergence.

#### Pre-configuration Tasks

Before configuring OSPFv3 fast convergence, complete the following tasks:

* Configure a link layer protocol.
* Configure IPv6 addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2003.html).


[Setting the Interval at Which Hello Packets Are Sent](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2044.html)

You can adjust the value of the Hello timer to change the speed of OSPFv3 neighbor relationship establishment and the network convergence speed.

[Setting the Dead Time of the Neighbor Relationship](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2045.html)

If a device does not receive a Hello packet from its neighbor within the dead interval, the device considers the neighbor Down.

[Configuring OSPFv3 Sham Hello](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2079.html)

With OSPFv3 sham hello, device can exchange Hello and LSU and LSAck packets to maintain OSPFv3 neighbor relationships, which strengthens the neighbor detection mechanism.

[Setting the Interval at Which LSAs Are Updated](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2087.html)

You can set the interval at which LSAs are updated based on network connections and router resources.

[Setting the Interval at Which LSAs Are Received](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2088.html)

You can set the interval at which LSAs are received based on network connections and router resources.

[Disabling OSPFv3 LSA Aging Management](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2099.html)

By default, the OSPFv3 LSA aging management function is enabled. To disable this function, perform this task.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2047.html)

After configuring OSPFv3 fast convergence, verify brief information about OSPFv3.