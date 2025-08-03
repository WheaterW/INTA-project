Configuring Multicast Multi-Topologies
======================================

With multicast multi-topologies, multicast services can run in a specified topology, which isolates multicast services from unicast services and eliminates the configuration conflict when both multicast services and unidirectional Traffic Engineering (TE) tunnel services are deployed. In deploying multicast multi-topologies, you can specify either a multicast topology instance or a unicast topology instance for running multicast services.

#### Usage Scenario

* Currently, multicast services highly depend on unicast routes. During multicast routing, a router searches a unicast routing table for an optimal route. If the unicast optimal route, shared by both multicast services and unicast services, is faulty, the multicast services and unicast services will be interrupted and users will fail to receive the multicast data. With multicast multi-topologies, multicast services can run in a specified topology, which isolates multicast services from unicast services.
* With both multicast services and unidirectional TE tunnel services deployed, if a unidirectional TE tunnel interface is chosen during multicast routing, the multicast data will fail to pass the Reverse Path Forwarding (RPF) check. The local multicast-topology (MT) feature can address this problem. However, in this situation, a separate Multicast Interior Gateway Protocol (MIGP) routing table has to be maintained, which consumes network resources. With multicast multi-topologies, the system searches for routes only in the unicast routing table, the static multicast routing table, and the MBGP routing table specified by the multicast topology. These routing tables contain no unidirectional TE tunnel interfaces, avoiding the problem that multicast data fails to pass the RPF check when a unidirectional TE tunnel interface is chosen. In addition, no separate MIGP routing tables have to be maintained, so network resources can be properly planned.

When configuring multicast multi-topologies, you can configure a multicast topology instance or a unicast topology instance. A multicast topology can be used in both PIM-SM intra-domain and inter-domain scenarios, but a unicast topology instance can be used only in a PIM-SM intra-domain scenario.


#### Pre-configuration Tasks

Before configuring multicast multi-topologies, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure basic PIM-SM functions](dc_vrp_multicast_cfg_0006.html).
* [Configure IPv4 multi-topology](dc_vrp_ip-route_cfg_0017.html).


[Enabling Multicast Services to Run in a Multicast Topology Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2167.html)

Using a multicast topology instance for multicast services applies to both PIM-SM intra-domain and inter-domain scenarios.

[Enabling Multicast Services to Run in a Unicast Topology Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2168.html)

Using a unicast topology instance for multicast services applies only to the PIM-SM intra-domain scenario.

[Verifying the Configuration of Running Multicast Services in a Multicast Multi-topology Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2169.html)

After configuring multicast multi-topologies for multicast services, verify information about the current topology of the multicast network.