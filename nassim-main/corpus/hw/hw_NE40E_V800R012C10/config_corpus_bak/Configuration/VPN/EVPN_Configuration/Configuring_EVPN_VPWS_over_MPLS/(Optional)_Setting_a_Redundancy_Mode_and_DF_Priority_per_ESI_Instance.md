(Optional) Setting a Redundancy Mode and DF Priority per ESI Instance
=====================================================================

In a scenario where multiple CEs are dual-homed to PEs, if you want to use different transmission modes (load balancing and non-load balancing) to send unicast traffic to different CEs or if you want to specify DFs for traffic forwarding by setting priority values, you can set a redundancy mode and DF priority values based on ESIs.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0273479577__fig_dc_vrp_evpn_cfg_011001), CE1 and CE2 are both dual-homed to PE1 and PE2. The PE interfaces that connect to CE1 have ESI 1, and the PE interfaces that connect to CE2 have ESI 2. If you want CE3-to-CE1 unicast traffic and CE3-to-CE2 unicast traffic to be transmitted in load balancing and non-load balancing mode, respectively, you can set a redundancy mode per ESI instance. Specifically, you can set the redundancy mode of the ESI 1 instance to all-active and that of the ESI 2 instance to single-active.

If you want CE3-to-CE2 BUM traffic to be forwarded by PE1, configure ESI-based DF priority election on PE1 and PE2 and specify PE1 as the primary DF.

**Figure 1** Setting a redundancy mode per ESI  
![](figure/en-us_image_0273480764.png)

An ESI can be dynamically generated or statically configured. A redundancy mode per ESI instance must be set based on the ESI generation mode.


#### Procedure

* Set a redundancy mode based on a statically configured ESI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**evpn**](cmdqueryname=evpn+%28system+view%29)
     
     
     
     The global EVPN configuration view is displayed.
  3. Run [**esi**](cmdqueryname=esi) *esi*
     
     
     
     A static ESI instance name is configured.
     
     The *esi* value must be the same as the name of the statically configured ESI on the interface.
  4. Run [**evpn redundancy-mode**](cmdqueryname=evpn+redundancy-mode) { **single-active** | **all-active** }
     
     
     
     A redundancy mode is configured for the static ESI instance.
  5. (Optional) Run [**df-election type preference-based**](cmdqueryname=df-election+type+preference-based)
     
     
     
     Priority-based DF election is enabled in EVPN VPWS scenarios.
  6. (Optional) Run [**preference**](cmdqueryname=preference) *preference*
     
     
     
     A priority value is set. A larger *preference* value indicates a higher priority.
  7. (Optional) Run [**non-revertive**](cmdqueryname=non-revertive)
     
     
     
     The non-revertive mode is enabled.
     
     
     
     On the network shown in [Figure 1](#EN-US_TASK_0273479577__fig_dc_vrp_evpn_cfg_011001), CE2 is dual-homed to PE1 and PE2. PE1 is elected as the primary DF to forward traffic because it has a higher priority. If PE1 fails, traffic is switched to PE2 for forwarding. After PE1 recovers, traffic is switched back to PE1. To reduce traffic switching times and maintain service topology stability, run the [**non-revertive**](cmdqueryname=non-revertive) command to disable traffic switchback.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set a redundancy mode based on a dynamically generated ESI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**evpn**](cmdqueryname=evpn+%28system+view%29)
     
     
     
     The global EVPN configuration view is displayed.
  3. Run [**esi dynamic-name**](cmdqueryname=esi+dynamic-name) *esi-name*
     
     
     
     A dynamic ESI instance name is configured.
  4. Run [**evpn redundancy-mode**](cmdqueryname=evpn+redundancy-mode) { **single-active** | **all-active** }
     
     
     
     A redundancy mode is configured for the dynamic ESI instance.
  5. (Optional) Run [**df-election type preference-based**](cmdqueryname=df-election+type+preference-based)
     
     
     
     Priority-based DF election is enabled in EVPN VPWS scenarios.
  6. (Optional) Run [**preference**](cmdqueryname=preference) *preference*
     
     
     
     A priority value is set. A larger *preference* value indicates a higher priority.
  7. (Optional) Run [**non-revertive**](cmdqueryname=non-revertive)
     
     
     
     The non-revertive mode is enabled.
     
     
     
     On the network shown in [Figure 1](#EN-US_TASK_0273479577__fig_dc_vrp_evpn_cfg_011001), CE2 is dual-homed to PE1 and PE2. PE1 is elected as the primary DF to forward traffic because it has a higher priority. If PE1 fails, traffic is switched to PE2 for forwarding. After PE1 recovers, traffic is switched back to PE1. To reduce traffic switching times and maintain service topology stability, run the [**non-revertive**](cmdqueryname=non-revertive) command to disable traffic switchback.
  8. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the ESI-dynamic view.
  9. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the global EVPN configuration view.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
  11. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
      
      
      
      The Eth-Trunk interface view is displayed.
  12. Run [**esi dynamic**](cmdqueryname=esi+dynamic) *esi-name*
      
      
      
      A dynamic ESI instance is bound to the Eth-Trunk interface.
  13. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.