Configuring IP+VPNv4 Hybrid FRR
===============================

This section describes how to configure IP+VPNv4 hybrid FRR. On a network where a CE is dual-homed to two PEs, if the link between the master PE and the CE is unreachable, the master PE switches traffic to the link between the backup PE and the CE for transmission. IP+VPNv4 hybrid FRR improves network reliability.

#### Usage Scenario

IP+VPNv4 hybrid FRR can quickly switch traffic from a PE to another PE that serves as the backup next hop if the primary route to a CE is unreachable.

A PE learns VPN routes with the same prefix from a CE and other PEs. In this situation, IP+VPNv4 hybrid FRR can be configured on the PE. After being enabled with IP+VPNv4 hybrid FRR, the PE generates a primary route and a backup route to the VPN prefix. If the link between the PE and CE fails, the traffic quickly switches to the backup next hop (backup PE).

On the network shown in [Figure 1](dc_vrp_mpls-l3vpn-v4_cfg_2013.html#EN-US_TASK_0172369425__fig_dc_vrp_mpls-l3vpn-v4_cfg_201301), in normal situations, PE1 selects Link\_A to forward traffic to the CE and uses Link\_B as the backup link. If PE2 detects that the route to the CE is unreachable, it immediately switches traffic to Link\_B and performs VPN route convergence, minimizing the impact on VPN services.

**Figure 1** IP+VPNv4 hybrid FRR  
![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_201301.png)

At present, the NE40E supports the following IP+VPNv4 hybrid FRR modes:

* VPN IP FRR: applies to the networking where a non-BGP routing protocol runs between the PEs and CE.
* VPN BGP auto FRR: applies to the networking where BGP runs between the PEs and CE.

#### Pre-configuration Tasks

Before configuring IP+VPNv4 hybrid FRR, complete the following tasks:

* Configure a BGP/MPLS IP VPN.
* Configure a PE to learn IP routes with the same prefix from a CE and other VPNv4 peers.

#### Procedure

* Configure VPN IP FRR.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to enter the VPN instance view.
  3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to enter the VPN instance IPv4 address family view.
  4. Run the [**ip frr**](cmdqueryname=ip+frr) command to enable VPN IP FRR.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure VPN BGP auto FRR.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
  4. Run the [**auto-frr**](cmdqueryname=auto-frr) command to enable BGP auto FRR.
  5. (Optional) Run the [**route-select delay**](cmdqueryname=route-select+delay) *delay-value* command to configure a route selection delay. Delayed route selection ensures that after the primary path recovers, the device on the primary path performs route selection only after the corresponding forwarding entries on the device are stable. This prevents traffic loss during traffic switchback.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.