Configuring P2MP TE FRR
=======================

P2MP TE fast reroute (FRR) provides local link protection for a P2MP TE tunnel. It establishes a bypass tunnel to protect sub-LSPs. If a link fails on the P2MP TE tunnel, traffic switches to the bypass tunnel within 50 milliseconds, which increases tunnel reliability.

#### Usage Scenario

P2MP TE FRR establishes a bypass tunnel to provide local link protection for the P2MP TE tunnel called the primary tunnel. The bypass tunnel is a P2P TE tunnel. The principles and concepts of P2MP TE FRR are similar to those of P2P TE FRR.

The NE40E supports FRR link protection, not node protection, over a P2MP TE tunnel. Therefore, path planning for the bypass tunnel is irrelevant to node protection. For example, in [Figure 1](#EN-US_TASK_0172368210__fig_dc_vrp_te-p2p_cfg_013801), the bypass tunnel path planned for the link between P1 and P2 can provide link protection. However, the link between P3 and PE4 for which a bypass tunnel path is planned traverses the node P4 so that the bypass tunnel cannot be bound to the primary tunnel or provide link protection.**Figure 1** FRR link protection for a P2MP TE tunnel  
![](images/fig_dc_vrp_te-p2p_cfg_013801.png)  

P2P and P2MP TE tunnels can share a bypass tunnel. Therefore, when planning bandwidth for the bypass tunnel, ensure that the bypass tunnel bandwidth is equal to the total bandwidth of the bound P2P and P2MP tunnels.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If traffic is switched to a P2MP FRR tunnel, the forwarding performance deteriorates temporarily, and the impact is removed after traffic switches back to the primary tunnel.

In NG MVPN scenarios, when P2MP TE FRR protection is used,
the interface of a primary P2MP tunnel needs to be enabled to delay
in going Up. The delay is related to the number of VPN multicast groups
over the tunnel. For 1000 multicast groups, set the delay time to
30s. Increase the delay time if more multicast groups are configured.



#### Pre-configuration Tasks

Before configuring P2MP TE FRR, complete the following task:

* [Configure a P2MP TE tunnel.](dc_vrp_te-p2p_cfg_0133.html)


[Configuring Manual FRR for a Manually Configured P2MP TE Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0195.html)

Manual FRR can be configured on the tunnel interface of a manually configured P2MP TE tunnel.

[Configuring FRR for Automatic P2MP TE Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0196.html)

Auto P2MP TE FRR is configured in a P2MP TE template for automatic P2MP TE tunnels.

[Verifying the P2MP TE FRR Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0197.html)

After configuring P2MP TE FRR, verify P2MP TE FRR information.