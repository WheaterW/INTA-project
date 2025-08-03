Configuring VPNv4 FRR
=====================

In an H-VPN scenario in which VPNv4 FRR is configured, if the primary LSP between an ASBR or SPE and its next hop is unreachable, traffic quickly switches to the secondary LSP.

#### Usage Scenario

In an H-VPN scenario in which VPNv4 FRR is configured on an SPE, the SPE immediately switches VPN services to the standby link if the active link fails.

**Figure 1** VPNv4 FRR  
![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_201601.png)

#### Pre-configuration Tasks

Before you configure VPNv4 FRR, complete the following tasks:

* Configure a routing protocol on Routers for them to communicate.
* Configure two unequal-cost routes between the SPE and remote PE.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4**
   
   
   
   The BGP VPNv4 address family view is displayed.
4. Run [**auto-frr**](cmdqueryname=auto-frr)
   
   
   
   VPNv4 FRR is enabled.
5. Run [**bestroute nexthop-resolved**](cmdqueryname=bestroute+nexthop-resolved) **tunnel** [ **inherit-ip-cost** ]
   
   
   
   A VPNv4 route is configured to participate in route selection only when its next hop recurses to a tunnel. This configuration ensures that packets are not lost during traffic switchback.
6. (Optional) Run [**route-select delay**](cmdqueryname=route-select+delay) *delay-value*
   
   
   
   A delay for route selection is configured. Delayed route selection ensures that after the primary path recovers, the device on the primary path performs route selection only after the corresponding forwarding entries on the device are stable. This prevents traffic loss during traffic switchback.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) **include** *ip-address* *mask-length* **verbose** command to check the index and label of the backup LSP to which the VPNv4 route recurses.