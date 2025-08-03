Configuring Basic SR-MPLS TE Functions
======================================

This section describes how to configure basic SR-MPLS TE functions.

#### Context

SR-MPLS TE supports both strict and loose explicit paths. Strict explicit paths mainly use adjacency SIDs, whereas loose explicit paths use both adjacency and node SIDs. Adjacency and node SIDs must be generated before you configure an SR-MPLS TE tunnel.


#### Procedure

1. Configure an SR-MPLS-specific SRGB range.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
      
      
      
      The IS-IS view is displayed.
   3. Run [**network-entity**](cmdqueryname=network-entity) *net-addr*
      
      
      
      A network entity title (NET) is configured.
   4. Run [**cost-style**](cmdqueryname=cost-style) { **wide** | **compatible** | **wide-compatible** }
      
      
      
      The IS-IS wide metric function is enabled.
   5. Run [**traffic-eng**](cmdqueryname=traffic-eng) [ **level-1** | **level-2** | **level-1-2** ]
      
      
      
      IS-IS TE is enabled.
   6. Run [**segment-routing mpls**](cmdqueryname=segment-routing+mpls)
      
      
      
      IS-IS SR-MPLS is enabled.
   7. Run [**segment-routing global-block**](cmdqueryname=segment-routing+global-block) *begin-value* *end-value* [ **ignore-conflict** ]
      
      
      
      An SR-MPLS-specific SRGB range is configured for the current IS-IS instance.
      
      
      
      If a message is displayed indicating that a label in the specified SRGB range is in use, you can use the **ignore-conflict** parameter to enable configuration delivery. However, the configuration will not take effect until the device is restarted and the label is released. In general, using the **ignore-conflict** parameter is not recommended.
   8. (Optional) Run [**segment-routing auto-adj-sid protected**](cmdqueryname=segment-routing+auto-adj-sid+protected)
      
      
      
      The function of automatically generating dynamic protected adjacency SIDs is enabled.
   9. (Optional) Run [**segment-routing mpls static adj-sid advertise**](cmdqueryname=segment-routing+mpls+static+adj-sid+advertise)
      
      
      
      Advertisement of static adjacency SIDs is enabled.
      
      
      
      Typically, in SR-MPLS TE scenarios, adjacency SIDs are dynamically generated and advertised by IGP. Static adjacency SIDs are manually configured. To enable the device to advertise such SIDs, run the [**segment-routing mpls static adj-sid advertise**](cmdqueryname=segment-routing+mpls+static+adj-sid+advertise) command in the IS-IS view.
   10. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
   11. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
2. Configure an SR-MPLS prefix SID.
   1. Run [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number*
      
      
      
      A loopback interface is created, and the interface view is displayed.
   2. Run [**isis enable**](cmdqueryname=isis+enable) [ *process-id* ]
      
      
      
      IS-IS is enabled on the interface.
   3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
      
      
      
      An IP address is configured for the loopback interface.
   4. Run [**isis prefix-sid**](cmdqueryname=isis+prefix-sid) { **absolute** *sid-value* | **index** *index-value* } [ **node-disable** ]
      
      
      
      An SR-MPLS prefix SID is configured for the IP address of the interface.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. (Optional) Configure an adjacency SID.
   
   
   
   After IS-IS SR is enabled, an adjacency SID is automatically generated. To disable the automatic generation of adjacency SIDs, run the [**segment-routing auto-adj-sid disable**](cmdqueryname=segment-routing+auto-adj-sid+disable) command. Dynamically generated adjacency SIDs may change after a device restart. If an explicit path uses such an adjacency SID and the associated device is restarted, the adjacency SID needs to be reconfigured. You can also manually configure an adjacency SID to facilitate the use of an explicit path.
   
   
   
   1. Run [**segment-routing**](cmdqueryname=segment-routing)
      
      
      
      The SR view is displayed.
   2. Run [**ipv4 adjacency**](cmdqueryname=ipv4+adjacency) **local-ip-addr** *local-ip-address* **remote-ip-addr** *remote-ip-address* **sid** *sid-value* [ **vpn-instance** *vpn-name* ] or [**ipv4 adjacency**](cmdqueryname=ipv4+adjacency) **local-ip-addr** *local-ip-address* **remote-ip-addr** *remote-ip-address* **sid** *sid-value* **protected**
      
      
      
      A static SR adjacency SID is configured.
      
      
      
      To enable the device to steer traffic to a VPN link based on the static adjacency SID, specify the **vpn-instance** *vpn-name* parameter.
      
      To configure an adjacency SID carrying the protection flag so that it can be protected by another adjacency SID, specify the **protected** parameter.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.