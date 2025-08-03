(Optional) Configuring Flow Label-based Load Balancing
======================================================

Flow label-based load balancing enables L2VPN data flows on a PW to be load-balanced over tunnels between P devices based on flow labels, improving forwarding efficiency.

#### Context

When multiple links exist between P devices, configure flow label-based load balancing to improve L2VPN traffic forwarding efficiency. After flow label-based load balancing is enabled on a PE, the PE adds different labels for different L2VPN data flows to distinguish them one from the other. After a P device receives a data packet carrying a flow label, it performs the Hash calculation and selects a forwarding path based on the flow label in the data packet. This processing implements load balancing. To enable flow label-based load balancing for PWs, run the [**flow-label**](cmdqueryname=flow-label) command.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Currently, only LDP VPWS, LDP VPLS, static VPWS, and static VPLS support flow label-based load balancing.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**flow-label hash-fields**](cmdqueryname=flow-label+hash-fields) { **l2** | **l3** | **l4** }
   
   
   
   The hash factor for flow label-based load balancing is configured.
   
   
   
   This command takes effect only after PW L2VPN flow label-based load balancing is enabled in the interface view.
   
   This command is supported only by the admin VS.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The AC interface view is displayed.
4. Run [**mpls l2vpn flow-label**](cmdqueryname=mpls+l2vpn+flow-label) { **both** | **send** | **receive** } [ **secondary** ] [ **static** ]
   
   
   
   Flow label-based load balancing is enabled for PWs on the interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Flow label-based load balancing can be enabled only when any of the following conditions is met:
     + The **receive** parameter is configured on the local PE, and the **send** parameter is configured on the remote PE.
     + The **send** parameter is configured on the local PE, and the **receive** parameter is configured on the remote PE.
     + Both the **send** and **receive** parameters are configured on the local and remote PEs.
   * If **secondary** is configured, the flow label-based load balancing capability takes effect only for the secondary PW on the interface. If **secondary** is not configured, the flow label-based load balancing capability takes effect only for the primary PW on the interface.
   * If **static** is configured, the flow label-based load balancing capability is statically configured. The endpoint PEs deliver the flow label-based load balancing capability, irrespective of whether the other end has the capability enabled. For dynamic PWs, if **static** is not configured, the flow label-based load balancing capability of the local end is negotiated by the remote end. For static PWs, the flow label-based load balancing capability is statically configured, irrespective of whether **static** is configured.
     
     If the static flow label-based load balancing configuration does not match on both ends, the device discards packets carrying a flow label, causing packet loss.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.