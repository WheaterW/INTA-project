Verifying the Intra-AS NG MVPN Configuration
============================================

After configuring an intra-AS NG MVPN, verify the BGP MVPN peer relationships, I-PMSI tunnels, and VPN instance PIM routing table information.

#### Prerequisites

An intra-AS NG MVPN has been configured.


#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp) **mvpn** **all** **peer** [ [ *ipv4-address* ] **verbose** ] command to check BGP MVPN peer configurations.
* Run the [**display mvpn vpn-instance**](cmdqueryname=display+mvpn+vpn-instance) { **vpn-instance** *vpn-instance-name* | **all-instance** } **ipmsi** [ **verbose** [ *grpAddr* | *srcAddr* ] \* ] command to check I-PMSI tunnel configurations of MVPN services in a specified VPN instance.
* Run the [**display mvpn**](cmdqueryname=display+mvpn) { **vpn-instance** *vpn-instance-name* | **all-instance** } **spmsi** [ **verbose** [ *grpAddr* | *srcAddr* ] \* ] command to check information about S-PMSI tunnels of MVPN services in a specified VPN instance.
* Run the [**display pim**](cmdqueryname=display+pim) { **vpn-instance** *vpn-instance-name* | **all-instance** } **routing-table** command to check PIM routing table configurations of a specified or all VPN instances.
* Run either of the following commands to check multicast-LSP configurations.
  
  
  + For mLDP P2MP LSPs, run the [**display mpls multicast-lsp protocol mldp**](cmdqueryname=display+mpls+multicast-lsp+protocol+mldp) **p2mp** [ **root-ip** *root-ip-address* { **lsp-id** *lsp-id* | **opaque-value** *opaque-value* } ] [ **lsr-role** { **bud** | **ingress** | **transit** | **egress** } ] command.
  + For RSVP-TE P2MP LSPs, run the [**display mpls multicast-lsp protocol p2mp-te**](cmdqueryname=display+mpls+multicast-lsp+protocol+p2mp-te) [ **lsp-id** *ingress-lsr-id* *session-id* *p2mp-id* *lsp-id* [ **s2l-destination** *s2l-destination-address* ] ] command.