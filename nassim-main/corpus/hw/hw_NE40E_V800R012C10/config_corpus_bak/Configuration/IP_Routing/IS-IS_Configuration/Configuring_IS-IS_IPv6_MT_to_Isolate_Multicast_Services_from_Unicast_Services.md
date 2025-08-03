Configuring IS-IS IPv6 MT to Isolate Multicast Services from Unicast Services
=============================================================================

On an IS-IS IPv6 network, IS-IS MT improves usage of network resources by allowing services to run in multiple logical topologies.

#### Usage Scenario

On a traditional IPv6 network, only one unicast forwarding table is available in the forwarding plane because only one unicast topology exists. Therefore, traffic of all services shares the same hop-by-hop forwarding behavior as long as the destination IP addresses of the traffic are the same. This means that various end-to-end services (for example, voice services and data services) share the same physical links. As a result, some links may be heavily congested whereas some other links are relatively idle. In addition, QoS requirements vary according to services. The traditional unicast topology cannot meet various QoS requirements.

IS-IS MT allows multiple separate logical topologies to be deployed in an IS-IS autonomous system (AS). Separate multicast topologies can be set up for multicast services, and this configuration isolates multicast topologies from unicast topologies.

IS-IS MT allows users to configure the network flexibly, reducing network construction cost.

To configure IS-IS MT, perform the following steps. First, associate an IS-IS process with topology instances so that the SPF calculation can be performed for the topology instances in the IS-IS process. Second, associate a specified interface with the topology instances so that every link can participate in the SPF calculation.


#### Pre-configuration Tasks

Before configuring IS-IS MT to isolate IPv6 multicast services from IPv6 unicast services, complete the following tasks:


[Enabling MT for an IPv6 IS-IS Process](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0100.html)

Based on service requirements and the network plan, an IS-IS process can be associated with various topology instances so that multiple logical topologies are deployed in an IS-IS AS.

[Enabling MT for an IPv6 IS-IS Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0101.html)

After IS-IS MT is enabled, associate a specified interface with MT instances.

[Verifying the Configuration of IS-IS IPv6 Multi-Topologies Used to Isolate Multicast Services from Unicast Services](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0102.html)

After configuring IPv6 IS-IS MT to isolate multicast services from unicast services, check the IS-IS MT configurations.