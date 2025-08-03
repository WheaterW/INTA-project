(Optional) Configuring FRR
==========================

In EVPN VPWS over MPLS multi-homing single-active scenarios, FRR needs to be configured to prevent traffic loss if the primary PE fails.

#### Usage Scenario

As shown in the following figure, in the EVPN VPWS over MPLS multi-homing single-active scenario, a CE is dual-homed to PE1 and PE2 in active-active mode, and PE3 forwards traffic to PE1 and PE2 working in active/standby mode. When PE1 is the active device, the red path between CE1 and CE2 is the active path, and the blue path is the standby path. To prevent traffic loss when the active path fails, FRR needs to be configured.

In normal situations, downstream traffic of PE3 is sent to PE1. Local-remote FRR is enabled on PE1 and PE2. If PE1 detects a fault on the link between itself and CE1, PE1 forwards traffic to PE2 and then to CE1. Remote FRR is enabled on PE3. When PE3 detects a fault between itself and PE1, PE3 rapidly switches traffic to PE2 and then sends traffic to CE1, preventing traffic loss.

**Figure 1** Configuring EVPN VPWS over MPLS  
![](images/fig_dc_vrp_evpn_cfg_110006.png)

#### Procedure

* Configure local-remote FRR on PE1 and PE2.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **vpws**
     
     
     
     The EVPN VPWS instance view.
  3. Run [**local-remote frr enable**](cmdqueryname=local-remote+frr+enable)
     
     
     
     Local-remote FRR is enabled for the EVPN VPWS instance.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     In addition to enabling local-remote FRR in the EVPN VPWS instance view, you can run the [**local-remote vpws-frr enable**](cmdqueryname=local-remote+vpws-frr+enable) command in the global EVPN configuration view to enable local-remote FRR.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure remote FRR on PE3.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **vpws**
     
     
     
     The EVPN VPWS instance view.
  3. Run [**remote frr**](cmdqueryname=remote+frr) **enable**
     
     
     
     Remote FRR is enabled for the EVPN VPWS instance.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     In addition to enabling remote FRR in the EVPN VPWS instance view, you can run the [**remote vpws-frr enable**](cmdqueryname=remote+vpws-frr+enable) command in the global EVPN configuration view to enable remote FRR globally. By default, if the [**remote frr**](cmdqueryname=remote+frr) command is not run in the EVPN VPWS instance view, the [**remote frr**](cmdqueryname=remote+frr) command configuration in the global view takes effect. If the [**remote frr**](cmdqueryname=remote+frr) command is run in the EVPN VPWS instance view, this configuration takes effect.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.