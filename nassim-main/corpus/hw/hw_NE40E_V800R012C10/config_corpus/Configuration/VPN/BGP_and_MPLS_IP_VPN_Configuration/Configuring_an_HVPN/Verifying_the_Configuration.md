Verifying the Configuration
===========================

After you configure an HVPN, check on a local CE the default route or specific routes from this CE to a remote CE.

#### Prerequisites

The HVPN has been configured.


#### Procedure

* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on a local CE to check routing table information.
  
  
  + If you have configured an HoVPN, the command output shows a default route from the local CE to the remote CE. The next hop of the route is a UPE.
  + If you have configured an H-VPN, the command output shows specific routes from the local CE to the remote CE.
* Run the [**display mpls lsp protocol bgp**](cmdqueryname=display+mpls+lsp+protocol+bgp) [ **nexthop** *nexthop-address* ] [ **lsr-role** { **egress** | **ingress** | **transit** } ] [ **verbose** ] command to check information about the LSP established using BGP for BGP IPv4 VPN routes.