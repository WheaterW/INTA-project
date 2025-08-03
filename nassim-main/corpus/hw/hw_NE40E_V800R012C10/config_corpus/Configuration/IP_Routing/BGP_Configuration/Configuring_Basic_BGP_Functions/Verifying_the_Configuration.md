Verifying the Configuration
===========================

After configuring the basic BGP functions, verify BGP peer information.

#### Prerequisites

Basic BGP functions have been configured.


#### Procedure

* Run the [**display bgp router-id**](cmdqueryname=display+bgp+router-id+vpn-instance) [ **vpn-instance** [ *vpn-instance-name* ] ] command to check the router ID of the Router.
* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) [ **verbose** ] command to check the information about all BGP peers.
* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer+log-info+verbose) *ipv4-address* { **log-info** | **verbose** } command to check the information about a specified BGP peer.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) command to check the information about BGP routes.
* Run the [**display bgp routing-table route-filter**](cmdqueryname=display+bgp+routing-table+route-filter) *route-filter-name* command to check information about the BGP routes that match a specified XPL route-filter.