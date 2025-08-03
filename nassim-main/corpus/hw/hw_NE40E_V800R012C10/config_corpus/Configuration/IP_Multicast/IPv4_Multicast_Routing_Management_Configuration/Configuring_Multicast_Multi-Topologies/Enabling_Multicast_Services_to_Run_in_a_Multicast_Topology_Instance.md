Enabling Multicast Services to Run in a Multicast Topology Instance
===================================================================

Using a multicast topology instance for multicast services applies to both PIM-SM intra-domain and inter-domain scenarios.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before enabling multicast services to run in a specified multicast topology instance, you must configure the multicast topology instance in the system view.

For the configuration details, see [Configuring IPv4 Multi-topology](dc_vrp_ip-route_cfg_0017.html). Ensure that *topology-name* is **multicast**.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast rpf multi-topology**](cmdqueryname=multicast+rpf+multi-topology)
   
   
   
   Multicast services are enabled to run in a multicast topology instance.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.