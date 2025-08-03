Configuring Dual-Root 1+1 Protection
====================================

Configuring dual-root 1+1 protection accelerates multicast service convergence and improves reliability in case a sender PE on a P2MP tunnel fails.

#### Usage Scenario

In an NG MVPN scenario, if a sender PE on a P2MP tunnel fails, the VPN multicast service will be interrupted. The network can rely only on unicast route convergence for recovery. However, unicast route convergence takes a long time and may fail to meet the high reliability requirements of some multicast services. To resolve this problem, configure dual-root 1+1 protection. On the network shown in [Figure 1](#EN-US_TASK_0000001270153613__fig_dc_vrp_cfg_ngmvpn_001501), a primary P2MP tunnel is established with PE1 as the root node, and a backup P2MP tunnel is established with PE2 as the root node. When the links are working properly, multicast traffic is forwarded through both the primary and backup tunnels bidirectionally. The leaf node PE3 selects the multicast traffic received from the primary tunnel and discards the multicast traffic received from the backup tunnel. If PE1 or a public network link fails, PE3 can use BFD for P2MP TE/mLDP or traffic detection to quickly detect the P2MP tunnel fault and choose to accept the multicast traffic received from the backup tunnel. This accelerates multicast service convergence and improves reliability.**Figure 1** Configuring dual-root 1+1 protection  
![](figure/en-us_image_0000001225833828.png)


#### Pre-configuration Tasks

Before configuring BFD for P2MP TE/mLDP based dual-root 1+1 protection, complete the following tasks:

* RSVP-TE P2MP Tunnel:
  
  + Configure NG MVPN.
  + [Configure BFD for P2MP TE](dc_vrp_te-p2p_cfg_0198.html) on the root nodes.
  + [Configure VPN FRR](dc_vrp_mpls-l3vpn-v4_cfg_2017.html) on the leaf nodes.
  + Globally enable BFD on the root and leaf nodes.
* mLDP P2MP Tunnel:
  
  + Configure NG MVPN.
  + [Configure BFD for mLDP P2MP](dc_vrp_ldp-p2p_cfg_0112.html) on the root and leaf nodes.
  + [Configure VPN FRR](dc_vrp_mpls-l3vpn-v4_cfg_2017.html) on the leaf nodes.
  + Globally enable BFD on the root and leaf nodes.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If static default routes are configured on leaf nodes, to enable the leaf nodes to forward received BFD detection packets properly, configure IPv4 route import between VPN and public network instances so that public network routes can be replicated to the NG MVPN instance. For details on how to import public network routes into an NG MVPN instance, see [Configuring Route Import Between VPN and Public Network Instances](dc_vrp_mpls-l3vpn-v4_cfg_2024.html). Ensure that the specified route-policy has been configured using the [**route-policy**](cmdqueryname=route-policy) command.



Before configuring multicast traffic detection based dual-root 1+1 protection, complete the following tasks:

* Configure NG MVPN.
* [Configure VPN FRR](dc_vrp_mpls-l3vpn-v4_cfg_2017.html) on the leaf nodes.

Perform the following steps on the leaf nodes:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance)*vpn-instance-name*
   
   
   
   The VPN instance view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
   
   
   
   The VPN instance IPv4 address family view is displayed.
4. Run [**mvpn**](cmdqueryname=mvpn)
   
   
   
   The VPN instance IPv4 address family MVPN view is displayed.
5. Run [**c-multicast frr**](cmdqueryname=c-multicast+frr)
   
   
   
   C-multicast FRR is enabled. C-multicast FRR allows C-multicast traffic to be diverted to the primary and backup tunnels.
6. (Only for traffic detection-based configuration) Run [**c-multicast frr flow-detection-based**](cmdqueryname=c-multicast+frr+flow-detection-based)
   
   
   
   Traffic detection-based C-multicast FRR is enabled.
7. (Optional) Run [**multicast wtr**](cmdqueryname=multicast+wtr)*wtr-time*
   
   
   
   A switchback wait time is set for C-multicast FRR in the NG MVPN 1+1 scenario.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring dual-root 1+1 protection, check the configurations.

Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **routing-table** [ *group-address* [ **mask** { *group-mask-length* | *group-mask* } ] | *source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | **incoming-interface** { *interface-type* *interface-number* | **register** | **through-bgp** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **register** | **none** | **pseudo** } | **mode** { **ssm** | **sm** } | **flags** *flag-value* | **fsm** ] \* [ **outgoing-interface-number** [ *number* ] ] command to check information about the PIM routing table.

# Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **routing-table** command. The command output shows backup PIM entries in the PIM routing table.