Configuring Dual-Root 1+1 Protection
====================================

This section describes how to configure upstream multicast hop (UMH) route selection rules on receiver PEs on an NG MVPN, so that the receiver PEs can select the same sender PE as their root node during VPN route selection.

#### Usage Scenario

In an NG MVPN scenario, if a sender PE on a P2MP tunnel fails, the C-multicast service will be interrupted. Multicast services can rely only on unicast route convergence for recovery. However, unicast route convergence takes a long time, which is unacceptable to the multicast services that have high reliability requirements. To resolve this problem, you can configure dual-root 1+1 protection. On the network shown in [Figure 1](#EN-US_TASK_0314877576__fig_dc_vrp_cfg_ngmvpn_001501), a primary P2MP tunnel is established with PE1 as the root node, and a backup P2MP tunnel is established with PE2 as the root node. When links are working properly, multicast traffic is forwarded through both the primary and backup tunnels bidirectionally. The leaf node PE3 selects the multicast traffic received from the primary tunnel and discards the multicast traffic received from the backup tunnel. If PE1 or a public network link fails, PE3 can use BFD for P2MP TE/mLDP or traffic detection to quickly detect the P2MP tunnel fault and choose to accept the multicast traffic received from the backup tunnel. This accelerates multicast service convergence and improves reliability.**Figure 1** Configuring dual-root 1+1 protection  
![](figure/en-us_image_0315957778.png)


#### Pre-configuration Tasks

Before configuring BFD for P2MP TE/mLDP-based dual-root 1+1 protection, complete the following tasks:

* To use RSVP-TE P2MP tunnels:
  
  + Configure an NG MVPN.
  + [Configure BFD for P2MP TE](dc_vrp_te-p2p_cfg_0198.html) on the root nodes.
  + [Configure VPN FRR](dc_vrp_mpls-l3vpn-v4_cfg_2017.html) on leaf nodes.
  + Enable BFD globally on the root and leaf nodes.
* To use mLDP P2MP tunnels:
  
  + Configure an NG MVPN.
  + [Configure BFD for mLDP P2MP](dc_vrp_ldp-p2p_cfg_0112.html) on the root and leaf nodes.
  + [Configure VPN FRR](dc_vrp_mpls-l3vpn-v4_cfg_2017.html) on leaf nodes.
  + Enable BFD globally on the root and leaf nodes.

Before configuring traffic detection-based dual-root 1+1 protection, complete the following tasks:

* Configure an NG MVPN.
* [Configure VPN FRR](dc_vrp_mpls-l3vpn-v4_cfg_2017.html) on leaf nodes.

Perform the following steps on the leaf nodes:


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to enter the VPN instance view.
3. Run the [**ipv6-family**](cmdqueryname=ipv6-family) command to enter the VPN instance IPv6 address family view.
4. Run the [**mvpn**](cmdqueryname=mvpn) command to enter the VPN instance IPv6 address family MVPN view.
5. Run the [**c-multicast frr**](cmdqueryname=c-multicast+frr) command to enable C-multicast FRR.
6. (Only for the flow detection-based configuration) Run the [**c-multicast frr flow-detection-based**](cmdqueryname=c-multicast+frr+flow-detection-based) command to configure flow detection-based C-multicast FRR.
7. (Optional) Run the [**multicast wtr**](cmdqueryname=multicast+wtr) *wtr-time* command to configure a switchback wait time for C-multicast FRR in NG MVPN 1+1 protection scenarios.
8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After configuring dual-root 1+1 protection, check the configurations.

Run the [**display pim ipv6**](cmdqueryname=display+pim+ipv6) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **routing-table** [ *group-address* [ **mask** { *group-mask-length* | *group-mask* } ] | *source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | **incoming-interface** { *interface-type* *interface-number* | **register** | **through-bgp** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **register** | **none** | **pseudo** } | **mode** { **ssm** | **sm** } | **flags** *flag-value* | **fsm** ] \* [ **outgoing-interface-number** [ *number* ] ] command to check information about the IPv6 PIM routing table.

# Run the [**display pim ipv6**](cmdqueryname=display+pim+ipv6) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **routing-table** command. The command output shows backup PIM entries in the IPv6 PIM routing table.