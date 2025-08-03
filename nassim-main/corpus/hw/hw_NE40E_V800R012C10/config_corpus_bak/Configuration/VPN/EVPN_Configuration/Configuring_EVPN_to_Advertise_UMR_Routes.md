Configuring EVPN to Advertise UMR Routes
========================================

Configuring EVPN to advertise unknown MAC routes (UMRs) helps mitigate the MAC address learning pressure of RRs and aggregation devices.

#### Usage Scenario

In the standard EVPN VPLS networking solution, all user-side specific MAC routes are transmitted through an RR on the entire network. As a result, the RR has heavy MAC address learning pressure. In addition, an aggregation device usually connects to multiple access devices. Therefore, aggregation devices also have heavy MAC address learning pressure, and the MAC address table capacity of aggregation devices limits the number of access users.

To solve this problem, configure EVPN to advertise UMRs. On the network shown in [Figure 1](#EN-US_TASK_0318968522__fig17853203404315), configure each ALeaf node at the access layer to generate and advertise a UMR to the RR, but not to advertise specific MAC routes to the RR. This can reduce the MAC address learning pressure of the RR. In addition, configure the RR to reflect only the UMRs sent by ALeaf nodes to the SLeaf node at the aggregation layer. This can reduce the MAC address learning pressure of the SLeaf node and prevent the MAC address table capacity of the SLeaf node from limiting the number of access users. Moreover, you need to configure ALeaf nodes to send only specific MAC routes to each other and configure the RR to reflect only received specific MAC routes to ALeaf nodes, so that EVPN VPLS services can run properly.

**Figure 1** UMR advertisement through EVPN  
![](figure/en-us_image_0000001232566653.png)

#### Pre-configuration Tasks

Before configuring EVPN to advertise UMRs, complete one of the following tasks:

* [Configure EVPN VPLS over MPLS (BD EVPN instance)](dc_vrp_evpn_cfg_0065.html).
* [Configure EVPN VPLS over SRv6 BE](dc_vrp_srv6_cfg_all_0023_copy.html).
* [Configure EVPN VPLS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpls_over_srv6-te_policy_copy.html).

#### Procedure

1. Enable UMR generation on each ALeaf node.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the view of the BD bound to the EVPN instance.
   3. Run the [**umr originate**](cmdqueryname=umr+originate)[ **detail-suppressed** ] command to enable UMR generation.
      
      
      
      If **detail-suppressed** is not specified in this step, UMRs are generated, but specific MAC routes are not suppressed. In other words, both UMRs and specific MAC routes can be advertised. If **detail-suppressed** is specified, UMRs are generated, and specific MAC routes are suppressed. In other words, only UMRs can be advertised in this case.
      
      In the current scenario, the [**umr originate**](cmdqueryname=umr+originate) **detail-suppressed** command needs to be run on each ALeaf node to generate UMRs and suppress specific MAC routes.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
2. (Optional) On an ALeaf node working in **qualify** mode, configure the function to import MAC routes with the VLAN ID of 0 to the routing table of the EVPN instance.
   
   
   
   You are advised to configure this function when the local device works in **qualify** mode and the peer device works in **unqualify** mode.
   
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the view of the BD bound to the EVPN instance.
   3. Run the [**mac-learn-style qualify**](cmdqueryname=mac-learn-style+qualify) command to configure the MAC address learning mode as **qualify**.
      
      
      
      If no MAC address learning mode is configured, each MAC address is unique in the BD, and the device learns MAC addresses based on BDs. VLAN-based differentiation is not needed in this case. If users need to be differentiated based on VLANs, perform this step to set the MAC address learning mode to **qualify**, so that each VLAN has its own MAC address space. The device learns MAC addresses based on both MAC addresses and VLAN tags carried in user Ethernet packets.
   4. Run the [**evpn mac-learning remote-unqualified**](cmdqueryname=evpn+mac-learning+remote-unqualified) command to configure the current device working in **qualify** mode to import MAC routes with the VLAN ID of 0 into the routing table of the EVPN instance.
      
      
      
      By default, if a device that learns MAC addresses in **qualify** mode receives an EVPN MAC route with the VLAN ID of 0 from an EVPN peer, it does not import the route into the routing table of the EVPN instance. As a result, the corresponding traffic forwarding fails. After this command is run, the device can import EVPN MAC routes with the VLAN ID of 0 into the routing table of the EVPN instance to guide traffic forwarding.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
3. Configure an ALeaf node to advertise only specific MAC routes to other ALeaf nodes.
   1. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   2. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enter the BGP EVPN address family view.
   3. Run the [**peer**](cmdqueryname=peer+advertise+evpn+mac-route+detail-only) { *peerIpv4Addr* | *peerIpv6Addr* | *groupName* } **advertise evpn mac-route detail-only** command to configure the device to advertise only specific MAC routes to a specified peer or peer group.
      
      
      
      Because ALeaf nodes only need to exchange specific MAC routes with each other and do not need to exchange UMRs, the peers or peer groups specified in this step refer to other ALeaf nodes. After this step is performed, ALeaf nodes advertise only UMRs to the RR and advertise specific MAC routes to other ALeaf nodes.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
4. Configure the RR to advertise only specific MAC routes to ALeaf nodes.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enter the BGP EVPN address family view.
   4. Run the [**peer**](cmdqueryname=peer+advertise+evpn+mac-route+detail-only) { *peerIpv4Addr* | *peerIpv6Addr* | *groupName* } **advertise evpn mac-route detail-only** command to configure the device to advertise only specific MAC routes to a specified peer or peer group.
      
      
      
      Because ALeaf nodes only need to learn specific MAC routes and do not need to learn UMRs, the peers or peer groups specified in this step refer to other ALeaf nodes. After this step is performed, the RR reflects only UMRs to the SLeaf node and reflects only specific MAC routes to ALeaf nodes.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
5. Enable UMR forwarding on the SLeaf node.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the view of the BD bound to the EVPN instance.
   3. Run the [**umr forward enable**](cmdqueryname=umr+forward+enable) command to enable UMR forwarding.
      
      
      
      After this step is performed, the SLeaf node forwards received unknown unicast packets based on UMRs first. If no matching UMR is found, the SLeaf node forwards these packets as BUM packets.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After the configuration is complete, perform the following operations to verify it:

* Run the [**display bgp evpn all routing-table mac-route**](cmdqueryname=display+bgp+evpn+routing-table) **0:48:0000-0000-0000:0:0.0.0.0** command on an ALeaf node to check the advertised UMR or on the SLeaf node to check the received UMR.
* If specific MAC route suppression is specified when UMR generation is enabled on an ALeaf node, you can run the [**display bgp evpn all routing-table mac-route**](cmdqueryname=display+bgp+evpn+routing-table) *prefix* command on the ALeaf node to view a specified specific MAC route. The command output shows that the route is marked with the **suppressed** flag.