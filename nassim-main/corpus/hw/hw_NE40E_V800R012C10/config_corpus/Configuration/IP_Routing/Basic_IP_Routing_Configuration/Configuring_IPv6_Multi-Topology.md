Configuring IPv6 Multi-Topology
===============================

Multi-topology on an IPv6 network enables devices to allocate network resources more effectively.

#### Usage Scenario

On traditional IPv6 networks, only one unicast forwarding table is available on the forwarding plane because only one unicast topology exists, which forces services transmitted from one router to the same destination address to share the same next hop, and various end-to-end services, such as voice and data services, to share the same physical links. As a result, some links may be heavily congested while others remain relatively idle. Deploying MT (different logical topologies) for different services on a physical network can solve the problem.


#### Pre-configuration Tasks

Before configuring IPv6 multi-topology, configure parameters of the link layer protocol and IPv6 addresses for interfaces and ensure that the link layer protocol on the interfaces is Up.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 topology**](cmdqueryname=ipv6+topology) *topology-name*
   
   
   
   An IPv6 topology is created.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-name*
   
   
   
   The view of the specified interface is displayed.
4. Run [**ipv6 topology**](cmdqueryname=ipv6+topology) *topology-name* [**enable**](cmdqueryname=enable)
   
   
   
   The topology is bound to the interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the [**display ipv6 topology**](cmdqueryname=display+ipv6+topology) command to check the previous configuration.