Configuring the POPGO Function
==============================

After the POPGO function is configured on the egress of a BGP LSP, the egress forwards each data packet received from the LSP through the outbound interface found in the ILM based on the label information carried in the packet.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0172366244__fig_dc_vrp_bgp_cfg_409301), DeviceC has two static routes, 10.1.1.0/24 and 10.1.1.0/30, and the next hops of the two routes are DeviceA and DeviceB, respectively. DeviceC only imports route 10.1.1.0/24 to BGP and then sends this route to DeviceD. A BGP LSP is established between DeviceC and DeviceD. By default, after DeviceC receives a data packet destined for 10.1.1.0 from DeviceD, DeviceC removes the BGP LSP label from the packet, searches the IP forwarding table for the outbound interface, and forwards the packet along the route 10.1.1.0/30 based on the longest match rule. That is, the packet is incorrectly forwarded to DeviceB.

To solve the preceding problem, run the [**apply-label per-route pop-go**](cmdqueryname=apply-label+per-route+pop-go) command in the BGP view on DeviceC. After the [**apply-label per-route pop-go**](cmdqueryname=apply-label+per-route+pop-go) command is configured, when DeviceC sends route 10.1.1.0/24 to DeviceD, DeviceC records in the ILM the mapping between the label assigned to the route and the outbound interface of the route. After the local device receives a labeled data packet through a BGP LSP, the local device no longer searches the IP forwarding table based on the longest match rule. Instead, the local device searches the ILM for an outbound interface based on the label value and forwards the packet through this outbound interface after removing its label. This ensures correct packet forwarding.

**Figure 1** POPGO networking  
![](images/fig_dc_vrp_bgp_cfg_409301.png)  


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**apply-label per-route pop-go**](cmdqueryname=apply-label+per-route+pop-go)
   
   
   
   The BGP POPGO function is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

Run the [**display mpls lsp protocol bgp**](cmdqueryname=display+mpls+lsp+protocol+bgp) command on the device to view detailed information about BGP LSP establishment. If **POPGO** is displayed in the **Label Operation** field, the POPGO function is successfully configured.