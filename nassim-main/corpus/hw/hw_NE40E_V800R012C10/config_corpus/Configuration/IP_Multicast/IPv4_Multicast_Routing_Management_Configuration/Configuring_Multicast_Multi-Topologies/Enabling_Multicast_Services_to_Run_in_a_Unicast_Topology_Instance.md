Enabling Multicast Services to Run in a Unicast Topology Instance
=================================================================

Using a unicast topology instance for multicast services applies only to the PIM-SM intra-domain scenario.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before enabling multicast services to run in a specified unicast topology instance, you must configure a multicast topology instance and a unicast topology instance in the system view.

For the configuration details, see [Configuring IPv4 Multi-topology](dc_vrp_ip-route_cfg_0017.html). Ensure that one of the topology names is **multicast**.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast rpf multi-topology**](cmdqueryname=multicast+rpf+multi-topology)
   
   
   
   The multicast multi-topologies view of the public network instance is displayed.
3. Run [**apply topology**](cmdqueryname=apply+topology) { **base** | *topology-name* }
   
   
   
   Multicast services are enabled to run in a unicast topology instance.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.