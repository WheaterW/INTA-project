Configuring IS-IS MT to Isolate IPv4 Services from IPv6 Services
================================================================

On an IS-IS network, IS-IS MT improves usage of network resources by allowing multiple logical topologies to be deployed.

#### Usage Scenario

IPv4 and IPv6 share the same topology structure. An IPv4/IPv6 topology is an integrated topology in which IPv4 and IPv6 use the same shortest path in the SPF calculation. Therefore, the topology information of IPv6 must be the same as that of IPv4 when an IPv4/IPv6 topology is deployed.

However, in real-world situations, IPv4 and IPv6 may be deployed differently, and the topology information of IPv6 may differ from that of IPv4. In the scenario where an IPv4/IPv6 topology is deployed, some Routers and links do not support IPv6, and they cannot receive IPv6 packets from the Routers supporting the IPv4/IPv6 dual stack. As a result, these IPv6 packets are discarded. Similarly, IPv4 packets cannot be forwarded if Routers and links that do not support IPv4 on the network. When various end-to-end services, such as voice and data services, share the same physical links, either IPv4 or IPv6 packets are discarded on the shared links, affecting transmission quality.

IS-IS MT allows multiple separate logical topologies to be deployed in an IS-IS AS, and the SPF calculation can be performed in an IPv6 topology independently. In addition, IPv6 forwarding tables can be created for the IPv6 topology.

IS-IS MT allows users to configure the network flexibly, reducing network construction cost.

To configure IS-IS MT, perform the following steps. First, associate an IS-IS process with topology instances so that the SPF calculation can be performed for the topology instances in the IS-IS process. Second, associate a specified interface with the topology instances so that every link can participate in the SPF calculation.


[Enabling MT for an IS-IS Process](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0105.html)

Based on service requirements and the network plan, an IS-IS process can be associated with various topology instances so that multiple logical topologies are deployed in an IS-IS AS.

[Enabling MT for an IS-IS Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0106.html)

After IS-IS MT is enabled, associate a specified interface with MT instances.

[Verifying the Configuration of IS-IS Multi-Topologies Used to Isolate IPv4 Services from IPv6 Services](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0107.html)

After configuring IPv4 IS-IS MT to isolate IPv4 services from IPv6 services, check the configuration about IS-IS multi-topologies.