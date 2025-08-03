Configuring EVPN VPLS HVPN over MPLS
====================================

EVPN VPLS HVPN over MPLS can be configured as a replacement of HVPLS to carry Layer 2 services on a hierarchical network.

#### Context

To evolve from VPLS to EVPN on an HVPLS-deployed network, deploy EVPN HVPN VPLS over MPLS as a replacement of HVPLS to carry Layer 2 services.

As shown in [Figure 1](#EN-US_TASK_0172370527__fig1079394911920), an access network is deployed between UPEs and SPEs, and an aggregation network is deployed between SPEs and NPEs. An IGP needs to be deployed on both the access network and aggregation network to achieve route communication at each layer. The BD EVPN function needs to be deployed between neighboring devices. In addition, the EVPN RR function can be deployed on SPEs to allow CE1 and CE2 to transmit information, such as the MAC address.

**Figure 1** Configuring EVPN VPLS HVPN over MPLS  
![](figure/en-us_image_0000001182556782.png)

#### Pre-configuration Tasks

Before configuring EVPN VPLS HVPN over MPLS, complete the following tasks:

* Configure [EVPN VPLS over MPLS (BD EVPN instance)](dc_vrp_evpn_cfg_0065.html) between SPEs and NPEs.
* Perform the following operations on each SPE to implement the EVPN RR function.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The BGP-EVPN address family view is displayed.
4. Specify a UPE and an RR client.
   
   
   * Run the [**peer**](cmdqueryname=peer+upe) { *ipv4-address* | *group-name* } **upe** command to configure the UPE as a peer.
   * Specify an RR client.
     
     1. Run the [**peer**](cmdqueryname=peer+reflect-client) { *ipv4-address* | *group-name* } [**reflect-client**](cmdqueryname=reflect-client) command to configure the RR function and specify the UPE as an RR client.
     2. Run the [**peer**](cmdqueryname=peer+next-hop-local) { *ipv4-address* | *group-name* } [**next-hop-local**](cmdqueryname=next-hop-local) command to configure a device to use its own IP address as the next hop IP address during route advertisement.
        
        To allow an SPE to use its own address as the next-hop address when advertising routes to UPEs and NPEs, run the [**peer next-hop-local**](cmdqueryname=peer+next-hop-local) command on the SPE twice with different parameters specified for UPEs and NPEs.
5. (Optional) Run [**apply-label per-nexthop**](cmdqueryname=apply-label+per-nexthop)
   
   
   
   One-label-per-next-hop label distribution is enabled for EVPN routes.
   
   
   
   In an EVPN HVPN scenario, if an SPE needs to send a large number of EVPN routes but the MPLS labels are insufficient, one-label-per-next-hop label distribution can be configured on the SPE to conserve MPLS label resources.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   After one-label-per-next-hop label distribution is enabled or disabled, the label allocated by the SPE changes, causing packet loss.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

On NPEs, configure the MAC-based load balancing function to improve network resource utilization.

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Enter the EVPN instance or BD EVPN instance view.
   
   * Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* command to enter the EVPN instance view.
   * Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode** command to enter the BD EVPN instance view.
3. Run [**mac load-balancing**](cmdqueryname=mac+load-balancing)
   
   MAC route-based load balancing is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix* command on the SPE to check detailed BGP EVPN route information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) **vpn-instance** *vpn-instance-name* **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* command on the SPE to check the EVPN route information of the specified EVPN instance.