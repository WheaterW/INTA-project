Configuring OSPF Flex-Algo Functions
====================================

The Flex-Algos associated with the local prefix SIDs of a device as well as the FADs on the device all need to be advertised through OSPF.

#### Context

Each device can use an IGP to advertise their supported Flex-Algos and the specific calculation rules of a Flex-Algo through the FAD Sub-TLV.

These Flex-Algos can be associated with prefix SIDs during prefix SID configuration. The IGP can then advertise the Flex-Algos and prefix SIDs through the Prefix-SID Sub-TLV.


#### Procedure

1. Enable SR-MPLS globally.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**segment-routing**](cmdqueryname=segment-routing)
      
      
      
      The SR view is displayed.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Enable OSPF to advertise Flex-Algos.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
      
      
      
      The OSPF view is displayed.
   3. Run [**opaque-capability enable**](cmdqueryname=opaque-capability+enable)
      
      
      
      The Opaque LSA capability is enabled.
   4. Run [**segment-routing mpls**](cmdqueryname=segment-routing+mpls)
      
      
      
      OSPF SR-MPLS is enabled.
   5. Run [**segment-routing global-block**](cmdqueryname=segment-routing+global-block) *begin-value* *end-value* [ **ignore-conflict** ]
      
      
      
      An SR-MPLS-specific SRGB range is configured for the current OSPF process.
      
      
      
      If a message is displayed indicating that a label in the specified SRGB range is in use, you can use the **ignore-conflict** parameter to enable configuration delivery. However, the configuration will not take effect until the device is restarted and the label is released. In general, using the **ignore-conflict** parameter is not recommended.
   6. Run [**flex-algo**](cmdqueryname=flex-algo)*flexAlgoIdentifier*
      
      
      
      The Flex-Algo advertisement capability is enabled for OSPF.
      
      
      
      The configuration in the OSPF view takes effect for all areas.
   7. Run [**advertise link-attributes application flex-algo**](cmdqueryname=advertise+link-attributes+application+flex-algo)
      
      
      
      The capability to advertise application-specific link attributes is configured.
      
      
      
      When Flex-Algo is used to compute paths based on constraints (such as the link delay, TE attributes, and affinity attributes) to meet different requirements, run the [**advertise link-attributes application flex-algo**](cmdqueryname=advertise+link-attributes+application+flex-algo) command so that the link attributes applied to Flex-Algo can be advertised through the Application-Specific Link Attributes (ASLA) sub-TLV in OSPF LSAs.
   8. Run [**area**](cmdqueryname=area) *area-id*
      
      
      
      The OSPF area view is displayed.
   9. Run [**flex-algo**](cmdqueryname=flex-algo)*flexAlgoIdentifier* [ **disable** ]
      
      
      
      The Flex-Algo advertisement capability is enabled for the OSPF area.
      
      
      
      The Flex-Algo advertisement capability can be configured in both the OSPF view and OSPF area view but the configuration in the OSPF area view takes precedence.
      
      * If this configuration exists both in the OSPF view and OSPF area view, the one in the OSPF area view takes effect preferentially.
      * If this configuration exists only in the OSPF view, the OSPF area inherits it in the OSPF view. If you do not want to advertise Flex-Algo in this area, specify the **disable** parameter.
   10. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
   11. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
3. Associate a Flex-Algo with a prefix SID.
   1. Run [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number*
      
      
      
      A loopback interface is created, and its view is displayed.
   2. Run [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id*
      
      
      
      OSPF is enabled on the interface.
   3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
      
      
      
      An IP address is configured for the loopback interface.
   4. Run [**ospf prefix-sid**](cmdqueryname=ospf+prefix-sid) { **absolute** *sid-value* | **index** *index-value* } **flex-algo** *flex-algo-id* [ **node-disable** ]
      
      
      
      An SR-MPLS prefix SID is configured for the IP address of the loopback interface.
      
      
      
      The **flex-algo** *flex-algo-id* parameter allows you to associate the prefix SID with a specified Flex-Algo, so that OSPF advertises the associated Flex-Algo when advertising the prefix SID.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.