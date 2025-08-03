Enabling MT for an IPv6 IS-IS Process
=====================================

Based on service requirements and the network plan, an IS-IS process can be associated with various topology instances so that multiple logical topologies are deployed in an IS-IS AS.

#### Context

You can associate an IS-IS process with unicast or multicast topology instances as required so that the SPF calculation can be performed for the topology instances in the IS-IS process. Then, you can configure parameters, such as the interface cost and protocol priority for the topology instances.

The configuration in an IS-IS topology instance view takes effect only on the topology instance. Therefore, you can configure different features and parameters for different topology instances as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 topology**](cmdqueryname=ipv6+topology) *topology-name*
   
   
   
   An IPv6 topology instance is configured.
3. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
4. Run [**cost-style**](cmdqueryname=cost-style) { **wide** | **wide-compatible** }
   
   
   
   The cost style of packets to be sent and accepted by the Router is set to **wide** or **wide-compatible**.
5. Run [**ipv6 topology**](cmdqueryname=ipv6+topology) *topology-name* **topology-id** { *topology-id* | **multicast** }
   
   
   
   The IS-IS process is associated with a specified topology instance, and the IS-IS IPv6 topology instance view is displayed.
6. (Optional) Perform configurations for the IS-IS IPv6 topology instance as required.
   
   
   * To set a preference for IS-IS, run the [**ipv6 preference**](cmdqueryname=ipv6+preference) command.
   * To enable an IS-IS device to generate a default route, run the [**default-route-advertise**](cmdqueryname=default-route-advertise) command.
   * To enable a device to import routes from another routing protocol into IS-IS, run the [**ipv6 import-route**](cmdqueryname=ipv6+import-route) command in the IS-IS view.
   * To control IS-IS route leaking from a Level-1 area to a Level-2 area, run the [**ipv6 import-route isis level-1 into level-2**](cmdqueryname=ipv6+import-route+isis+level-1+into+level-2) command.
   * To control IS-IS route leaking from a Level-2 area to a Level-1 area, run the [**ipv6 import-route isis level-2 into level-1**](cmdqueryname=ipv6+import-route+isis+level-2+into+level-1) command.
   * To enable IS-IS summarization, run the [**summary**](cmdqueryname=summary) command.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.