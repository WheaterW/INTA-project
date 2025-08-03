Configuring IPv6 Multicast Multi-Topologies
===========================================

With multicast multi-topologies, IPv6 multicast services can run in a specified topology, which isolates IPv6 multicast services from unicast services.

#### Usage Scenario

On the current network, multicast services highly depend on unicast routes. During multicast routing, a router searches a unicast routing table for an optimal route. If the unicast optimal route, shared by both multicast services and unicast services, is faulty, the multicast services and unicast services will be interrupted and users will fail to receive the multicast data.

With multicast multi-topologies, IPv6 multicast services can run in a specified topology, which isolates IPv6 multicast services from unicast services.

When configuring multicast multi-topologies, you can configure a multicast topology instance or a unicast topology instance. A multicast topology can be used in both PIM-SM intra-domain and inter-domain scenarios, but a unicast topology instance can be used only in a PIM-SM intra-domain scenario.


#### Pre-configuration Tasks

Before configuring IPv6 multicast multi-topologies, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure IPv6 PIM-SM](dc_vrp_multicast_cfg_2005.html).
* [Configure IPv6 multi-topology](dc_vrp_ip-route_cfg_0026.html).


[Enabling IPv6 Multicast Services to Run in a Multicast Topology Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_ipv6_cfg_0011.html)

Using a multicast topology instance for IPv6 multicast services applies to both PIM-SM intra-domain and inter-domain scenarios.

[Enabling IPv6 Multicast Services to Run in a Unicast Topology or the Base Topology Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_ipv6_cfg_0012.html)

Using a unicast topology or the base topology instance for IPv6 multicast services is applicable only to the PIM-SM intra-domain scenario.

[Verifying the Configuration of Running IPv6 Multicast Services in a Multicast Multi-topology Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_ipv6_cfg_0013.html)

After configuring multicast multi-topologies for multicast services, verify information about the current topology of the multicast network.