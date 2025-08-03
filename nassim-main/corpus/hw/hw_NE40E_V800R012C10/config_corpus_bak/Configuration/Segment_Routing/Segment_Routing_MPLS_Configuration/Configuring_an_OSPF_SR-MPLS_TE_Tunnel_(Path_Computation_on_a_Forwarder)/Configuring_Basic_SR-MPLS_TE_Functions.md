Configuring Basic SR-MPLS TE Functions
======================================

This section describes how to configure basic SR-MPLS TE functions.

#### Context

SR-MPLS TE uses strict and loose explicit paths. Strict explicit paths use adjacency SIDs, and loose explicit paths use adjacency and node SIDs. Before an SR-MPLS TE tunnel is configured, the adjacency and node SIDs must be configured.


#### Procedure

1. Configure an SR-MPLS-specific SRGB range.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
      
      
      
      The OSPF view is displayed.
   3. Run [**opaque-capability enable**](cmdqueryname=opaque-capability+enable)
      
      
      
      The Opaque LSA capability is enabled.
   4. Run [**segment-routing mpls**](cmdqueryname=segment-routing+mpls)
      
      
      
      OSPF SR-MPLS is enabled.
   5. Run [**segment-routing global-block**](cmdqueryname=segment-routing+global-block) *begin-value* *end-value* [ **ignore-conflict** ]
      
      
      
      An SR-MPLS-specific OSPF SRGB range is configured.
      
      
      
      If a message is displayed indicating that a label in the specified SRGB range is in use, you can use the **ignore-conflict** parameter to enable configuration delivery. However, the configuration will not take effect until the device is restarted and the label is released. In general, using the **ignore-conflict** parameter is not recommended.
   6. Run [**area**](cmdqueryname=area) *area-id*
      
      
      
      The OSPF area view is displayed.
   7. Run [**mpls-te enable**](cmdqueryname=mpls-te+enable) [ **standard-complying** ]
      
      
      
      TE is enabled in the OSPF area.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Configure an SR-MPLS prefix SID.
   1. Run [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number*
      
      
      
      A loopback interface is created, and the loopback interface view is displayed.
   2. Run [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id*
      
      
      
      OSPF is enabled on the interface.
   3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
      
      
      
      The IP address is configured for the loopback interface.
   4. Run [**ospf prefix-sid**](cmdqueryname=ospf+prefix-sid) { **absolute** *sid-value* | **index** *index-value* } [ **node-disable** ]
      
      
      
      An SR-MPLS prefix SID is configured for the IP address of the interface.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.