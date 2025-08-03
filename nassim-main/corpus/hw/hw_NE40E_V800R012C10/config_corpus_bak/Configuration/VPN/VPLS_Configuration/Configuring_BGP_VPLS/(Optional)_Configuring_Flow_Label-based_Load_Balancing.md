(Optional) Configuring Flow Label-based Load Balancing
======================================================

After flow label-based load balancing is configured for an L2VPN, L2VPN services can be classified by flow labels and forwarding paths can be selected based on the flow labels, improving forwarding efficiency.

#### Prerequisites

Before configuring flow label-based load balancing, complete the following task:

* Configure MPLS L2VPN.

#### Context

On an L2VPN carrying service traffic, if multiple links for a PW exist between Ps, flow label-based load balancing can be configured to improve traffic forwarding efficiency and mitigate the forwarding pressure on Ps. After this function is configured, the PEs can add flow labels to different types of traffic to distinguish one from another. When a P receives packets carrying flow labels, the P selects paths based on the flow labels to forward the packets, implementing load balancing.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
   
   
   
   The VSI view is displayed.
3. Run [**pwsignal**](cmdqueryname=pwsignal) **bgp**
   
   
   
   The VSI-BGP view is displayed.
4. Run [**flow-label**](cmdqueryname=flow-label) { **both** | **send** | **receive** } [ **static** ]
   
   
   
   L2VPN flow label-based load balancing is enabled for the VSI.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Flow label-based load balancing can be successfully configured if one of the following conditions is met:
     + The **receive** parameter is configured on the local end, and the **send** parameter is configured on the remote end.
     + The **send** parameter is configured on the local end, and the **receive** parameter is configured on the remote end.
     + The **both** parameter is configured on both ends.
   * If the **static** parameter is configured, the static flow label-based load balancing mode is enabled.
     
     In this mode, if the two ends have inconsistent configurations, packets carrying flow labels are discarded, causing traffic loss.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.