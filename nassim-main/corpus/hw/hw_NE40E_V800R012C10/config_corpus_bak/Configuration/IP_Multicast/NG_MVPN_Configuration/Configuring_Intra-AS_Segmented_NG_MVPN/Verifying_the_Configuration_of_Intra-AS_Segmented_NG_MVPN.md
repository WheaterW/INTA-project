Verifying the Configuration of Intra-AS Segmented NG MVPN
=========================================================

After configuring intra-AS segmented NG MVPN, verify information about BGP MVPN peer relationships, I-PMSI tunnels, and VPN instances' PIM routing tables on PEs.

#### Prerequisites

Intra-AS segmented NG MVPN has been configured.


#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp) **mvpn** **all** **peer** [ [ *ipv4-address* ] **verbose** ] command to check BGP MVPN peer relationship information.
* Run the [**display mvpn vpn-instance**](cmdqueryname=display+mvpn+vpn-instance) *vpn-instance-name* **ipmsi** [ **verbose** [ *grpAddr* | *srcAddr*] \* ] command to check I-PMSI tunnel configurations for the MVPN service of a specified VPN instance.
* Run the [**display mvpn**](cmdqueryname=display+mvpn) { **vpn-instance** *vpn-instance-name* | **all-instance** } **spmsi** [ **verbose** [ *grpAddr* | *srcAddr* ] \* ] command to check S-PMSI tunnel configurations for the MVPN service of a specified VPN instance.
* Run the [**display pim**](cmdqueryname=display+pim) { **vpn-instance** *vpn-instance-name* | **all-instance** } **routing-table** command to check PIM routing tables of a specified or all VPN instances.
* Run either of the following commands to check multicast-LSP configurations.
  
  
  + For mLDP P2MP LSPs: [**display mpls multicast-lsp protocol mldp**](cmdqueryname=display+mpls+multicast-lsp+protocol+mldp) **p2mp** [ **root-ip** *root-ip-address* { **lsp-id** *lsp-id* | **opaque-value** *opaque-value* }] [ **lsr-role** { **bud** | **ingress** | **transit** | **egress** }]
  + For RSVP-TE P2MP LSPs: [**display mpls multicast-lsp protocol p2mp-te**](cmdqueryname=display+mpls+multicast-lsp+protocol+p2mp-te) [ **lsp-id** *ingress-lsr-id* *session-id* *p2mp-id* *lsp-id* [ **s2l-destination** *s2l-destination-address* ]]
* Run the [**display mvpn inter-region-segmented**](cmdqueryname=display+mvpn+inter-region-segmented) { **spmsi** [ **route-distinguisher** *route-distinguisher* **source** *source-address* **group** *group-address* ] | **ipmsi** [ **route-distinguisher** *route-distinguisher* ] } command to check I-PMSI or S-PMSI tunnel stitching information and leaf information on the node that connects tunnels.