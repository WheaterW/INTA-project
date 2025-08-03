Configuring Association between LDP and Static Routes
=====================================================

On an MPLS network with primary and secondary LSPs established by label switched routers (LSRs) using static routes, association between LDP and static routes prevents MPLS traffic from being interrupted during traffic switching between the primary and secondary LSPs.

#### Usage Scenario

Association between LDP and static routes is mainly used on MPLS networks with primary and secondary LSPs established by LSRs using static routes. The association prevents traffic from being interrupted during traffic switchover from the primary LSP to the secondary LSP when the LDP session on the primary link fails (not because of a link fault) or during traffic switchback when the primary link recovers from a fault. [Figure 1](#EN-US_TASK_0172365440__fig_dc_vrp_bgp_cfg_004001) shows the typical networking for association between LDP and static routes. LSRA and LSRD interwork through static routes. Primary and backup static routes are deployed on LSRA, with LSRB and LSRC as next hops. Primary and secondary LDP LSPs are established through the static routes. The primary LSP uses link A, and the secondary LSP uses link B. In normal cases, link A is preferred. The following part describes association between LDP and static routes in switchover and switchback scenarios.

**Figure 1** Networking for association between LDP and static routes  
![](figure/en-us_image_0256253471.png)

**Switchover scenario**

In the switchover scenario, traffic over the primary static route is not switched to the backup link when the LDP session on the primary link fails (not because of a link fault). As a result, LSP traffic over the primary link is interrupted.

When the LDP session is normal, LSP traffic travels along the primary link (link A: LSRA -> LSRB -> LSRD). If the LDP session between LSRA and LSRB is interrupted, the LSP immediately switches to the backup link (LinkB: LSRA -> LSRC -> LSRD). However, because the link between LSRA and LSRB is normal, traffic over the static route is not switched to the backup link. The asynchrony between LDP and the static route causes an LSP traffic interruption.

If association between LDP and static routes is enabled, traffic is automatically switched to the backup link when the LDP session goes down, ensuring uninterrupted traffic forwarding.

**Switchback scenario**

In the switchback scenario, after the primary link recovers from a fault, traffic transmitted through the static route is first switched back to the primary link because static routes converge faster than LDP. As a result, the secondary LSP cannot be used, and the primary LSP has not been set up yet, causing an LSP traffic interruption.

If the link between LSRA and LSRB fails, traffic is immediately switched to the backup link (link B: LSRA -> LSRC -> LSRD). After the link between LSRA and LSRB recovers, traffic over the static route is immediately switched to the primary link (Link A: LSRA -> LSRB -> LSRD). As a result, the secondary LSP cannot be used, and the primary LSP has not been restored yet, causing a traffic interruption.

If association between LDP and static routes is enabled, the static route on link A becomes active only after the LDP session goes up during the switchback. In this manner, the static route and LSP are synchronous, preventing traffic loss.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the static routes with outbound interfaces specified can be associated with LDP.



#### Pre-configuration Tasks

Before configuring association between LDP and static routes, complete the following tasks:

* Enable MPLS.
* Enable MPLS LDP globally and on interfaces.
* Ensure that LDP sessions are set up between devices.

#### Procedure

* Enable association between LDP and static routes.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**ip route-static**](cmdqueryname=ip+route-static) [ **vpn-instance** *vpn-instance-name* ] *ip-address* { *mask* | *mask-length* } *interface-type* *interface-number* [ *nexthop-address* ] [ **preference** *preference* | **tag** *tag* ] \* **ldp-sync** [ **description** *text* ]
     
     Association between LDP and static routes is configured.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* (Optional) Set a Hold-down timer.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The view of the outbound interface corresponding to the primary link used by static routes is displayed.
  3. Run [**static-route timer ldp-sync hold-down**](cmdqueryname=static-route+timer+ldp-sync+hold-down) { *timer* | **infinite** }
     
     A period in which the static route is inactive and waits for the establishment of an LDP session is set.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The preceding configurations need to be performed on both ends of the primary and secondary links.

#### Verifying the Configuration

After configuring association between LDP and static routes, run the **display static-route ldp-sync** command.