Adjusting the OSPF Network Convergence Speed
============================================

By adjusting OSPF timers, you can implement OSPF network convergence speed.

#### Pre-configuration Tasks

Before adjusting the OSPF network convergence speed, complete the following tasks:

* Configure a link layer protocol.
* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPF functions](dc_vrp_ospf_cfg_0003.html).


[Setting the Interval at Which Hello Packets Are Sent](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0010.html)

You can adjust the value of the Hello timer to change the speed of the OSPF neighbor relationship establishment and change the network convergence speed.

[Setting the Delay for Transmitting LSAs on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0009.html)

This configuration is important for low-speed networks.

[Setting the Dead Time of an OSPF Neighbor](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0011.html)

If no Hello packet is received from a neighbor within a dead interval, the neighbor is considered Down.

[Configuring OSPF Sham Hello](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2052.html)

With OSPF sham hello, device can exchange Hello and LSU and LSAck packets to maintain OSPF neighbor relationships, which strengthens the neighbor detection mechanism.

[Configuring Smart-discover](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0057.html)

After Smart-discover is configured, when the neighbor status changes or the DR or BDR on the multiple-access network (broadcast network or NBMA network) changes, the local router sends Hello packets to its neighbor immediately without waiting for the Hello timer to expire.

[Setting the Interval at Which LSAs Are Updated](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0058.html)

You can set the interval at which LSAs are updated based on network connections and router resources.

[Setting the Interval at Which LSAs Are Received](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0059.html)

You can set the interval at which LSAs are received based on network connections and router resources.

[Setting the Interval for the SPF Calculation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0060.html)

By setting the interval for the SPF calculation, you can save resources consumed by frequent network changes.

[Configuring the Function to Suppress the Advertisement of Interface Addresses](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0066.html)

This section describes how to configure the function to suppress the advertisement of interface addresses so that interface addresses can be reused.

[Configuring the Route Calculation Delay Function to Suppress Frequent LSA Flapping](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0056.html)

A route calculation delay can suppress frequent OSPF LSA flapping.

[Disabling Active/Standby Board Switching Triggered by Abnormal OSPF Aging](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0063.html)

By default, active/standby board switching triggered by abnormal OSPF aging is enabled. To disable this function, perform this task.

[Disabling OSPF LSA Aging Management](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2057.html)

By default, the OSPF LSA aging management function is enabled. To disable this function, perform this task.

[Setting a Period During Which OSPF Keeps the Maximum Cost in Local LSAs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2072_a.html)

If a period during which OSPF keeps the maximum cost in local LSAs is configured and an OSPF interface changes from Down to Up, traffic is switched back only when the period elapses.

[Configuring Secure Synchronization](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0109.html)

Secure synchronization prevents traffic loss after a device is restarted.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0061.html)

After configuring OSPF fast network convergence, verify OSPF brief information.