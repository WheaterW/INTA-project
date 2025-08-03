Configuring Basic RIPng Functions
=================================

To use RIPng features, configure basic RIPng functions, including creating RIPng processes and enabling RIPng on interfaces.

#### Usage Scenario

While RIPng is simple and easy to use, it offers less powerful functions than OSPFv3 and IS-IS. As such, RIPng is mainly used on small-scale networks.

Configuring basic RIPng functions is a prerequisite for building RIPng networks.


#### Pre-configuration Tasks

Before configuring basic RIPng functions, complete the following tasks:

* Configure a link layer protocol.
* Configure network-layer addresses for interfaces to ensure that neighboring devices are reachable at the network layer.
* Enable IPv6 in the system view.


[Creating a RIPng process](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0004.html)

The creation of a RIPng process is a precondition of all RIPng configurations.

[Enabling RIPng on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0005.html)

After an interface is associated with a RIPng process, routing information on this interface can be exchanged through RIPng.

[(Optional) Configuring the RIPng Priority](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0006.html)

When multiple routing protocols are running on the same device, you can adjust the priority of RIPng for route selection.

[(Optional) Enabling Check on Zero Fields of RIPng Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0007.html)

Certain fields in RIPng packets must be 0, and these fields are called zero fields.

[Verifying the Basic RIPng Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ripng_cfg_0008.html)

After configuring basic RIPng functions, verify the current operating status and routing information of RIPng.