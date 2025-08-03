Configuring IS-IS Flex-Algo Functions
=====================================

The Flex-Algos associated with the local prefix SIDs of a device as well as the FADs on the device all need to be advertised through IS-IS.

#### Context

After Flex-Algos are defined, each device can use an IGP to advertise their supported Flex-Algos and the specific calculation rules of a Flex-Algo through the FAD Sub-TLV.

These Flex-Algos can be associated with prefix SIDs during prefix SID configuration. The IGP can then advertise the Flex-Algos and prefix SIDs through the Prefix-SID Sub-TLV.


#### Procedure

1. Enable SR-MPLS globally.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**segment-routing**](cmdqueryname=segment-routing)
      
      
      
      SR is enabled, and the SR view is displayed.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Enable IS-IS to advertise Flex-Algos.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
      
      
      
      The IS-IS view is displayed.
   3. Run [**network-entity**](cmdqueryname=network-entity) *net-addr*
      
      
      
      A network entity title (NET) is configured.
   4. Run [**cost-style**](cmdqueryname=cost-style) { **wide** | **compatible** | **wide-compatible** }
      
      
      
      The IS-IS wide metric attribute is configured.
   5. Run [**traffic-eng**](cmdqueryname=traffic-eng) [ **level-1** | **level-2** | **level-1-2** ]
      
      
      
      IS-IS TE is enabled.
   6. Run [**advertise link attributes**](cmdqueryname=advertise+link+attributes)
      
      
      
      The IS-IS process is enabled to advertise link attribute-related TLVs through LSPs. Link attributes include the IP address and interface index.
   7. (Optional) Run **[**metric-delay advertisement enable**](cmdqueryname=metric-delay+advertisement+enable)** [ **level-1** | **level-2** | **level-1-2** ]
      
      
      
      Delay information advertisement is enabled.
      
      In a scenario where IS-IS Flex-Algos calculate paths based on delay information, you need to run this command to enable link delay advertisement through IS-IS.
   8. Run [**segment-routing mpls**](cmdqueryname=segment-routing+mpls)
      
      
      
      IS-IS SR-MPLS is enabled.
   9. Run [**segment-routing global-block**](cmdqueryname=segment-routing+global-block) *begin-value* *end-value* [ **ignore-conflict** ]
      
      
      
      An SR-MPLS-specific SRGB range is configured for the current IS-IS process.
      
      
      
      If a message is displayed indicating that a label in the specified SRGB range is in use, you can use the **ignore-conflict** parameter to enable configuration delivery. However, the configuration will not take effect until the device is restarted and the label is released. In general, using the **ignore-conflict** parameter is not recommended.
   10. Run [**flex-algo**](cmdqueryname=flex-algo)*flexAlgoIdentifier* [ **level-1** | **level-2** | **level-1-2** ]
       
       
       
       IS-IS is enabled to advertise Flex-Algos.
   11. (Optional) Run [**flex-algo prefix-sid incr-prefix-cost**](cmdqueryname=flex-algo+prefix-sid+incr-prefix-cost)
       
       
       
       The device is enabled to count in the IS-IS cost of the loopback interface when calculating the cost of an IS-IS Flex-Algo SR-MPLS prefix SID route.
       
       
       
       By default, the device does not count in the IS-IS cost of the loopback interface when calculating the cost of an IS-IS Flex-Algo SR-MPLS prefix SID route in the same IS-IS level. After you run the [**flex-algo prefix-sid incr-prefix-cost**](cmdqueryname=flex-algo+prefix-sid+incr-prefix-cost) command, the cost of the prefix SID route covers the IS-IS cost of the loopback interface, regardless of the metric type used in Flex-Algo calculation.
       
       When a Huawei device interworks with a non-Huawei device, you can run this command to prevent loops caused by the difference in default route calculation behaviors.
   12. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
   13. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
3. Associate a Flex-Algo with a prefix SID.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number*
      
      
      
      A loopback interface is created, and its view is displayed.
   3. Run [**isis enable**](cmdqueryname=isis+enable) [ *process-id* ]
      
      
      
      IS-IS is enabled on the loopback interface.
   4. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
      
      
      
      An IP address is configured for the loopback interface.
   5. Run [**isis prefix-sid**](cmdqueryname=isis+prefix-sid) { **absolute** *sid-value* | **index** *index-value* } [ **node-disable** ] **flex-algo** *flex-algo-id*
      
      
      
      A prefix SID is configured for the IP address of the loopback interface.
      
      
      
      The **flex-algo** *flex-algo-id* parameter allows you to associate the prefix SID with a specified Flex-Algo, so that IS-IS advertises the associated Flex-Algo when advertising the prefix SID.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.