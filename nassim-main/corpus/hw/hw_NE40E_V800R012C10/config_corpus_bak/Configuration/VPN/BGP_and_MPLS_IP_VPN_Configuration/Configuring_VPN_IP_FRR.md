Configuring VPN IP FRR
======================

This section describes how to configure VPN IP FRR. At a VPN site where multiple CEs connect to the same PE, this feature can immediately switch traffic to another PE-CE link when the next hop of the active route is unreachable.

#### Usage Scenario

This feature is suitable for IP services that are sensitive to the packet loss and delay on a VPN. After VPN IP FRR is configured, traffic is immediately switched to another PE-CE link when the next hop of the active route is unreachable. This reduces IP service interruption time.

On the network shown in [Figure 1](dc_vrp_mpls-l3vpn-v4_cfg_2012.html#EN-US_TASK_0172369422__fig_dc_vrp_mpls-l3vpn-v4_cfg_201201), in normal situations, the PE selects Link\_A to forward traffic to site vpn1 and uses Link\_B as the backup link. If the PE detects that the route to CE1 is unreachable, it immediately switches traffic to Link\_B and performs VPN route convergence, minimizing the impact on VPN services.

**Figure 1** VPN IP FRR  
![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_201201.png)

At present, the NE40E supports the following VPN IP FRR modes:

* IP FRR: applies to the networking where different PE-CE pairs use different routing protocols.
* VPN BGP auto FRR: applies to the networking where BGP runs between the PEs and CE.

#### Pre-configuration Tasks

Before configuring VPN IP FRR, complete the following tasks:

* Configure a BGP/MPLS IP VPN.
* Configure the PE to learn VPN routes with the same prefix from different CEs attached to it.

#### Procedure

* Configure IP FRR.
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
* (Optional) Enable IP FRR poison reverse.
  
  
  
  In [Figure 2](#EN-US_TASK_0172369422__fig20345859153119), IP FRR is deployed on the IP ring network, and the traffic enters the ring network from DeviceD and leaves the ring network from DeviceA. The primary and backup next hops of DeviceD are DeviceC and DeviceE, respectively. The primary and backup next hops of DeviceC are DeviceB and DeviceD, respectively. If the link between DeviceB and DeviceC fails, DeviceC forwards the traffic received from DeviceD back to DeviceD. However, before the route convergence is complete, DeviceD cannot detect the link failure between DeviceB and DeviceC, and continues to forward the traffic to DeviceC. As a result, an instantaneous traffic storm is generated between DeviceC and DeviceD. After DeviceD detects the link failure between DeviceB and DeviceC through route convergence, the traffic is forwarded from DeviceD to the backup next hop, DeviceE.
  
  **Figure 2** IP ring network  
  ![](figure/en-us_image_0174096154.png)
  **Figure 3** IP ring network with IP FRR poison reverse enabled  
  ![](figure/en-us_image_0174096222.png)
  
  1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface or sub-interface view.
     
     
     
     The view can be the Eth-Trunk interface, Eth-Trunk sub-interface, GE interface, or GE sub-interface view.
  2. Run the [**poison-reverse enable**](cmdqueryname=poison-reverse+enable) command to enable IP FRR poison reverse.
     
     
     
     On an IP ring network configured with IP FRR, this command is used to prevent instantaneous traffic storms caused by route convergence.
     
     In a load balancing scenario, poison reverse does not take effect.