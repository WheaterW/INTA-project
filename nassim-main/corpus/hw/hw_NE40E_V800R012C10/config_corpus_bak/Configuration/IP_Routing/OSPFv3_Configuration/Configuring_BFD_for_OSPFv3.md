Configuring BFD for OSPFv3
==========================

To speed up OSPFv3 convergence when the link status changes, you can configure BFD for OSPFv3. After detecting a link failure, BFD notifies the routing protocol of the failure, which triggers fast convergence. When the neighbor relationship is Down, the BFD session is deleted dynamically.

#### Usage Scenario

When a network fault occurs, OSPFv3 can use BFD to implement fast route convergence.

BFD can quickly detect link faults based on the validity of network links. If OSPFv3 is associated with a BFD session, BFD can notify OSPFv3 of link failures immediately, and then OSPFv3 perform route calculation and convergence in the new network topology.


#### Pre-configuration Tasks

Before configuring BFD for OSPFv3, complete the following tasks:

* Configure a link layer protocol.
* Configure IPv6 addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2003.html).


[Configuring BFD Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2037.html)

On the two devices that need to establish a BFD session, you can configure BFD for all the interfaces in a certain OSPFv3 process.

[Configuring BFD for OSPFv3](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2038.html)

After enabling BFD for OSPFv3, you need to configure BFD parameters in the OSPFv3 process.

[(Optional) Configuring BFD for a Specified Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2040.html)

To configure BFD only on a specified interface, or enable an interface to detect link failures faster after BFD for OSPFv3 is enabled globally, configure BFD on the specified interface.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2041.html)

After configuring BFD for OSPFv3, verify information about the BFD session.