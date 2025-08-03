Setting a Delay in Releasing an Obtained Label in a BGP EVPN FRR Switchover Scenario
====================================================================================

After you set a delay in releasing an obtained label in a BGP EVPN FRR switchover scenario, you can prevent second-time packet loss.

#### Usage Scenario

As shown in [Figure 1](#EN-US_TASK_0183675446__fig1499024145414), DeviceA and DeviceD belong to AS100, and DeviceB, DeviceC, DeviceE, and DeviceF belong to AS200 in a BGP EVPN FRR switchover scenario. DeviceB selects the optimal route that is learned from the EBGP EVPN peer DeviceA and the sub-optimal route that is learned from the IBGP EVPN peer DeviceE. In normal situations, DeviceB preferentially selects a labeled BGP route learned from EBGP EVPN peer DeviceA and advertises the route to the IBGP EVPN peer DeviceC. DeviceB delivers an incoming label map (ILM) entry and next hop label forwarding entry (NHLFE), and DeviceC also delivers an NHLFE entry. If DeviceA is restarted due to a fault, DeviceB withdraws the route learned from DeviceA, selects the sub-optimal route learned from IBGP EVPN peer DeviceE, and reflects the route to DeviceC through the RR. Then, DeviceB releases the applied label and deletes the ILM entry mapped to the label. If traffic arrives at DeviceC before DeviceC updates the NHLFE entry, DeviceC still uses this entry to forward traffic to DeviceB. Because DeviceB has released the label and deleted the ILM entry, packets are lost for the second time.

**Figure 1** Networking for packet loss during a BGP EVPN FRR switchover  
![](figure/en-us_image_0000001184881798.png)  

To prevent traffic loss during a BGP EVPN FRR switchover, configure the local device to delay deleting the ILM entry.


#### Pre-configuration Tasks

Before setting a delay in releasing an obtained label in a BGP EVPN FRR switchover scenario, complete the following tasks:

* [Configure EVPN VPLS over MPLS (common EVPN instance)](dc_vrp_evpn_cfg_0003.html) or [EVPN VPLS over MPLS (BD EVPN instance)](dc_vrp_evpn_cfg_0065.html).
* [Configure BGP auto FRR](dc_vrp_bgp_cfg_4057.html) in the BGP-EVPN address family view.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run **l2vpn-family evpn**
   
   
   
   The BGP-EVPN address family view is displayed.
4. Run [**label-free delay**](cmdqueryname=label-free+delay) *delay-value*
   
   
   
   A delay for releasing obtained labels is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After completing the configuration, verify the configuration.

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check the current configuration.