Upgrading LDP to SR-MPLS BE
===========================

This section describes how to upgrade LDP to SR-MPLS BE.

#### Prerequisites

All devices involved in the upgrade run LDP, and traffic has recursed to the LDP LSP between the ingress and egress.

By default, the priority of an LDP LSP is higher than that of an SR-MPLS BE LSP (SR LSP for short).


#### Context

MPLS LDP is widely deployed on existing networks to carry services such as BGP/MPLS IP VPN services. The SR-MPLS technology, which is designed based on the source routing concept, simplifies network protocols and supports efficient TI-LFA protection technologies, facilitating smooth evolution to SDN networks. [Figure 1](#EN-US_TASK_0000001122993236__fig_dc_vrp_sr_all_cfg_001801) shows the recommended process of upgrading LDP to SR-MPLS BE.

**Figure 1** Process of upgrading LDP to SR-MPLS BE  
![](figure/en-us_image_0000001122997210.png "Click to enlarge")

#### Procedure

1. Upgrade all devices to support SR, specify an SRGB, and configure prefix SIDs for desired loopback interface addresses. For configuration details, see "Configuring Basic SR-MPLS BE Functions" in [Configuring an IS-IS SR-MPLS BE Tunnel](dc_vrp_sr-be_cfg_0008.html) or [Configuring an OSPF SR-MPLS BE Tunnel](dc_vrp_sr_all_cfg_0001.html).
   
   
   
   In this case, although traffic still recurses to the LDP LSP, an SR LSP has already been generated.
2. Check whether SR LSP entries are correctly generated on the devices.
   
   
   1. Run the [**display segment-routing prefix mpls forwarding**](cmdqueryname=display+segment-routing+prefix+mpls+forwarding) command to check information about the SR label forwarding table.
   2. Run the [**ping lsp**](cmdqueryname=ping+lsp) command to check end-to-end SR LSP connectivity.
3. Run the [**tunnel-prefer segment-routing**](cmdqueryname=tunnel-prefer+segment-routing) command to configure the SR LSP to take precedence over the LDP LSP.
   
   
   1. Run this command on PE1. Then the traffic whose ingress is PE1 recurses to the SR LSP, whereas the traffic whose ingress is PE2 still recurses to the LDP LSP.
   2. Run this command on PE2. Then the traffic whose ingress is PE2 also recurses to the SR LSP.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   During the configuration, check whether traffic is normal. If the traffic is abnormal, you can run the [**undo tunnel-prefer segment-routing**](cmdqueryname=undo+tunnel-prefer+segment-routing) command to perform a rollback so that the traffic continues to be carried over the LDP LSP.
4. Run the [**undo mpls ldp**](cmdqueryname=undo+mpls+ldp) command on each device to delete the LDP configuration.
   
   
   
   In this case, only the SR LSP (not the LDP LSP) exists on the network, meaning that the upgrade process is complete.