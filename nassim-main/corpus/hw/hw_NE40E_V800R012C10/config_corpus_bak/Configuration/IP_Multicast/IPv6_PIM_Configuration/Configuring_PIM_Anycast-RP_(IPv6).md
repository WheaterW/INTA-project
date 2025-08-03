Configuring PIM Anycast-RP (IPv6)
=================================

Anycast-Rendezvous Point (RP) is a feature supporting the configuration of several RPs with the same address in a PIM-SM domain. Peer relationships are established between RPs so that the multicast source can register with the topologically closest RP and the multicast receiver can join the closest RP. This alleviates burdens on RPs, implements RP backup, and optimizes multicast forwarding paths.

#### Usage Scenario

In a traditional PIM-SM domain, each multicast group is mapped only to one RP. When the network is overloaded or traffic congests on an RP, the RP may be overburdened.

If the RP fails, routes are converged slowly or multicast packets are forwarded over non-optimal paths. To resolve these issues, configure PIM Anycast-RP.


#### Pre-configuration Tasks

Before configuring the PIM Anycast-RP, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure IPv6 PIM-SM](dc_vrp_multicast_cfg_2005.html).


[Configuring the Global Anycast-RP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2155.html)

On several devices to be deployed with the Anycast-Rendezvous Point (RP) in a PIM-SM domain, configure the address of the RP elected in the PIM-SM domain as the Anycast-RP address.

[Setting a Local Address for the Anycast-RP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2156.html)

When sending a PIM Register message to all Anycast-Rendezvous Point (RP) peers, the local RP needs to use its own IP address (called the local address) as the source address of the Register message.

[Configuring an Anycast-RP Peer](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2157.html)

When sending a Register message to an Anycast-Rendezvous Point (RP) peer, a device needs to change the destination address of the Register message to the peer address.

[Verifying the PIM Anycast-RP Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2158.html)

After configuring PIM Anycast-Rendezvous Point (RP), verify the Anycast-RP configuration.