Enabling MT for an IS-IS Process (IPv4)
=======================================

Based on service requirements and the network plan, an IS-IS process can be associated with various topology instances so that multiple logical topologies are deployed in an IS-IS AS.

#### Context

You can associate an IS-IS process with unicast or multicast topology instances as required so that the SPF calculation can be performed for the topology instances in the IS-IS process. Then, you can configure parameters, such as the interface cost and protocol priority for the topology instances.

The configuration in an IS-IS topology instance view takes effect only on the topology instance. Therefore, you can configure different features and parameters for different topology instances as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip topology**](cmdqueryname=ip+topology) *topology-name*
   
   
   
   An IPv4 topology instance is configured.
3. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
4. Run [**cost-style**](cmdqueryname=cost-style) { **wide** | **wide-compatible** }
   
   
   
   The cost style of packets to be sent and accepted by the Router is set to **wide** or **wide-compatible**.
5. Run [**topology**](cmdqueryname=topology) *topology-name* **topology-id** { *mt-id* | **multicast** }
   
   
   
   The IS-IS process is associated with a specified topology instance, and the IS-IS topology instance view is displayed.
6. (Optional) Configure IS-IS parameters for the IPv4 topology instance. The supported commands are as follows:
   
   
   * To set a preference for IS-IS, run the [**preference**](cmdqueryname=preference) command.
   * To enable an IS-IS device to generate a default route, run the [**default-route-advertise**](cmdqueryname=default-route-advertise) command.
   * To enable an IS-IS device to import routes from other routing protocols in the IS-IS view, run the [**import-route**](cmdqueryname=import-route) command.
   * To control IS-IS route leaking from a Level-1 area to a Level-2 area, run the [**import-route isis level-1 into level-2**](cmdqueryname=import-route+isis+level-1+into+level-2) command.
   * To control IS-IS route leaking from a Level-2 area to a Level-1 area, run the [**import-route isis level-2 into level-1**](cmdqueryname=import-route+isis+level-2+into+level-1) command.
   * To enable IS-IS summarization, run the [**summary**](cmdqueryname=summary) command.
   * To configure a link cost for all interfaces of a specified IS-IS process, run the [**circuit-cost**](cmdqueryname=circuit-cost) { *cost* | **maximum** } [ **level-1** | **level-2** ] command.
   * To enable IS-IS to automatically calculate the interface cost according to the interface bandwidth, run the [**auto-cost enable**](cmdqueryname=auto-cost+enable) [ **compatible** ] command.
   * To set a bandwidth reference value used for automatic interface cost calculation, run the [**bandwidth-reference**](cmdqueryname=bandwidth-reference) *value* command.
   * To set the maximum number of equal-cost routes for load balancing, run the [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) *number* command.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.