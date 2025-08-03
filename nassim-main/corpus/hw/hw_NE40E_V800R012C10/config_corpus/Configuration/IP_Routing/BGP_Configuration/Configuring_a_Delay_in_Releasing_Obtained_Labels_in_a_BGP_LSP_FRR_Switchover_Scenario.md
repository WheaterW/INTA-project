Configuring a Delay in Releasing Obtained Labels in a BGP LSP FRR Switchover Scenario
=====================================================================================

Configuring a delay in releasing obtained labels in a BGP LSP FRR switchover scenario can prevent second-time packet loss.

#### Usage Scenario

In a BGP LSP FRR switchover scenario shown in [Figure 1](#EN-US_TASK_0172366261__fig_label-free_delay_0001), DeviceA and DeviceD belong to AS 100, and DeviceB, DeviceC, DeviceE, and DeviceF belong to AS 200. The optimal route selected by DeviceB is a route learned from its EBGP peer DeviceA, and the suboptimal route selected by DeviceB is a route learned from its IBGP peer DeviceE. In normal cases, DeviceB preferentially selects the labeled BGP route learned from its EBGP peer DeviceA and sends the route to its IBGP peer DeviceC. DeviceB delivers an incoming label map (ILM) entry and next hop label forwarding entry (NHLFE). DeviceC also delivers an NHLFE. If DeviceA restarts due to a fault, DeviceB withdraws the route learned from DeviceA. The suboptimal route learned from its IBGP peer DeviceE becomes the new optimal route and is not sent to its IBGP peer DeviceC. Instead, DeviceB (RR) reflects this route to DeviceC. Therefore, DeviceB releases the label that has been applied for, deletes the ILM entry. If the NHLFE entry of DeviceC is updated slowly, traffic is still sent to DeviceB. In this case, packet loss occurs again because the ILM entry of DeviceB has been deleted.

**Figure 1** BGP LSP FRR switchover networking  
![](images/fig_label-free_delay_0001.png)  

To prevent this problem, configure a delay in releasing obtained labels (deleting ILM entries) on Device B.


#### Pre-configuration Tasks

Before configuring a delay in releasing obtained labels in a BGP LSP FRR switchover scenario, complete the following tasks:

* [Configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).
* [Configure BGP Auto FRR](dc_vrp_bgp_cfg_4057.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
4. Run [**label-free delay**](cmdqueryname=label-free+delay) *delay-value*
   
   
   
   A delay in releasing obtained labels is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check the valid configuration.