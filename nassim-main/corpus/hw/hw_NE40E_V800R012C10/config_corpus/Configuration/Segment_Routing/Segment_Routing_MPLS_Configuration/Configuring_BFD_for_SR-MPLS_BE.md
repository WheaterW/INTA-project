Configuring BFD for SR-MPLS BE
==============================

BFD for SR LSP can be configured to detect faults of SR LSPs.

#### Usage Scenario

Segment Routing-MPLS Best Effort (SR-MPLS BE) refers to the use of an IGP to compute an optimal SR LSP based on the shortest path first algorithm. An SR LSP is a label forwarding path that is established using SR and guides data packet forwarding through a prefix or node SID.

BFD for SR-MPLS BE is used to detect SR LSP connectivity. If BFD for SR-MPLS BE detects a fault on the primary SR LSP, an application such as VPN FRR rapidly switches traffic, which minimizes the impact on services.


#### Pre-configuration Tasks

Before configuring BFD for SR-MPLS BE, complete the following tasks:

* [Configure an IS-IS SR-MPLS BE tunnel](dc_vrp_sr-be_cfg_0008.html) or [configure an OSPF SR-MPLS BE tunnel](dc_vrp_sr_all_cfg_0001.html).
* Set each LSR ID using the [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id* command. Ensure that the route to the local *lsr-id* is reachable.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   The BFD view is displayed.
3. Run [**mpls-passive**](cmdqueryname=mpls-passive)
   
   
   
   The egress is enabled to create a BFD session passively.
   
   The egress has to receive an LSP ping request carrying a BFD TLV before creating a BFD session.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**segment-routing**](cmdqueryname=segment-routing)
   
   
   
   The Segment Routing view is displayed.
6. Run [**bfd enable**](cmdqueryname=bfd+enable) **mode** **tunnel** [ **filter-policy** **ip-prefix** *ip-prefix-name* | **effect-sr-lsp** ] \*
   
   
   
   BFD is enabled for SR LSPs.
   
   If **effect-sr-lsp** is specified and BFD goes down, the SR LSPs are withdrawn.
7. (Optional) Run [**bfd**](cmdqueryname=bfd) **tunnel** { **min-rx-interval** *receive-interval* | **min-tx-interval** *transmit-interval* | **detect-multiplier** *multiplier-value* } \*
   
   
   
   BFD parameters are set for SR LSPs.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After successfully configuring BFD for SR-MPLS BE, run the [**display segment-routing bfd tunnel session**](cmdqueryname=display+segment-routing+bfd+tunnel+session) [ **prefix** *ip-address* { *mask* | *mask-length* } ] command to check information about the BFD session that monitors SR LSPs.