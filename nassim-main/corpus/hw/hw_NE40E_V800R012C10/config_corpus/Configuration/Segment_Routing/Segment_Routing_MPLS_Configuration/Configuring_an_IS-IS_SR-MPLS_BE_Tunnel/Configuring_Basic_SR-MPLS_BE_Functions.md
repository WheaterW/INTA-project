Configuring Basic SR-MPLS BE Functions
======================================

This section describes how to configure basic SR-MPLS BE functions.

#### Context

Basic SR-MPLS BE function configurations mainly involve enabling SR globally, specifying an SR-MPLS-specific SRGB range, and configuring an SR-MPLS prefix SID.


#### Procedure

1. Enable SR globally.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**segment-routing**](cmdqueryname=segment-routing)
      
      
      
      SR is enabled globally, and the Segment Routing view is displayed.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Configure an SR-MPLS-specific SRGB range.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
      
      
      
      The IS-IS view is displayed.
   3. Run [**network-entity**](cmdqueryname=network-entity) *net-addr*
      
      
      
      A network entity title (NET) is configured.
   4. Run [**cost-style**](cmdqueryname=cost-style) { **wide** | **compatible** | **wide-compatible** }
      
      
      
      The IS-IS wide metric function is enabled.
   5. Run [**segment-routing mpls**](cmdqueryname=segment-routing+mpls)
      
      
      
      IS-IS SR-MPLS is enabled.
   6. Run [**segment-routing global-block**](cmdqueryname=segment-routing+global-block) *begin-value* *end-value* [ **ignore-conflict** ]
      
      
      
      An SR-MPLS-specific SRGB range is configured for the current IS-IS instance.
      
      
      
      If a message is displayed indicating that a label in the specified SRGB range is in use, you can use the **ignore-conflict** parameter to enable configuration delivery. However, the configuration will not take effect until the device is restarted and the label is released. In general, using the **ignore-conflict** parameter is not recommended.
   7. (Optional) Run [**segment-routing mpls over gre**](cmdqueryname=segment-routing+mpls+over+gre)
      
      
      
      The device is enabled to recurse SR-MPLS routes to GRE tunnels.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Configure an SR-MPLS prefix SID.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number*
      
      
      
      A loopback interface is created, and the loopback interface view is displayed.
   3. Run [**isis enable**](cmdqueryname=isis+enable) [ *process-id* ]
      
      
      
      The IS-IS interface is enabled.
   4. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
      
      
      
      The IP address is configured for the loopback interface.
   5. Run [**isis prefix-sid**](cmdqueryname=isis+prefix-sid) { **absolute** *sid-value* | **index** *index-value* } [ **node-disable** ]
      
      
      
      An SR-MPLS prefix SID is configured for the IP address of the loopback interface.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.