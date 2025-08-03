Enabling IPv6 Multicast Services to Run in a Unicast Topology or the Base Topology Instance
===========================================================================================

Using a unicast topology or the base topology instance for IPv6 multicast services is applicable only to the PIM-SM intra-domain scenario.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before enabling multicast services to run in a specified unicast topology instance, you must configure a multicast topology instance and a unicast topology instance in the system view.

For configuration details, see [Configuring IPv6 Multi-Topologies](dc_vrp_ip-route_cfg_0026.html). Make sure that *topology-name* is **multicast**.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast ipv6 rpf multi-topology**](cmdqueryname=multicast+ipv6+rpf+multi-topology)
   
   
   
   The IPv6 multicast multi-topology view is displayed.
3. Run [**apply topology**](cmdqueryname=apply+topology) { **base** | *topology-name* }
   
   
   
   IPv6 multicast services are enabled to run in a unicast topology instance or the base topology instance.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.