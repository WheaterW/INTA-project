Configuring IS-IS IPv4 MT to Isolate Multicast Services from Unicast Services
=============================================================================

On an IS-IS IPv4 network, IS-IS multi-topology (MT) improves usage of network resources by allowing services to run in multiple logical topologies.

#### Usage Scenario

On a traditional IP network, only one unicast forwarding table is available on the forwarding plane because only one unicast topology exists, which forces services transmitted from one router to the same destination address to share the same next hop, and various end-to-end services such as voice and data services, to share the same physical links. As a result, some links may become heavily congested while others remain relatively idle. In addition, QoS requirements vary based on services. The traditional unicast topology cannot meet various QoS requirements.

IS-IS MT allows multiple separate logical topologies to be deployed in an IS-IS autonomous system (AS). Separate multicast topologies can be set up for multicast services, and this configuration isolates multicast topologies from unicast topologies.

IS-IS MT allows users to configure the network flexibly, reducing network construction cost.

To configure IS-IS MT, perform the following steps. First, associate an IS-IS process with topology instances so that the SPF calculation can be performed for the topology instances in the IS-IS process. Second, associate a specified interface with the topology instances so that every link can participate in the SPF calculation.


#### Pre-configuration Tasks

Before configuring IS-IS MT to isolate IPv4 multicast services from IPv4 unicast services, complete the following tasks:


[Enabling MT for an IS-IS Process (IPv4)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0095.html)

Based on service requirements and the network plan, an IS-IS process can be associated with various topology instances so that multiple logical topologies are deployed in an IS-IS AS.

[Enabling MT for IPv4 an IS-IS Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0096.html)

After IS-IS MT is enabled, associate a specified interface with MT instances so that specified links can participate in the SPF calculation for the topology instances.

[Verifying the Configuration of IS-IS IPv4 Multi-Topologies Used to Isolate Multicast Services from Unicast Services](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0097.html)

After configuring IPv4 IS-IS MT to isolate multicast services from unicast services, check the IS-IS MT configurations.