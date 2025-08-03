Configuring BFD for OSPF
========================

After BFD for OSPF is enabled, if a link fails, the Router rapidly detects the failure, notifies the OSPF process or interface of the fault, and instructs OSPF to recalculate routes. This speeds up OSPF network convergence. 

#### Usage Scenario

OSPF enables the router to periodically send Hello packets to a neighboring router for fault detection. Detecting a fault takes more than 1s. As voice, video, and other VOD services are widely used. These services are sensitive to packet loss and delays. When traffic is transmitted at gigabit rates, long-time fault detection will cause packet loss. This cannot meet high reliability requirements of the carrier-class network. BFD for OSPF was introduced to resolve this problem. After BFD for OSPF is configured in a specified process or on a specified interface, the link status can be rapidly detected and fault detection can be completed in milliseconds. This speeds up OSPF convergence when the link status changes.


#### Pre-configuration Tasks

Before configuring BFD for OSPF, complete the following tasks:

* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPF functions](dc_vrp_ospf_cfg_0003.html).


[Configuring BFD Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2237.html)

On two devices that need to establish a BFD session with each other, you can configure BFD for all the interfaces in a certain OSPF process.

[Configuring BFD for an OSPF Process](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2047.html)

Configuring BFD for an OSPF process helps the system rapidly detect link states and speeds up OSPF convergence in the case of a link state change.

[(Optional) Configuring BFD for a Specified Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2048.html)

Configuring BFD for OSPF on a specified interface helps speed up OSPF convergence in the case of an interface failure.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0054.html)

After BFD for OSPF is configured, you can check information about the BFD session.