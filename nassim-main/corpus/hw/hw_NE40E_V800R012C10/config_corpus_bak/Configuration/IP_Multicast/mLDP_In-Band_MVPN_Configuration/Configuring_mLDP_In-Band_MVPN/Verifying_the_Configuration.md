Verifying the Configuration
===========================

After configuring mLDP in-band MVPN, check the BGP unicast peer relationships, unicast routes, and PIM routing tables of VPN instances on a PE.

#### Prerequisites

mLDP in-band MVPN has been configured.


#### Procedure

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) command to check BGP peer information.
* Run the [**display pim**](cmdqueryname=display+pim) { **vpn-instance** *vpn-instance-name* | **all-instance** } **routing-table** command to check the PIM routing entries of a specified VPN instance, or those of all VPN instances.
* Run the [**display mpls multicast-lsp protocol mldp**](cmdqueryname=display+mpls+multicast-lsp+protocol+mldp) **p2mp** [ **root-ip** *root-ip-address* { **lsp-id** *lsp-id* | **opaque-value** *opaque-value* } ] [ **lsr-role** { **bud** | **ingress** | **transit** | **egress** } ] command to check multicast LSP information.