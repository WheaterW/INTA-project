Configuring Evolution from Traditional VPWS to EVPN VPWS over MPLS
==================================================================

EVPN is today's mainstream transport solution. To prevent live network services from being affected, a new transport solution must be deployed based on these services. If a large number of traditional VPWS services exist on the live network, you can configure evolution from traditional VPWS to EVPN VPWS over MPLS to prevent traffic interruption caused by direct transition from traditional VPWS to EVPN VPWS over MPLS.

#### Context

Traditional L2VPNs use VPWS for Layer 2 communication. Compared with traditional VPWS, EVPN â a next-generation VPN technology â has many advantages, such as support for multi-homing all-active networking and easy maintenance. Therefore, traditional VPWS is gradually evolving to EVPN. However, there are still a large number of existing VPWS services on the live network. To use EVPN VPWS over MPLS, you must configure evolution from traditional VPWS to EVPN VPWS over MPLS to ensure that existing services are not interrupted during the evolution.

On the network shown in [Figure 1](#EN-US_TASK_0000001285473473__fig579251613147), both traditional VPWS and EVPN VPWS over MPLS are deployed on PE1 and PE2. In this case, you need to configure evolution from traditional VPWS to EVPN VPWS over MPLS on PE1 and PE2.

**Figure 1** Evolution from traditional VPWS to EVPN VPWS over MPLS  
![](figure/en-us_image_0000001322788609.png)

#### Pre-configuration Tasks

Before configuring evolution from traditional VPWS to EVPN VPWS over MPLS, complete the following tasks:

* [Configure LDP VPWS](dc_vrp_vpws_cfg_3004.html) or [BGP VPWS](dc_vrp_vpws_cfg_6054.html) between PE1 and PE2.
* [Configure EVPN VPWS over MPLS](dc_vrp_evpn_cfg_0020.html) between PE1 and PE2. ![](../../../../public_sys-resources/note_3.0-en-us.png) The pre-configuration tasks have the following requirements:
  + VPWS and the EVPL instance that carry the same service must be configured on the same AC interface.
  + Traditional VPWS must be configured prior to the EVPL instance of EVPN VPWS on the AC interface. Otherwise, the configuration fails.

Perform the following steps on PE1 and PE2.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpn**](cmdqueryname=evpn)
   
   
   
   The EVPN global configuration view is displayed.
3. Run [**timer migrate delay**](cmdqueryname=timer+migrate+delay) *delay-value*
   
   
   
   An EVPN VPWS switching delay is configured.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To forcibly roll services that have been switched to EVPN VPWS back to traditional VPWS, run the [**migration rollback l2vpn**](cmdqueryname=migration+rollback+l2vpn) command in the EVPL instance view.

#### Verifying the Configuration

* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix* command to check detailed BGP EVPN route information, including PW information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) **vpn-instance** *vpn-instance-name* **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* command to check EVPN routing information (including PW information) about the specified EVPN instance.
* In a scenario where a CE is dual-homed to PEs, run the [**display evpn vpn-instance name**](cmdqueryname=display+evpn+vpn-instance+name) *vpn-instance-name* **df result** [ **esi** *esi* ] command to check the DF election result (including PW information) of the specified EVPN instance.
* Run the [**display l2vpn traffic-forwarding**](cmdqueryname=display+l2vpn+traffic-forwarding) **interface** { *interface-name* | *interface-type* *interface-num* } command to check whether the current service type is EVPN VPWS or traditional VPWS on the specified interface.